# David Kreismann – Personal Website

Source of [davidkreismann.github.io](https://davidkreismann.github.io), built with Jekyll on the [Academic Pages](https://github.com/academicpages/academicpages.github.io) template. English and German pages are deployed to GitHub Pages via [GitHub Actions](.github/workflows/jekyll.yml).

## Where things live

| What | File |
| --- | --- |
| Name, sidebar, social links, analytics | `_config.yml` |
| Top navigation | `_data/navigation.yml`, `_includes/masthead.html` |
| Home pages | `_pages/about.md`, `_pages/de/about.md` |
| English CV content (web and PDF) | `_data/cv.yml` |
| German web CV content | `_data/cv_de.yml` |
| Web CV pages and entry layout | `_pages/cv.md`, `_pages/de/cv.md`, `_includes/cv-entry.html` |
| English CV PDF layout | `_pages/cv-pdf.tex` (compiled to `/files/David_Kreismann_CV.pdf` on deploy) |
| Publications and patents | `_publications/` |
| German publication detail pages | `_pages/de/publications/` |
| Projects and German summaries | `_portfolio/`; German detail pages: `_pages/de/projects/` |
| Blog posts in both languages | `_posts/` |
| Shared project/blog list entries | `_includes/archive-card.html` |
| Translated interface labels | `_data/ui-text.yml` |
| Profile picture and favicons | `images/profile.jpg`, `images/favicon*`, `favicon.ico` |
| CV, project and mobile profile styles | `_sass/layout/_cv.scss` |
| Navigation styles and behavior | `_sass/layout/_navigation.scss`, `assets/js/plugins/jquery.greedy-navigation.js` |
| Theme switching and other JavaScript | `assets/js/_main.js` |

The web CV shows education, experience, awards and activities. Papers and patents have their own Publications page and remain included in the English PDF CV.

## English and German pages

Translated pages use `lang: de` and a `translation:` URL pointing to their English counterpart. Add the reciprocal `translation:` URL to the English page as well. The language switch stays on the corresponding page; direct URLs determine the language without automatic redirects.

Paper titles stay in their original language. German paper pages reuse the English abstract through `_includes/publication-original.html`; update the abstract in `_publications/`. Keep the German page's publication metadata in sync with the original. German project summaries for the project list use `excerpt_de` in `_portfolio/`.

## Run locally

Install Ruby and Bundler, then run:

```bash
bundle install
bundle exec jekyll serve -l -H localhost
```

Open [localhost:4000](http://localhost:4000). Restart Jekyll after changing `_config.yml`.

Jekyll generates the CV's LaTeX source, but does not compile its PDF. The PDF link will return 404 in a fresh local preview unless you compile or provide the PDF separately.

## JavaScript changes

The site loads the committed `assets/js/main.min.js` bundle. After editing the JavaScript sources, rebuild it and include the updated bundle in your commit:

```bash
npm install
npm run build:js
```

SCSS changes are compiled by Jekyll. CSS and JavaScript URLs include a build timestamp to prevent browsers from retaining outdated assets after deployment.

## Deployment and analytics

Pushing to `master` runs `.github/workflows/jekyll.yml`. The workflow builds the production site, compiles the CV PDF, removes the generated LaTeX sources, subsets icon fonts and checks internal links before publishing to GitHub Pages.

GoatCounter is configured in `_config.yml` and loaded through `_includes/analytics-providers/custom.html` only when `JEKYLL_ENV=production`. Local development does not send visitor statistics.
