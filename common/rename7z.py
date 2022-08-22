import os
import py7zr


def renameTo7z(path:str,pwd:str):

    dist_path =os.path.join(path,"picture")
    if(not os.path.exists(dist_path)):
        os.makedirs(dist_path)
        print("创建文件夹:",dist_path)
    else:
        print(dist_path,"已存在")


    for fileyw in os.listdir(path):
        file7z_path = ""
        if fileyw.endswith("yw"):
            file7z = fileyw.replace(".yw",".7z")
            # print(file7z)
            fileyw_path = os.path.join(path,fileyw)
            file7z_path = os.path.join(path,file7z)
            os.rename(fileyw_path,file7z_path)
            print(file7z_path)
        if fileyw.endswith(".7z"):
            file7z = fileyw
            file7z_path = os.path.join(path,file7z)
            print(file7z_path)


        if file7z_path !="":
            with py7zr.SevenZipFile(file7z_path, mode='r', password=pwd) as z7:
                print("正在解压:",file7z_path)
                z7.extractall(path)
                print("解压至:", path)

                file_extract_path = file7z_path.replace(".7z","")
                if os.path.exists(file_extract_path):
                    file7z_path2 = os.path.join(file_extract_path,file7z)
                    print("file7z_path2",file7z_path2)
                    with open(file7z_path2, 'ab') as outfile:  # append in binary mode
                        for sub_file in os.listdir(file_extract_path):
                            sub_file_extract_path = os.path.join(file_extract_path,sub_file)
                            print("sub_file_extract_path",sub_file_extract_path)
                            with open(sub_file_extract_path, 'rb') as infile:  # open in binary mode also
                                outfile.write(infile.read())

                        with py7zr.SevenZipFile(file7z_path2, mode='r', password=pwd) as z72:
                            print("正在解压:", file7z_path2)
                            z72.extractall(dist_path)
                            print("解压至:", dist_path)
                            print("= " * 30)
                        # for fname in filenames:
                        #     with open(fname, 'rb') as infile:  # open in binary mode also
                        #         outfile.write(infile.read())

                    # for sub_file in os.listdir(file_extract_path):
                    #     print(sub_file)
                    #     if sub_file.endswith(".001"):
                    #         sub_file_extract_path = os.path.join(file_extract_path,sub_file)






if __name__ == '__main__':
    path = "D:\下载\BaiduNetdiskDownload"
    pwd = "youwu"

    renameTo7z(path,pwd)