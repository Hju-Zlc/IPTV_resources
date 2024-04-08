import os
import subprocess

# 要上传的文件路径
local_file_path = r'D:\DATA\resources_1.txt'

# 检查当前目录是否是一个 Git 仓库
git_repo_exists = os.path.exists('.git')

# 如果当前目录不是一个 Git 仓库，则初始化本地仓库
if not git_repo_exists:
    subprocess.run('git init', shell=True, check=True)

# 将文件添加到暂存区
subprocess.run(f'git add "{local_file_path}"', shell=True, check=True)

# 提交更改
subprocess.run('git commit -m "Add resources_1.txt"', shell=True, check=True)

# 将本地仓库关联到 GitHub 仓库（请替换为你自己的 GitHub 仓库 URL）
github_repo_url = 'https://github.com/Hju-Zlc/IPTV_resources.git'
subprocess.run(f'git remote add origin {github_repo_url}', shell=True, check=True)

# 推送更改到 GitHub
subprocess.run('git push -u origin master', shell=True, check=True)

print("文件上传成功！")
