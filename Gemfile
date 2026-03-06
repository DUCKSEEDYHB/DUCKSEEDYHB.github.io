source "https://rubygems.org"

# 锁定Ruby版本（适配GitHub Pages官方环境）
ruby "3.1.4"

# 适配GitHub Pages官方版本（核心依赖）
gem "github-pages", "~> 231", group: :jekyll_plugins
gem "bundler", "~> 2.3"  # 适配GitHub Pages的bundler版本

# 主题（与github-pages 231兼容）
gem "minima", "~> 2.5"

# Jekyll插件（与_config.yml严格对应）
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
  gem "jekyll-paginate", "~> 1.1"
  gem "jekyll-seo-tag", "~> 2.8"
end

# 系统兼容（保留）
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

gem "wdm", "~> 0.1", :platforms => [:mingw, :x64_mingw, :mswin]
gem "http_parser.rb", "~> 0.8.0", :platforms => [:jruby]