import os
import shutil
import tarfile
import py7zr


def create_if_not_exist(dist_path):
    if (not os.path.exists(dist_path)):
        os.makedirs(dist_path)
        print("创建文件夹:", dist_path)
    else:
        print(dist_path, "已存在")


def clear_path(dist_path):
    for f in os.listdir(dist_path):
        fff = os.path.join(dist_path,f)
        if os.path.isdir(fff):
            shutil.rmtree(fff)
        if os.path.isfile(fff):
            os.remove(fff)



def rename_yw_7z(filename):
    file7z = ""
    if filename.endswith("yw"):
        file7z = filename.replace(".yw", ".7z")
        # print(file7z)
        fileyw_path = os.path.join(path, filename)
        file7z_path = os.path.join(path, file7z)
        os.rename(fileyw_path, file7z_path)
        print("重命名为:",file7z_path)
    else:
        file7z = filename
        file7z_path = os.path.join(path, file7z)
        print(file7z_path)

    return file7z_path


def extract_7zfile(file7z_path, path_extract):
    if file7z_path.endswith("7z"):
        with py7zr.SevenZipFile(file7z_path, mode='r', password=pwd) as z7:
            print("正在解压:", file7z_path)
            z7.extractall(path_extract)
            print("解压至:", path_extract)

    if file7z_path.endswith("tar"):
        with tarfile.open(file7z_path, "r") as tar:
            print("正在解压:", file7z_path)
            tar.extractall(path_extract)
            print("解压至:", path_extract)


def extract_sub7zfile(file7z_path2, file_extract_path, dist_path):
    with open(file7z_path2, 'ab') as outfile:  # append in binary mode
        for sub_file in os.listdir(file_extract_path):
            if "7z" in sub_file:
                sub_file_extract_path = os.path.join(file_extract_path, sub_file)
                print("多级压缩文件 - ", sub_file_extract_path)
                with open(sub_file_extract_path, 'rb') as infile:  # open in binary mode also
                    outfile.write(infile.read())

        with py7zr.SevenZipFile(file7z_path2, mode='r', password=pwd) as z72:
            print("正在解压:", file7z_path2)
            z72.extractall(dist_path)
            print("解压至:", dist_path)


#                 print("= " * 30)


def renameTo7z(path: str, flag=False):
    """
    :param path: 路径
    :param flag: 解压过得是否重新解压，true表示解压过不再解压
    """
    path_pic = os.path.join(path, "picture")
    path_extract = os.path.join(path, "extract")
    create_if_not_exist(path_pic)
    create_if_not_exist(path_extract)

    num = 1
    for fileyw in os.listdir(path):
        if fileyw.endswith("7z") and flag is True:
            print(os.path.join(path, fileyw), "已解压过不再解压")
            pass
        elif os.path.isdir(fileyw):
            pass
        else:
            file7z_path = rename_yw_7z(fileyw)
            if file7z_path != "":
                extract_7zfile(file7z_path, path_extract)
                file_num = os.listdir(path_extract)
                if len(file_num) == 1:
                    file1 = os.path.join(path_extract, file_num[0])
                    if os.path.isdir(file1):
                        if len(os.listdir(file1)) > 10:
                            extract_7zfile(file7z_path, path_pic)
                        else:
                            file7z_path2 = os.path.join(path_extract, "temp.7z")
                            extract_sub7zfile(file7z_path2, file1, path_pic)

                    else:
                        file2 = rename_yw_7z(os.path.join(path_extract, file_num[0]))
                        extract_7zfile(file2, path_pic)
                    print("第", num, "个解压完成")
                    print("- " * 30)
                    num += 1
                else:
                    pass

                clear_path(path_extract)


if __name__ == '__main__':
    path = r"D:\下载\BaiduNetdiskDownload"
    # path = r"C:\Users\sututu\Downloads"
    pwd = "youwu"

    renameTo7z(path, True)
