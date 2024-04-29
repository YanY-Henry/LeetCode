#!/bin/bash


# parameters
num=$1
title="$2"
difficulty=$3


# check parameters
check_args() {
    if [ $# -ne 3 ]; then
        echo "Usage: $0 {num} \"{title}\" {difficulty}"
        exit 1
    fi
}

check_file() {
    if git ls-files --error-unmatch "code/$1.py" >/dev/null 2>&1; then
        echo "Error: $1.py is already being tracked by git."
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


# read existing solution information
existing_solutions=$(sed -n '/^\| #\|^---/p' README.md)


# extract solution information from existing solutions
while read -r line; do
    if [[ "$line" =~ ^\| [0-9]{4} \| ]]; then
        num=$(echo $line | cut -d '|' -f 2)
        title=$(echo $line | cut -d '|' -f 3 | sed 's/^"|"$//g')
        code_link=$(echo $line | cut -d '|' -f 4 | sed 's/^"|"$//g')
        difficulty=$(echo $line | cut -d '|' -f 5 | sed 's/^"|"$//g')
        solutions[$num]="|$num|$title|$code_link|$difficulty|"
    fi
done <<< "$existing_solutions"


# add new solution information
new_solution="|$num|$title|[Code](https://github.com/YanY-Henry/LeetCode/blob/main/code/$num.py)|$difficulty|"
solutions[$num]=$new_solution


# sort solutions array by num
sorted_solutions=$(sort -k 1n <<< "${!solutions[@]}")


# generate new table
echo "| # | Title | Solution | Difficulty |" | tee README.md
for num in "${sorted_solutions[@]}"; do
    echo "${solutions[$num]}" >> README.md
done


# update GitHub repo
git status
git add .
git commit -m "$current_date-$num"
git push origin main
