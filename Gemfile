source "https://rubygems.org"

# 适配 GitHub Pages（必须优先使用 github-pages 包）
gem "github-pages", "~> 231", group: :jekyll_plugins
gem "jekyll", "~> 4.3.2" # 与 github-pages 231 兼容的版本

# 主题
gem "minima", "~> 2.5"

# Jekyll 插件（与 _config.yml 对应）
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
  gem "jekyll-paginate", "~> 1.1" # 补充分页插件
  gem "jekyll-seo-tag" # SEO 优化插件
end

# 系统兼容
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

gem "wdm", "~> 0.1", :platforms => [:mingw, :x64_mingw, :mswin]
gem "http_parser.rb", "~> 0.8.0", :platforms => [:jruby]