#!/usr/bin/env python3
"""Generate standalone Codex icon skills from original style descriptions."""

from pathlib import Path
import json
import shutil
import sys
from zipfile import ZipFile, ZIP_DEFLATED


ROOT = Path(__file__).resolve().parents[1]
SITE_SAMPLES = {name: f"assets/{name}.png" for name in ("colorcut", "hologram", "nightfall", "storyworld")}
ADDED_STYLES = {"colorcut", "hologram", "nightfall", "storyworld"}

# name, visual medium, form and viewpoint, surface/light, color behavior, exclusion
STYLES = [
    ("clay", "chalky handmade clay and painted plaster miniature", "soft thick rounded forms, slightly uneven molded edges, shallow three-quarter view", "fine mottled sponge texture, matte surface, diffuse shadows, almost no specular shine", "pale pistachio and lime main forms, seafoam or turquoise secondary parts, tiny orange-gold details", "smooth rubber, glossy polymer, dark outlines, or saturated rainbow colors"),
    ("flare", "flat vector illustration with restrained faux depth", "compact app-icon silhouette built from a few crisp geometric planes, mild three-quarter view", "hard-edged light and dark color blocks, one narrow pale highlight, solid navy side faces; no reflective material", "bright spring green dominates; deep navy defines depth; cyan and pale blue mark secondary details; yellow-orange only as a small accent", "chrome, metallic reflections, gradients across broad surfaces, photorealism, dense grooves, or complex controls"),
    ("zing", "minimal editorial line-and-fill drawing", "recognizable school or study object, thin black outer and inner contours, white open planes, gentle three-quarter tilt", "flat untextured fills, small simple side faces, almost no shadow", "mostly white with periwinkle blue side planes; small lemon-yellow and bubblegum-pink details", "thick comic outlines, realistic volume, gradients, or a full-color body"),
    ("gloss", "ornate fantasy-game enamel icon", "chunky rounded collectible object with thick gold framing and inset blue panels, centered three-quarter view", "bright hard-edged gleams, bevels, glassy gem inserts, rich local contrast", "warm amber and gold dominate edges; electric cyan and royal blue fill insets; tiny emerald accents", "soft minimalist UI shapes, matte surfaces, dull gold, or desaturated colors"),
    ("mist", "airy modern digital icon with soft volume", "very simple rounded UI object with few parts, mostly frontal with subtle three-quarter depth", "smooth pale-blue-to-cobalt shading, milky white top-left glow, soft edge highlights and no dark stroke", "powder blue and white dominate; coral red is a tiny functional accent", "hard black outlines, heavy shadows, detailed machinery, or metallic shine"),
    ("pebble", "friendly compact product illustration", "sturdy rounded everyday object with simple proportions, shallow three-quarter view", "mostly flat blue fills, restrained smooth shading, short dark-blue side face, tiny glints", "medium cornflower or cobalt blue dominates, bright yellow for large functional parts, orange for tiny details, navy for holes and shadows", "fine technical detail, realistic gloss, thin contours, or a large cast shadow"),
    ("drift", "soft toy-like retail product illustration", "rounded simplified consumer object, visible functional feature, three-quarter view", "smooth molded satin surface, broad gentle value shifts, sparse narrow highlights, no black stroke", "vivid emerald or teal-green main body, sunny yellow hardware, cyan secondary panel, navy only inside recesses", "chrome, harsh gradients, tiny controls, black outlines, or gritty texture"),
    ("ink", "loose black marker-ink icon", "single instantly readable object drawn with confidently irregular medium black lines, nearly frontal", "white interiors, selective solid-black side or cavity, a few short motion ticks; little to no hatching", "black ink only on white", "gray shading, watercolor wash, neat CAD precision, or colored accents"),
    ("cardboard", "hand-built cardboard craft miniature", "folded kraft-paper construction with real-looking seams, edge thickness, straps, tabs, and cutouts, three-quarter view", "fine corrugated fiber and paper grain, matte edges, soft tabletop lighting", "warm tan kraft dominates; muted indigo-blue and teal paper panels; tiny coral or golden fasteners", "plastic coating, metal, glossy gradients, or perfectly seamless geometry"),
    ("linepop", "precise technical line illustration", "mostly white object described by thin even near-black contours and clean inner construction lines, slight three-quarter view", "little to no shaded fill, extremely restrained pale-blue side plane, tiny crisp highlight", "white dominates; neon lime focal marks and smaller yellow marks; pale blue for depth; near-black for hairline outlines", "heavy black comic strokes, dark filled body, painterly shading, or dense gradients"),
    ("glide", "ultra-clean flat vector with gentle dimensional cutouts", "simplified lifestyle object built from a few broad rounded planes, mild three-quarter view", "no drawn outlines or texture; at most a slightly darker green side plane and one minimal highlight", "deep emerald green dominates; saturated golden yellow on key parts; tiny violet and cream accents", "black contour lines, blue-dominant palette, metallic gradients, or small technical details"),
    ("nimble", "clean outlined product vector", "simple commerce or utility object with accurate functional parts, shallow three-quarter view", "thin consistent black outlines, white broad faces, restrained light-blue side shade, flat fills", "white dominates; strong royal blue areas; small vivid yellow functional accents; black contours", "lime green, heavy shading, rough sketching, or thick comic outlines"),
    ("jot", "spare hand-inked editorial drawing", "single everyday object with thin slightly imperfect black contours, mostly front or mild three-quarter view", "open white interiors, few faint cool-gray shadow strokes, no dense hatch", "white and black dominate; buttery pale yellow fills only one or two simple sections", "full-color rendering, lime green, dense geometry, dark side planes, or glossy 3D"),
    ("riso", "bright misregistered risograph print", "chunky editorial object made from overlapping graphic print plates, shallow three-quarter view", "visible halftone dots and slight ink offset, paper grain, hard print edges, no volumetric shine", "electric cobalt blue, acid yellow, aqua mint, lavender, small coral-red offset; cream-paper gaps", "smooth airbrush gradients, perfect alignment, realistic materials, or muted natural colors"),
    ("marker", "playful hand-colored marker drawing", "object simplified to a strong contour and few interior marks, near-front view", "thick slightly wobbly deep forest-green outline, flat marker-filled shapes with tiny uneven edges, almost no shadow", "bubblegum pink and green dominate, with lemon yellow and pale aqua fills", "black technical lines, realistic depth, glossy finish, or busy hatching"),
    ("glass", "pastel translucent glass-like collectible", "simple object with rounded clear walls and readable silhouette, three-quarter view", "very pale frosted cyan body, layered transparency, narrow iridescent cyan edge, faint glow rather than dark contrast", "icy cyan and powder blue dominate; tiny warm coral, peach, or lemon accents; large white luminous gaps", "dark outlines, smoky glass, high-contrast chrome, opaque colored body, or harsh caustics"),
    ("watercolor", "small handmade watercolor illustration", "object with realistic simplified structure, mostly three-quarter view", "visible uneven pigment wash, granulation and dry-paper flecks, soft edges within a clear silhouette", "dusty medium blue dominates, warm ochre-yellow on key parts, cream-paper highlights", "rainbow naturalism, glossy plastic, hard vector fills, or heavy black outlines"),
    ("yarn", "hand-crocheted miniature", "recognizable cozy object built from thick stitched pieces and sewn-on small details, three-quarter view", "individual yarn loops and cable-knit ridges visible throughout, soft wool fibers, gentle warm lighting", "muted sage green, oatmeal cream, chestnut brown, and tiny burnt-orange stitches", "smooth felt, plastic, saturated neon, or hard glossy surfaces"),
    ("sketchy", "bold hand-drawn flat cartoon", "object with chunky slightly irregular black contour, shallow three-quarter view", "solid flat fills, tiny white shine marks, an occasional second interior line; no texture", "bright turquoise-cyan main fill, coral pink secondary, vivid blue tertiary, black outline", "thin technical drawing, green-yellow palette, realistic shading, or airbrushed volume"),
    ("pulse", "geometric flat vector with offset depth", "office or utility object assembled from broad straight-edged color panels, mostly frontal", "matte solid fill, no contour stroke, one dark navy offset side face, zero texture", "indigo-periwinkle dominates, dusty sage green secondary, coral-orange and mustard-yellow small panels, deep navy depth", "rounded toy gloss, blue-green gradients, fine details, or black line art"),
    ("candypop", "maximal glossy candy-store toy", "inflated sweets or playful fantasy object made of fat rounded pieces, centered three-quarter view", "hard white reflections, glassy candy coating, thick luminous rims, occasional tiny sparkle", "hot magenta and candy pink, electric cyan and royal blue, vivid violet, bright yellow highlights", "matte minimalism, muted colors, sketch strokes, or realistic natural materials"),
    ("charcoal", "colored-pencil and charcoal sketch", "familiar household object with believable form and slightly uneven dark contours, three-quarter view", "dense visible pencil strokes following form, gray-blue hatching, soft paper-grain shadows", "slate and denim blue-gray dominate, cream highlights, small dusty salmon or pale gold accents", "pure monochrome, smooth vector fill, thick marker black, or glossy rendering"),
    ("ceramic", "decorative glazed ceramic collectible", "rounded molded home-decor form with raised relief, scalloped or fluted edges, centered three-quarter view", "soft porcelain glaze with small smooth specular highlights, hand-shaped irregularity, delicate inset ornament", "blush pink dominates, pale aqua or mint inset parts, lavender, cream, and tiny gold details", "hard plastic, dark outlines, rough stone, or high-contrast chrome"),
    ("fuzzy", "short-pile flocked plush", "compact soft object with a puffy but precise silhouette, near-front view", "dense velvety microfibers over every surface, rounded seams and appliqued details, soft diffuse light", "hot pink main body, lavender secondary, baby-blue panels, tiny peach details", "crochet loops, long fur, shiny plastic, hard edges, or dark outlines"),
    ("colorcut", "tiny colorful cut-paper vector glyph", "one compact object reduced to a few irregular overlapping silhouettes, near-front view, no perspective grid", "mostly flat opaque fills with small soft gradient transitions at overlaps, rounded corners, no stroke outline or cast shadow", "vivid cobalt blue, leaf green, vermilion red, bubblegum pink, sunny orange, and pale lime chosen as two or three dominant hues per icon", "black outlines, glossy 3D, detailed realism, uniform rainbow fill, lettering, or a pictogram inside a card"),
    ("hologram", "luminous pastel holographic vector-3D illustration", "small floating pictogram built from five to seven broad beveled geometric facets, subtle three-quarter tilt and faint horizontal ground shadow", "opalescent cyan-violet-pink-gold color transitions on select facets, clean narrow edge lights, sparse sparkles; icon-like rather than physically metallic", "powder cyan and lavender dominate, with peach pink, golden yellow and mint reflections against a very pale aqua field", "realistic metal, microtexture, physical controls, dark heavy shadows, thick gold frames, or large detailed product renders"),
    ("nightfall", "whimsical editorial 2.5D spot illustration", "one expressive subject with at most one or two small related props, dynamic tilt or float, rounded silhouette on a deep slate field", "soft painted gradients on simplified matte beveled planes, mild grain, small bright highlights and occasional motion/cloud/star accents", "coral peach, sky blue, lime green, sunflower yellow and warm orange against dark blue-charcoal #2B424A", "white card backgrounds, realistic microdetail, rigid centered product renders, neon plastic gloss, hard black outlines, or crowded full scenes"),
    ("storyworld", "small isometric narrative diorama", "architectural mini-scene on a square or diamond plinth, one strong hero object, at most two supporting pieces and a clear isometric grid", "hard vector facets plus limited blue-violet-coral-yellow gradients on selected faces, deep midnight portal interiors with tiny stars, sharply defined platform shadows", "cobalt blue and violet structures, warm lemon-yellow planes, coral-pink and mint accents, near-black navy portals on a warm white field", "generic floating emoji, random objects, too many props, soft toy shading, realistic surfaces, broad airbrush, or a busy landscape"),
]

