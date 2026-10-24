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
{% assign months_de = "Jan.,Feb.,März,Apr.,Mai,Juni,Juli,Aug.,Sept.,Okt.,Nov.,Dez." | split: "," %}

<div class="wordwrap">Meinen Lebenslauf gibt es auch als <a href="{{ base_path }}/files/David_Kreismann_CV.pdf">PDF</a> (auf Englisch).</div>


<div class="cv-section">
  <h2>Ausbildung</h2><hr />
  {% for entry in site.data.cv_de.education %}{% include cv-entry.html entry=entry %}{% endfor %}
</div>

<div class="cv-section">
  <h2>Berufserfahrung</h2><hr />
  {% for entry in site.data.cv_de.experience %}{% include cv-entry.html entry=entry %}{% endfor %}
</div>

<div class="cv-section">
  <h2>Publikationen</h2><hr />
  {% for post in site.publications reversed %}{% if post.category != 'patents' %}
  <div class="cv-entry">
    <div class="cv-entry__head">
      <a class="cv-entry__title" href="{{ base_path }}{{ post.url }}">{{ post.title }}</a>
      <span class="cv-entry__date">{% assign month = post.date | date: "%-m" | minus: 1 %}{{ months_de[month] }} {{ post.date | date: "%Y" }}</span>
    </div>
    <div class="cv-entry__org">{{ post.venue }}</div>
    <p class="cv-role__text">{{ post.citation | split: '. (' | first }}</p>
  </div>
  {% endif %}{% endfor %}
</div>

<div class="cv-section">
  <h2>Patente</h2><hr />
  {% for post in site.publications reversed %}{% if post.category == 'patents' %}
  <div class="cv-entry">
    <div class="cv-entry__head">
      <a class="cv-entry__title" href="{{ base_path }}{{ post.url }}">{{ post.title }}</a>
      <span class="cv-entry__date">{% assign month = post.date | date: "%-m" | minus: 1 %}{{ months_de[month] }} {{ post.date | date: "%Y" }}</span>
    </div>
    <div class="cv-entry__org">Angemeldet bei {{ post.venue }}</div>
    <p class="cv-role__text">{{ post.citation | split: '. (' | first }}</p>
  </div>
  {% endif %}{% endfor %}
</div>

<div class="cv-section">
  <h2>Auszeichnungen und Stipendien</h2><hr />
  {% for entry in site.data.cv_de.awards %}{% include cv-entry.html entry=entry %}{% endfor %}
</div>

<div class="cv-section">
  <h2>Ehrenamtliches Engagement</h2><hr />
  {% for entry in site.data.cv_de.activities %}{% include cv-entry.html entry=entry %}{% endfor %}
</div>
