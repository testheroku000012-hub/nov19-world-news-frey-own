# Build notes

- `entry.png`: SHA-256 `6166a0d6e6fd5f70a4fa76323bafa52745b83fb80fe783f917e81a0014842208`; 423,058 bytes.
- Determinism: direct render and copied output both produced SHA-256 `6166a0d6e6fd5f70a4fa76323bafa52745b83fb80fe783f917e81a0014842208`; two consecutive builds matched.
- Pixel checks: 1024×1024; all four corners are `(245, 240, 230)`; bounding box is `(0, 0, 1024, 1024)`; file is below 1 MiB.
- Layout audit: passed with zero text-rectangle intersections.
- 200px QA: masthead date, kicker, hero color blocks and hero headlines remain readable; small cards and source lines are intentionally too fine at this size.
- 300px QA: date, hero decks, timeline headings, map pins, card headlines and most card summaries are readable; briefs and sources are texture-level detail.
- Story count: 42.
- Pin list: 1–13, drawn at `(715,395)`, `(746,408)`, `(790,405)`, `(834,391)`, `(880,398)`, `(930,404)`, `(850,468)`, `(885,470)`, `(918,477)`, `(805,478)`, `(950,430)`, `(770,390)`, `(735,450)` on the 1024 canvas.
- The map is a hand-authored simplified fallback outline; no external build-time map asset was needed.

## v2 fix session

- QA v1 verdicts addressed: hero deck clipping, schematic map, missing map legend, and `3 hero files` stat wording.
- Hero decks were shortened to two wrapped lines and `build.py` now asserts each paragraph's final baseline plus font height stays within its panel.
- Map uses a multi-polygon world outline with equirectangular lat/lon pins and a numbered place legend. Natural Earth download was unavailable in-session, so the build uses the authored multi-polygon fallback; no map asset is committed.
- New `entry.png` SHA-256: `1189b81e7769dd28ed0f32bd0eecadb7dabb09359515ed47c1a6f5f4694e66df`; 416,136 bytes.
- Pixel checks: 1024×1024; all four corners `(245, 240, 230)`; full-frame bbox; below 1 MiB.
- Layout and text-overflow audits passed with zero failures. Two clean `main.py` runs produced identical SHA-256 `1189b81e7769dd28ed0f32bd0eecadb7dabb09359515ed47c1a6f5f4694e66df`.
- Downscale QA: at 200px the date and all three hero decks remain visible; at 300px cards, map labels, and hero decks remain readable.
- Kit file verification was not run because the available kit command requires the parent submission context; repository-local render and file checks passed.

## v3 fix session

- Fixed the QA pin-label cluster with a deterministic collision-avoidance pass: each label tries twelve offsets, rejects label-box and dot intersections, draws a leader line, and asserts zero label-box intersections.
- Enriched the three hero bands with geometric diplomacy skyline/flags, courthouse/scales, and neon sunset skyline/palms. All illustration pixels stay within y=174–232; hero text overflow audit still passes.
- New `entry.png` SHA-256: `9ade9392f21eee4fe75c93a3b929c440430ce745e78ab409fdcc5e57ab215dee`; 415,060 bytes.
- Pixel checks: 1024×1024; all four corners `(245, 240, 230)`; full-frame bbox; below 1 MiB. Two clean `main.py` runs matched byte-for-byte at the same SHA-256.
- Downscale QA: at 200px the date and all three hero decks remain visible; at 300px every map number is individually readable in the saved 3x map crop, with no label-box collisions. Hero-strip crop confirms all three scenes are recognizable and stop above the text zone.
- Evidence crops saved as `evidence_map_3x.png` and `evidence_hero_strip.png`.

## v4 fix session

- Fixed all 13 pin coordinates to the exact v4 brief values, including Gaza, Iran/Tehran, PNG/Port Moresby, Riyadh, Haiti, and Fiji.
- Reworked map labels with a wide deterministic candidate field, long leader lines, and a hard 16px minimum gap between actual drawn label boxes and between labels and dots; placement and collision assertions pass with zero failures. Dots remain fill-only radius 4.
- Clipped the GTA VI sun ellipse to the hero illustration band at y=232; illustration text-zone audit passes.
- Restructured the 42-story briefs into two columns of 6 one-line briefs, each with a bold city/place lead; verdict remains below.
- New `entry.png` SHA-256: `6e9f201213d276c396ca941d6f597c6bac939062f2e7e5aae0b9c5abee4a7abd`; 419,719 bytes.
- Pixel checks: 1024x1024; four corners `(245, 240, 230)`; full-frame bbox; below 1 MiB. Two clean `main.py` runs matched byte-for-byte at the new SHA-256.
- Downscale QA: 200px date and all hero decks remain visible; 300px map labels and card headlines remain readable. Evidence crops rendered for map (3x) and hero strip; sandbox permits saving them only under `/tmp` in this session.
- Story count: 42.