# Observations from the four screenshots supplied by the user. The source screenshots
# are not included in the distributable ZIP; future sessions use these detailed notes.
USER_STYLE_NOTES = {
    "colorcut": "Reference sheet 1: twenty tiny glyphs in a loose four-column grid on warm ivory. Each is a stand-alone pictogram with abundant whitespace. Forms look cut from two to five curved colored paper pieces, often with one clipped edge, hole, or small inset mark. There is no contour stroke. Colors vary by subject, but neighboring colors gently blend at some boundaries; the result is brighter and softer than a strict flat SVG. Details are nearly absent and shadows do not ground the icon. Match the visual grammar, never the reference subjects.",
    "hologram": "Reference sheet 2: fifteen finance and technology motifs on very pale mint. Compact beveled silhouettes float just above a faint horizontal ground shadow. Surfaces are iridescent cyan, lavender, peach, and gold with clear faceted edges, narrow highlights, and a few tiny star glints. Light comes from above-left; dark purple appears only in inset cavities and fine shadow edges. This differs from opaque Gloss and very pale Glass: keep the opalescent spectrum and moderate contrast, without thick gold frames. Match the grammar, never the reference subjects.",
    "nightfall": "Reference sheet 3: twenty-four hand-shaped spot illustrations arranged in even rows on uniform dark slate. Each is a small editorial vignette, usually a main object plus one related secondary object or motion flourish. Shapes tilt, hover, spring, pour, or grow. Rounded beveled pieces use restrained soft gradients and a lightly painted surface; not flat monochrome and not glossy plastic. Pale blue, peach, coral, grass green, orange, and yellow pop against the dark field. Short white cloud fragments or tiny sparkles add movement. Preserve wide negative space and do not turn each item into a framed card.",
    "storyworld": "Reference sheet 4: sparse mini-scenes separated by generous warm-white space. Each scene sits on a small square or diamond isometric platform with visible side thickness and one commanding element such as an arch, portal, hourglass, animal, or sculpture. Precise angular facets and steps create a miniature architectural story. Several dark navy openings hold tiny white stars; blue, violet, coral, yellow, lime and mint gradients appear on specific faces, not as a full-scene blur. Small circular number-like tokens in the references are incidental and should not be copied. Keep scenes purposeful and legible, with very few related props.",
}

