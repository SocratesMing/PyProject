import os.path


def has_save_to_cloud(name:str)->set:
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
    set_txt("安然Maleah")
    pass
