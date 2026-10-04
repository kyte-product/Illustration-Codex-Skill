---
name: nightfall-icon
description: Generate consistent Nightfall style product icons as high-resolution square transparent PNGs. Use when the user requests a Nightfall icon, an icon set, or this visual style for a product illustration.
---

# Nightfall icon

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

- Medium: matte painted editorial spot illustration.
- Form: small tilted or floating vignette on a solid deep-slate field; one expressive subject with no more than one related prop or motion flourish.
- Surface and light: rounded softly beveled shapes, restrained hand-painted gradients and very light pigment grain, gentle upper-left light; sparse cloud fragments or tiny sparkles.
- Default color direction: coral-peach, pale sky blue, grass green, warm orange and sunflower yellow against dark blue-charcoal #2B424A.
- Avoid: white card backgrounds, realistic surface detail, dead-center product renders, glossy plastic, neon effects, hard black outlines, full environments, or crowded props, text, letters, logos, watermarks, frames, unrelated props, and busy backgrounds.

## Visual calibration

Reference sheet 3: twenty-four isolated editorial vignettes in a regular 4-by-6 arrangement on uniform deep slate. Every small vignette has one expressive object and at most one related prop or motion flourish. Use lively tilt, hover, spring, pour or growth. Rounded matte forms have gentle bevels, restrained hand-painted gradients and a lightly painted finish; they are neither flat monochrome nor glossy plastic. Peach, coral, pale blue, green, orange and yellow stand out clearly against the slate. A few vignettes use short pale cloud fragments or tiny sparkles. Keep generous dark negative space and never place items in framed cards or detailed scenes. If this conversation still contains the user's reference sheet, use it as a style reference in an image tool that accepts conversation images. Otherwise follow these notes and the Style lock. Do not copy any subject from the sheet.

## Generate

Keep the vignette compact and expressive at 96 px; preserve a clear dark margin around every shape. The output is always a high-resolution **square PNG with genuine alpha transparency**. Never ask the user about background, canvas shape, resolution, or format. A style-reference background is only for calibration, never part of the output. Center the visible subject, including its glow or cast shadow, inside the middle 65% of both axes. Leave at least 17.5% transparent margin on every side. Make the visible bounds balanced around the canvas center; no object part, flourish, or shadow may touch the safe-zone boundary. Reduce the subject to its identifying parts; omit tiny details that disappear at the intended size. Preserve the same viewpoint, scale, stroke weight or material treatment, light direction, shadow softness, and palette across a set.

Build a prompt with the subject, every style lock above, and the chosen color mapping. Explicitly describe which parts of the subject get primary, secondary, and accent colors. Use the image generation tool directly with its transparent-background option enabled (`transparent_background: true` for `image_gen.imagegen`). Request its highest available native square resolution. Deliver a PNG with alpha, not an opaque image with a painted white or checkerboard background. For a series, reuse the same style block word for word and change only subject anatomy and user-requested colors. Prefer individual square deliverables over a contact sheet unless the user asks for a sheet.

Review against the user's reference notes, especially material, outline thickness, highlight type, number of details, color proportions, and object scale. Inspect the actual output: width must equal height; it must contain transparent alpha outside the artwork; the visible alpha bounds, including shadows and glows, must fit inside the central 65% and be centered. Also check subject recognition, clipping, and text artifacts. If any check fails, revise and regenerate before delivering; do not stretch, crop, or label an opaque file as transparent. If the tool cannot meet these fixed requirements, state the limitation clearly instead of claiming a finished icon. Return the finished image or files and a short note identifying the style and palette used.
