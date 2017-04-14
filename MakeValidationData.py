# coding=utf-8
import pandas as pd
from pandas.tseries.offsets import CustomBusinessDay

df_user_profile_table = pd.read_csv('user_profile_table.csv')
df_mfd_bank_shibor_sep = pd.read_excel('mfd_bank_shibor_sep.xls', 'Sheet')

df_mfd_bank_shibor_sep = df_mfd_bank_shibor_sep.fillna(0)
print (df_mfd_bank_shibor_sep.head(20))
# 转换成星期 TODO 考虑休假
df_mfd_bank_shibor_sep['diff'] = df_mfd_bank_shibor_sep['mfd_date'].apply(
    lambda x: (pd.to_datetime(x) - pd.to_datetime('2013-07-01')).days)
df_mfd_bank_shibor_sep['mfd_date'] = df_mfd_bank_shibor_sep['mfd_date'].apply(
    lambda x: pd.Timestamp(pd.to_datetime(x)).weekday())
df_mfd_bank_shibor_sep.to_csv('mfd_bank_shibor_sep.csv')

df_user_profile_table['x'] = '1'
df_mfd_bank_shibor_sep['y'] = '1'
# print (df_user_profile_table.head())
#    user_id  sex     city constellation  x
# 0        2    1  6411949           shizizuo  1
# 1       12    1  6412149           moxiezuo  1
# 2       22    1  6411949           shuangzizuo  1
# 3       23    1  6411949           shuangyu  1
# 4       25    1  6481949           shuangyu  1

# print (df_mfd_bank_shibor_sep.head())
#    mfd_date    O/N     1W     2W     1M      3M      6M      9M  1Y  y
# 0       427  2.906  3.584  4.117  4.057  4.6665  4.8716  4.9373   5  1
# 1       428  2.847  3.510  3.981  4.096  4.6654  4.8714  4.9364   5  1
# 2       429  2.824  3.391  3.765  4.033  4.6652  4.8608  4.9323   5  1
# 3       430  2.815  3.275  3.615  3.970  4.6632  4.8640  4.9339   5  1
# 4       431  2.807  3.188  3.497  3.965  4.6539  4.8631  4.9328   5  1
# print (df_user_profile_table.groupby('city').sum())
# sex 0,1
# city
# 6081949
# 6281949
# 6301949
# 6411949
# 6412149
# 6481949
# 6581949
# 双子座
# 双鱼座
# 处女座
# 天秤座
# 天蝎座
# 射手座
# 巨蟹座
# 摩羯座
# 水瓶座
# 狮子座
# 白羊座
# 金牛座
# print (df_user_profile_table.merge(df_mfd_bank_shibor_sep, left_on='x', right_on='y').head())
#    user_id  sex     city constellation  x  mfd_date    O/N     1W     2W  \
# 0        2    1  6411949           shizizuo  1       427  2.906  3.584  4.117
# 1        2    1  6411949           shizizuo  1       428  2.847  3.510  3.981
# 2        2    1  6411949           shizizuo  1       429  2.824  3.391  3.765
# 3        2    1  6411949           shizizuo  1       430  2.815  3.275  3.615
# 4        2    1  6411949           shizizuo  1       431  2.807  3.188  3.497
#
#       1M      3M      6M      9M  1Y  y
# 0  4.057  4.6665  4.8716  4.9373   5  1
# 1  4.096  4.6654  4.8714  4.9364   5  1
# 2  4.033  4.6652  4.8608  4.9323   5  1
# 3  3.970  4.6632  4.8640  4.9339   5  1
# 4  3.965  4.6539  4.8631  4.9328   5  1
df_val = df_user_profile_table.merge(df_mfd_bank_shibor_sep, left_on='x', right_on='y').loc[:,
         ['user_id', 'sex', 'city', 'constellation', 'mfd_date', 'diff', 'O/N', '1W', '2W', '1M', '3M', '6M', '9M',
          '1Y']]
print (df_val.head(10))
df_val.to_csv('data_val.csv')
#    user_id  mfd_date    O/N     1W     2W     1M      3M      6M      9M  1Y
# 0        2       427  2.906  3.584  4.117  4.057  4.6665  4.8716  4.9373   5
# 1        2       428  2.847  3.510  3.981  4.096  4.6654  4.8714  4.9364   5
# 2        2       429  2.824  3.391  3.765  4.033  4.6652  4.8608  4.9323   5
# 3        2       430  2.815  3.275  3.615  3.970  4.6632  4.8640  4.9339   5
# 4        2       431  2.807  3.188  3.497  3.965  4.6539  4.8631  4.9328   5
# 5        2       432  0.000  0.000  0.000  0.000  0.0000  0.0000  0.0000   0
# 6        2       433  0.000  0.000  0.000  0.000  0.0000  0.0000  0.0000   0
# 7        2       434  0.000  0.000  0.000  0.000  0.0000  0.0000  0.0000   0
# 8        2       435  2.816  3.152  3.407  3.930  4.6522  4.8638  4.9326   5
# 9        2       436  2.839  3.161  3.414  3.892  4.6495  4.8564  4.9305   5
print (df_val.count)
