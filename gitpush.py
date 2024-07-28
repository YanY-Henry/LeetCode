import re
import sys

def update_readme(num, title, difficulty):
    # 读取现有的 README 文件
    with open('README.md', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 定义新行
    new_line = f"| {num} | {title} | [Python](https://github.com/YanY-Henry/LeetCode/blob/main/code/{num.zfill(4)}.py) | {difficulty} |\n"

    # 处理现有行
    new_lines = []
    inserted = False

    for line in lines:
        if not re.match(r'\|\s*\d+\s*\|', line):
            # 如果不是表格格式的行，直接添加到 new_lines
            new_lines.append(line)
        else:
            # 提取当前行的编号
            match = re.match(r'\|\s*(\d+)\s*\|', line)
            if match:
                current_num = match.group(1)
                if num < current_num and not inserted:
                    # 在找到第一个大于新编号的位置之前，插入新行
                    new_lines.append(new_line)
                    inserted = True
            new_lines.append(line)
    
    if not inserted:
        # 如果没有找到比新编号大的编号，追加到文件末尾
        new_lines.append(new_line)

    # 写入更新后的内容
    with open('README.md', 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python update_readme.py {num} \"{title}\" {difficulty}")
        sys.exit(1)
    
    num = sys.argv[1]
    title = sys.argv[2]
    difficulty = sys.argv[3]
    
    update_readme(num, title, difficulty)
