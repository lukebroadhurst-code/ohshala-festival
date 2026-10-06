# Oh Shala Festival: website upgrade (static)

Plain HTML/CSS/JS, no build step to serve. Open `index.html`, or run `python3 -m http.server 4173` in this folder.

## Pages
`index` · `story` · `programme` · `tickets` · `gatherings` · `team` · `family` · `food` (food, stalls & treatments) · `faqs` · `contact` · `terms` · `404`

`build.py` regenerates every page except `index.html` (and refreshes the nav/footer on `index.html`), so edit content there and run `python3 build.py`. Styles are in `styles.css` (tokens at the top), behaviour in `main.js`.

## Brand
- **Logo:** the Oh Shala Bhakti Festival mark from the current site, shown white on the dark theme (CSS filter), in the nav, home hero and footer. Also the favicon.
- **Fonts:** the old site uses Adobe Fonts **Orpheus Pro** (headings, buttons) and **Adobe Garamond Pro** (body, nav). These are licensed to their Squarespace account, so the files are not copied here. `styles.css` already asks for `orpheus-pro` and `adobe-garamond-pro` first, with EB Garamond (body) and Cormorant (headings) as stand-ins, chosen by side-by-side comparison against the live fonts. To get the real fonts: Adobe Fonts → new web project → add both families → add the new domain → uncomment the `<link ... use.typekit.net/YOURKIT.css>` line in `index.html` and in `head()` in `build.py`, then re-run `build.py`.

## Before this goes live
1. **Forms:** the mailing-list form is front-end only (wire `#signup` to your mailing platform). The contact form opens the visitor's email app pre-filled (no backend needed).
2. **Hero film:** streams from the current Squarespace account (HLS, 3:07, 1080p) via hls.js. It will stop working when that site/plan is cancelled. Before then, re-host it (Cloudflare Stream, Mux, or an MP4 + HLS of your own) and change the two `data-hls` URLs in `index.html`.
3. **Hot-linked assets:** photos, logo and the 2026 schedule PDFs/images load from the current Squarespace site. Download them into this folder before that site is switched off.
4. **Tickets:** "Book on Ticket Tailor" points at the existing `/tickets` page (which holds the embed). Swap in the direct Ticket Tailor URL.
5. **Old site is broken in places:** these homepage links 404 today: `/treatments`, `/food`, `/create`, `/move`, `/explore`, `/move-1-1`, `/heal`, `/woodland`, `/move-1-3`, `/thihnkgita`, `/red-tent`, `/wiseheartproject`. Their content is folded into `programme`, `family` and `food`. Set up redirects when you go live.
6. **Content to confirm with Emily:**
   - Tent/area descriptions on `programme` (Move, Explore, Listen, Heal, Think Gita, Temple, Wiseheart, Live music) were drafted from the workshop list; the old pages are gone. Wiseheart is a placeholder.
   - Tickets: banner says "Golden Tickets live", old body copy said "opening soon".
   - Kids free: homepage said under 8s, FAQ said under 12s. New copy says "children go free" and defers to the tickets page.
   - **Terms** name "Parmoor Park" (not Penn House Estate) and need checking word-for-word against the original legal text. See the TODO comment in `terms.html`.
   - Contact page lists "Sarah" for facilitator applications (as on the old site) but she isn't on the team page.
   - Gatherings: the two upcoming events (17 Oct and 14 Nov 2026) come from the old site's live calendar and will go stale. Link them to individual Bookwhen events, or embed the Bookwhen feed.
   - Programme "2026 schedule" is last year's; replace when the 2027 schedule is ready.
   - Team page uses monogram arches. Add portraits when you have names matched to photos.
