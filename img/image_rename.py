import os


def batch_rename_images(
        folder: str = os.getcwd(),
        prefix: str = "image",
        start_num: int = 1,
        num_digits: int = 4,
        preview: bool = False
) -> None:
    """
    按文件夹内文件默认排序的批量重命名工具
    :param folder: 目标文件夹（默认当前目录）
    :param prefix: 文件名前缀（默认：image）
    :param start_num: 起始序号（默认：1）
    :param num_digits: 序号位数（补零，默认：4）
    :param preview: 预览模式（不实际修改，默认：False）
    """
    # 支持的图片格式
    img_ext = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg')

    # 验证文件夹是否存在
    if not os.path.isdir(folder):
        print(f"❌ 错误：文件夹不存在 - {folder}")
        return

    # 获取所有图片文件（按「文件名默认顺序」排序，与文件夹显示一致）
    img_files = [f for f in os.listdir(folder) if
                 f.lower().endswith(img_ext) and os.path.isfile(os.path.join(folder, f))]
    img_files.sort()  # 关键修改：按文件名本身排序（系统默认顺序）

    if not img_files:
        print("❌ 未找到图片文件！")
        return

    print(f"找到 {len(img_files)} 张图片，{'预览' if preview else '开始'}重命名：")
    print("-" * 60)

    # 批量处理
    for idx, old_name in enumerate(img_files, start=start_num):
        # 分离扩展名
        ext = os.path.splitext(old_name)[1]
        # 生成新文件名
        new_name = f"{prefix}_{idx:0{num_digits}d}{ext}"
        old_path = os.path.join(folder, old_name)
        new_path = os.path.join(folder, new_name)

        # 跳过已存在的文件
        if os.path.exists(new_path):
            print(f"❌ 跳过：{old_name} -> {new_name}（已存在）")
            continue

        # 预览或执行重命名
        if preview:
            print(f"👀 预览：{old_name} -> {new_name}")
        else:
            try:
                os.rename(old_path, new_path)
                print(f"✅ 成功：{old_name} -> {new_name}")
            except Exception as e:
                print(f"❌ 失败：{old_name} -> {new_name}（错误：{str(e)}）")

    print("-" * 60)
    print("处理完成！")


if __name__ == "__main__":
    # 直接修改这里的参数即可使用
    batch_rename_images(
        folder="D:/boke/my-blog/hugo-reimu-template/content/img/NO.34",  # 目标文件夹路径
        prefix="图",  # 自定义前缀（如"风景"、"旅行"）
        start_num=1,  # 起始序号
        num_digits=2,  # 序号位数（如3位：001, 002...）
        preview=False  # 先预览（True），确认后改False执行
    )