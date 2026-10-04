---
name: storyworld-icon
description: Generate consistent Storyworld style product icons with configurable palettes and transparent backgrounds. Use when the user requests a Storyworld icon, an icon set, or this visual style for a product illustration.
---

# Storyworld icon

Create one or more polished product icons using an image generation tool available in the current session. If no image generation tool is available, provide the complete generation prompts so the user can run them elsewhere. Do not claim an image was created when only a prompt was produced.

## Guided selection

This style is already selected. Before generating, ask the user **one question at a time** in the order below. Wait for their answer before asking the next question. Use a question or selection tool when available; otherwise ask in chat and stop until the user replies. Never bundle questions, fill in an unanswered choice, or start image generation early. If a value was supplied in the opening request, show it as the proposed choice and still ask for confirmation at its step. Let the user say "default" or "back" to choose a default or revise the previous choice.

1. "One icon or a matching set?" Offer one / set.
2. "What should the icon or icons show?" Request one subject or a comma-separated subject list, matching the choice above.
3. "Where will you use them?" Offer app or product UI / marketing or social / other, and accept a custom answer.
4. "How should colors be chosen?" Offer this style's default palette / realistic object colors / custom palette. If custom, ask separately for primary, secondary, tertiary, accent, and detail colors, in that order. Accept hex codes or plain color names; offer "use style default" for each slot. Keep object colors recognizable unless strict brand colors are requested.
5. "What background do you want?" Offer native Storyworld background (warm white #FFFEF8) / transparent / custom solid color. If custom solid, ask for its color in a separate question. Preserve the user's choice; the native background is the closest visual match to this style's reference sheet.
6. "What canvas shape do you want?" Offer square / portrait / landscape. Square is recommended for icons.
7. "What size or intended export do you want?" Offer high resolution PNG / another size or format. Do not promise a format the available tool cannot produce; explain its actual output if needed.
8. Summarize all selections and ask **one** final question: "Generate with these choices, or change one?" If they choose change, revisit that choice and then confirm again.

Only an explicit answer, including "default", advances a step. A skipped or unanswered question leaves the wizard paused. Preserve selections across turns.

## Style lock

- Medium: fantastical isometric storybook diorama illustration.
- Form: one surreal narrative hero or tiny architectural world arranged as a self-contained vignette; use a precise 30-degree isometric view for platforms and structures, with sculptural characters or objects integrated into the scene.
- Surface and light: crisp vector-like facets, hard-edged geometric planes, bold colored side faces, selective luminous gradients on portals or magical forms, deep midnight-navy starfield openings, tiny white stars, and a clean compact cast shadow.
- Default color direction: electric cobalt and royal blue, violet and magenta, warm lemon yellow, coral red, mint and lime; set glowing color against deep navy voids and generous white space.
- Avoid: uniform gray 3D renders, soft toy materials, thin technical wireframes, broad painterly backgrounds, realistic landscapes, dense clutter, tiny illegible surface detail, or generic emoji treatment, text, letters, logos, watermarks, frames, unrelated props, and busy backgrounds.

## Visual calibration

Reference sheet 4: a collection of isolated, imaginative miniature worlds on pure white, spaced far apart with no cards or borders. Each vignette is a tiny narrative moment, not merely a single product icon: examples of the visual grammar include a person crossing a luminous threshold, paired hands emerging from portals, an hourglass suspended in a starry cabinet, an animal framed by a night-sky arch, a vividly patterned butterfly on a dark platform, a large lock on a blue plinth, a cloud creature in an open box, a potion vessel, or a bird perched on colorful architectural forms. Never reuse these exact subjects; invent varied storybook symbols. Use crisp 30-degree isometric construction for bases and architecture, with clearly thick platforms, visible top and side planes, stepped edges, and sharp geometry. Some vignettes stand on a small square or diamond stage; others use an arch, open box, portal, or suspended object as the frame. Let each hero be large and immediately readable, supported by only a few deliberate details. A deep navy or near-black interior void with tiny white stars is a recurring magical contrast, but reserve it for openings and selected objects. Use saturated cobalt, royal blue, violet, magenta, lemon yellow, coral, mint and lime in distinct hard-edged planes; allow a few narrow gradients on glowing portals and facets. Small round numbered medallions sometimes sit on the front corner of a stage as a collectible-world detail. Lighting and shadows stay crisp and compact. Preserve abundant white negative space; no full environment, scenery, cards, borders, or repeated layout grid inside an individual vignette. If this conversation still contains the user's reference sheet, use it as a style reference in an image tool that accepts conversation images. Otherwise follow these notes and the Style lock. Do not copy any subject from the sheet.

## Generate

Check the complete story vignette at 128 px; keep its hero readable, isometric stage edges crisp, and any starfield confined to the intended void. Keep the whole object or mini-scene within the central 65% of the canvas width and height, leaving generous balanced empty space. Reduce the subject to its identifying parts; omit tiny details that disappear at the intended size. Preserve the same viewpoint, scale, stroke weight or material treatment, light direction, shadow softness, and palette across a set. A solid background is a uniform field, not an app tile or surrounding scene.

Build a prompt with the subject, every style lock above, the chosen color mapping, selected canvas, and requested background. Explicitly describe which parts of the subject get primary, secondary, and accent colors. Use the image generation tool directly. Set its transparent background option when the user wants a transparent icon. For a series, reuse the same style block word for word and change only subject anatomy and user-requested colors. Prefer individual deliverables over a contact sheet unless the user asks for a sheet.

Review against the user's reference notes, especially material, outline thickness, highlight type, number of details, color proportions, and object scale. Also check subject recognition, clipping, text artifacts, and unintended background. If it drifts toward a generic style, revise the prompt with specific forbidden traits and regenerate. Return the finished image or files and a short note identifying the style and palette used.
