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

- Medium: compact painted editorial spot illustration with graphic 2.5D depth.
- Form: one expressive subject, usually tilted, lifting, bending or in motion; build its silhouette from a few broad hand-shaped pieces and allow at most one meaningful secondary element.
- Surface and light: matte color planes with a soft short gradient on selected curves, one narrow darker underside or inner cut, and a quiet upper-left highlight; edges stay clean but slightly organic; any cloud curl, steam, sparkle or motion mark must explain the action.
- Default color direction: choose two main colors and one small accent per icon from coral-peach, powder blue, leaf green, warm orange and butter yellow; use midnight blue only for recesses or underside cuts; design for a deep blue-charcoal #2B424A presentation field but export transparent artwork.
- Avoid: realistic product detail, glossy toy plastic, bright specular stripes, heavy outlines, all-over brush texture, grain, many tiny parts, symmetric emoji poses, full environments, or decorative confetti, text, letters, logos, watermarks, frames, unrelated props, and busy backgrounds.

## Visual calibration

Reference sheet 3: twenty-four tiny editorial vignettes float in a regular four-column grid on uniform deep slate. The slate is a presentation color, not part of the exported icon. Most subjects are recognizable from a quick silhouette and a single action: a form springs upward, pours, grows, flies, unfurls or reaches. A related prop appears only when it strengthens that action. Forms are compact and slightly asymmetrical, with broad simplified color shapes, softly rounded tips, occasional sharp fold or dark interior wedge, and selective subtle shading rather than uniform extrusion. Bright and pale colors carry the subject; midnight blue is a small structural shadow, not an outline around everything. Individual examples mix roughly two main colors and one restrained accent, rather than the entire palette. Pale blue cloud wisps and tiny warm sparkles occur in only a few examples. Maintain generous negative space, no staged floor, no scenic background, no sticker border, and no photo-real material description. At 96 px the action and silhouette must still read. Match the construction, color economy, movement, and soft-matte finish; do not copy the sheet's particular subjects. If this conversation still contains the user's reference sheet, use it as a style reference in an image tool that accepts conversation images. Otherwise follow these notes and the Style lock. Do not copy any subject from the sheet.

## Generate

Keep the complete vignette compact and expressive at 96 px; preview it on deep slate #2B424A, while preserving transparent margins in the exported PNG. The output is always a high-resolution **square PNG with genuine alpha transparency**. Never ask the user about background, canvas shape, resolution, or format. A style-reference background is only for calibration, never part of the output. Center the visible subject, including its glow or cast shadow, inside the middle 52% of both axes. Leave at least 24% transparent margin on every side. Make the visible bounds balanced around the canvas center; no object part, flourish, or shadow may touch the safe-zone boundary. Reduce the subject to its identifying parts; omit tiny details that disappear at the intended size. Preserve the same viewpoint, scale, stroke weight or material treatment, light direction, shadow softness, and palette across a set.

Build a prompt with the subject, every style lock above, and the chosen color mapping. Explicitly describe which parts of the subject get primary, secondary, and accent colors. Use the image generation tool directly with its transparent-background option enabled (`transparent_background: true` for `image_gen.imagegen`). Request its highest available native square resolution. Deliver a PNG with alpha, not an opaque image with a painted white or checkerboard background. For a series, reuse the same style block word for word and change only subject anatomy and user-requested colors. Prefer individual square deliverables over a contact sheet unless the user asks for a sheet.

Review against the user's reference notes, especially material, outline thickness, highlight type, number of details, color proportions, and object scale. Inspect the actual output: width must equal height; it must contain transparent alpha outside the artwork; the visible alpha bounds, including shadows and glows, must fit inside the central 52% and be centered. Also check subject recognition, clipping, and text artifacts. If any check fails, revise and regenerate before delivering; do not stretch, crop, or label an opaque file as transparent. If the tool cannot meet these fixed requirements, state the limitation clearly instead of claiming a finished icon. Return the finished image or files and a short note identifying the style and palette used.
