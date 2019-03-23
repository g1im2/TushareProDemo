# -*- encoding:utf-8 -*-

import tushare as ts

from common import TokenReader as tr


class MarketDataProvider(object):
    """
    desc: 市场行情数据 demo
    """

    def __init__(self):
        self.pro = ts.pro_api(tr.get())

    # 日线行情
    def get_daily(self):
        return self.pro.daily(ts_code='002230.SZ',
                              start_date='20190320',
                              end_date='20190322')

    # 周线行情
    def get_weekly(self):
        return self.pro.weekly(ts_code='000001.SZ',
                               start_date='20190101',
                               end_date='20190322',
                               fields='ts_code,trade_date,open,high,low,close,vol,amount')

    # 月线行情
    def get_monthly(self):
        return self.pro.monthly(ts_code='000001.SZ',
                                start_date='20180101',
                                end_date='20190322',
                                fields='ts_code,trade_date,open,high,low,close,vol,amount')

    # 复权行情
    def get_pro_bar(self):
        return ts.pro_bar(pro_api=self.pro,
                          ts_code='000001.SZ',
                          adj='qfq',
                          start_date='20180101',
                          end_date='20181011')

    # 停复牌信息
    def get_suspend(self):
        return self.pro.suspend(ts_code='600848.SH',
                                suspend_date='',
                                resume_date='',
                                fields='')

    # 每日指标, 可以看做是日线图数据的详细情况
    def get_daily_basic(self):
        return self.pro.daily_basic(ts_code='002230.SZ',
                                    trade_date='20190322',
                                    fields='ts_code,trade_date,turnover_rate,volume_ratio,pe,pb')

    # 复权因子
    def get_adj_factor(self):
        return self.pro.adj_factor(ts_code='000001.SZ', trade_date='')


if __name__ == '__main__':
    provider = MarketDataProvider()
    print(provider.get_daily_basic())
