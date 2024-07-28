#!/bin/bash

# 检查参数数量
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 {num} \"{title}\" {difficulty}"
    exit 1
fi

num=$1
title=$2
difficulty=$3

# 检查 num 是否是有效的数字且在指定范围内
if ! [[ "$num" =~ ^[0-9]+$ ]] || [ "$num" -le 0 ] || [ "$num" -ge 10000 ]; then
    echo "Error: num must be a number between 0001 and 9999"
    exit 1
fi

# 检查 title 的格式是否符合要求
if ! echo "$title" | grep -E "^[A-Za-z ]+/[一-龥]+$" > /dev/null; then
    echo "Error: title must be in the format 'English/Chinese', e.g., 'Two Sum/两数之和'"
    exit 1
fi

# 检查 difficulty 是否为有效值
if [[ "$difficulty" != "Easy" && "$difficulty" != "Medium" && "$difficulty" != "Difficult" ]]; then
    echo "Error: difficulty must be one of 'Easy', 'Medium', or 'Difficult'"
    exit 1
fi

# 更新 README.md 文件
python update_readme.py "$num" "$title" "$difficulty"

# Git 提交信息
commit_message="$(date +%Y%m%d)-$num"

# 更新 Git 主分支
git status
git add .
git commit -m "$commit_message"
git push origin main
