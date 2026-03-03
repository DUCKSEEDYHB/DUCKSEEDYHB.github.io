---
layout: page
title: 展览
permalink: /exhibition/
---

# 展览
是个人项目、专业技能与书籍收藏的聚合。

<!-- 统一样式优化 + 展开/收起样式 -->
<style>
  .exhibition-container {
    display: flex;
    flex-wrap: wrap;
    gap: 25px;
    margin: 30px 0;
  }
  .exhibition-card {
    flex: 1;
    min-width: 320px;
    background: #f8f8f8;
    padding: 30px;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    transition: all 0.3s ease;
  }
  .exhibition-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 16px rgba(0,0,0,0.12);
  }
  .card-icon {
    font-size: 40px;
    margin-bottom: 15px;
    cursor: pointer;
  }
  .card-title {
    font-size: 20px;
    margin: 10px 0;
    color: #333;
    cursor: pointer;
    user-select: none;
  }
  .card-desc {
    color: #666;
    margin-bottom: 20px;
    font-size: 14px;
  }
  .card-divider {
    width: 60px;
    margin: 20px auto;
    border: 0;
    border-top: 1px solid #ddd;
  }
  .sub-category {
    text-align: left;
    margin: 25px 0 10px;
    font-size: 16px;
    color: #444;
    font-weight: 600;
  }
  .sub-category::before {
    content: "▸ ";
    color: #007bff;
  }
  .card-list {
    list-style: none;
    padding: 0 0 0 15px;
    text-align: left;
    line-height: 1.8;
  }
  .card-list li a {
    color: #007bff;
    text-decoration: none;
  }
  .card-list li a:hover {
    text-decoration: underline;
  }
  /* 展开/收起核心样式 */
  .card-content {
    display: none; /* 默认隐藏内容 */
    margin-top: 15px;
  }
  .card-content.active {
    display: block; /* 激活后显示 */
  }
  .card-title::after {
    content: " ▼";
    font-size: 14px;
    color: #999;
    transition: transform 0.3s ease;
  }
  .card-title.active::after {
    transform: rotate(180deg);
  }
</style>

<div class="exhibition-container">
  <!-- 项目模块（点击标题展开/收起） -->
  <div class="exhibition-card">
    <div class="card-icon">📂</div>
    <h3 class="card-title" onclick="toggleCard('project')">项目</h3>
    <p class="card-desc">我的开发项目组合（按开发状态分类）</p>
    <hr class="card-divider">
    
    <div id="project" class="card-content">
      <div class="sub-category">待开发</div>
      <ul class="card-list">
        <li>电力系统故障分析小程序</li>
        <li>考研知识点思维导图工具</li>
        <li>Python 自动化办公脚本集</li>
      </ul>

      <div class="sub-category">正在开发</div>
      <ul class="card-list">
        <li>Jekyll 博客自动部署脚本</li>
        <li>电力系统潮流计算小工具</li>
      </ul>

      <div class="sub-category">完成开发</div>
      <ul class="card-list">
        <li><a href="#">考研笔记 LaTeX 模板</a></li>
        <li><a href="#">个人博客 favicon 生成工具</a></li>
      </ul>
    </div>
  </div>

  <!-- 技能模块（点击标题展开/收起） -->
  <div class="exhibition-card">
    <div class="card-icon">⚡</div>
    <h3 class="card-title" onclick="toggleCard('skill')">技能</h3>
    <p class="card-desc">我的技术栈和专业能力汇总</p>
    <hr class="card-divider">
    
    <div id="skill" class="card-content">
      <div class="sub-category">专业能力</div>
      <ul class="card-list">
        <li>电气工程及其自动化（电力系统方向）</li>
        <li>电力系统分析与仿真</li>
        <li>电气控制与PLC编程</li>
      </ul>

      <div class="sub-category">编程技术栈</div>
      <ul class="card-list">
        <li>Python（数据分析/自动化）</li>
        <li>MATLAB（电力系统仿真）</li>
        <li>C 语言（底层编程）</li>
        <li>Jekyll / GitHub Pages（静态博客）</li>
        <li>LaTeX（专业文档排版）</li>
      </ul>
    </div>
  </div>

  <!-- 书籍模块（点击标题展开/收起） -->
  <div class="exhibition-card">
    <div class="card-icon">📚</div>
    <h3 class="card-title" onclick="toggleCard('book')">书籍</h3>
    <p class="card-desc">我的阅读清单（按阅读状态分类）</p>
    <hr class="card-divider">
    
    <div id="book" class="card-content">
      <div class="sub-category">已看过</div>
      <ul class="card-list">
        <li>《电力系统分析（上册）》（陈珩）</li>
        <li>《Python编程：从入门到实践》</li>
        <li>《解忧杂货店》（东野圭吾）</li>
        <li>《小王子》（圣埃克苏佩里）</li>
      </ul>

      <div class="sub-category">正在看</div>
      <ul class="card-list">
        <li>《电力系统继电保护原理》</li>
        <li>《数学分析八讲》（辛钦）</li>
      </ul>

      <div class="sub-category">想看</div>
      <ul class="card-list">
        <li>《深入理解计算机系统》</li>
        <li>《沉默的大多数》（王小波）</li>
        <li>《电气控制与PLC应用》</li>
      </ul>
    </div>
  </div>
</div>

<!-- 展开/收起逻辑脚本 -->
<script>
function toggleCard(cardId) {
  // 获取内容区域和标题
  const content = document.getElementById(cardId);
  const title = content.previousElementSibling.previousElementSibling; // 定位到标题
  
  // 切换显示/隐藏
  content.classList.toggle('active');
  title.classList.toggle('active');
}
</script>