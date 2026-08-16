# 如何把 `wiki/` 发布为 GitHub Wiki

GitHub Wiki 是**独立 git 仓库**（`Awesome-TCM-LLM.wiki.git`），和主仓库的 `wiki/` 目录不是自动同步的。建议：主仓库里的 `wiki/` 当源，Wiki 当发布副本。

## 1. 打开 Wiki

仓库 **Settings → Features → Wikis**。未打开时，浏览者仍可直接读主仓库 `wiki/*.md`。

## 2. 首次推送

```bash
# 在仓库根目录
git clone https://github.com/tyang816/Awesome-TCM-LLM.wiki.git /tmp/Awesome-TCM-LLM.wiki
rsync -a --delete --exclude PUBLISH.md wiki/ /tmp/Awesome-TCM-LLM.wiki/
cd /tmp/Awesome-TCM-LLM.wiki
git add -A
git status
git commit -m "Sync wiki from main repo wiki/"
git push
```

`PUBLISH.md` 只给维护者看，不必出现在 Wiki 导航里。

## 3. 日常更新

`python3 scripts/build_readme.py` 会重写：

- `wiki/Models.md`
- `wiki/Datasets.md`
- `wiki/Benchmarks.md`

手写页（Home、Getting-Started、Taxonomy、FAQ 等）改完后，重复上面的 `rsync` + `commit` + `push`。

也可用 [github-wiki-action](https://github.com/Andrew-Chen-Wang/github-wiki-action) 在 CI 里同步，避免漏推。

## 4. 页面清单

| 文件 | 生成还是手写 | Wiki 标题 |
| --- | --- | --- |
| `Home.md` | 手写 | Home |
| `Getting-Started.md` | 手写 | Getting-Started |
| `Models.md` | 脚本生成 | Models |
| `Datasets.md` | 脚本生成 | Datasets |
| `Benchmarks.md` | 脚本生成 | Benchmarks |
| `Taxonomy.md` | 手写 | Taxonomy |
| `Contributing.md` | 手写 | Contributing |
| `FAQ.md` | 手写 | FAQ |
| `About.md` | 手写 | About |
| `_Sidebar.md` | 手写 | 左侧栏 |
| `_Footer.md` | 手写 | 页脚 |

## 5. 和 README 的分工

| | README | Wiki |
| --- | --- | --- |
| 目标 | 发现：目录、折叠、专栏表 | 说明：选型、分类、流程 |
| 长度 | 控制首屏，旧年折叠 | 可以铺开完整列表 |
| 更新 | 每次改 catalog 必生成 | 生成三页 + 必要时手改其余 |
