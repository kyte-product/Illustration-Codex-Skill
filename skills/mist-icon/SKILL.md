---
name: mist-icon
description: Generate consistent Mist style product icons as high-resolution square transparent PNGs. Use when the user requests a Mist icon, an icon set, or this visual style for a product illustration.
---

# Mist icon

Create one or more polished product icons using an image generation tool available in the current session. If no image generation tool is available, provide the complete generation prompts so the user can run them elsewhere. Do not claim an image was created when only a prompt was produced.

## Guided selection

This style is already selected. Before generating, ask the user **one question at a time** in the order below. Wait for their answer before asking the next question. Use a question or selection tool when available; otherwise ask in chat and stop until the user replies. Never bundle questions, fill in an unanswered choice, or start image generation early. If a value was supplied in the opening request, show it as the proposed choice and still ask for confirmation at its step. Let the user say "default" or "back" to choose a default or revise the previous choice.

1. "One icon or a matching set?" Offer one / set.
2. "What should the icon or icons show? Describe the subject, or attach a reference illustration to restyle." For a set, accept a subject list, one image per subject, or one image whose subject should be repeated across the set. If an image is already attached, identify it and ask one question: "Use the attached illustration as the subject reference?" If an image contains multiple possible subjects, ask which one to use before advancing.
3. "Where will you use them?" Offer app or product UI / marketing or social / other, and accept a custom answer.
4. "How should colors be chosen?" Offer this style's default palette / realistic object colors / custom palette. If custom, ask separately for primary, secondary, tertiary, accent, and detail colors, in that order. Accept hex codes or plain color names; offer "use style default" for each slot. Keep object colors recognizable unless strict brand colors are requested.
5. Summarize the selections and the fixed output (high-resolution square transparent PNG); ask **one** final question: "Generate with these choices, or change one?" If they choose change, revisit that choice and then confirm again.

Only an explicit answer, including "default", advances a step. A skipped or unanswered question leaves the wizard paused. Preserve selections across turns.

## Uploaded illustration as subject

An image supplied by the user at the subject step defines **what** to draw. This skill's Style lock and Visual calibration define **how** to draw it. Inspect the uploaded image and retain its recognizable subject, silhouette, pose or viewpoint, key parts, and meaningful relationships between parts. Reconstruct those features in the selected style; do not simply recolor the source or preserve its original rendering. The selected palette controls colors unless the user explicitly asks to keep source colors. Discard the source background, surrounding card, labels, and incidental details. If several images are supplied, keep the mapping from each image to its requested output. Do not treat a user-uploaded subject image as a new style unless the user explicitly asks to add a style.

When generating, include the subject image as an image-tool reference. If the platform supplies an uploaded file ID, use its file-download tool to obtain a local path. Use local paths with `referenced_image_paths` when available; if the image exists only in the conversation, use the smallest `num_last_images_to_include` that includes it. Never pass both arguments to the same image generation call. If both subject and style-reference files are local, pass both paths and state clearly in the prompt which is the subject and which is style calibration. If they cannot be passed together, prioritize the user's subject image, spell out the selected style recipe in the prompt, and compare the result with the style examples. If the tool cannot read the uploaded image, ask for it to be attached again instead of inventing its contents.

## Style lock

- Medium: soft-volume digital app icon.
- Form: a single simple UI object with a compact rounded silhouette and only a few essential parts; mostly front-facing, with just enough three-quarter depth to read its edge.
- Surface and light: opaque, softly airbrushed pale-cyan-to-mid-blue shading, brightest at the upper left and deeper blue at the lower right; one broad milky highlight and a restrained cool edge glow, no drawn contour.
- Default color direction: powder blue and white occupy nearly all the icon; cobalt is limited to lower edges and recesses, with coral red on one tiny functional control.
- Avoid: glass or see-through material, hard black outlines, sharp specular streaks, heavy bloom, deep cast shadows, many controls, or metallic reflections, text, letters, logos, watermarks, frames, unrelated props, and busy backgrounds.

## Visual calibration

These four publicly visible gallery images show the style across different subjects. When network access and the image tool permit, inspect them and provide them to the image tool as **style references only**: `https://sohna.dev/waterlemon/src/image/min/skill/mist/mist_1.png`, `https://sohna.dev/waterlemon/src/image/min/skill/mist/mist_4.png`, `https://sohna.dev/waterlemon/src/image/min/skill/mist/mist_7.png`, and `https://sohna.dev/waterlemon/src/image/min/skill/mist/mist_10.png`. Download into a temporary location, verify each file is an image, and follow the tool's reference-image instructions. Never copy a reference subject, symbols, or composition into the output; apply only its palette, construction, material, line weight, lighting, and detail density. If references cannot be loaded, use the Style lock above. Do not claim access to the paid source prompts.

## Generate

Make the silhouette unmistakable at 64 px. The output is always a high-resolution **square PNG with genuine alpha transparency**. Never ask the user about background, canvas shape, resolution, or format. A style-reference background is only for calibration, never part of the output. Center the visible subject, including its glow or cast shadow, inside the middle 52% of both axes. Leave at least 24% transparent margin on every side. Make the visible bounds balanced around the canvas center; no object part, flourish, or shadow may touch the safe-zone boundary. Reduce the subject to its identifying parts; omit tiny details that disappear at the intended size. Preserve the same viewpoint, scale, stroke weight or material treatment, light direction, shadow softness, and palette across a set.

Build a prompt with the subject, every style lock above, and the chosen color mapping. Explicitly describe which parts of the subject get primary, secondary, and accent colors. Use the image generation tool directly with its transparent-background option enabled (`transparent_background: true` for `image_gen.imagegen`). Request its highest available native square resolution. Deliver a PNG with alpha, not an opaque image with a painted white or checkerboard background. For a series, reuse the same style block word for word and change only subject anatomy and user-requested colors. Prefer individual square deliverables over a contact sheet unless the user asks for a sheet.

When a user supplies a reference illustration, include it in the generation call as the **subject reference**. Preserve its identifying shape, pose, viewpoint, and essential parts while translating all linework, lighting, material, texture, and detail density into this style. Use the chosen color method; do not accidentally copy the source image's background or art style. If an uploaded file ID is available, download it to a local path. With `image_gen.imagegen`, pass local images through `referenced_image_paths`; when an attachment has no local path, use the smallest `num_last_images_to_include` that contains it. Never provide both parameters together. If a local style image is available alongside a local subject image, provide both as paths and label their roles in the prompt. If only the subject can be attached, describe this style's visual recipe in full and review the output against its examples. If the image input cannot be accessed, ask the user to reattach it rather than guessing.

Review against the four style references, especially material, outline thickness, highlight type, number of details, color proportions, and object scale. If a subject image was supplied, compare the generated subject's silhouette, viewpoint, pose and essential details with it while judging the rendering against this style. Inspect the actual output: width must equal height; it must contain transparent alpha outside the artwork; the visible alpha bounds, including shadows and glows, must fit inside the central 52% and be centered. Also check subject recognition, clipping, and text artifacts. If any check fails, revise and regenerate before delivering; do not stretch, crop, or label an opaque file as transparent. If the tool cannot meet these fixed requirements, state the limitation clearly instead of claiming a finished icon. Return the finished image or files and a short note identifying the style and palette used.
