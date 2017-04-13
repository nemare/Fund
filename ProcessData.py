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
# convert to datetime and sort by report_date
df_user_balance_zhifubao_bank['report_date'] = df_user_balance_zhifubao_bank['report_date'].apply(
    lambda x: (pd.to_datetime(x, format='%Y%m%d') - pd.to_datetime('2013-07-01')).days)
df_user_balance_zhifubao_bank = df_user_balance_zhifubao_bank.sort('report_date')
# print (df_user_balance_zhifubao_bank)
# print (df_user_balance_zhifubao_bank.head())
#          user_id  report_date  tBalance  yBalance  total_purchase_amt  \
# 2835621    20060            0     10011     10010                   1
# 2835322    24564            0    200131    200100                  31
# 2835323    24883            0     42249     42243                   6
# 2835324    24893            0     50007     50000                   7
# 2835325    24900            0         0         0                   0
#
#          direct_purchase_amt  purchase_bal_amt  purchase_bank_amt  \
# 2835621                    0                 0                  0
# 2835322                    0                 0                  0
# 2835323                    0                 0                  0
# 2835324                    0                 0                  0
# 2835325                    0                 0                  0
#
#          total_redeem_amt  consume_amt  transfer_amt  tftobal_amt  \
# 2835621                 0            0             0            0
# 2835322                 0            0             0            0
# 2835323                 0            0             0            0
# 2835324                 0            0             0            0
# 2835325                 0            0             0            0
#
#          tftocard_amt  share_amt  category1  category2  category3  category4  \
# 2835621             0          1          0          0          0          0
# 2835322             0         31          0          0          0          0
# 2835323             0          6          0          0          0          0
# 2835324             0          7          0          0          0          0
# 2835325             0          0          0          0          0          0
#
#          mfd_date  mfd_daily_yield
# 2835621  20130701           1.5787 ...
# 2835322  20130701           1.5787 ...
# 2835323  20130701           1.5787 ...
# 2835324  20130701           1.5787 ...
# 2835325  20130701           1.5787 ...
# proccess data
print (pd.merge(df_user_profile_table, df_user_balance_zhifubao_bank, on='user_id').head())
df = pd.merge(df_user_profile_table, df_user_balance_zhifubao_bank, on='user_id').loc[:
, ['user_id', 'sex', 'city', 'constellation', 'report_date', 'mfd_date', 'mfd_daily_yield', 'mfd_7daily_yield'
         , 'Interest_O_N', 'Interest_1_W', 'Interest_2_W', 'Interest_1_M'
         , 'Interest_3_M', 'Interest_6_M', 'Interest_9_M', 'Interest_1_Y', 'total_purchase_amt', 'total_redeem_amt']]
# 	user_id	report_date	mfd_date	mfd_daily_yield	mfd_7daily_yield	Interest_O_N	Interest_1_W	Interest_2_W	Interest_1_M	Interest_3_M	Interest_6_M	Interest_9_M	Interest_1_Y
# 2835211	332	2013-07-01 00:00:00	20130701	1.5787	6.307	4.456	5.423	6.04	6.88	5.295	4.239	4.282	4.4125

df.to_csv('data.csv')
# print (df)
