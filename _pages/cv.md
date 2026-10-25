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

<div class="wordwrap">You can also find my CV as a <a href="{{ base_path }}/files/David_Kreismann_CV.pdf" data-umami-event="cv-download">PDF</a>.</div>


<div class="cv-section">
  <h2>Education</h2><hr />
  {% for entry in site.data.cv.education %}{% include cv-entry.html entry=entry %}{% endfor %}
</div>

<div class="cv-section">
  <h2>Experience</h2><hr />
  {% for entry in site.data.cv.experience %}{% include cv-entry.html entry=entry %}{% endfor %}
</div>

<div class="cv-section">
  <h2>Honours and Awards</h2><hr />
  {% for entry in site.data.cv.awards %}{% include cv-entry.html entry=entry %}{% endfor %}
</div>

<div class="cv-section">
  <h2>Extracurricular Activities</h2><hr />
  {% for entry in site.data.cv.activities %}{% include cv-entry.html entry=entry %}{% endfor %}
</div>
