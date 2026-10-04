---
name: colorcut-icon
description: Generate consistent Colorcut style product icons with configurable palettes and transparent backgrounds. Use when the user requests a Colorcut icon, an icon set, or this visual style for a product illustration.
---

# Colorcut icon

Create one or more polished product icons using an image generation tool available in the current session. If no image generation tool is available, provide the complete generation prompts so the user can run them elsewhere. Do not claim an image was created when only a prompt was produced.

## Guided selection

This style is already selected. Before generating, ask the user **one question at a time** in the order below. Wait for their answer before asking the next question. Use a question or selection tool when available; otherwise ask in chat and stop until the user replies. Never bundle questions, fill in an unanswered choice, or start image generation early. If a value was supplied in the opening request, show it as the proposed choice and still ask for confirmation at its step. Let the user say "default" or "back" to choose a default or revise the previous choice.

1. "One icon or a matching set?" Offer one / set.
2. "What should the icon or icons show?" Request one subject or a comma-separated subject list, matching the choice above.
3. "Where will you use them?" Offer app or product UI / marketing or social / other, and accept a custom answer.
4. "How should colors be chosen?" Offer this style's default palette / realistic object colors / custom palette. If custom, ask separately for primary, secondary, tertiary, accent, and detail colors, in that order. Accept hex codes or plain color names; offer "use style default" for each slot. Keep object colors recognizable unless strict brand colors are requested.
5. "What background do you want?" Offer native Colorcut background (warm ivory #FFFEF8) / transparent / custom solid color. If custom solid, ask for its color in a separate question. Preserve the user's choice; the native background is the closest visual match to this style's reference sheet.
6. "What canvas shape do you want?" Offer square / portrait / landscape. Square is recommended for icons.
7. "What size or intended export do you want?" Offer high resolution PNG / another size or format. Do not promise a format the available tool cannot produce; explain its actual output if needed.
8. Summarize all selections and ask **one** final question: "Generate with these choices, or change one?" If they choose change, revisit that choice and then confirm again.

Only an explicit answer, including "default", advances a step. A skipped or unanswered question leaves the wizard paused. Preserve selections across turns.

## Style lock

- Medium: soft-edged colorful vector glyph.
- Form: one small compact pictogram built from two to five rounded, irregular interlocking color shapes, front-facing without perspective.
- Surface and light: mostly flat digital fills, softly blended overlap edges, occasional clipped edge, hole or inset; no physical paper texture, stroke or grounding shadow.
- Default color direction: bright cobalt, leaf green, vermilion, pink, orange and pale lime; limit each glyph to two or three hues.
- Avoid: large logo-like scale, hard flat SVG edges, physical paper grain, black outlines, glossy 3D, realism, uniform rainbow fill, lettering, or a pictogram inside a card, text, letters, logos, watermarks, frames, unrelated props, and busy backgrounds.

## Visual calibration

Reference sheet 1: twenty very small glyphs in an open four-column grid on warm ivory. Keep each glyph modest inside its cell, surrounded by conspicuous space. Stand-alone pictograms use two to five soft, organic vector pieces that interlock like simple cutouts; this is digital illustration, not textured craft paper. Some edges gently blend or overlap; a clipped edge, hole or inset can identify the object. No contour stroke, grounding shadow or extra decoration. The colors are vivid but friendly and usually limited to two or three hues per symbol. Match the visual grammar, never the reference subjects. If this conversation still contains the user's reference sheet, use it as a style reference in an image tool that accepts conversation images. Otherwise follow these notes and the Style lock. Do not copy any subject from the sheet.

## Generate

Keep an individual glyph compact, centered, and simple enough to read at 64 px; preserve clear empty space around it. Keep the whole object or mini-scene within the central 65% of the canvas width and height, leaving generous balanced empty space. Reduce the subject to its identifying parts; omit tiny details that disappear at the intended size. Preserve the same viewpoint, scale, stroke weight or material treatment, light direction, shadow softness, and palette across a set. A solid background is a uniform field, not an app tile or surrounding scene.

Build a prompt with the subject, every style lock above, the chosen color mapping, selected canvas, and requested background. Explicitly describe which parts of the subject get primary, secondary, and accent colors. Use the image generation tool directly. Set its transparent background option when the user wants a transparent icon. For a series, reuse the same style block word for word and change only subject anatomy and user-requested colors. Prefer individual deliverables over a contact sheet unless the user asks for a sheet.

Review against the user's reference notes, especially material, outline thickness, highlight type, number of details, color proportions, and object scale. Also check subject recognition, clipping, text artifacts, and unintended background. If it drifts toward a generic style, revise the prompt with specific forbidden traits and regenerate. Return the finished image or files and a short note identifying the style and palette used.
