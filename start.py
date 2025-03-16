import os
import json

def get_directory_structure(rootdir):
    """
    遍历指定目录，生成嵌套的字典结构，只记录文件名
    """
    dir_structure = {}
    for item in os.listdir(rootdir):
        item_path = os.path.join(rootdir, item)
        if os.path.isdir(item_path):
            # 如果是文件夹，递归处理
            dir_structure[item] = get_directory_structure(item_path)
        else:
            # 如果是文件，直接记录文件名
            dir_structure[item] = item
    return dir_structure

def save_to_json(data, output_file):
    """
    将字典数据保存为 JSON 文件
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    # 设置要遍历的根目录路径
    root_directory = input("请输入要遍历的根目录路径: ").strip()
    if not os.path.isdir(root_directory):
        print("输入的路径不是一个有效的目录!")
        exit(1)

    # 获取目录结构
    directory_structure = get_directory_structure(root_directory)

    # 设置输出的 JSON 文件路径
    output_json_file = os.path.join(root_directory, "directory_structure.json")

    # 保存为 JSON 文件
    save_to_json(directory_structure, output_json_file)
    print(f"目录结构已保存到 {output_json_file}")