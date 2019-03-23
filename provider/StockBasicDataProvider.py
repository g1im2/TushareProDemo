# -*- encoding:utf-8 -*-

import tushare as ts

from common import TokenReader as tr


class StockBasicDataProvider(object):
    """
    desc: 包含 tushare 股票基本信息的接口调用，这些结果的返回结果一般为 pandas 的 frame-data
    """

    def __init__(self):
        self.pro = ts.pro_api(tr.get())

    # 获取沪深股市的股票列表, 具体参数请参考 tushare 网站的接口说明文档
    def get_stock_basic(self):
        return self.pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')

    # 用来获取沪深股市的交易状态, 可用来查询某一天是否开市或者闭市
    def get_trade_cal(self):
        return self.pro.trade_cal(exchange='', start_date='20190321', end_date='20190322')

    # 获取深股通或者沪股通的成分数据, 也就是这个成分中所有的股票代码以及纳入时间信息
    def get_hs_const(self):
        return self.pro.hs_const(hs_type='SZ')

    # 获取股票的曾用名信息
    def get_name_change(self):
        return self.pro.namechange(ts_code='600848.SH', fields='ts_code,name,start_date,end_date,change_reason')

    # 获取上市公司的基本信息
    def get_stock_company_info(self):
        return self.pro.stock_company(exchange='SZSE',
                                      fields='ts_code,chairman,manager,secretary,reg_capital,setup_date,province')

    # 获取 ipo 新股列表
    def get_new_share(self):
        return self.pro.new_share(start_date='20190322', end_date='20190331')


if __name__ == '__main__':
    bs = StockBasicDataProvider()
    print(bs.get_new_share())
