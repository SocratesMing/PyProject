import qlib
print(qlib.__version__)

from qlib.constant import REG_CN
provider_uri = "./qlib_data/cn_data"  # target_dir
qlib.init(provider_uri=provider_uri, region=REG_CN)

from qlib.data import D

print(D.calendar(start_time='2010-01-01', end_time='2017-12-31', freq='day')[:2])
print(D.instruments(market='all'))
