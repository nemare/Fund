# coding=utf-8
import pandas as pd

# read data
df_mfd_bank_shibor = pd.read_csv('mfd_bank_shibor.csv')
df_mfd_day_share_interest = pd.read_csv('mfd_day_share_interest.csv')
df_user_balance_table = pd.read_csv('user_balance_table.csv')
# fill with 0
df_user_balance_table = df_user_balance_table.fillna(0)
df_user_profile_table = pd.read_csv('user_profile_table.csv')
# df_mfd_bank_shibor_sep = pd.read_excel('mfd_bank_shibor_sep.xls', 'Sheet')

# left outer joind df_mfd_day_share_interest with df_mfd_bank_shibor
df_mfd_zhifubao_bank = pd.merge(df_mfd_day_share_interest, df_mfd_bank_shibor, how='left', on='mfd_date')
# suppose weekends' shibor doesn't make any sense, so fill with 0
df_mfd_zhifubao_bank = df_mfd_zhifubao_bank.fillna(0)
# left outer join
df_user_balance_zhifubao_bank = pd.merge(df_user_balance_table, df_mfd_zhifubao_bank, how='left', left_on='report_date',
                                         right_on='mfd_date')
# convert to datetime and sort by report_date TODO 考虑休假
df_user_balance_zhifubao_bank['diff'] = df_user_balance_zhifubao_bank['report_date'].apply(
    lambda x: (pd.to_datetime(x, format='%Y%m%d') - pd.to_datetime('2013-07-01')).days)
df_user_balance_zhifubao_bank['report_date'] = df_user_balance_zhifubao_bank['report_date'].apply(
    lambda x: (pd.Timestamp(pd.to_datetime(x, format='%Y%m%d')).weekday()))
# df_user_balance_zhifubao_bank = df_user_balance_zhifubao_bank.sort('report_date')
df_user_balance_zhifubao_bank = df_user_balance_zhifubao_bank.sort('report_date')
# print (df_user_balance_zhifubao_bank)
print (df_user_balance_zhifubao_bank.head())

# proccess data
print (pd.merge(df_user_profile_table, df_user_balance_zhifubao_bank, on='user_id').head())
df = pd.merge(df_user_profile_table, df_user_balance_zhifubao_bank, on='user_id').loc[:
, ['user_id', 'sex', 'city', 'constellation', 'report_date', 'diff', 'mfd_date', 'mfd_daily_yield', 'mfd_7daily_yield'
         , 'Interest_O_N', 'Interest_1_W', 'Interest_2_W', 'Interest_1_M'
         , 'Interest_3_M', 'Interest_6_M', 'Interest_9_M', 'Interest_1_Y', 'total_purchase_amt', 'total_redeem_amt']]
# 	user_id	report_date	mfd_date	mfd_daily_yield	mfd_7daily_yield	Interest_O_N	Interest_1_W	Interest_2_W	Interest_1_M	Interest_3_M	Interest_6_M	Interest_9_M	Interest_1_Y
# 2835211	332	2013-07-01 00:00:00	20130701	1.5787	6.307	4.456	5.423	6.04	6.88	5.295	4.239	4.282	4.4125

df.to_csv('data.csv')
# print (df)
print ('done')
