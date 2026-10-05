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

- Medium: small polished commercial 3D spot illustration.
- Form: a compact isolated everyday subject, usually one hero object; across a set vary products, food, a simplified floating head, a hand-led action and simple service symbols; use shallow three-quarter views for objects and near-front views for faces and symbols.
- Surface and light: soft cool upper-left studio light, simple believable matte or satin materials, slight selective bevels and a tiny pale contact shadow only where an object touches ground; facial features and seams are few and deliberate, and no surface needs photorealistic microdetail.
- Default color direction: emerald green #00A86B recurs as one useful part of most icons but does not flood every object; balance it with charcoal, ivory, warm kraft tan, natural skin and food colors, with occasional tiny gold or red focal details.
- Avoid: brand names, logos or printed words, giant expressive cartoon eyes, detailed facial anatomy, photorealistic microtexture, heavy dark oval ground shadows, glossy inflated toy plastic, uniformly green objects, flat vector fills, thick outlines, scenery or colored backgrounds, text, letters, logos, watermarks, frames, unrelated props, and busy backgrounds.

## Visual calibration

Reference sheet 5: twenty tiny, widely spaced service illustrations in a four-column by five-row grid on a barely cool off-white presentation field. Each subject uses only about half the width of its grid cell, so the wide quiet margins are a defining trait. The sheet mixes insulated bags, food, small human heads, hands, service glyphs and functional objects; do not reduce this style to twelve green hardware products. Object proportions are simple and slightly rounded, but readable details are selective: a handle or strap, one seam, a glass rim, a few food layers or a tiny control. Faces have compact features and simple glasses or headwear, without big animation eyes or complex skin texture. Material cues distinguish paper, cloth, ceramic, food, metal and skin, yet most surfaces remain satin or matte with a small restrained upper-left highlight. Grounded objects get a short pale gray contact shadow almost tucked beneath the silhouette; floating heads and symbols need no floor. Emerald green is the repeated family cue, sometimes a large panel and sometimes only trim; charcoal and warm neutrals provide contrast, while food keeps natural colors. Tiny sparks or confetti are rare and meaningful. The original pale field is presentation only; deliver genuine transparent pixels around the complete artwork and never copy its brand text, marks or exact subjects. If this conversation still contains the user's reference sheet, use it as a style reference in an image tool that accepts conversation images. Otherwise follow these notes and the Style lock. Do not copy any subject from the sheet.

## Generate

Check the miniature at 96 px: the subject reads through broad forms, green feels selective, and any contact shadow stays pale and tucked close beneath the object. For a set, include varied subject categories rather than repeating one product type. The output is always a high-resolution **square PNG with genuine alpha transparency**. Never ask the user about background, canvas shape, resolution, or format. A style-reference background is only for calibration, never part of the output. Center the visible subject, including its glow or cast shadow, inside the middle 52% of both axes. Leave at least 24% transparent margin on every side. Make the visible bounds balanced around the canvas center; no object part, flourish, or shadow may touch the safe-zone boundary. Reduce the subject to its identifying parts; omit tiny details that disappear at the intended size. Preserve the same viewpoint, scale, stroke weight or material treatment, light direction, shadow softness, and palette across a set.

Build a prompt with the subject, every style lock above, and the chosen color mapping. Explicitly describe which parts of the subject get primary, secondary, and accent colors. Use the image generation tool directly with its transparent-background option enabled (`transparent_background: true` for `image_gen.imagegen`). Request its highest available native square resolution. Deliver a PNG with alpha, not an opaque image with a painted white or checkerboard background. For a series, reuse the same style block word for word and change only subject anatomy and user-requested colors. Prefer individual square deliverables over a contact sheet unless the user asks for a sheet.

Review against the user's reference notes, especially material, outline thickness, highlight type, number of details, color proportions, and object scale. Inspect the actual output: width must equal height; it must contain transparent alpha outside the artwork; the visible alpha bounds, including shadows and glows, must fit inside the central 52% and be centered. Also check subject recognition, clipping, and text artifacts. If any check fails, revise and regenerate before delivering; do not stretch, crop, or label an opaque file as transparent. If the tool cannot meet these fixed requirements, state the limitation clearly instead of claiming a finished icon. Return the finished image or files and a short note identifying the style and palette used.
