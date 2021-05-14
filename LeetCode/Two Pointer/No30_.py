# import pprint
#
# mm = "test driver"
#
# assert "driver" in mm
#
# dic = {}
# for x in range(100, 1, -1):
#     dic[x] = "66"
#
# for k, v in dic.items():
#     print(k, v)
#
# pp = pprint.PrettyPrinter(indent=4)
# print(dic)
# raise ValueError("dddd")  # python3 抛出异常的方式

# Import logging module
import logging
logger = logging.getLogger(__name__)  # Create a custom logger
handler = logging.StreamHandler  # Using stream handler
# Set logging levels
handler.setLevel(level=logging.DEBUG)
# handler.setLevel(logging.ERROR)
format_c = logging.Formatter("%(name) - %(levelname) - % (message) ")
handler.setFormatter(fmt=format_c)  # Add formater to handler
logger.addHandler(handler)


def division(divident, divisor):
    try:
        return divident / divisor
    except ZeroDivisionError:
        logger.error("Zero Division Error")


num = division(4, 0)
