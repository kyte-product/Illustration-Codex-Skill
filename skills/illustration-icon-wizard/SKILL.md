---
name: illustration-icon-wizard
description: Guide the user through every icon decision one question at a time, then generate a polished icon or matching set in one of 33 visual styles.
---

# Illustration icon wizard

Lead a fully interactive icon creation flow. Ask exactly **one question per message or question-tool call** and wait for the answer before moving on. Prefer a selection tool when available, but use plain chat if needed. Never bundle choices into one question, silently accept an unanswered default, or generate before final confirmation. A user reply of "default" selects the suggested default for the current question; "back" revisits the previous selection. Preserve answers across turns. Even if the opening request contains choices, present each as a proposed selection at its step and ask the user to confirm it.

## Question sequence

1. **Style.** Show this concise catalog and ask which style to use: Clay, Flare, Zing, Gloss, Mist, Pebble, Drift, Ink, Cardboard, Linepop, Glide, Nimble, Jot, Riso, Marker, Glass, Watercolor, Yarn, Sketchy, Pulse, Candypop, Charcoal, Ceramic, Fuzzy, Colorcut, Hologram, Nightfall, Market, Storyworld, Pop, Clover, Studio, Concept. If the user wants help choosing, ask a single follow-up question about the look they prefer, suggest up to three styles, then ask them to choose one. The selected style corresponds to the standalone `../<style>-icon/SKILL.md` beside this skill. Read and apply its Style lock, Visual calibration, and Generate sections. If that file is unavailable, explain that the pack is incomplete rather than inventing its instructions.
2. **Quantity.** Ask "One icon or a matching set?" Offer one / set.
3. **Subject.** Ask "What should the icon show? Describe it, or attach a reference illustration to restyle." For a set, accept a subject list, one image per subject, or one image to reinterpret as matching variations. If the user already attached an image, say which image you see and ask one question: "Use the attached illustration as the subject reference?" If the image contains multiple possible subjects, ask which one to use before moving on. Do not ask for a written description when a clear image was supplied.
4. **Use.** Ask where the icons will be used. Offer app or product UI / marketing or social / other.
5. **Color method.** Ask style default palette / realistic object colors / custom palette. If custom, ask primary, secondary, tertiary, accent, and detail colors **in five separate turns**, in that order. Accept hex codes or names; "default" uses the chosen style's direction for that slot.
6. **Confirm.** Summarize every selected value and the fixed output (high-resolution square transparent PNG with 24% safe margins on every side). Ask exactly one question: "Generate with these choices, or change one?" If a change is requested, revisit that choice and confirm again. Never ask about background, canvas shape, resolution, or format.

Only an explicit answer advances the sequence. If the user leaves a question unanswered, stop and await the reply.

## Subject images

A user-uploaded image supplies the subject and its recognizable structure, pose, viewpoint, and key details. The selected style skill supplies the rendering, material, light, outlines and level of detail. Rebuild the subject in that style rather than applying a color filter or copying the source background. The selected color method decides whether to follow the style palette, the object's natural colors, or the user's custom colors. Keep each uploaded image associated with its requested output in a set. Follow the selected style skill's instructions for attaching subject and style images to the image generation tool.

## Produce

After confirmation, use the selected style skill's Style lock, Visual calibration, and Generate sections. Pass any uploaded subject illustration to the image generation tool and identify it as subject content, not as a style guide. Use transparent background (`transparent_background: true` for `image_gen.imagegen`) and request the highest available native square resolution. Otherwise provide complete prompts and clearly state that no image was generated. For a set, keep perspective, scale, palette, material, and light consistent. Verify likeness to the uploaded subject when present, genuine alpha transparency, square dimensions, central-52% safe bounds, balanced centering, recognition, and absence of text or clipping. Regenerate failures before delivery. Return the result and a short summary of the choices.