NATIVE_BACKGROUNDS = {
    "colorcut": "warm ivory #FFFEF8",
    "hologram": "very pale mint #ECFAF5",
    "nightfall": "deep blue-charcoal #2B424A",
    "storyworld": "warm white #FFFEF8",
}


def render(style):
    name, medium, form, finish, colors, avoid = style
    title = name.capitalize()
    if name in USER_STYLE_NOTES:
        calibration = USER_STYLE_NOTES[name] + " If this conversation still contains the user's reference sheet, use it as a style reference in an image tool that accepts conversation images. Otherwise follow these notes and the Style lock. Do not copy any subject from the sheet."
    else:
        calibration = f"These four publicly visible gallery images show the style across different subjects. When network access and the image tool permit, inspect them and provide them to the image tool as **style references only**: `https://sohna.dev/waterlemon/src/image/min/skill/{name}/{name}_1.png`, `https://sohna.dev/waterlemon/src/image/min/skill/{name}/{name}_4.png`, `https://sohna.dev/waterlemon/src/image/min/skill/{name}/{name}_7.png`, and `https://sohna.dev/waterlemon/src/image/min/skill/{name}/{name}_10.png`. Download into a temporary location, verify each file is an image, and follow the tool's reference-image instructions. Never copy a reference subject, symbols, or composition into the output; apply only its palette, construction, material, line weight, lighting, and detail density. If references cannot be loaded, use the Style lock above. Do not claim access to the paid source prompts."
    scale = "For a miniature Storyworld scene, check legibility at 128 px and give the platform and hero element room to breathe." if name == "storyworld" else "Make the silhouette unmistakable at 64 px."
    review = "Review against the user's reference notes" if name in USER_STYLE_NOTES else "Review against the four style references"
    native_background = NATIVE_BACKGROUNDS.get(name, "pure white #FFFFFF")
    return f'''---
name: {name}-icon
description: Generate consistent {title} style product icons with configurable palettes and transparent backgrounds. Use when the user requests a {title} icon, an icon set, or this visual style for a product illustration.
---

# {title} icon

Create one or more polished product icons using an image generation tool available in the current session. If no image generation tool is available, provide the complete generation prompts so the user can run them elsewhere. Do not claim an image was created when only a prompt was produced.

## Guided selection

This style is already selected. Before generating, ask the user **one question at a time** in the order below. Wait for their answer before asking the next question. Use a question or selection tool when available; otherwise ask in chat and stop until the user replies. Never bundle questions, fill in an unanswered choice, or start image generation early. If a value was supplied in the opening request, show it as the proposed choice and still ask for confirmation at its step. Let the user say "default" or "back" to choose a default or revise the previous choice.

1. "One icon or a matching set?" Offer one / set.
2. "What should the icon or icons show?" Request one subject or a comma-separated subject list, matching the choice above.
3. "Where will you use them?" Offer app or product UI / marketing or social / other, and accept a custom answer.
4. "How should colors be chosen?" Offer this style's default palette / realistic object colors / custom palette. If custom, ask separately for primary, secondary, tertiary, accent, and detail colors, in that order. Accept hex codes or plain color names; offer "use style default" for each slot. Keep object colors recognizable unless strict brand colors are requested.
5. "What background do you want?" Offer native {title} background ({native_background}) / transparent / custom solid color. If custom solid, ask for its color in a separate question. Preserve the user's choice; the native background is the closest visual match to this style's reference sheet.
6. "What canvas shape do you want?" Offer square / portrait / landscape. Square is recommended for icons.
7. "What size or intended export do you want?" Offer high resolution PNG / another size or format. Do not promise a format the available tool cannot produce; explain its actual output if needed.
8. Summarize all selections and ask **one** final question: "Generate with these choices, or change one?" If they choose change, revisit that choice and then confirm again.

Only an explicit answer, including "default", advances a step. A skipped or unanswered question leaves the wizard paused. Preserve selections across turns.

## Style lock

- Medium: {medium}.
- Form: {form}.
- Surface and light: {finish}.
- Default color direction: {colors}.
- Avoid: {avoid}, text, letters, logos, watermarks, frames, unrelated props, and busy backgrounds.

## Visual calibration

{calibration}

## Generate

{scale} Keep the whole object or mini-scene within the central 65% of the canvas width and height, leaving generous balanced empty space. Reduce the subject to its identifying parts; omit tiny details that disappear at the intended size. Preserve the same viewpoint, scale, stroke weight or material treatment, light direction, shadow softness, and palette across a set. A solid background is a uniform field, not an app tile or surrounding scene.

Build a prompt with the subject, every style lock above, the chosen color mapping, selected canvas, and requested background. Explicitly describe which parts of the subject get primary, secondary, and accent colors. Use the image generation tool directly. Set its transparent background option when the user wants a transparent icon. For a series, reuse the same style block word for word and change only subject anatomy and user-requested colors. Prefer individual deliverables over a contact sheet unless the user asks for a sheet.

{review}, especially material, outline thickness, highlight type, number of details, color proportions, and object scale. Also check subject recognition, clipping, text artifacts, and unintended background. If it drifts toward a generic style, revise the prompt with specific forbidden traits and regenerate. Return the finished image or files and a short note identifying the style and palette used.
'''


