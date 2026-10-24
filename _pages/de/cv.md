---
layout: archive
title: "Lebenslauf"
permalink: /de/cv/
author_profile: true
description: "Lebenslauf von David Kreismann: Studium an TUM, DHBW Stuttgart und University College Dublin, Forschung an der University of Cambridge, bei IBM Research und am KSRI."
lang: de
translation: /cv/
---

{% include base_path %}

<div class="wordwrap">Meinen Lebenslauf gibt es auch als <a href="{{ base_path }}/files/David_Kreismann_CV.pdf">PDF</a> (Englisch).</div>


<div class="cv-section">
  <h2>Ausbildung</h2><hr />
  {% for entry in site.data.cv_de.education %}{% include cv-entry.html entry=entry %}{% endfor %}
</div>

<div class="cv-section">
  <h2>Berufserfahrung</h2><hr />
  {% for entry in site.data.cv_de.experience %}{% include cv-entry.html entry=entry %}{% endfor %}
</div>

<div class="cv-section">
  <h2>Auszeichnungen und Stipendien</h2><hr />
  {% for entry in site.data.cv_de.awards %}{% include cv-entry.html entry=entry %}{% endfor %}
</div>

<div class="cv-section">
  <h2>Ehrenamtliches Engagement</h2><hr />
  {% for entry in site.data.cv_de.activities %}{% include cv-entry.html entry=entry %}{% endfor %}
</div>
