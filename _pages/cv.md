---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
description: "CV of David Kreismann: education at TUM, DHBW Stuttgart and University College Dublin, research at the University of Cambridge, IBM Research and KSRI."
translation: /de/cv/
redirect_from:
  - /resume
---

{% include base_path %}
{% assign months = "Jan.,Feb.,March,April,May,June,July,Aug.,Sept.,Oct.,Nov.,Dec." | split: "," %}


<div class="cv-section">
  <h2>Education</h2>
  {% for entry in site.data.cv.education %}{% include cv-entry.html entry=entry %}{% endfor %}
</div>

<div class="cv-section">
  <h2>Experience</h2>
  {% for entry in site.data.cv.experience %}{% include cv-entry.html entry=entry %}{% endfor %}
</div>

<div class="cv-section">
  <h2>Publications</h2>
  {% for post in site.publications reversed %}{% if post.category != 'patents' %}
  <div class="cv-entry">
    <div class="cv-entry__head">
      <a class="cv-entry__title" href="{{ base_path }}{{ post.url }}">{{ post.title }}</a>
      <span class="cv-entry__date">{% assign month = post.date | date: "%-m" | minus: 1 %}{{ months[month] }} {{ post.date | date: "%Y" }}</span>
    </div>
    <div class="cv-entry__org">{{ post.venue }}</div>
    <p class="cv-role__text">{{ post.citation | split: '. (' | first }}</p>
  </div>
  {% endif %}{% endfor %}
</div>

<div class="cv-section">
  <h2>Patents</h2>
  {% for post in site.publications reversed %}{% if post.category == 'patents' %}
  <div class="cv-entry">
    <div class="cv-entry__head">
      <a class="cv-entry__title" href="{{ base_path }}{{ post.url }}">{{ post.title }}</a>
      <span class="cv-entry__date">{% assign month = post.date | date: "%-m" | minus: 1 %}{{ months[month] }} {{ post.date | date: "%Y" }}</span>
    </div>
    <div class="cv-entry__org">Filed with {{ post.venue }}</div>
    <p class="cv-role__text">{{ post.citation | split: '. (' | first }}</p>
  </div>
  {% endif %}{% endfor %}
</div>

<div class="cv-section">
  <h2>Honours and Awards</h2>
  {% for entry in site.data.cv.awards %}{% include cv-entry.html entry=entry %}{% endfor %}
</div>

<div class="cv-section">
  <h2>Extracurricular Activities</h2>
  {% for entry in site.data.cv.activities %}{% include cv-entry.html entry=entry %}{% endfor %}
</div>
<div class="project-card__footer project-meta cv-download">
  <span class="project-card__stack">Full CV with skills and languages</span>
  <a class="project-card__link" href="{{ base_path }}/files/David_Kreismann_CV.pdf"><i class="fas fa-file-pdf" aria-hidden="true"></i> Download PDF</a>
</div>
