#!/usr/bin/env python3
"""Generate standalone Codex icon skills from original style descriptions."""

from pathlib import Path
import json
import shutil
import sys
from zipfile import ZipFile, ZIP_DEFLATED


ROOT = Path(__file__).resolve().parents[1]
ADDED_STYLES = {"colorcut", "hologram", "nightfall", "storyworld", "pop", "clover", "studio", "concept"}

# name, visual medium, form and viewpoint, surface/light, color behavior, exclusion
STYLES = [
    ("clay", "chalky handmade clay and painted plaster miniature", "soft thick rounded forms, slightly uneven molded edges, shallow three-quarter view", "fine mottled sponge texture, matte surface, diffuse shadows, almost no specular shine", "pale pistachio and lime main forms, seafoam or turquoise secondary parts, tiny orange-gold details", "smooth rubber, glossy polymer, dark outlines, or saturated rainbow colors"),
    ("flare", "flat vector illustration with restrained faux depth", "compact app-icon silhouette built from a few crisp geometric planes, mild three-quarter view", "hard-edged light and dark color blocks, one narrow pale highlight, solid navy side faces; no reflective material", "bright spring green dominates; deep navy defines depth; cyan and pale blue mark secondary details; yellow-orange only as a small accent", "chrome, metallic reflections, gradients across broad surfaces, photorealism, dense grooves, or complex controls"),
    ("zing", "minimal editorial school-object illustration", "one familiar study object, simplified to its essential parts, with open white planes, a gentle tilt, and a steady fine black contour", "crisp, even monoline outlines and flat untextured fills; add a pale periwinkle-blue side plane, with little or no shading and almost no cast shadow", "white is the main field; periwinkle is the principal spot color, while lemon yellow and bubblegum pink appear as small details rather than large filled regions", "thick comic strokes, loose scratchy drawing, gradients, inflated 3D volume, or coloring every surface"),
    ("gloss", "polished casual-game enamel icon", "single compact, instantly readable object with a chunky rounded silhouette, simple frontal or shallow three-quarter view", "smooth molded enamel, bold gold rims and bevels, a few broad white shine marks, clean bright highlights and soft short grounding shade", "vivid golden yellow and amber dominate; royal blue and cyan form one or two large inset panels; tiny emerald accents only", "photorealistic metal, microtexture, intricate engraving, filigree, many tiny gems, spiky ornament, dark dramatic lighting, or busy detail"),
    ("mist", "soft-volume digital app icon", "a single simple UI object with a compact rounded silhouette and only a few essential parts; mostly front-facing, with just enough three-quarter depth to read its edge", "opaque, softly airbrushed pale-cyan-to-mid-blue shading, brightest at the upper left and deeper blue at the lower right; one broad milky highlight and a restrained cool edge glow, no drawn contour", "powder blue and white occupy nearly all the icon; cobalt is limited to lower edges and recesses, with coral red on one tiny functional control", "glass or see-through material, hard black outlines, sharp specular streaks, heavy bloom, deep cast shadows, many controls, or metallic reflections"),
    ("pebble", "friendly rounded product vector", "a compact practical object with sturdy rounded forms, simple functional parts, and a shallow three-quarter angle that reveals a short dark-blue side", "mostly clean blue fills with only gentle edge shading, crisp rounded edges, a small soft highlight, and a faint short grounding shadow; keep the finish smooth but not shiny", "medium cornflower or cobalt blue dominates; bright yellow marks a key functional component, orange is a pin-size detail, and navy is reserved for openings and the side face", "high-gloss toy plastic, hard white specular bands, mirror shine, metallic trim, thin black outlines, dense controls, or a long cast shadow"),
    ("drift", "soft toy-like retail product illustration", "rounded simplified consumer object, visible functional feature, three-quarter view", "smooth molded satin surface, broad gentle value shifts, sparse narrow highlights, no black stroke", "vivid emerald or teal-green main body, sunny yellow hardware, cyan secondary panel, navy only inside recesses", "chrome, harsh gradients, tiny controls, black outlines, or gritty texture"),
    ("ink", "spare hand-drawn black ink icon", "one instantly recognizable everyday object, nearly frontal, with a clear silhouette and loose but controlled hand-drawn contours; keep the inside mostly open", "fine-to-medium black lines with slight human variation, a few short interior strokes, and occasional short gesture marks; use a small solid-black patch only for a cavity or cast side, with no dense hatching", "black ink alone on clean white", "thick comic-marker outlines, ruler-straight CAD geometry, gray rendering, dense crosshatching, colored accents, or decorative scenery"),
    ("cardboard", "hand-built corrugated-card miniature", "one compact everyday object visibly assembled from folded kraft-paper pieces, with real layered thickness, seams, tabs, slots or a paper strap; use a consistent three-quarter view", "softly lit studio-craft rendering with matte fibrous paper, visible corrugation along cut edges, crisp folds, and restrained surface grain; keep the object isolated with a soft short contact shadow", "warm natural kraft tan is dominant; muted denim-indigo or sage-teal form one or two paper panels, with a tiny coral or ochre fastener", "wood grain, rough dirty paper, plastic coating, metal hardware, smooth seamless forms, theatrical lighting, or a surrounding craft-table scene"),
    ("linepop", "minimal precise outline icon", "one simple utility object with a clean, recognizable silhouette, mostly front-facing or slightly tilted; show its function with only a few interior divisions", "thin, even near-black contour lines with clean joins; keep broad faces white, use at most one pale-blue side plane, no modeled gray shading, and only a faint contact mark", "white dominates; use a small neon-lime focal fill and one much smaller yellow accent, with near-black reserved for the outline", "dense controls or grille details, thick comic strokes, loose hand sketching, broad dark fills, 3D rendering, gradients, or ornamental line clutter"),
    ("glide", "ultra-clean flat lifestyle vector", "one familiar home or daily-use object built from two to five broad, softly rounded geometric shapes; use a mild three-quarter view only when needed to clarify its construction", "solid matte color planes with crisp overlap boundaries and simple cutout shapes; no outline, surface texture, airbrush, or modeled light; one darker-green plane may indicate depth", "deep emerald is the main shape; golden yellow marks one large functional component, while violet and cream appear only as tiny secondary accents", "3D product rendering, gradients, glossy highlights, outlines, realistic material texture, fussy controls, or a blue-dominant palette"),
    ("nimble", "clear outlined commerce and utility icon", "one functional household, retail, or electronic object with accurate recognizable parts, a compact silhouette, and a shallow three-quarter view", "steady medium-fine black contours around flat faces; use broad royal-blue panels, open white face areas, and only a pale-blue side plane for depth, with no modeled gradient", "royal blue and white share the main body; yellow marks one important control or fitting, and black is reserved for the consistent outline and small openings", "lime or emerald accents, sketchy linework, heavy comic contours, toy-like rounded volume, extensive gray shading, or a long cast shadow"),
    ("jot", "spare hand-inked editorial object drawing", "one simple everyday object in a mostly frontal or mild three-quarter view; fine, slightly imperfect contours define it while leaving generous white interior space", "light black pen lines with subtle hand variation, a few short construction marks and faint cool-gray grounding strokes; use a soft pale-butter-yellow tint on only one or two small identifying areas", "white paper and black linework dominate; pale butter yellow stays light and occupies a small part of the object", "medium-bold marker contours, large solid black masses, saturated color, broad yellow panels, dense hatching, precise vector geometry, or glossy volume"),
    ("riso", "bright misregistered risograph print", "chunky editorial object made from overlapping graphic print plates, shallow three-quarter view", "visible halftone dots and slight ink offset, paper grain, hard print edges, no volumetric shine", "electric cobalt blue, acid yellow, aqua mint, lavender, small coral-red offset; cream-paper gaps", "smooth airbrush gradients, perfect alignment, realistic materials, or muted natural colors"),
    ("marker", "playful hand-colored marker drawing", "object simplified to a strong contour and few interior marks, near-front view", "thick slightly wobbly deep forest-green outline, flat marker-filled shapes with tiny uneven edges, almost no shadow", "bubblegum pink and green dominate, with lemon yellow and pale aqua fills", "black technical lines, realistic depth, glossy finish, or busy hatching"),
    ("glass", "pastel translucent glass icon", "single simple object with a rounded, softly tinted solid-glass silhouette, front or shallow three-quarter view", "smooth milky transparency, broad soft internal panes, one clear cyan rim highlight and a few pastel reflections; bright, airy light with a readable softly colored body", "icy cyan and powder blue provide visible body color; tiny coral, peach or lemon reflections; generous white space", "near-invisible colorless edges, wireframe construction, many fine seams, dark outlines, smoky glass, chrome, heavy rainbow refraction, photorealism, or harsh caustics"),
    ("watercolor", "small hand-painted watercolor spot illustration", "one familiar object with believable but simplified construction, arranged as a compact three-quarter view with a clear outer silhouette and no surrounding scene", "build the form from a few translucent, overlapping pigment washes; keep soft blooms, granulation, and occasional dry-brush paper flecks inside the painted shape, with slightly pooled edges and only a faint grounding wash", "dusty denim or slate blue carries the main form; warm ochre marks one or two key parts, with cream paper left visible as highlights", "photographic product rendering, glossy 3D plastic, smooth airbrush gradients, hard vector fills, uniformly fuzzy edges, heavy black outlines, rainbow color, or a painted backdrop"),
    ("yarn", "hand-crocheted miniature", "recognizable cozy object built from thick stitched pieces and sewn-on small details, three-quarter view", "individual yarn loops and cable-knit ridges visible throughout, soft wool fibers, gentle warm lighting", "muted sage green, oatmeal cream, chestnut brown, and tiny burnt-orange stitches", "smooth felt, plastic, saturated neon, or hard glossy surfaces"),
    ("sketchy", "bold hand-drawn flat cartoon icon", "one isolated, immediately recognizable everyday object with a chunky rounded silhouette, mostly side-on or gently tilted", "thick smooth slightly wobbly black marker contour, large flat solid color regions, only a few simple interior lines and tiny white shine marks; no shading or texture", "turquoise-cyan is the dominant fill; coral pink is the secondary fill; vivid blue is a small third color; black contours stay consistent", "landscape scenery, illustrative vignettes, detailed perspective, gradients, realistic shading, scratchy linework, fine hatching, or thin technical outlines"),
    ("pulse", "geometric flat vector with offset depth", "office or utility object assembled from broad straight-edged color panels, mostly frontal", "matte solid fill, no contour stroke, one dark navy offset side face, zero texture", "indigo-periwinkle dominates, dusty sage green secondary, coral-orange and mustard-yellow small panels, deep navy depth", "rounded toy gloss, blue-green gradients, fine details, or black line art"),
    ("candypop", "glossy candy-store toy icon", "single plump candy or playful confection with an inflated rounded silhouette, simple front or shallow three-quarter view", "smooth hard-candy lacquer, a few broad crisp white highlights and a soft luminous rim; clean molded surfaces", "hot pink and magenta dominate, with bold cyan, royal blue, violet or yellow in two or three large color patches", "matte surfaces, muted colors, faceted gems, transparent glass, tiny sprinkles, many small candies, intricate patterns, excessive ornament, or realistic materials"),
    ("charcoal", "colored-pencil and charcoal sketch", "familiar household object with believable form and slightly uneven dark contours, three-quarter view", "dense visible pencil strokes following form, gray-blue hatching, soft paper-grain shadows", "slate and denim blue-gray dominate, cream highlights, small dusty salmon or pale gold accents", "pure monochrome, smooth vector fill, thick marker black, or glossy rendering"),
    ("ceramic", "friendly decorative glazed pottery icon", "single rounded home-decor object with a simple, softly molded silhouette, front or shallow three-quarter view", "smooth glossy porcelain glaze, broad gentle highlights, softly modeled volume, hand-shaped edges and one or two restrained raised relief details", "blush pink is dominant; pale aqua or mint marks one inset or secondary part; lavender, cream and tiny warm yellow accents", "photorealistic product staging, dense floral patterns, repeated tiny petals, extensive gold trim, sharp plastic edges, matte clay, dark outlines, dramatic reflections, or background props"),
    ("fuzzy", "short-pile flocked plush", "compact soft object with a puffy but precise silhouette, near-front view", "dense velvety microfibers over every surface, rounded seams and appliqued details, soft diffuse light", "hot pink main body, lavender secondary, baby-blue panels, tiny peach details", "crochet loops, long fur, shiny plastic, hard edges, or dark outlines"),
    ("colorcut", "soft-edged colorful vector glyph", "one small compact pictogram built from two to five rounded, irregular interlocking color shapes, front-facing without perspective", "mostly flat digital fills, softly blended overlap edges, occasional clipped edge, hole or inset; no physical paper texture, stroke or grounding shadow", "bright cobalt, leaf green, vermilion, pink, orange and pale lime; limit each glyph to two or three hues", "large logo-like scale, hard flat SVG edges, physical paper grain, black outlines, glossy 3D, realism, uniform rainbow fill, lettering, or a pictogram inside a card"),
    ("hologram", "opalescent faceted vector-3D illustration", "compact floating icon built from a handful of broad beveled planes, subtly tilted in three-quarter view, small clear silhouette and faint ground shadow", "crisp facet boundaries with restrained cyan-lavender-peach-gold refraction on selected faces, narrow pale edge glints, only occasional pin-size star glint; light from above-left", "powder cyan and lavender dominate, with blush-peach and small golden reflections over very pale mint", "gold wireframe outlines, densely tessellated jewel surfaces, realistic metal, microtexture, huge glow, all-over rainbow, physical controls, dark shadows, or large product renders"),
    ("nightfall", "compact painted editorial spot illustration with graphic 2.5D depth", "one expressive subject, usually tilted, lifting, bending or in motion; build its silhouette from a few broad hand-shaped pieces and allow at most one meaningful secondary element", "matte color planes with a soft short gradient on selected curves, one narrow darker underside or inner cut, and a quiet upper-left highlight; edges stay clean but slightly organic; any cloud curl, steam, sparkle or motion mark must explain the action", "choose two main colors and one small accent per icon from coral-peach, powder blue, leaf green, warm orange and butter yellow; use midnight blue only for recesses or underside cuts; design for a deep blue-charcoal #2B424A presentation field but export transparent artwork", "realistic product detail, glossy toy plastic, bright specular stripes, heavy outlines, all-over brush texture, grain, many tiny parts, symmetric emoji poses, full environments, or decorative confetti"),
    ("storyworld", "fantastical isometric storybook diorama illustration", "one surreal narrative hero or tiny architectural world arranged as a self-contained vignette; use precise 30-degree isometric geometry for platforms and structures, supported by only one or two meaningful elements", "crisp vector-like facets, clean hard-edged planes, a few clear steps or cutouts, selective gradient on a portal or magical form, occasional deep midnight-navy starry opening, and a short compact cast shadow", "restrained but lively color grouping: usually two main hues with one or two small accents selected from cobalt, royal blue, violet, magenta, lemon yellow, coral, mint and lime; vary combinations between scenes and reserve navy for cavities", "rainbow-colored scenes, more than four prominent hues in one vignette, ornamental tiling, excessive trim, clusters of tiny props, dense starfields, tiny illegible detail, uniform gray 3D renders, soft toy materials, broad painterly backgrounds, realistic landscapes, or generic emoji treatment"),
    ("pop", "bold flat geometric editorial pictogram", "one familiar object or character reduced to a compact, instantly recognizable silhouette assembled from a few large geometric shapes; mostly front-facing with no perspective", "crisp hard-edged solid fills, clean cutout overlaps, minimal internal divisions, no outline except where a deliberate black shape defines a feature; completely flat with no shading", "bright red, yellow, cobalt, sky blue, orange, pink, mint and black; choose only a few clear blocks per symbol, with white negative space", "gradients, shadows, texture, realistic detail, thin strokes, rounded 3D volume, excessive internal parts, or using every palette color in every symbol"),
    ("clover", "soft green-gradient editorial glyph", "one immediately readable app symbol built from a few bold rounded shapes, centered and nearly front-facing", "clean flat vector construction with gentle green tonal blends and only a narrow soft darker edge on selected overlaps; simple cutout details and almost no cast shadow", "fresh emerald and spring green tie the set together, with pale mint or cream openings and occasional small coral, orange or yellow accents; a fruit may use coral-red", "thick extruded side walls, shiny plastic highlights, strong hard shadows, busy outlines, dense details, texture, or using only one monotonous shade of green"),
    ("studio", "softly rendered miniature product illustration", "one ordinary household object, food item, or small furnishing, carefully constructed and isolated in a calm three-quarter view", "soft diffuse studio light, realistic but simplified material cues, gentle ambient contact shadow, subtle surface texture, softly rounded edges and restrained highlights; no cartoon outline", "natural object colors with warm wood, cream, stone, muted greens and small authentic color accents against clean white", "hard vector fills, toy-like plastic gloss, dramatic lighting, hard black outlines, oversaturated colors, excessive props, or full room scenes"),
    ("concept", "spare editorial line-and-lavender conceptual illustration", "one clever metaphor assembled from two or three recognizable elements in a loose, asymmetrical composition; mostly front-facing with only slight perspective where the idea needs it", "hairline near-black hand-guided contours, mostly open white interiors, one small flat soft-lavender shape that overlaps or sits behind the line drawing; a small near-black solid is allowed only as an essential focal part; no gradients, texture, modeled volume or shadows", "near-black lines and transparent negative space dominate; muted lavender #A98CE7 is the only fill and occupies less than one quarter of the visible artwork", "thick outlines, uniformly geometric icon geometry, filled purple bodies, full black silhouettes, decorative detail, extra colors, caption text, card backgrounds or border boxes"),
]

