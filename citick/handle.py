import os
import sys

#########   日志设置    ##########
import logging
import time

logger = logging.getLogger("AppName")  # 获取logger实例，如果参数为空则返回root logger
formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")  # 指定logger输出格式

file_handler = logging.FileHandler("out.log", encoding='utf-8')  # 文件日志
file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式

logger.addHandler(file_handler)  # 为logger添加的日志处理器，可以自定义日志处理器让其输出到其他地方
logger.setLevel(logging.INFO)  # 指定日志的最低输出级别，默认为WARN级别


def handle_data(path1, word, path2, result_file):
    """
    :param path1: 是样本文件，主要用来筛选573那行的
    :param word: 数据文件，对比573那行找出含有标题的样本
    :param path2: 要筛选的文件，取出符合的四行
    :param result_file: 保存的结果文件
    :return: none
    """

    logger.info("======= 开始处理文件 =======")
    try:
        if(os.path.exists(result_file)):
            os.remove(result_file)  # 先删除文件
            logger.info("删除文件%s成功", result_file)
        else:
            logger.info("文件不存在开始写入...", result_file)

    except Exception as e:
        logger.info("删除文件%s失败，%s", result_file, e)

    start = time.time()
    line_num = 0
    with open(path1, "r") as f1:  # 打开第一个文件
        logger.info("打开参考文件 ---" + path1)

        with open(path2, "r") as f2:  # 打开第二个文件
            logger.info("打开数据文件 ---" + path2)

            with open(result_file, "a+") as f3:  # 打开要保存的文件
                logger.info("打开存储文件 ---" + result_file)

                for line1 in f1:
                    one_line = line1.split()  # 分割一行

                    if one_line[2] == word:

                        for line2 in f2:  # 如果存在话就开始写入文件
                            if one_line[1] in line2:
                                line_num += 1
                                f3.write(line2)
                                f3.write(f2.readline())
                                f3.write(f2.readline())
                                f3.write(f2.readline())
                                if line_num % 10000 == 0:
                                    temp = time.time()

                                    logger.info("已处理数据 %s,耗时 %s", line_num, temp - start)

                                break
                logger.info("共处理数据%s条，共耗时", line_num, time.time() - start)
                logger.info("======= 结束处理文件 =======")


if __name__ == '__main__':

    out_txt = sys.argv[1]  # 第一个参数
    word = sys.argv[2]  # 第二个参数
    mid_txt = sys.argv[3]
    result_txt = "result.txt"
    if len(sys.argv) == 5:
        result_txt = sys.argv[4]

    handle_data(out_txt, word, mid_txt, result_txt)
