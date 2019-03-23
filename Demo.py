# -*- encoding:utf-8 -*-

import tushare as ts

from common import TokenReader as tr


class Demo(object):
    """
    desc: 这是一个如何使用日线数据进行筛选并打印的示例
    """

    def __init__(self):
        self.pro = ts.pro_api(tr.get())

    def run(self):
        df = self.pro.daily(ts_code='000001.SZ',
                       start_date='20190101',
                       end_date='20190322')

        for index in df.index:
            index_data = df.loc[index]
            print('股票代码', index_data['ts_code'],
                  '交易日期', index_data['trade_date'],
                  '开盘价', index_data['open'],
                  '最高价', index_data['high'],
                  '最低价', index_data['low'],
                  '收盘价', index_data['close'],
                  '昨天收盘价', index_data['pre_close'],
                  '涨跌幅', index_data['change'],
                  '涨跌幅(未复权)', index_data['pct_chg'],
                  '成交量', index_data['vol'],
                  '成交额', index_data['amount'],)


if __name__ == '__main__':
    demo = Demo()
    demo.run()
