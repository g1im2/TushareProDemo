# -*- encoding=utf-8 -*-

import tushare as ts

from common import TokenReader as tr


class IndexDataProvider(object):
    """
    desc: 指数 demo
    """

    def __init__(self):
        self.pro = ts.pro_api(tr.get())

    # 指数基本信息
    def get_index_basic(self):
        return self.pro.index_basic(market='SW')

    # 指数日线行情
    def get_index_daily(self):
        return self.pro.index_daily(ts_code='399300.SZ')

    # 指数成分和权重
    def get_index_weight(self):
        return self.pro.index_weight(index_code='399300.SZ',
                                     start_date='20180901',
                                     end_date='20180930')

    # 大盘指数每日指标
    def get_index_daily_basic(self):
        return self.pro.index_dailybasic(trade_date='20190322',
                                         fields='ts_code,trade_date,turnover_rate,pe')


if __name__ == '__main__':
    provider = IndexDataProvider()
    print(provider.get_index_daily_basic())