SITE_SAMPLE_COUNTS = {style[0]: 12 for style in STYLES}
SITE_SAMPLE_COUNTS["clover"] = 6

# Observations from the eight reference sheets supplied by the user. The source screenshots
# are not included in the distributable ZIP; future sessions use these detailed notes.
USER_STYLE_NOTES = {
    "colorcut": "Reference sheet 1: twenty very small glyphs in an open four-column grid on warm ivory. Keep each glyph modest inside its cell, surrounded by conspicuous space. Stand-alone pictograms use two to five soft, organic vector pieces that interlock like simple cutouts; this is digital illustration, not textured craft paper. Some edges gently blend or overlap; a clipped edge, hole or inset can identify the object. No contour stroke, grounding shadow or extra decoration. The colors are vivid but friendly and usually limited to two or three hues per symbol. Match the visual grammar, never the reference subjects.",
    "hologram": "Reference sheet 2: fifteen technology and finance icons in a tidy 5-by-3 layout on very pale mint. Each is a small clean silhouette made from a handful of broad, beveled faceted surfaces, with clear transitions between planes. Opalescent cyan and lavender dominate; peach and gold are selective face reflections, not outlines. Add slender pale edge glints, upper-left lighting, a faint short shadow underneath and only a rare pin-size star. Keep moderate contrast and visible object color. This differs from gold-framed Gloss and pale frosted Glass: avoid wireframes, dense jewel tessellation, oversized glow and broad rainbow wash. Match the grammar, never the reference subjects.",
    "nightfall": "Reference sheet 3: twenty-four tiny editorial vignettes float in a regular four-column grid on uniform deep slate. The slate is a presentation color, not part of the exported icon. Most subjects are recognizable from a quick silhouette and a single action: a form springs upward, pours, grows, flies, unfurls or reaches. A related prop appears only when it strengthens that action. Forms are compact and slightly asymmetrical, with broad simplified color shapes, softly rounded tips, occasional sharp fold or dark interior wedge, and selective subtle shading rather than uniform extrusion. Bright and pale colors carry the subject; midnight blue is a small structural shadow, not an outline around everything. Individual examples mix roughly two main colors and one restrained accent, rather than the entire palette. Pale blue cloud wisps and tiny warm sparkles occur in only a few examples. Maintain generous negative space, no staged floor, no scenic background, no sticker border, and no photo-real material description. At 96 px the action and silhouette must still read. Match the construction, color economy, movement, and soft-matte finish; do not copy the sheet's particular subjects.",
    "storyworld": "Reference sheet 4: isolated imaginative miniature worlds on pure white, with broad gaps and no cards or borders. Each image is a tiny story moment, such as a figure at a portal, an animal under a starry arch, a butterfly on a dark plinth, or a fantastical object in a small geometric setting. Invent fresh subjects. Build with crisp 30-degree isometric bases and architecture: visible top and side planes, thick angular platform edges, a few simple stairs or cutouts. Vary the framing—some subjects stand on a small stage, others use an arch, open box, portal, or suspended object. Keep one large clear hero with only one or two supporting elements. Use the details that define the reference—strong silhouette, a few clean facets, occasional tiny stars inside a dark opening, selective color on stage edges, and a small round collectible medallion on some bases. Avoid extra ornamental tiling, repeated trim, clusters of props, dense star patterns, or elaborate surface marks. Keep each vignette to two main colors and one or two small accents, changing the combination from scene to scene; the reference uses blue, violet, coral, yellow, mint and lime, but not all together in every image. Gradients are limited to a few magical or translucent planes. Use crisp compact shadows and preserve the generous white negative space. No full environment, scenery, cards, borders, or repeated layout grid inside an individual vignette.",
    "pop": "Reference image 1: a dense but airy gallery grid of small colorful pictograms on pure white. Shapes are sharp, flat and constructed from a handful of bold geometric pieces. Silhouettes have playful character but are simplified, mostly frontal and immediately readable at small size. Use hard-edged solids—red, yellow, blue, orange, pink, mint and black—usually just two or three colors per symbol. Black appears as a shape or a few defining marks, not a universal stroke. No outline around every shape, no gradients, shadows, surface texture, perspective or 3D. Match the crisp flat graphic language, not the reference objects.",
    "clover": "Reference image 2: six sparse glyphs in a 3-by-2 arrangement on pale warm ivory. Use simple rounded silhouettes with smooth emerald-to-spring-green blending and only the faintest darker edge on selected overlaps. Green is the family color, but each object keeps a small natural accent: pale mint on openings/buttons, tiny orange or yellow hardware, and coral-red for a fruit. The shapes remain flat and clean, with no black contour, heavy extrusion, hard shadow or texture. Broad negative space is essential. Match the reference's muted gradient depth and restrained accent use, not its subjects.",
    "studio": "Reference image 3: isolated small everyday objects rendered as carefully made soft 3D miniatures on pure white. Objects use believable proportions and shallow three-quarter views, with gentle soft-edged studio lighting and a faint grounding shadow. Materials feel distinct and tactile—woven cloth, matte wood, ceramic, glass, paper, food and painted metal—yet surfaces remain clean and simplified. Use natural, slightly muted real-world colors. Keep each object alone with ample whitespace; no icon outlines, platform, surrounding room, extra decorative props, label or text. Match the style and scale, not the reference objects.",
    "concept": "Reference image 4: eight editorial metaphors arranged above captions in a four-by-two pale-gray card grid. Copy the visual grammar, not the words or exact subjects: roughly 1 px near-black hand-guided strokes at a 300 px cell size, a few unclosed or doubled contours, deliberately imperfect alignment, and one soft-lavender oval, circle, or angular patch per vignette. Most of each drawing remains unfilled open space. Examples of construction in the reference include a line-drawn optical instrument with lavender corner brackets, an outlined open box with a lavender disk and bulb, jagged mountain lines in front of a lavender circle, two outlined hands around one lavender disc, and a folded paper figure above a lavender ellipse. The line work does the explaining; lavender adds one visual anchor. Keep symbols modest, varied, and asymmetrical with generous air around them. Draw only the artwork: no card, pale-gray backing, caption, grid border, or text. Avoid thick strokes, complete filled silhouettes, multiple accent colors, shading, gradients, texture, and polished corporate-vector symmetry.",
}

