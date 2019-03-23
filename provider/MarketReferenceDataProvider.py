# -*- encoding:utf-8 -*-

import tushare as ts

from common import TokenReader as tr


class MarketReferenceDataProvider(object):
    """
    desc: tushare 的市场参考数据 demo
    """

    def __init__(self):
        self.pro = ts.pro_api(tr.get())

    # 沪深港通资金流向
    def get_moneyflow_hsgt(self):
        return self.pro.moneyflow_hsgt(start_date='20190101', end_date='20190321')

    # 沪深通十大成交股
    def get_hsgt_top_10(self):
        return self.pro.hsgt_top10(trade_date='20190322', market_type='1')

    # 港股通十大成交股
    def get_ggt_top_10(self):
        return self.pro.ggt_top10(trade_date='20190322')

    # 融资融券交易汇总
    def get_margin(self):
        return self.pro.margin(trade_date='20190322')

    # 融资融券交易明细
    def get_margin_detail(self):
        return self.pro.margin_detail(trade_date='20190322')

    # 前十大股东
    def get_holders_top_10(self):
        return self.pro.top10_holders(ts_code='600000.SH',
                                      start_date='20170101',
                                      end_date='20171231')

    # 前十大流通股东
    def get_float_holders_top_10(self):
        return self.pro.top10_floatholders(ts_code='600000.SH',
                                           start_date='20170101',
                                           end_date='20171231')

    # 龙虎榜每日明细
    def get_top_list(self):
        return self.pro.top_list(trade_date='20190322')

    # 龙虎榜机构明细
    def get_top_inst(self):
        return self.pro.top_inst(trade_date='20190322')

    # 股权质押统计数据
    def get_pledge_stat(self):
        return self.pro.pledge_stat(ts_code='000014.SZ')

    # 股权质押明细数据
    def get_pledge_detail(self):
        return self.pro.pledge_detail(ts_code='000014.SZ')

    # 股票回购
    def get_repurchase(self):
        return self.pro.repurchase(ann_date='',
                                   start_date='20190101',
                                   end_date='20190322')

    # 概念股分类表
    def get_concept(self):
        return self.pro.concept(src='ts')

    # 限售股解禁
    def get_share_float(self):
        return self.pro.share_float(ann_date='20190322')

    # 大宗交易
    def get_block_trade(self):
        return self.pro.block_trade(trade_date='20190322')

    # 股票开户数据
    def get_stk_account(self):
        return self.pro.stk_account(start_date='20180101', end_date='20181231')

    # 股东人数
    def get_stk_holder_number(self):
        return self.pro.stk_holdernumber(ts_code='300199.SZ',
                                         start_date='20160101',
                                         end_date='20181231')


if __name__ == '__main__':
    provider = MarketReferenceDataProvider()
    print(provider.get_margin_detail())