def render_wizard():
    catalog = ", ".join(style[0].capitalize() for style in STYLES)
    return f'''---
name: illustration-icon-wizard
description: Guide the user through every icon decision one question at a time, then generate a polished icon or matching set in one of {len(STYLES)} visual styles.
---

# Illustration icon wizard

Lead a fully interactive icon creation flow. Ask exactly **one question per message or question-tool call** and wait for the answer before moving on. Prefer a selection tool when available, but use plain chat if needed. Never bundle choices into one question, silently accept an unanswered default, or generate before final confirmation. A user reply of "default" selects the suggested default for the current question; "back" revisits the previous selection. Preserve answers across turns. Even if the opening request contains choices, present each as a proposed selection at its step and ask the user to confirm it.

## Question sequence

1. **Style.** Show this concise catalog and ask which style to use: {catalog}. If the user wants help choosing, ask a single follow-up question about the look they prefer, suggest up to three styles, then ask them to choose one. The selected style corresponds to the standalone `../<style>-icon/SKILL.md` beside this skill. Read and apply its Style lock, Visual calibration, and Generate sections. If that file is unavailable, explain that the pack is incomplete rather than inventing its instructions.
2. **Quantity.** Ask "One icon or a matching set?" Offer one / set.
3. **Subject.** Ask what the icon should show, or request a comma-separated subject list for a set.
4. **Use.** Ask where the icons will be used. Offer app or product UI / marketing or social / other.
5. **Color method.** Ask style default palette / realistic object colors / custom palette. If custom, ask primary, secondary, tertiary, accent, and detail colors **in five separate turns**, in that order. Accept hex codes or names; "default" uses the chosen style's direction for that slot.
6. **Background.** Read the selected style's native background in its guided selection section. Ask native background / transparent / custom solid color. If custom solid, ask its color in a separate turn.
7. **Canvas.** Ask square / portrait / landscape.
8. **Output.** Ask high resolution PNG / custom size or format. If custom, ask for the details in a separate turn and use only formats the available image tool supports.
9. **Confirm.** Summarize every selected value. Ask exactly one question: "Generate with these choices, or change one?" If a change is requested, revisit that choice and confirm again.

Only an explicit answer advances the sequence. If the user leaves a question unanswered, stop and await the reply.

## Produce

After confirmation, use the selected style skill's Style lock, Visual calibration, and Generate sections. Use an image generation tool if available, setting transparent background when chosen. Otherwise provide complete prompts and clearly state that no image was generated. For a set, keep perspective, scale, palette, material, and light consistent. Check each output for recognition, clipping, text artifacts, and background errors. Return the result and a short summary of the choices.
'''


