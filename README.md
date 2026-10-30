# 镜镜喵 · Codex 桌宠

黑发、紫框眼镜、半睁眼和猫耳双尾的简线 Q 版猫娘。包含九组动作与十六方向视线，使用透明 v2 精灵图。

![镜镜喵](assets/preview.png)

## 给室友的安装方法

1. 下载 [安装包](packages/jingjing-neko-codex-pet-v1.0.0.zip)，解压到一个文件夹。
2. 打开 `install.html`，点击 **安装镜镜喵**，允许浏览器打开 Codex。
3. 在 Codex 的安装窗口完成导入；到 **设置 → Pets** 刷新并选择「镜镜喵」。

需要已安装且启用 Pets 功能的新版桌面客户端。安装入口会从此公开仓库下载精灵图，需要网络连接。也可把仓库链接发给 Codex，让它按 [INSTALL.md](INSTALL.md) 使用现有精灵图导入。

`install.html` 只打开官方支持的 `codex://pets/install` 导入流程；不会修改系统配置或安装其他软件。GitHub 网页可能过滤自定义协议链接，因此请下载后打开 HTML。

## 预览

![九组动作](previews/all-states.gif)
![十六方向视线](previews/look-loop.gif)

[MP4 动画](previews/all-states.mp4) · [待机—跳跃—待机](previews/idle-jump-idle.gif)

## 素材与校验

- 最终精灵图：[`assets/spritesheet.png`](assets/spritesheet.png)，1536×2288，73 帧，约 2.1 MiB。
- 九组动作：待机、右跑、左跑、挥手、跳跃、失落、等待输入、思考工作、检查。
- [`pet.json`](pet.json) 是发布包元数据，不是要放进 Codex 配置目录的原生配置。
- [`qa/validation-summary.json`](qa/validation-summary.json) 保存检查摘要。精灵图通过结构、动作、连续性、独立视觉复核和 Pets MCP 预检。
- 有 Python 3 时，在解压目录运行 `python verify.py` 可验证所有文件的 SHA-256。也可单独核对精灵图：`3b3bc47b8ef2c2ea02fcd1e5cbb96a9d617dd2a88fdd91e8fc57fb9a441e47c2`。

版本：1.0.0。本包只包含最终生成素材与必要说明；不包含真人原照、账号凭据、原作者账户宠物 ID 或本机工作记录。

## 来源

角色素材由 AI 生成并人工迭代。猫娘元素参考绮良良；简线与团子比例参考蕾米埃尔及此前弗洛洛桌宠。具体来源见 [NOTICES.md](NOTICES.md)。

安装入口依据 OpenAI Docs 的 [Pets 安装链接说明](https://learn.chatgpt.com/docs/reference/commands#pets)，显式指定 `spriteVersionNumber=2`。桌宠入口说明见 [Pets 官方文档](https://learn.chatgpt.com/docs/pets)。桌面版、网页版与 IDE 的功能不同，本包以支持 v2 导入的桌面版为目标。
