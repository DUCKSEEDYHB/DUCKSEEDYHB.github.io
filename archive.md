---
layout: page
title: 档案
permalink: /archive/
---

# 档案
所有已发布帖子的时间顺序列表与分类索引。

## 📅 按时间归档
{% assign posts_by_year = site.posts | group_by_exp: "post", "post.date | date: '%Y'" %}
{% for year in posts_by_year %}
### {{ year.name }}（{{ year.items | size }} 个帖子）
{% assign posts_by_month = year.items | group_by_exp: "post", "post.date | date: '%m-%B'" %}
{% for month in posts_by_month %}
- **{{ month.name | split: '-' | last }}**
  <ul style="list-style: none; padding-left: 20px;">
    {% for post in month.items %}
    <li>
      {{ post.date | date: '%m-%d' }} - <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      {% for tag in post.tags %}
      <span style="font-size: 0.8em; color: #666;">#{{ tag }}</span>
      {% endfor %}
    </li>
    {% endfor %}
  </ul>
{% endfor %}
{% endfor %}

## 📁 按分类浏览
<div style="margin: 20px 0;">
{% assign categories = site.categories | sort %}
{% for category in categories %}
<a href="#cat-{{ category[0] | slugify }}" style="text-decoration: none; background: #e0e0e0; padding: 4px 12px; border-radius: 16px; margin: 4px; display: inline-block;">
  {{ category[0] }} ({{ category[1] | size }})
</a>
{% endfor %}
</div>

{% for category in categories %}
### <a id="cat-{{ category[0] | slugify }}"></a>{{ category[0] }}
<ul style="list-style: none; padding-left: 20px;">
  {% for post in category[1] %}
  <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a> - {{ post.date | date: '%Y-%m-%d' }}</li>
  {% endfor %}
</ul>
{% endfor %}

## 🏷️ 按标签浏览
<div style="margin: 20px 0;">
{% assign tags = site.tags | sort %}
{% for tag in tags %}
<a href="#tag-{{ tag[0] | slugify }}" style="text-decoration: none; background: #f0f0f0; padding: 6px 14px; border-radius: 20px; margin: 4px; display: inline-block;">
  #{{ tag[0] }} ({{ tag[1] | size }})
</a>
{% endfor %}
</div>

{% for tag in tags %}
### <a id="tag-{{ tag[0] | slugify }}"></a>{{ tag[0] }}
<ul style="list-style: none; padding-left: 20px;">
  {% for post in tag[1] %}
  <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a> - {{ post.date | date: '%Y-%m-%d' }}</li>
  {% endfor %}
</ul>
{% endfor %}