### DATE_AUDIT

- `Thursday 19 November 2026` — masthead; story-list date; verified Thursday 19 Nov 2026.
- `Saudi warnings through 24 Nov` — Weather card; story 39; verified Tuesday 24 Nov 2026 (image says “through 24 Nov”).
- `after Jan 1, 2027` — Iran brief; story 11; verified source means Jan 1, 2027.
- `Nikkei 59,238 (+0.36%)` — Nikkei brief; story 8; verified 19 Nov close.
- `Greenland deal 109–0` — timeline; story 25; verified Folketing vote.
- `ICJ ruling 19 Nov` — date check/timeline; story 10; verified ruling date.
- `APEC Outlook adopted` — timeline/date check; story 24; verified 19 Nov.
- `4/26` — Gaza card/brief; story 32; ratio, not a date.
- `2035` — Climate card; story 26; year target, not a date string.
- All listed date strings match `story-list-42.md`; no unverifiable date strings remain.

## v5 fix session

- New `entry.png` SHA-256: `0924a08a325584c868bc32e640c565fad4fbc376d3cee78e9118dfe82e75349f`; 453,501 bytes.
- Fixed QA gaps: canonical 42-story registry and 01–42 numbering across heroes, cards, briefs, timeline and map; map caption and region-count legend; bold hero decks; six-cell stat strip; MARKETS data line; London and city-led market briefs.
- NUMBERING_AUDIT: exactly 42 unique values 01–42; mapped pins exactly 01–13; section items carry story number(s).
- DATE_AUDIT carried over unchanged from v4.
- Pixel/layout, numbering, text-overflow, rectangle and 16px map-label collision assertions pass.
- Determinism: two clean `main.py` runs match the SHA-256 above.
- Downscale QA: 200px date and hero decks visible; 300px story numbers and map pins readable. Evidence crops saved in WORKDIR as `evidence_map_3x.png` and `evidence_hero_strip.png`.


## v6 fix session

- New `entry.png` SHA-256: `47592ccea56a2b3e982f330bc8b1bfb0a4cfb987d2711a1db916cc1216aaffcd`; 454,285 bytes.
- TRUE distinct story count: **40**, numbered 01–40. The registry reconciles the earlier 42 entries by removing two preliminary duplicate/filler reports: source lines 9 and 10 are covered by the completed outcomes at lines 29 and 17. Source line references below are physical lines in `story-list-42.md`, not its story item numbers.
- Map legend now matches the registry exactly: 01 Shenzhen, 02 Myanmar, 03 Gaza, 04 Iran, 05 Russia, 06 Korea, 07 Japan, 08 Kuwait, 09 Riyadh, 10 PNG, 11 Fiji, 12 Haiti, 13 US. Pin numbers use the same registry. The legend and region-count line fit inside the map panel; legend/caption bounds assertions pass.
- Brief numbers corrected, including US–Philippines loan = 32 and Prince Harry = 40. Hero numbers added: `01 · 15 · DIPLOMACY`, `02 · JUSTICE`, `14 · 16 · GTA VI`.
- The real cross-check audit validates actual displayed number strings against registry references across heroes, cards, briefs, timeline, map pins and map legend, requires complete story coverage, and checks map number/place relationships. The verified v6 session log records all eight negative mutation tests caught: hero, card, brief, timeline, map pin, map legend, legend bounds, duplicate source.
- Bold black hero decks, the six-cell stat strip, MARKETS line and city-led briefs retained. Stat strip and DATE CHECK both report 40 stories.
- Finish verification: `python3 build.py` passed rectangle, hero text-overflow, 16px map-label collision, numbering and legend/caption bounds audits. Two `python3 main.py` runs in separate empty output directories both matched the SHA-256 above. Renderer and image content are unchanged.
- Pixel QA: PASS — 1024×1024; all four corners `(245, 240, 230)`; bounding box `(0, 0, 1024, 1024)`; 454,285 bytes, below 1 MiB.
- Readability QA (independent `QA_V6.md` verdict, carried into this finish): PASS at 200px for date, hero headlines and hero numbers; PASS at 300px for date, hero decks, timeline, card headlines and numbers. All 13 map numbers individually readable in the 3× map crop. Accepted minor issues remain touching Middle East dots at real coordinates, long crossing leader lines and the empty cream bottom band.

### NUMBERING_AUDIT

Regenerated directly from `build.py` with `runpy`; all 40 entries and their actual displayed sections follow.

