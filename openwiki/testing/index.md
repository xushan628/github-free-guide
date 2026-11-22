# 文件

- [验证手段：没有单测时如何证明改动安全](validation-harness.md) - 仓库没有 pytest/unittest、没有构建步骤也没有依赖清单，验证只能靠脚本自带的开关（sync_atlas --check、verify_links --strict、deploy --dry-run、check_site 三态退出码）与生成区标记守卫；本页给出每类改动的最小命令、可接受的输出字样、幂等判据，以及最容易静默失败的几个坑。