def render(style):
    name, medium, form, finish, colors, avoid = style
    title = name.capitalize()
    if name in USER_STYLE_NOTES:
        calibration = USER_STYLE_NOTES[name] + " If this conversation still contains the user's reference sheet, use it as a style reference in an image tool that accepts conversation images. Otherwise follow these notes and the Style lock. Do not copy any subject from the sheet."
    else:
        calibration = f"These four publicly visible gallery images show the style across different subjects. When network access and the image tool permit, inspect them and provide them to the image tool as **style references only**: `https://sohna.dev/waterlemon/src/image/min/skill/{name}/{name}_1.png`, `https://sohna.dev/waterlemon/src/image/min/skill/{name}/{name}_4.png`, `https://sohna.dev/waterlemon/src/image/min/skill/{name}/{name}_7.png`, and `https://sohna.dev/waterlemon/src/image/min/skill/{name}/{name}_10.png`. Download into a temporary location, verify each file is an image, and follow the tool's reference-image instructions. Never copy a reference subject, symbols, or composition into the output; apply only its palette, construction, material, line weight, lighting, and detail density. If references cannot be loaded, use the Style lock above. Do not claim access to the paid source prompts."
    scale = {
        "colorcut": "Keep an individual glyph compact, centered, and simple enough to read at 64 px; preserve clear empty space around it.",
        "hologram": "Keep the icon compact and its broad facets readable at 64 px; avoid tiny facet lines and oversize glow.",
        "nightfall": "Keep the complete vignette compact and expressive at 96 px; preview it on deep slate #2B424A, while preserving transparent margins in the exported PNG.",
        "storyworld": "Check the complete story vignette at 128 px; keep one hero readable, the isometric edges crisp, details sparse, color accents restrained, and any stars confined to the intended void.",
        "pop": "Check the silhouette at 64 px; use crisp solid blocks and no unnecessary outline or shading.",
        "clover": "Check the glyph at 64 px; keep its green blending soft, any subject accent small, and dark-green depth minimal.",
        "studio": "Check the object at 128 px; keep realistic materials softly lit, recognizable and isolated on white.",
        "concept": "Check the metaphor at 128 px; keep the hand-guided linework delicate, the single lavender accent subordinate, the composition slightly asymmetric, and open space dominant.",
    }.get(name, "Make the silhouette unmistakable at 64 px.")
    review = "Review against the user's reference notes" if name in USER_STYLE_NOTES else "Review against the four style references"
    return f'''---
name: {name}-icon
description: Generate consistent {title} style product icons as high-resolution square transparent PNGs. Use when the user requests a {title} icon, an icon set, or this visual style for a product illustration.
---

# {title} icon

Create one or more polished product icons using an image generation tool available in the current session. If no image generation tool is available, provide the complete generation prompts so the user can run them elsewhere. Do not claim an image was created when only a prompt was produced.

## Guided selection

This style is already selected. Before generating, ask the user **one question at a time** in the order below. Wait for their answer before asking the next question. Use a question or selection tool when available; otherwise ask in chat and stop until the user replies. Never bundle questions, fill in an unanswered choice, or start image generation early. If a value was supplied in the opening request, show it as the proposed choice and still ask for confirmation at its step. Let the user say "default" or "back" to choose a default or revise the previous choice.

1. "One icon or a matching set?" Offer one / set.
2. "What should the icon or icons show?" Request one subject or a comma-separated subject list, matching the choice above.
3. "Where will you use them?" Offer app or product UI / marketing or social / other, and accept a custom answer.
4. "How should colors be chosen?" Offer this style's default palette / realistic object colors / custom palette. If custom, ask separately for primary, secondary, tertiary, accent, and detail colors, in that order. Accept hex codes or plain color names; offer "use style default" for each slot. Keep object colors recognizable unless strict brand colors are requested.
5. Summarize the selections and the fixed output (high-resolution square transparent PNG); ask **one** final question: "Generate with these choices, or change one?" If they choose change, revisit that choice and then confirm again.

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

{scale} The output is always a high-resolution **square PNG with genuine alpha transparency**. Never ask the user about background, canvas shape, resolution, or format. A style-reference background is only for calibration, never part of the output. Center the visible subject, including its glow or cast shadow, inside the middle 52% of both axes. Leave at least 24% transparent margin on every side. Make the visible bounds balanced around the canvas center; no object part, flourish, or shadow may touch the safe-zone boundary. Reduce the subject to its identifying parts; omit tiny details that disappear at the intended size. Preserve the same viewpoint, scale, stroke weight or material treatment, light direction, shadow softness, and palette across a set.

Build a prompt with the subject, every style lock above, and the chosen color mapping. Explicitly describe which parts of the subject get primary, secondary, and accent colors. Use the image generation tool directly with its transparent-background option enabled (`transparent_background: true` for `image_gen.imagegen`). Request its highest available native square resolution. Deliver a PNG with alpha, not an opaque image with a painted white or checkerboard background. For a series, reuse the same style block word for word and change only subject anatomy and user-requested colors. Prefer individual square deliverables over a contact sheet unless the user asks for a sheet.

{review}, especially material, outline thickness, highlight type, number of details, color proportions, and object scale. Inspect the actual output: width must equal height; it must contain transparent alpha outside the artwork; the visible alpha bounds, including shadows and glows, must fit inside the central 52% and be centered. Also check subject recognition, clipping, and text artifacts. If any check fails, revise and regenerate before delivering; do not stretch, crop, or label an opaque file as transparent. If the tool cannot meet these fixed requirements, state the limitation clearly instead of claiming a finished icon. Return the finished image or files and a short note identifying the style and palette used.
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
6. **Confirm.** Summarize every selected value and the fixed output (high-resolution square transparent PNG with 24% safe margins on every side). Ask exactly one question: "Generate with these choices, or change one?" If a change is requested, revisit that choice and confirm again. Never ask about background, canvas shape, resolution, or format.

Only an explicit answer advances the sequence. If the user leaves a question unanswered, stop and await the reply.

## Produce

After confirmation, use the selected style skill's Style lock, Visual calibration, and Generate sections. Use an image generation tool with transparent background enabled (`transparent_background: true` for `image_gen.imagegen`) and request its highest available native square resolution. Otherwise provide complete prompts and clearly state that no image was generated. For a set, keep perspective, scale, palette, material, and light consistent. Verify genuine alpha transparency, square dimensions, central-52% safe bounds, balanced centering, recognition, and absence of text or clipping. Regenerate failures before delivery. Return the result and a short summary of the choices.
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
        references = [f"assets/icons/{name}/{index:02}.png" for index in range(1, SITE_SAMPLE_COUNTS[name] + 1)]
        for reference in references:
            sample_asset = site_dir / reference
            if not sample_asset.exists():
                raise FileNotFoundError(f"Missing generated gallery sample: {sample_asset.relative_to(ROOT)}")
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
