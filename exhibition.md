---
layout: page
title: 展览
permalink: /exhibition/
---

# 展览
是个人项目、专业技能与书籍收藏的聚合。

<!-- 统一样式优化 + 展开/收起样式 - 统一全站风格 -->
<style>
  /* 容器样式 */
  .exhibition-container {
    display: flex;
    flex-wrap: wrap;
    gap: 30px;
    margin: 40px 0;
    justify-content: center;
  }
  
  /* 卡片核心样式 - 统一全站设计语言 */
  .exhibition-card {
    flex: 1;
    min-width: 300px;
    max-width: 450px;
    background: rgba(255, 255, 255, 0.88);
    padding: 35px 25px;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
  }
  
  /* 卡片悬浮动效 */
  .exhibition-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.12);
  }
  
  /* 卡片图标 */
  .card-icon {
    font-size: 45px;
    margin-bottom: 20px;
    color: #3498db;
    transition: all 0.3s ease;
  }
  
  .exhibition-card:hover .card-icon {
    transform: scale(1.1);
    color: #2980b9;
  }
  
  /* 卡片标题 */
  .card-title {
    font-size: 1.5em;
    margin: 15px 0;
    color: #2c3e50;
    cursor: pointer;
    user-select: none;
    font-weight: 600;
    transition: color 0.3s ease;
  }
  
  .card-title:hover {
    color: #3498db;
  }
  
  /* 卡片描述 */
  .card-desc {
    color: #7f8c8d;
    margin-bottom: 25px;
    font-size: 1em;
    line-height: 1.6;
  }
  
  /* 分隔线 */
  .card-divider {
    width: 80px;
    margin: 25px auto;
    border: 0;
    border-top: 2px solid #f0f8ff;
  }
  
  /* 子分类标题 */
  .sub-category {
    text-align: left;
    margin: 30px 0 15px;
    font-size: 1.15em;
    color: #34495e;
    font-weight: 600;
    padding-left: 10px;
    border-left: 3px solid #3498db;
  }
  
  .sub-category::before {
    content: "▸ ";
    color: #3498db;
  }
  
  /* 列表样式 */
  .card-list {
    list-style: none;
    padding: 0 0 0 20px;
    text-align: left;
    line-height: 1.8;
    color: #2d3748;
  }
  
  .card-list li {
    margin-bottom: 8px;
    position: relative;
    padding-left: 8px;
    transition: all 0.2s ease;
  }
  
  .card-list li::before {
    content: "•";
    color: #3498db;
    position: absolute;
    left: -12px;
  }
  
  .card-list li:hover {
    padding-left: 12px;
    color: #3498db;
  }
  
  .card-list li a {
    color: #3498db;
    text-decoration: none;
    font-weight: 500;
  }
  
  .card-list li a:hover {
    text-decoration: underline;
    color: #2980b9;
  }
  
  /* 展开/收起核心样式 */
  .card-content {
    display: none; /* 默认隐藏内容 */
    margin-top: 20px;
    animation: fadeIn 0.3s ease;
  }
  
  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
  }
  
  .card-content.active {
    display: block; /* 激活后显示 */
  }
  
  .card-title::after {
    content: " ▼";
    font-size: 0.8em;
    color: #94a3b8;
    transition: transform 0.3s ease;
    margin-left: 8px;
  }
  
  .card-title.active::after {
    transform: rotate(180deg);
    color: #3498db;
  }
  
  /* 空数据提示 */
  .empty-tip {
    color: #7f8c8d;
    text-align: center;
    padding: 20px 0;
    font-size: 1em;
  }
  
  /* 移动端适配 */
  @media (max-width: 768px) {
    .exhibition-container {
      gap: 20px;
      margin: 20px 0;
    }
    
    .exhibition-card {
      min-width: 90%;
      padding: 25px 20px;
      max-width: 100%;
    }
    
    .card-icon {
      font-size: 40px;
    }
    
    .card-title {
      font-size: 1.3em;
    }
    
    .card-desc {
      font-size: 0.95em;
    }
    
    .sub-category {
      font-size: 1.1em;
      margin: 25px 0 12px;
    }
    
    .card-list {
      padding-left: 15px;
      font-size: 0.95em;
    }
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

  <!-- 技能模块（点击标题展开/收起）- 补充嵌入式入门标注 -->
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
        <li>Java（面向对象编程/后端开发基础）</li>
        <li>前端（HTML/CSS/JavaScript 开发）</li>
        <li>嵌入式软件（入门级别）</li>
        <li>嵌入式硬件（入门级别）</li>
        <li>Jekyll / GitHub Pages（静态博客）</li>
        <li>LaTeX（专业文档排版）</li>
      </ul>
    </div>
  </div>

  <!-- 书籍模块（点击标题展开/收起）- 仅保留指定人文书籍 -->
  <div class="exhibition-card">
    <div class="card-icon">📚</div>
    <h3 class="card-title" onclick="toggleCard('book')">书籍</h3>
    <p class="card-desc">我的阅读清单（按阅读状态分类）</p>
    <hr class="card-divider">
    
    <div id="book" class="card-content">
      <div class="sub-category">已看过</div>
      <ul class="card-list">
        <li>《你当像鸟飞往你的山》（塔拉·韦斯特弗）</li>
        <li>《被讨厌的勇气》（岸见一郎、古贺史健）</li>
      </ul>

      <div class="sub-category">正在看</div>
      <ul class="card-list">
        <li>《悉达多》（赫尔曼·黑塞）</li>
      </ul>

      <div class="sub-category">想看</div>
      <ul class="card-list">
        <li>《蛤蟆先生去看心理医生》</li>
        <li>《人类简史》（尤瓦尔·赫拉利）</li>
      </ul>
    </div>
  </div>
</div>

<!-- 展开/收起逻辑脚本 - 优化兼容性和体验 -->
<script>
// 修复切换逻辑 + 增加动画效果
function toggleCard(cardId) {
  // 阻止事件冒泡
  event && event.stopPropagation();
  
  // 获取内容区域和标题
  const content = document.getElementById(cardId);
  const title = content.closest('.exhibition-card').querySelector('.card-title');
  
  // 切换显示/隐藏
  content.classList.toggle('active');
  title.classList.toggle('active');
  
  // 平滑滚动到卡片内容
  if (content.classList.contains('active')) {
    setTimeout(() => {
      content.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 100);
  }
}

// 页面加载完成后初始化
document.addEventListener('DOMContentLoaded', function() {
  // 可选：默认展开第一个卡片（项目）
  // toggleCard('project');
  
  // 优化卡片点击体验：点击图标也能展开/收起
  const cardIcons = document.querySelectorAll('.card-icon');
  cardIcons.forEach(icon => {
    icon.addEventListener('click', function() {
      const cardId = this.nextElementSibling.getAttribute('onclick').match(/'(\w+)'/)[1];
      toggleCard(cardId);
    });
  });
});
</script>