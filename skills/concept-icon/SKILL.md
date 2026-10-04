---
name: concept-icon
description: Generate consistent Concept style product icons as high-resolution square transparent PNGs. Use when the user requests a Concept icon, an icon set, or this visual style for a product illustration.
---

# Concept icon

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

- Medium: spare editorial line-and-lavender conceptual illustration.
- Form: one clever metaphor assembled from two or three recognizable elements in a loose, asymmetrical composition; mostly front-facing with only slight perspective where the idea needs it.
- Surface and light: hairline near-black hand-guided contours, mostly open white interiors, one small flat soft-lavender shape that overlaps or sits behind the line drawing; a small near-black solid is allowed only as an essential focal part; no gradients, texture, modeled volume or shadows.
- Default color direction: near-black lines and transparent negative space dominate; muted lavender #A98CE7 is the only fill and occupies less than one quarter of the visible artwork.
- Avoid: thick outlines, uniformly geometric icon geometry, filled purple bodies, full black silhouettes, decorative detail, extra colors, caption text, card backgrounds or border boxes, text, letters, logos, watermarks, frames, unrelated props, and busy backgrounds.

## Visual calibration

Reference image 4: eight editorial metaphors arranged above captions in a four-by-two pale-gray card grid. Copy the visual grammar, not the words or exact subjects: roughly 1 px near-black hand-guided strokes at a 300 px cell size, a few unclosed or doubled contours, deliberately imperfect alignment, and one soft-lavender oval, circle, or angular patch per vignette. Most of each drawing remains unfilled open space. Examples of construction in the reference include a line-drawn optical instrument with lavender corner brackets, an outlined open box with a lavender disk and bulb, jagged mountain lines in front of a lavender circle, two outlined hands around one lavender disc, and a folded paper figure above a lavender ellipse. The line work does the explaining; lavender adds one visual anchor. Keep symbols modest, varied, and asymmetrical with generous air around them. Draw only the artwork: no card, pale-gray backing, caption, grid border, or text. Avoid thick strokes, complete filled silhouettes, multiple accent colors, shading, gradients, texture, and polished corporate-vector symmetry. If this conversation still contains the user's reference sheet, use it as a style reference in an image tool that accepts conversation images. Otherwise follow these notes and the Style lock. Do not copy any subject from the sheet.

## Generate

Check the metaphor at 128 px; keep the hand-guided linework delicate, the single lavender accent subordinate, the composition slightly asymmetric, and open space dominant. The output is always a high-resolution **square PNG with genuine alpha transparency**. Never ask the user about background, canvas shape, resolution, or format. A style-reference background is only for calibration, never part of the output. Center the visible subject, including its glow or cast shadow, inside the middle 65% of both axes. Leave at least 17.5% transparent margin on every side. Make the visible bounds balanced around the canvas center; no object part, flourish, or shadow may touch the safe-zone boundary. Reduce the subject to its identifying parts; omit tiny details that disappear at the intended size. Preserve the same viewpoint, scale, stroke weight or material treatment, light direction, shadow softness, and palette across a set.

Build a prompt with the subject, every style lock above, and the chosen color mapping. Explicitly describe which parts of the subject get primary, secondary, and accent colors. Use the image generation tool directly with its transparent-background option enabled (`transparent_background: true` for `image_gen.imagegen`). Request its highest available native square resolution. Deliver a PNG with alpha, not an opaque image with a painted white or checkerboard background. For a series, reuse the same style block word for word and change only subject anatomy and user-requested colors. Prefer individual square deliverables over a contact sheet unless the user asks for a sheet.

Review against the user's reference notes, especially material, outline thickness, highlight type, number of details, color proportions, and object scale. Inspect the actual output: width must equal height; it must contain transparent alpha outside the artwork; the visible alpha bounds, including shadows and glows, must fit inside the central 65% and be centered. Also check subject recognition, clipping, and text artifacts. If any check fails, revise and regenerate before delivering; do not stretch, crop, or label an opaque file as transparent. If the tool cannot meet these fixed requirements, state the limitation clearly instead of claiming a finished icon. Return the finished image or files and a short note identifying the style and palette used.
