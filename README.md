# David Kreismann – Personal Website

Source of [xdavld.github.io](https://xdavld.github.io), built with Jekyll on the [Academic Pages](https://github.com/academicpages/academicpages.github.io) template and deployed to GitHub Pages via GitHub Actions (`.github/workflows/jekyll.yml`).

## Where things live

| What | File |
| --- | --- |
| Name, sidebar, social links | `_config.yml` |
| Top navigation | `_data/navigation.yml` |
| Home page | `_pages/about.md` |
| CV | `_pages/cv.md` |
| Publications (one file each) | `_publications/` |
| Profile picture | `images/profile.png` |

## Run locally

```bash
bundle install
bundle exec jekyll serve -l -H localhost
```

Then open http://localhost:4000.
