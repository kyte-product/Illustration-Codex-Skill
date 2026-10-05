# Illustration icon skills for Codex

An original set of 33 image generation styles plus a guided wizard skill. The first 24 style recipes were calibrated against 287 public previews from the [Waterlemon gallery](https://sohna.dev/waterlemon/). Nine additional styles—Colorcut, Hologram, Nightfall, Market, Storyworld, Pop, Clover, Studio, and Concept—were studied from reference sheets supplied by the user. Gallery example sheets were generated with these recipes to test their results. These are independently written skills, not Waterlemon's paid prompts or Mac app.

## Install

Attach [`illustration-icon-skills.zip`](illustration-icon-skills.zip) to Codex Chat and ask it to install the skills, or copy the `skills/` folders into your Codex skills directory. Each folder contains a standalone `SKILL.md`.

## Use

For a guided session, say:

> Use the `illustration-icon-wizard` skill. Ask me one question at a time and wait for each selection.

The wizard asks for style, quantity, subject, intended use, palette, and final confirmation. A custom palette is chosen one color slot at a time. Every icon is generated as a high-resolution square transparent PNG, with its visible artwork centered inside the middle 52% of the canvas and at least 24% clear space on every side; the wizard does not ask about these fixed output settings. A direct style skill also asks its remaining questions one at a time.

To start with a particular style, say for example:

> Use the `linepop-icon` skill to make a camera icon. Primary `#39FF14`, secondary `#FFF700`, tertiary `#DCE6F7`, accent white, detail `#111111`.

For a set, provide the subjects when prompted. The skill keeps scale, angle, lighting, and palette consistent. If your Codex session has an image generation tool, it produces the icons directly. Otherwise, it returns ready to use image prompts.

Each of the first 24 style skills links four public gallery images for visual calibration. When `sohna.dev` is reachable and the image tool accepts references, the skill can use them as style examples without copying the shown subjects. The nine user-supplied styles include detailed visual notes; when the original screenshots remain available in a conversation, the image tool can use them as references. Image generation remains variable, so preview and revise results that drift from the selected style. Check the exported file's actual square dimensions, alpha channel, and safe margins before delivery.

Styles: Clay, Flare, Zing, Gloss, Mist, Pebble, Drift, Ink, Cardboard, Linepop, Glide, Nimble, Jot, Riso, Marker, Glass, Watercolor, Yarn, Sketchy, Pulse, Candypop, Charcoal, Ceramic, Fuzzy, Colorcut, Hologram, Nightfall, Storyworld, Pop, Clover, Studio, and Concept.

## Maintain

The skill files are generated from [`scripts/build_skills.py`](scripts/build_skills.py). Run `python3 scripts/build_skills.py` to rebuild them, or `python3 scripts/build_skills.py --check` to verify the checked in files. To add gallery examples from a new transparent contact sheet, supply a JSON file mapping style names to sheet paths to [`scripts/prepare_gallery.py`](scripts/prepare_gallery.py). That helper needs Pillow, NumPy, and SciPy; it extracts and centers each example in a square transparent PNG.

## Style gallery website

The responsive gallery and usage guide are in [`site/`](site/index.html). Run it locally from the repository root:

```sh
python3 -m http.server 8000 --directory site
```

Then open `http://localhost:8000`. The style catalog is generated from the same definitions as the skill pack. Each style has square transparent examples stored locally in `site/assets/icons/` (six for Clover, twelve for the others), so gallery images do not depend on the reference site loading in the browser. The independent site uses original branding and usage copy.

For Vercel, keep the project root set to the repository root (`.`). [`vercel.json`](vercel.json) configures a static deployment whose output is `site/`. The files must be committed and pushed to the connected Git branch before Vercel can deploy them.
