#!/bin/bash


# parameters
num=$1
title="$2"
difficulty=$3


# check parameters
check_args() {
    if [ $# -ne 3 ]; then
        echo "Usage: $0 num title difficulty"
        exit 1
    fi
}

check_file() {
    if git ls-files --error-unmatch "code.$1.py" >/dev/null 2>&1; then
        echo "Error: code.$1.py is already being tracked by git."
        exit 1
    fi
}

check_difficulty() {
    if [ "$1" != "Easy" ] && [ "$1" != "Medium" ] && [ "$1" != "Difficult" ]; then
        echo "Error: Difficulty must be Easy, Medium, or Difficult."
        exit 1
    fi
}

check_args "$@"
check_file "$num"
check_difficulty "$difficulty"


# date
current_date=$(date +%Y.%m.%d)


# update README.md
echo "| $num | $title | [Code](https://github.com/YanY-Henry/LeetCode/blob/main/code/$num.py) | $difficulty |" >> README.md


# update GitHub repo
git add .
git commit -m "$current_date-$num"
git push origin main