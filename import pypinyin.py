import chardet
from pypinyin import lazy_pinyin

def read_idiom_file(file_path):
    try:
        with open(file_path, 'rb') as f:
            raw_data = f.read()
            result = chardet.detect(raw_data)
            encoding = result['encoding']
        try:
            with open(file_path, 'r', encoding=encoding) as rd:
                data = rd.read()
        except UnicodeDecodeError:
            try:
                with open(file_path, 'r', encoding='gbk') as rd:
                    data = rd.read()
            except UnicodeDecodeError:
                with open(file_path, 'r', encoding='latin1') as rd:
                    data = rd.read()
        return data.split("\n")
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        exit()
    except UnicodeDecodeError:
        print("Error: Unable to decode file with detected encoding.")
        exit()

# 读取成语文件
file_path = r"D:\Code\idiom.txt"
idioms = read_idiom_file(file_path)

while True:
    # 获取用户输入
    print("Input some partial pinyin (e.g., zh? an ? jie)：")
    input_sequence = input().split()  # 获取用户输入并按空格分割

    outs = []

    # 遍历成语，查找与输入拼音模式匹配的成语
    for idiom in idioms:
        if len(idiom) == 4:
            idiom_pinyin_list = lazy_pinyin(idiom)  # 获取成语的拼音列表
            if len(idiom_pinyin_list) != len(input_sequence):
                continue

            match = True
            for idx, (user_input, idiom_pinyin) in enumerate(zip(input_sequence, idiom_pinyin_list)):
                if user_input == "/" or user_input == "":
                    continue  # 忽略用户输入中的问号或空字符串
                if user_input not in idiom_pinyin:
                    match = False
                    break

            if match:
                outs.append(idiom)

    # 输出匹配的成语
    print("Output：")
    if outs:
        for idiom in outs:
            print(idiom)
    else:
        print("No matching idioms found.")

    # 询问用户是否继续
    print("\nPress Enter to try again or any other key followed by Enter to exit:")
    choice = input().lower()
    if choice != '':
        print("Thanks for playing! Goodbye!")
        break
