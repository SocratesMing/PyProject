import os.path
import re


def has_save_to_cloud(name: str) -> set:
    """
    通过txt里面的内容记录有哪些是存过的
    :param name:
    :return:
    """
    txt = name + ".txt"
    saved_list = []
    if not os.path.exists(txt):
        with open(txt, "w") as f:
            pass
    if os.path.exists(txt):
        with open(txt, 'r', encoding="utf-8") as f:
            for t in f:
                if "-----" not in t:
                    saved_list.append(t.replace("\n", ""))

    return set(saved_list)


def check_ok(list_txt, path):
    record_list = []
    for txt in list_txt:
        with open(txt, "r", encoding="utf-8") as f:
            for line in f:
                # print(line)
                match = re.findall(r'No\.(\d+)', line)
                if len(match) > 0:
                    record_list.append(match[0])

    # 查找记录和那些不在已经下载的列表里面

    listdir = os.listdir(path)
    print("存到百度云的总计:", len(record_list))
    print("下载解压完的总计:", len(listdir))
    for saved in record_list:
        if saved in listdir:
            pass
        else:
            print(saved, "没有下载...")

    for upzip in listdir:
        if upzip in record_list:
            pass
        else:
            print(upzip, "没有存到txt")


def set_txt(name: str) -> None:
    """
    去重
    :param name:
    :return:
    """
    txt = name + ".txt"
    saved_list = []
    if os.path.exists(txt):
        with open(txt, 'r', encoding="utf-8") as f:
            for t in f:
                saved_list.append(t)

    os.remove(name + ".txt")
    with open(txt, 'a', encoding="utf-8") as f:
        for t in set(saved_list):
            f.write(t)


if __name__ == '__main__':
    # set_txt("安然anran")
    path = "D:\下载\BaiduNetdiskDownload\picture"
    list = ["YUNDUOER_.txt", "安然anran.txt", "安然Maleah.txt"]
    check_ok(list, path)
    pass