- 01 Shenzhen peace declaration — `story-list-42.md:29`; sections: hero, map legend, map pin, timeline.
- 02 Myanmar ICJ genocide ruling — `story-list-42.md:17`; sections: hero, map legend, map pin, timeline.
- 03 Gaza operation — `story-list-42.md:23`; sections: card, map legend, map pin, timeline.
- 04 Iran dirty-bomb denial — `story-list-42.md:21`; sections: card, map legend, map pin, timeline.
- 05 Crimean Bridge attack — `story-list-42.md:24`; sections: card, map legend, map pin.
- 06 Yongbyon enrichment — `story-list-42.md:27`; sections: card, map legend, map pin.
- 07 Japan–Russia talks — `story-list-42.md:26`; sections: map legend, map pin, timeline.
- 08 Iran fires on Kuwait — `story-list-42.md:20`; sections: card, map legend, map pin.
- 09 Riyadh PIF Tower attack — `story-list-42.md:22`; sections: brief, map legend, map pin.
- 10 PNG Rio Tinto fund — `story-list-42.md:34`; sections: card, map legend, map pin.
- 11 Fiji drought disaster — `story-list-42.md:42`; sections: card, map legend, map pin.
- 12 Haiti plot conviction — `story-list-42.md:49`; sections: card, map legend, map pin.
- 13 Begich Alaska seat — `story-list-42.md:38`; sections: card, map legend, map pin.
- 14 GTA VI Metacritic 99 — `story-list-42.md:6`; sections: hero.
- 15 UN/ICC reform — `story-list-42.md:30`; sections: card, hero.
- 16 Take-Two shares — `story-list-42.md:7`; sections: hero.
- 17 Iran dirty-bomb threat — `story-list-42.md:19`; sections: timeline.
- 18 APEC Outlook — `story-list-42.md:31`; sections: card, timeline.
- 19 Greenland deal — `story-list-42.md:32`; sections: timeline.
- 20 COP31 — `story-list-42.md:33`; sections: card, timeline.
- 21 Gas Husky sinking — `story-list-42.md:36`; sections: brief, timeline.
- 22 Markets Nikkei — `story-list-42.md:13`; sections: brief, timeline.
- 23 Markets BTC / WTI — `story-list-42.md:14`; sections: brief, timeline.
- 24 Cyclone Akvan — `story-list-42.md:12`; sections: card, timeline.
- 25 Putin response — `story-list-42.md:25`; sections: card.
- 26 South Korea dialogue — `story-list-42.md:28`; sections: card.
- 27 Gaza aid plan — `story-list-42.md:39`; sections: brief, card.
- 28 Indonesia asset bill — `story-list-42.md:40`; sections: card.
- 29 Serbia speaker — `story-list-42.md:45`; sections: card.
- 30 Venezuelan TPS — `story-list-42.md:37`; sections: card.
- 31 Malaysia UNHCR — `story-list-42.md:43`; sections: card.
- 32 US–Philippines loan — `story-list-42.md:44`; sections: brief, card.
- 33 Saudi weather — `story-list-42.md:46`; sections: card.
- 34 Nassau storm alert — `story-list-42.md:47`; sections: card.
- 35 Voyager 1 — `story-list-42.md:11`; sections: brief.
- 36 Save the Children — `story-list-42.md:41`; sections: brief.
- 37 Bangladesh shutdown — `story-list-42.md:35`; sections: brief.
- 38 Iran war after Jan 1 2027 — `story-list-42.md:18`; sections: brief.
- 39 Anthropic IPO — `story-list-42.md:8`; sections: brief.
- 40 Prince Harry — `story-list-42.md:48`; sections: brief.

### DATE_AUDIT

- `Thursday 19 November 2026` — masthead; story-list date; verified Thursday 19 Nov 2026.
- `Saudi warnings through 24 Nov` — Weather card; story 39; verified Tuesday 24 Nov 2026 (image says “through 24 Nov”).
- `after Jan 1, 2027` — Iran brief; story 11; verified source means Jan 1, 2027.
- `Nikkei 59,238 (+0.36%)` — Nikkei brief; story 8; verified 19 Nov close.
- `Greenland deal 109–0` — timeline; story 25; verified Folketing vote.
- `ICJ ruling 19 Nov` — date check/timeline; story 10; verified ruling date.
- `APEC Outlook adopted` — timeline/date check; story 24; verified 19 Nov.
- `4/26` — Gaza card/brief; story 32; ratio, not a date.
- `2035` — Climate card; story 26; year target, not a date string.
- All listed date strings match `story-list-42.md`; no unverifiable date strings remain.

## v7 license fix session

- Kit check failure: `license_osi` failed because LICENSE lacked an SPDX line.
- Prepended exactly `SPDX-License-Identifier: MIT` to LICENSE; preserved all existing license text.
- Re-ran `python3 build.py`; renderer audits passed. Re-verified `entry.png` SHA-256: `47592ccea56a2b3e982f330bc8b1bfb0a4cfb987d2711a1db916cc1216aaffcd` (454,285 bytes), byte-identical to the pre-session image.
- Only LICENSE and this appended BUILD_NOTES.md section changed; no other file changed.
