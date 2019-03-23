# -*- encoding:utf-8 -*-

import tushare as ts

from common import TokenReader as tr


class FundDataProvider(object):
    """
    desc: 基金 demo
    """

    def __init__(self):
        self.pro = ts.pro_api(tr.get())

    # 公募基金列表
    def get_fund_basic(self):
        return self.pro.fund_basic(market='E')

    # 公募基金管理人列表
    def get_fund_company(self):
        return self.pro.fund_company()

    # 公募基金净值
    def get_fund_nav(self):
        return self.pro.fund_nav(ts_code='165509.SZ')

    # 公募基金分红
    def get_fund_div(self):
        return self.pro.fund_div(ann_date='20190321')

    # 公募基金持仓数据
    def get_fund_portfolio(self):
        return self.pro.fund_portfolio(ts_code='001753.OF')

    # 场内基金日线行情
    def get_fund_daily(self):
        return self.pro.fund_daily(ts_code='150018.SZ',
                                   start_date='20190101',
                                   end_date='20190322')


if __name__ == '__main__':
    provider = FundDataProvider()
    print(provider.get_fund_daily())
