# 安装镜镜喵

## 推荐：打开安装入口

下载本仓库的 ZIP 并解压，使用浏览器打开 `install.html`，点击安装按钮。它会请求系统打开 Codex 的桌宠安装窗口，并从仓库下载 `assets/spritesheet.png`。导入后在设置的 Pets 页面刷新并选择镜镜喵。

Windows 也可打开 `install.url`。如果系统询问是否打开 Codex，这是正常的协议处理提示。不要把 ZIP、预览 GIF 或 `pet.json` 当成精灵图上传。

直接安装链接（某些网站会过滤该协议；可复制完整链接）：

```text
codex://pets/install?name=%E9%95%9C%E9%95%9C%E5%96%B5&imageUrl=https%3A%2F%2Fraw.githubusercontent.com%2FXinyaoPan%2Fjingjing-neko-codex-pet%2Fmain%2Fassets%2Fspritesheet.png&description=%E7%AE%80%E7%BA%BFQ%E7%89%88%E7%8C%AB%E5%A8%98%EF%BC%9A%E9%BB%91%E5%8F%91%E7%B4%AB%E6%A1%86%E7%9C%BC%E9%95%9C%E3%80%81%E6%85%B5%E6%87%92%E5%8D%8A%E7%9D%81%E7%9C%BC%E3%80%81%E7%8C%AB%E8%80%B3%E5%8F%8C%E5%B0%BE%E4%B8%8E%E8%96%84%E8%8D%B7%E7%BB%BF%E5%B0%8F%E6%8A%AB%E8%82%A9%E3%80%82&spriteVersionNumber=2
```

## 把现成素材交给 Codex 导入

把以下请求连同本仓库地址发给室友自己的 Codex：

> 请安装此仓库中的现成桌宠「镜镜喵」。按 INSTALL.md 操作，先核对 pet.json 和 assets/spritesheet.png 的 SHA-256。它是1536×2288、192×208单元格的v2精灵图，有九组动作和十六方向视线。请使用现有图片导入，不要重新生成、改画或压成v1；可打开文档列出的官方安装链接并明确 spriteVersionNumber=2。若你有 Pets 插件，可用其现有图片预检及导入工具导入此 PNG，并回读核验。导入成功后按我的意愿选择镜镜喵。

如果通过 Pets 工具导入：验证必须返回 `valid:true`；用同一 PNG 准备上传，再消费返回的上传会话创建一个属于室友账号的新宠物。上传会话不能当作宠物 ID。已有同名宠物时先确认，避免重复创建。

## 常见问题

- **点了没反应**：确认已安装支持 Pets 的桌面客户端；从下载的 HTML 打开，或复制链接后交给 Codex。浏览器若拦截自定义协议，可使用系统的正常“打开 Codex”提示。
- **只有网页版/IDE**：这两者不等同于桌面浮动桌宠。网页版文档中仍列出 v1 的上传限制；不要为了适配它直接上传这个 v2 文件。
- **安装提示格式不支持**：先更新客户端；不要直接裁掉十六方向。需要时把原始 PNG、pet.json 和错误信息交给 Codex。
- **完全离线**：先从 ZIP 取得 PNG；支持本地文件导入的 Pets 工作流可使用它。此包中的快捷安装链接仍需要访问 GitHub。

完整图 SHA-256：`3b3bc47b8ef2c2ea02fcd1e5cbb96a9d617dd2a88fdd91e8fc57fb9a441e47c2`。

来源：[OpenAI Docs · Pets 安装链接](https://learn.chatgpt.com/docs/reference/commands#pets)；[Pets](https://learn.chatgpt.com/docs/pets)。
