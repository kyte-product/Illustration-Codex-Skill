---
name: illustration-icon-wizard
description: Guide the user through every icon decision one question at a time, then generate a polished icon or matching set in one of 32 visual styles.
---

# Illustration icon wizard

Lead a fully interactive icon creation flow. Ask exactly **one question per message or question-tool call** and wait for the answer before moving on. Prefer a selection tool when available, but use plain chat if needed. Never bundle choices into one question, silently accept an unanswered default, or generate before final confirmation. A user reply of "default" selects the suggested default for the current question; "back" revisits the previous selection. Preserve answers across turns. Even if the opening request contains choices, present each as a proposed selection at its step and ask the user to confirm it.

## Question sequence

1. **Style.** Show this concise catalog and ask which style to use: Clay, Flare, Zing, Gloss, Mist, Pebble, Drift, Ink, Cardboard, Linepop, Glide, Nimble, Jot, Riso, Marker, Glass, Watercolor, Yarn, Sketchy, Pulse, Candypop, Charcoal, Ceramic, Fuzzy, Colorcut, Hologram, Nightfall, Storyworld, Pop, Clover, Studio, Concept. If the user wants help choosing, ask a single follow-up question about the look they prefer, suggest up to three styles, then ask them to choose one. The selected style corresponds to the standalone `../<style>-icon/SKILL.md` beside this skill. Read and apply its Style lock, Visual calibration, and Generate sections. If that file is unavailable, explain that the pack is incomplete rather than inventing its instructions.
2. **Quantity.** Ask "One icon or a matching set?" Offer one / set.
3. **Subject.** Ask what the icon should show, or request a comma-separated subject list for a set.
4. **Use.** Ask where the icons will be used. Offer app or product UI / marketing or social / other.
5. **Color method.** Ask style default palette / realistic object colors / custom palette. If custom, ask primary, secondary, tertiary, accent, and detail colors **in five separate turns**, in that order. Accept hex codes or names; "default" uses the chosen style's direction for that slot.
6. **Confirm.** Summarize every selected value and the fixed output (high-resolution square transparent PNG with 32% safe margins on every side). Ask exactly one question: "Generate with these choices, or change one?" If a change is requested, revisit that choice and confirm again. Never ask about background, canvas shape, resolution, or format.

Only an explicit answer advances the sequence. If the user leaves a question unanswered, stop and await the reply.

## Produce

After confirmation, use the selected style skill's Style lock, Visual calibration, and Generate sections. Use an image generation tool with transparent background enabled (`transparent_background: true` for `image_gen.imagegen`) and request its highest available native square resolution. Otherwise provide complete prompts and clearly state that no image was generated. For a set, keep perspective, scale, palette, material, and light consistent. Verify genuine alpha transparency, square dimensions, central-36% safe bounds, balanced centering, recognition, and absence of text or clipping. Regenerate failures before delivery. Return the result and a short summary of the choices.
