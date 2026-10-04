---
name: storyworld-icon
description: Generate consistent Storyworld style product icons as high-resolution square transparent PNGs. Use when the user requests a Storyworld icon, an icon set, or this visual style for a product illustration.
---

# Storyworld icon

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

- Medium: fantastical isometric storybook diorama illustration.
- Form: one surreal narrative hero or tiny architectural world arranged as a self-contained vignette; use precise 30-degree isometric geometry for platforms and structures, supported by only one or two meaningful elements.
- Surface and light: crisp vector-like facets, clean hard-edged planes, a few clear steps or cutouts, selective gradient on a portal or magical form, occasional deep midnight-navy starry opening, and a short compact cast shadow.
- Default color direction: restrained but lively color grouping: usually two main hues with one or two small accents selected from cobalt, royal blue, violet, magenta, lemon yellow, coral, mint and lime; vary combinations between scenes and reserve navy for cavities.
- Avoid: rainbow-colored scenes, more than four prominent hues in one vignette, ornamental tiling, excessive trim, clusters of tiny props, dense starfields, tiny illegible detail, uniform gray 3D renders, soft toy materials, broad painterly backgrounds, realistic landscapes, or generic emoji treatment, text, letters, logos, watermarks, frames, unrelated props, and busy backgrounds.

## Visual calibration

Reference sheet 4: isolated imaginative miniature worlds on pure white, with broad gaps and no cards or borders. Each image is a tiny story moment, such as a figure at a portal, an animal under a starry arch, a butterfly on a dark plinth, or a fantastical object in a small geometric setting. Invent fresh subjects. Build with crisp 30-degree isometric bases and architecture: visible top and side planes, thick angular platform edges, a few simple stairs or cutouts. Vary the framing—some subjects stand on a small stage, others use an arch, open box, portal, or suspended object. Keep one large clear hero with only one or two supporting elements. Use the details that define the reference—strong silhouette, a few clean facets, occasional tiny stars inside a dark opening, selective color on stage edges, and a small round collectible medallion on some bases. Avoid extra ornamental tiling, repeated trim, clusters of props, dense star patterns, or elaborate surface marks. Keep each vignette to two main colors and one or two small accents, changing the combination from scene to scene; the reference uses blue, violet, coral, yellow, mint and lime, but not all together in every image. Gradients are limited to a few magical or translucent planes. Use crisp compact shadows and preserve the generous white negative space. No full environment, scenery, cards, borders, or repeated layout grid inside an individual vignette. If this conversation still contains the user's reference sheet, use it as a style reference in an image tool that accepts conversation images. Otherwise follow these notes and the Style lock. Do not copy any subject from the sheet.

## Generate

Check the complete story vignette at 128 px; keep one hero readable, the isometric edges crisp, details sparse, color accents restrained, and any stars confined to the intended void. The output is always a high-resolution **square PNG with genuine alpha transparency**. Never ask the user about background, canvas shape, resolution, or format. A style-reference background is only for calibration, never part of the output. Center the visible subject, including its glow or cast shadow, inside the middle 36% of both axes. Leave at least 32% transparent margin on every side. Make the visible bounds balanced around the canvas center; no object part, flourish, or shadow may touch the safe-zone boundary. Reduce the subject to its identifying parts; omit tiny details that disappear at the intended size. Preserve the same viewpoint, scale, stroke weight or material treatment, light direction, shadow softness, and palette across a set.

Build a prompt with the subject, every style lock above, and the chosen color mapping. Explicitly describe which parts of the subject get primary, secondary, and accent colors. Use the image generation tool directly with its transparent-background option enabled (`transparent_background: true` for `image_gen.imagegen`). Request its highest available native square resolution. Deliver a PNG with alpha, not an opaque image with a painted white or checkerboard background. For a series, reuse the same style block word for word and change only subject anatomy and user-requested colors. Prefer individual square deliverables over a contact sheet unless the user asks for a sheet.

Review against the user's reference notes, especially material, outline thickness, highlight type, number of details, color proportions, and object scale. Inspect the actual output: width must equal height; it must contain transparent alpha outside the artwork; the visible alpha bounds, including shadows and glows, must fit inside the central 36% and be centered. Also check subject recognition, clipping, and text artifacts. If any check fails, revise and regenerate before delivering; do not stretch, crop, or label an opaque file as transparent. If the tool cannot meet these fixed requirements, state the limitation clearly instead of claiming a finished icon. Return the finished image or files and a short note identifying the style and palette used.
