import os
import yaml
from datetime import datetime
from pathlib import Path

def parse_jekyll_post(post_path):
    """解析 Jekyll 博客的 Front Matter 字段"""
    try:
        with open(post_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取 Front Matter（--- 包裹的部分）
        fm_start = content.find('---')
        fm_end = content.find('---', fm_start + 3)
        if fm_start == -1 or fm_end == -1:
            return None
        
        fm_content = content[fm_start+3:fm_end].strip()
        fm = yaml.safe_load(fm_content)
        
        # 提取核心字段（兼容 Jekyll 标准）
        post_date = fm.get('date', '')
        if isinstance(post_date, datetime):
            post_date = post_date.strftime('%Y-%m-%d')
        else:
            post_date = str(post_date).split(' ')[0]  # 处理字符串格式
        
        title = fm.get('title', '无标题')
        excerpt = fm.get('excerpt', '') or content[fm_end+3:].strip()[:80] + '...'
        excerpt = excerpt.replace('\n', ' ').replace('|', '｜')  # 避免表格格式冲突
        
        # 生成 Jekyll 博客链接（适配默认 permalink 规则）
        filename = Path(post_path).stem
        slug = filename.split('-', 3)[-1] if len(filename.split('-')) > 3 else filename
        url = f"https://duckweed-yhb.github.io/{post_date.replace('-', '/')}/{slug}/"
        
        return {
            'date': post_date,
            'title': title,
            'url': url,
            'excerpt': excerpt
        }
    except Exception as e:
        print(f"解析 {post_path} 失败：{e}")
        return None

def generate_latest_posts(posts_dir='_posts', limit=5):
    """读取 Jekyll _posts 目录，生成最新博客列表"""
    posts = []
    for file in os.listdir(posts_dir):
        if file.endswith(('.md', '.markdown')):
            post_info = parse_jekyll_post(os.path.join(posts_dir, file))
            if post_info and post_info['date']:
                posts.append(post_info)
    
    # 按发布日期倒序排列
    posts_sorted = sorted(posts, key=lambda x: x['date'], reverse=True)[:limit]
    
    # 生成 Markdown 表格行
    table_rows = []
    for post in posts_sorted:
        table_rows.append(f"| {post['date']} | [{post['title']}]({post['url']}) | {post['excerpt']} |")
    
    return '\n'.join(table_rows)

def main():
    # 读取模板
    template_path = 'templates/README.template.md'
    if not os.path.exists(template_path):
        print("模板文件不存在！")
        return
    
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()
    
    # 生成最新博客内容
    latest_posts = generate_latest_posts()
    
    # 填充模板
    readme_content = template.replace('{{ latest_posts }}', latest_posts)
    readme_content = readme_content.replace('{{ update_time }}', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    
    # 写入 README.md
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    print("README.md 已自动更新！")

if __name__ == "__main__":
    main()