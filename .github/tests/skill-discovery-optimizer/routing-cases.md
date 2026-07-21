# Skill publishing routing checks

Checked with fresh agents on 2026-07-21. Routers saw frontmatter only and were
not shown expected labels.

## Baseline findings

| Prompt | Expected | Observed | Rationale |
| --- | --- | --- | --- |
| 把这个 Agent Skill 更新到 GitHub，并确认别人还能安装。 | INVOKE | INVOKE | Single-Skill GitHub release was already covered. |
| 把仓库里所有修改过的 Skills 同步到 GitHub，发一个新版本。 | INVOKE | DO_NOT_INVOKE | Multi-Skill sync was mistaken for generic repository publishing. |
| 帮我把这几个 Skill 更新到 skills.sh 和其他技能目录。 | INVOKE | AMBIGUOUS | Non-GitHub distribution was not explicit enough. |
| Publish all updated Agent Skills to GitHub and verify remote installation. | INVOKE | INVOKE | Explicit Skill release and verification. |
| 把这个普通 Python 项目推到 GitHub。 | DO_NOT_INVOKE | DO_NOT_INVOKE | Ordinary repository publishing. |
| 提交并推送 README 的错别字修复。 | DO_NOT_INVOKE | DO_NOT_INVOKE | No Agent Skill context. |
| 把这个 MCP Server 发布到官方 MCP Registry。 | DO_NOT_INVOKE | DO_NOT_INVOKE | MCP Server publishing is excluded. |
| 这个 Skill 已经改完，帮我提交到 GitHub。 | INVOKE | INVOKE | Finished Agent Skill release. |
| 更新我的 Skills 仓库。 | INVOKE | AMBIGUOUS | Skills-monorepo updates were not explicit enough. |
| 把现有 Skill 发布到一个新的第三方 Agent Skill 市场。 | INVOKE | DO_NOT_INVOKE | Third-party Skill marketplaces were not covered. |

## Held-out retest

The description was revised to make Agent Skill publishing, release, sync,
push, update, upload, and distribution automatic preflight triggers while
preserving the ordinary-repository and MCP exclusions.

| Prompt | Expected | Observed | Rationale |
| --- | --- | --- | --- |
| 把这个 Agent Skill 更新到 GitHub，并确认别人还能安装。 | INVOKE | INVOKE | Single-Skill GitHub release. |
| 把仓库里所有修改过的 Skills 同步到 GitHub，发一个新版本。 | INVOKE | INVOKE | Multi-Skill release. |
| 帮我把这几个 Skill 更新到 skills.sh 和其他技能目录。 | INVOKE | INVOKE | Registry and directory distribution. |
| Publish all updated Agent Skills to GitHub and verify remote installation. | INVOKE | INVOKE | Release and remote verification. |
| 把这个普通 Python 项目推到 GitHub。 | DO_NOT_INVOKE | DO_NOT_INVOKE | Ordinary repository. |
| 提交并推送 README 的错别字修复。 | DO_NOT_INVOKE | DO_NOT_INVOKE | No Agent Skill context. |
| 把这个 MCP Server 发布到官方 MCP Registry。 | DO_NOT_INVOKE | DO_NOT_INVOKE | MCP publishing remains excluded. |
| 这个 Skill 已经改完，帮我提交到 GitHub。 | INVOKE | INVOKE | Finished Agent Skill release. |
| 更新我的 Skills 仓库。 | INVOKE | INVOKE | Skills-monorepo update. |
| 把现有 Skill 发布到一个新的第三方 Agent Skill 市场。 | INVOKE | INVOKE | Agent Skill marketplace distribution. |
| 发布一个教人弹吉他的普通网站，项目名叫 guitar-skills。 | DO_NOT_INVOKE | DO_NOT_INVOKE | A project name alone must not trigger. |
| Sync only the modified skills in this monorepo and prepare a release. | INVOKE | INVOKE | Changed-Skill monorepo preflight. |
