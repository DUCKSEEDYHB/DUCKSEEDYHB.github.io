---
layout: default  # 改用你存在的 default 布局，避免布局不存在
title: 首页
permalink: /     # 强制渲染为根目录 index.html
---

# 欢迎来到 Duckweed's Space 📚
这里是我的个人成长空间，记录编程学习、考研备考、读书思考的点滴。

## 最新笔记
{% for post in site.posts limit:5 %}
- [{{ post.title }}]({{ post.url }}) - {{ post.date | date: "%Y-%m-%d" }}
{% endfor %}

## 快速导航
- [文章归档](/pages/archive.html)
- [友链页面](/pages/friends.html)