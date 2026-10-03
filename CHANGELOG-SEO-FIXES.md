# HindiFont.co.in — SEO & Quality Fixes (3 Oct 2026)

116 files modified, 30 deleted, new folders `/assets/` and `/files/`.
Design is unchanged. Screenshots were compared before and after.

## Deploy notes (do these after uploading)
1. In **AdSense → Ads → Auto ads**: turn Auto ads off, or at least turn off in-page "anchor/vignette" placements. Auto ads are the main cause of layout shift (CLS).
2. In **Google Search Console**: submit the new `/sitemap.xml`, then use URL Inspection on `/`, `/tools/kruti-dev-to-unicode/` and `/fonts/mukta/`.
3. After deploy, check these URLs:
   - `curl -I https://hindifont.co.in/does-not-exist` should return **404**.
   - `curl -I https://hindifont.co.in/tools/kruti-dev-to-mangal/` should return **301** to `/tools/kruti-dev-to-unicode/`.
4. **Legacy fonts** (Kruti Dev, DevLys, Chanakya, Shree Lipi, Preeti, Agra, Richa, Chandas) are **not hosted**, because their redistribution licence is unclear. If you obtain a licence or an official source, put the file in `/files/` and change the sidebar button on that font page.

## Critical fixes
- **Converters rebuilt.** The old Kruti Dev / DevLys ↔ Unicode converters produced wrong output (for example `fdrkc` became "िकताब" instead of "किताब"). A new shared engine, `/assets/legacy-converter.v1.js`, handles ि ordering, reph (र्), half forms and nukta. It passes 46/46 tests in both directions. Used by: kruti-dev-to-unicode, unicode-to-kruti-dev, devlys-to-unicode, unicode-to-devlys.
- **Font downloads now work.** 12 open-source (SIL OFL) fonts are self-hosted as ZIPs with their licence in `/files/`. They are sourced from google/fonts, and Lohit was built from its upstream source.
  - **Mangal / Kokila / Aparajita:** these pages are now guides to installing them free via the Windows "Devanagari Supplemental Fonts" optional feature. These are Microsoft-licensed and cannot be redistributed.
  - **Legacy fonts:** these pages now give honest "not hosted" info, with links to the converter or a free Unicode alternative.
  - The 26 meta-refresh `/download/` pages were deleted and now 301 to the font page.
- **Font previews:** font pages and `/tools/font-preview/` now load the real fonts. User text in the preview tool is HTML-escaped.
- **Voice typing:** `_headers` used `microphone=()`, which blocked the tool. It is now `microphone=(self)`.
- **Keyboard charts:** the Remington, Kruti Dev and DevLys charts were wrong. They have been rebuilt from the same key table the tested converter uses. The Inscript chart and the virtual keyboard (`/tools/hindi-keyboard/`) now use the standard Inscript layout. Wrong "home row" text was removed from 5 font pages.
- **Ponnala (a Telugu font) removed** from the Hindi site, with a 301 to `/fonts/`.

## Accuracy and trust
- Removed "500+ fonts", "10L+ downloads" and "India's #1" everywhere (pages, OG alt text, schema, manifest). The site now states real numbers: 25 fonts, 12 free downloads.
- SSC information corrected: Hindi typing uses Mangal (Unicode) with a Remington GAIL or Inscript keyboard, and readers are told to confirm in their notice. This was fixed on 8 pages, and "official font" claims were softened.
- Licence lines corrected (for example, Mukta is SIL OFL, not "personal use only").
- Removed the unsupported "85–95% accuracy" claim from the translate pages.
- Typing certificate now says it is a practice certificate, not an official one.
- Typing tutor pages no longer claim lessons exist; they show a lesson plan and practice links.
- Privacy policy: added AdSense/cookie, Google Translate, voice-typing and local-processing disclosures.

## Technical SEO
- `_redirects`: removed the unsupported `/* /404.html 404` rule (Pages serves 404.html automatically). Added 301s for merged and removed pages.
- `robots.txt`: removed the `Disallow` that hid the noindex tags on download pages.
- `404.html`: now `noindex`, with no canonical, no ads and no schema, and adds links to Tools and Typing Tests.
- `sitemap.xml`: regenerated with only the 85 indexable URLs and real `lastmod` dates. Removed the self-entry and the external XSL.
- Merged cannibalising tools with 301s:
  - kruti-dev-to-mangal → kruti-dev-to-unicode
  - mangal-to-kruti-dev → unicode-to-kruti-dev
  - tools/english-to-hindi → tools/hindi-typing
- `noindex,follow` added to the 21 templated translate pairs (English↔Hindi stays indexed) and to the 3 typing-tutor pages. All of these still work for users.
- Fixed the "X Font Font" duplication in titles and headings.
- Font pages for non-hosted fonts were retitled from "Free Download" to "Download Guide".

## Structured data
- Homepage: Organization now has a 512px PNG logo. The WebSite search box was removed (it pointed to a search that doesn't exist).
- FAQPage schema regenerated from the visible FAQs on 84 pages, and removed on 4 pages with no visible FAQ.
- Font pages: `SoftwareApplication` replaced with `CreativeWork` (with a `license` field for OFL fonts).
- Blog `Article`: added `image`, `dateModified`, `mainEntityOfPage` and publisher logo. Real publish dates come from git history, and the visible dates now match.
- Removed the `WebApplication` type from static keyboard-chart pages. Added a BreadcrumbList to `/translate/`.

## Performance
- 8 shared inline `<style>` blocks (byte-identical across 105 pages) moved to content-hashed files in `/assets/css/`. They are cached for a year, saving about 23–38 KB per page view after the first.
- Google Fonts: removed unused weights (Plus Jakarta 300, Playfair regular 600).
- AdSense script removed from the 404 page and the old redirect pages.
- `favicon.ico` is now a real multi-size ICO.

## Internal linking
- Homepage has a new "Popular Hindi Tools" section with 8 tools.
- Keyboard Layouts and Typing Tutor added to the footer and mobile nav.
- Duplicate tool cards left over from the merge were removed.
