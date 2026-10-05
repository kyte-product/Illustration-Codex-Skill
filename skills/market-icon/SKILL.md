---
name: market-icon
description: Generate consistent Market style product icons as high-resolution square transparent PNGs. Use when the user requests a Market icon, an icon set, or this visual style for a product illustration.
---

# Market icon

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

- Medium: polished miniature commercial 3D illustration.
- Form: one familiar service, shopping, food, people or utility subject rendered as a small isolated icon; compact three-quarter view with a clear silhouette, or a nearly frontal view for simple symbols.
- Surface and light: soft cool studio light from the upper left, believable but simplified matte or satin materials, gently rounded edges, controlled highlights and a very short faint contact shadow; show only the few seams, openings or fittings needed to identify the subject.
- Default color direction: a recognizable emerald green accent ties the set together; balance it with charcoal, warm tan, cream and natural subject colors, using bright orange or gold only for a small focal detail.
- Avoid: brand names or logos, printed words, photorealistic microdetail, long or dark ground shadows, large floor discs, glossy toy plastic, flat vector fills, clay texture, crowded props, scenery or a colored background, text, letters, logos, watermarks, frames, unrelated props, and busy backgrounds.

## Visual calibration

Reference sheet 5: twenty small, widely spaced 3D service icons in an even four-column layout on a barely cool off-white field. They include objects, food, a few stylized human heads or hands, and a few simple symbols, all at similar modest visual scale. Copy the rendering language, not its specific subjects, brand mark or wording. Each icon has a clean silhouette and a slight studio-model volume: simple rounded geometry, a realistic but carefully reduced material cue, modest bevels, one soft upper-left highlight and a restrained shallow shadow immediately below. Green recurs as a bag, cap, trim, ribbon, cup or interface detail, while charcoal, warm kraft, ivory and natural food colors keep objects recognizable. Some examples mix two related objects into one tight vignette, but most use one hero and no extra decoration. Tiny graphic symbols are allowed only when they communicate the subject. Keep the darks small and the ground shadow pale; preserve the airy scale and clean visual rhythm. The reference's nearly white sheet is presentation only: export isolated transparent PNGs with no printed brand text or logo. If this conversation still contains the user's reference sheet, use it as a style reference in an image tool that accepts conversation images. Otherwise follow these notes and the Style lock. Do not copy any subject from the sheet.

## Generate

Check the miniature at 96 px: material and subject must read through broad forms, while any contact shadow stays faint and close beneath it. The output is always a high-resolution **square PNG with genuine alpha transparency**. Never ask the user about background, canvas shape, resolution, or format. A style-reference background is only for calibration, never part of the output. Center the visible subject, including its glow or cast shadow, inside the middle 52% of both axes. Leave at least 24% transparent margin on every side. Make the visible bounds balanced around the canvas center; no object part, flourish, or shadow may touch the safe-zone boundary. Reduce the subject to its identifying parts; omit tiny details that disappear at the intended size. Preserve the same viewpoint, scale, stroke weight or material treatment, light direction, shadow softness, and palette across a set.

Build a prompt with the subject, every style lock above, and the chosen color mapping. Explicitly describe which parts of the subject get primary, secondary, and accent colors. Use the image generation tool directly with its transparent-background option enabled (`transparent_background: true` for `image_gen.imagegen`). Request its highest available native square resolution. Deliver a PNG with alpha, not an opaque image with a painted white or checkerboard background. For a series, reuse the same style block word for word and change only subject anatomy and user-requested colors. Prefer individual square deliverables over a contact sheet unless the user asks for a sheet.

Review against the user's reference notes, especially material, outline thickness, highlight type, number of details, color proportions, and object scale. Inspect the actual output: width must equal height; it must contain transparent alpha outside the artwork; the visible alpha bounds, including shadows and glows, must fit inside the central 52% and be centered. Also check subject recognition, clipping, and text artifacts. If any check fails, revise and regenerate before delivering; do not stretch, crop, or label an opaque file as transparent. If the tool cannot meet these fixed requirements, state the limitation clearly instead of claiming a finished icon. Return the finished image or files and a short note identifying the style and palette used.
