# 湛蓝工作台

莫迪蓝色系创作工作台，面向抖音/小红书摄影博主 + 公众号教育/心理/个人成长。

## 功能

- **月历工作安排** — 点击日期添加工作备注，数据存储在浏览器本地
- **左侧赛道选择** — 抖音摄影 / 小红书摄影 / 公众号·教育 / 公众号·心理 / 公众号·成长
- **右侧项目细分** — 按赛道动态切换
- **每日内容** — 自动从 GitHub 仓库读取 10 条选题灵感 + 10 条二创角度
- **App 深链接** — 抖音/B站/小红书一键唤起 App
- **桌面应用** — 支持 macOS Electron 打包

## 数据源

默认从仓库 `56533042/lovely-dream` 的 `daily_content.json` 文件读取。
也支持配置 GitHub Gist ID 作为数据源。

## 每日自动化

WorkBuddy 定时任务每天 8:00 自动：
1. 抓取抖音/微博/B站/知乎热榜
2. AI 改写生成选题灵感和二创角度
3. 推送 JSON 到仓库 `daily_content.json`

## 文件结构

```
index.html          # 网页工作台（自包含单文件）
desktop-app/
  ├── index.html    # 同上
  ├── main.js       # Electron 主进程
  ├── package.json   # Electron 配置
  └── icon.icns     # 应用图标
```

## 构建桌面应用

```bash
cd desktop-app
npm install
npm run build    # 生成 dist/湛蓝工作台-darwin-arm64/
npm start        # 开发模式运行
```