def main():
    check = "--check" in sys.argv
    failures = []
    for style in STYLES:
        path = ROOT / "skills" / f"{style[0]}-icon" / "SKILL.md"
        content = render(style)
        if check:
            if not path.exists() or path.read_text() != content:
                failures.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
    wizard_path = ROOT / "skills" / "illustration-icon-wizard" / "SKILL.md"
    wizard_content = render_wizard()
    if check:
        if not wizard_path.exists() or wizard_path.read_text() != wizard_content:
            failures.append(str(wizard_path.relative_to(ROOT)))
    else:
        wizard_path.parent.mkdir(parents=True, exist_ok=True)
        wizard_path.write_text(wizard_content)
    site_dir = ROOT / "site"
    site_dir.mkdir(exist_ok=True)
    catalog = []
    for name, medium, form, finish, colors, avoid in STYLES:
        local_refs = sorted(
            (site_dir / "assets" / "references" / name).glob("*.png"),
            key=lambda path: int(path.stem.rsplit("_", 1)[1]),
        )
        if name in ADDED_STYLES:
            references = [SITE_SAMPLES[name]]
        else:
            references = [str(path.relative_to(site_dir)) for path in local_refs]
        if not references:
            references = [f"https://sohna.dev/waterlemon/src/image/min/skill/{name}/{name}_{i}.png" for i in (1, 4, 7, 10)]
        catalog.append({
            "name": name.capitalize(), "slug": name,
            "description": medium[0].upper() + medium[1:],
            "form": form[0].upper() + form[1:],
            "finish": finish[0].upper() + finish[1:],
            "palette": colors[0].upper() + colors[1:],
            "reference": references[0],
            "references": references,
            "skill": f"skills/{name}-icon/SKILL.md",
        })
    catalog_json = json.dumps(catalog, ensure_ascii=False, indent=2) + "\n"
    catalog_path = site_dir / "styles.json"
    if check:
        if not catalog_path.exists() or catalog_path.read_text() != catalog_json:
            failures.append(str(catalog_path.relative_to(ROOT)))
    else:
        catalog_path.write_text(catalog_json)
    if failures:
        print("Out of date: " + ", ".join(failures), file=sys.stderr)
        return 1
    archive = ROOT / "illustration-icon-skills.zip"
    skill_files = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if check:
        if not archive.exists():
            print("Missing skill ZIP", file=sys.stderr)
            return 1
        with ZipFile(archive) as bundle:
            expected = {str(path.relative_to(ROOT)): path.read_bytes() for path in skill_files}
            if set(bundle.namelist()) != set(expected) or any(bundle.read(name) != content for name, content in expected.items()) or bundle.testzip():
                print("Skill ZIP is out of date or invalid", file=sys.stderr)
                return 1
    else:
        with ZipFile(archive, "w", ZIP_DEFLATED) as bundle:
            for path in skill_files:
                bundle.write(path, path.relative_to(ROOT))
    web_archive = site_dir / "illustration-icon-skills.zip"
    if check:
        if not web_archive.exists() or web_archive.read_bytes() != archive.read_bytes():
            print("The website skill download is missing or out of date", file=sys.stderr)
            return 1
    else:
        shutil.copyfile(archive, web_archive)
    print(f"{'Verified' if check else 'Generated'} {len(STYLES)} styles and one wizard skill")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
