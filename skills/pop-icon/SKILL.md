---
name: pop-icon
description: Generate consistent Pop style product icons with configurable palettes and transparent backgrounds. Use when the user requests a Pop icon, an icon set, or this visual style for a product illustration.
---

# Pop icon

Create one or more polished product icons using an image generation tool available in the current session. If no image generation tool is available, provide the complete generation prompts so the user can run them elsewhere. Do not claim an image was created when only a prompt was produced.

## Guided selection

This style is already selected. Before generating, ask the user **one question at a time** in the order below. Wait for their answer before asking the next question. Use a question or selection tool when available; otherwise ask in chat and stop until the user replies. Never bundle questions, fill in an unanswered choice, or start image generation early. If a value was supplied in the opening request, show it as the proposed choice and still ask for confirmation at its step. Let the user say "default" or "back" to choose a default or revise the previous choice.

1. "One icon or a matching set?" Offer one / set.
2. "What should the icon or icons show?" Request one subject or a comma-separated subject list, matching the choice above.
3. "Where will you use them?" Offer app or product UI / marketing or social / other, and accept a custom answer.
4. "How should colors be chosen?" Offer this style's default palette / realistic object colors / custom palette. If custom, ask separately for primary, secondary, tertiary, accent, and detail colors, in that order. Accept hex codes or plain color names; offer "use style default" for each slot. Keep object colors recognizable unless strict brand colors are requested.
5. "What background do you want?" Offer native Pop background (pure white #FFFFFF) / transparent / custom solid color. If custom solid, ask for its color in a separate question. Preserve the user's choice; the native background is the closest visual match to this style's reference sheet.
6. "What canvas shape do you want?" Offer square / portrait / landscape. Square is recommended for icons.
7. "What size or intended export do you want?" Offer high resolution PNG / another size or format. Do not promise a format the available tool cannot produce; explain its actual output if needed.
8. Summarize all selections and ask **one** final question: "Generate with these choices, or change one?" If they choose change, revisit that choice and then confirm again.

Only an explicit answer, including "default", advances a step. A skipped or unanswered question leaves the wizard paused. Preserve selections across turns.

## Style lock

- Medium: bold flat geometric editorial pictogram.
- Form: one familiar object or character reduced to a compact, instantly recognizable silhouette assembled from a few large geometric shapes; mostly front-facing with no perspective.
- Surface and light: crisp hard-edged solid fills, clean cutout overlaps, minimal internal divisions, no outline except where a deliberate black shape defines a feature; completely flat with no shading.
- Default color direction: bright red, yellow, cobalt, sky blue, orange, pink, mint and black; choose only a few clear blocks per symbol, with white negative space.
- Avoid: gradients, shadows, texture, realistic detail, thin strokes, rounded 3D volume, excessive internal parts, or using every palette color in every symbol, text, letters, logos, watermarks, frames, unrelated props, and busy backgrounds.

## Visual calibration

Reference image 1: a dense but airy gallery grid of small colorful pictograms on pure white. Shapes are sharp, flat and constructed from a handful of bold geometric pieces. Silhouettes have playful character but are simplified, mostly frontal and immediately readable at small size. Use hard-edged solids—red, yellow, blue, orange, pink, mint and black—usually just two or three colors per symbol. Black appears as a shape or a few defining marks, not a universal stroke. No outline around every shape, no gradients, shadows, surface texture, perspective or 3D. Match the crisp flat graphic language, not the reference objects. If this conversation still contains the user's reference sheet, use it as a style reference in an image tool that accepts conversation images. Otherwise follow these notes and the Style lock. Do not copy any subject from the sheet.

## Generate

Check the silhouette at 64 px; use crisp solid blocks and no unnecessary outline or shading. Keep the whole object or mini-scene within the central 65% of the canvas width and height, leaving generous balanced empty space. Reduce the subject to its identifying parts; omit tiny details that disappear at the intended size. Preserve the same viewpoint, scale, stroke weight or material treatment, light direction, shadow softness, and palette across a set. A solid background is a uniform field, not an app tile or surrounding scene.

Build a prompt with the subject, every style lock above, the chosen color mapping, selected canvas, and requested background. Explicitly describe which parts of the subject get primary, secondary, and accent colors. Use the image generation tool directly. Set its transparent background option when the user wants a transparent icon. For a series, reuse the same style block word for word and change only subject anatomy and user-requested colors. Prefer individual deliverables over a contact sheet unless the user asks for a sheet.

Review against the user's reference notes, especially material, outline thickness, highlight type, number of details, color proportions, and object scale. Also check subject recognition, clipping, text artifacts, and unintended background. If it drifts toward a generic style, revise the prompt with specific forbidden traits and regenerate. Return the finished image or files and a short note identifying the style and palette used.
