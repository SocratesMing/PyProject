import os.path


def has_save_to_cloud(name):
    txt = name+".txt"
    saved_list = []
    if not os.path.exists(txt):
        with open(txt, "w") as f:
            pass
    if os.path.exists(txt):

        with open(txt,encoding="utf-8") as f:
            for line in f.read().splitlines():
                if name in line :
                    saved_list.append(line)

    return saved_list

if __name__ == '__main__':
    pass
    # has_save_to_cloud("梦心玥")
    # for x in [2,5,6]:
    #     print(x)