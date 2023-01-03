import os
import sys

import logging
# 获取logger实例，如果参数为空则返回root logger
logger = logging.getLogger("AppName")

# 指定logger输出格式
formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")

# 文件日志
file_handler = logging.FileHandler("handle.log",encoding='utf-8')
file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式

# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.formatter = formatter  # 也可以直接给formatter赋值

# 为logger添加的日志处理器，可以自定义日志处理器让其输出到其他地方
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 指定日志的最低输出级别，默认为WARN级别
logger.setLevel(logging.INFO)

# os.remove("ddd")

# def handle_data(path1,path2,compare,result_file);
def demo():
    logger.info("============开始处理数据==========")
    with open("requirements.txt", "r") as f:
        # print(f.readlines())
        for x in range(4):

            for line in f:
                print(line)
                print(f.readline())
                print(f.readline())
                print(f.readline())
                logger.info(line)
                break


        # one_line = line.split()
        # if one_line[2] == "573":
        #     with open("new_file.txt", "a+") as f2:
        #         f2.write(line)
        #         print(line.replace("\n", ""))
        # Pr    ocessing data

if __name__ == '__main__':
    demo()

    # out_txt = sys.argv[1]
    # word = sys.argv[2]
    # mid_txt = sys.argv[3]
    # if len(sys.argv) == 5:
    #     result_txt = sys.argv[4]
    #
    # handle_data(out_txt, mid_txt, word,result_txt)
