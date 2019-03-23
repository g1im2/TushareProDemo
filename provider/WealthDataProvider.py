# -*- encoding:utf-8 -*-


import tushare as ts

from common import TokenReader as tr


class WealthDataProvider(object):
    """
    desc: tushare 的财务数据demo
    """

    def __init__(self):
        self.pro = ts.pro_api(tr.get())

    # 获取利润表, 具体参数请参照 api 接口说明
    def get_income(self):
        return self.pro.income(ts_code='600000.SH',
                               start_date='20180101',
                               end_date='20180730',
                               fields='ts_code,ann_date,f_ann_date,end_date,report_type,comp_type,basic_eps,diluted_eps')

    # 获取资产负债表信息, 具体参数请参照 api 接口说明
    def get_balance_sheet(self):
        return self.pro.balancesheet(ts_code='600000.SH',
                                     start_date='20180101',
                                     end_date='20180730',
                                     fields='ts_code,ann_date,f_ann_date,end_date,report_type,comp_type,cap_rese')

    # 获取现金流表信息, 具体参数请参照 api 接口说明
    def get_cash_flow(self):
        return self.pro.cashflow(ts_code='600000.SH',
                                 start_date='20180101',
                                 end_date='20180730')

    # 获取业绩报告, 具体参数请参照 api 接口说明
    def get_forecast(self):
        return self.pro.forecast(ann_date='20190131',
                                 fields='ts_code,ann_date,end_date,type,p_change_min,p_change_max,net_profit_min')

    # 获取分红送股数据, 具体参数请参照 api 接口说明
    def get_dividend(self):
        return self.pro.dividend(ts_code='600848.SH',
                                 fields='ts_code,div_proc,stk_div,record_date,ex_date')

    # 获取业绩快报, 具体参数请参照 api 接口说明
    def get_express(self):
        return self.pro.express(ts_code='600000.SH',
                                start_date='20180101',
                                end_date='20180701',
                                fields='ts_code,ann_date,end_date,revenue,operate_profit,total_profit,n_income,total_assets')

    # 获取财务指标数据, 具体参数请参照 api 接口说明
    def get_fina_indicator(self):
        return self.pro.fina_indicator(ts_code='600000.SH')

    # 获取财务审计意见, 具体参数请参照 api 接口说明
    def get_fina_audit(self):
        return self.pro.fina_audit(ts_code='600000.SH', start_date='20100101', end_date='20180808')

    # 获取主营业务构成, 具体参数请参照 api 接口说明
    def get_fina_mainbz(self):
        return self.pro.fina_mainbz(ts_code='000627.SZ', period='20171231', type='P')

    # 获取财报披露计划
    def get_disclosure_date(self):
        return self.pro.disclosure_date(end_date='20181231')


if __name__ == '__main__':
    provider = WealthDataProvider()
    print(provider.get_disclosure_date())
