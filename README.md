# David Kreismann – Personal Website

Source of [xdavld.github.io](https://xdavld.github.io), built with Jekyll on the [Academic Pages](https://github.com/academicpages/academicpages.github.io) template and deployed to GitHub Pages via GitHub Actions (`.github/workflows/jekyll.yml`).

## Where things live

| What | File |
| --- | --- |
| Name, sidebar, social links | `_config.yml` |
| Top navigation | `_data/navigation.yml` |
| Home page | `_pages/about.md` |
| CV content (web and PDF) | `_data/cv.yml`, German: `_data/cv_de.yml` |
| CV PDF layout | `_pages/cv-pdf.tex` (compiled to `/files/David_Kreismann_CV.pdf` on deploy) |
| Publications (one file each) | `_publications/` |
| Profile picture | `images/profile.jpg` |
| German pages | `_pages/de/` (linked to their English page via `translation:`) |

## Run locally

```bash
bundle install
bundle exec jekyll serve -l -H localhost
```

Then open http://localhost:4000.

The deploy workflow also compiles the CV PDF, shrinks the icon fonts to the icons in use and checks all internal links. The PDF is only built on deploy, so its link returns 404 in local previews.
