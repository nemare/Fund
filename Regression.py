# coding=utf-8
import pandas as pd
from sklearn import cross_validation
from sklearn.tree import DecisionTreeRegressor


def getResult(q, y_purchase_predict, y_redeem_predict):
    df_result = pd.read_csv('tc_comp_predict_table_date.csv')
    q['purchase'] = y_purchase_predict
    q['redeem'] = y_redeem_predict
    q = q.loc[:, ['mfd_date', 'purchase', 'redeem']].groupby('mfd_date', as_index=False).sum()
    df_result['purchase'] = q['purchase'].round(2)
    df_result['redeem'] = q['redeem'].round(2)
    print (df_result.head())
    df_result.to_csv('tc_comp_predict_table.csv', index=False, header=False)


# read data
df = pd.read_csv('data.csv')
# print (df.head())
# print (df.count())
df_val = pd.read_csv('data_val.csv')
# print(df_val.head())
# retrive x and y
x = df.loc[:, ['sex', 'city', 'constellation', 'report_date',
               'Interest_O_N', 'Interest_1_W', 'Interest_2_W', 'Interest_1_M',
               'Interest_3_M', 'Interest_6_M', 'Interest_9_M', 'Interest_1_Y']]
# print (x.head())
#    sex     city constellation  report_date  Interest_O_N  Interest_1_W  \
# 0    1  6411949           shizizuo          231         2.951        3.8790
# 1    1  6412149           moxiezuo          367         2.960        3.3930
# 2    1  6411949           shuangzizuo          318         2.350        3.1355
# 3    1  6411949           shuangyuzuo          218         0.000        0.0000
# 4    1  6411949           shuangyuzuo          236         0.000        0.0000
#
#    Interest_2_W  Interest_1_M  Interest_3_M  Interest_6_M  Interest_9_M  \
# 0         4.483         5.365        5.6000        4.9984        5.0000
# 1         3.500         4.132        4.7500        4.9001        4.9654
# 2         3.202         3.651        5.2665        5.0000        5.0000
# 3         0.000         0.000        0.0000        0.0000        0.0000
# 4         0.000         0.000        0.0000        0.0000        0.0000
#
#    Interest_1_Y
# 0        5.0001
# 1        5.0000
# 2        5.0000
# 3        0.0000
# 4        0.0000

# retrieve character
# 21列
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
dummies_city = pd.get_dummies(x['city'])
dummies_constellation = pd.get_dummies(x['constellation'])
dummies_sex = pd.get_dummies(x['sex'])
# print (pd.get_dummies(x['city']).head())
# print (pd.get_dummies(x['constellation']).head())
# print (pd.get_dummies(x['sex']).head())
#    6081949  6281949  6301949  6411949  6412149  6481949  6581949
# 0        0        0        0        1        0        0        0
# 1        0        0        0        0        1        0        0
# 2        0        0        0        1        0        0        0
# 3        0        0        0        1        0        0        0
# 4        0        0        0        1        0        0        0
#
# [5 rows x 7 columns]
#    双子座  双鱼座  处女座  天秤座  天蝎座  射手座  巨蟹座  摩羯座  水瓶座  狮子座  白羊座  金牛座
# 0    0    0    0    0    0    0    0    0    0    1    0    0
# 1    0    0    0    0    0    0    0    1    0    0    0    0
# 2    1    0    0    0    0    0    0    0    0    0    0    0
# 3    0    1    0    0    0    0    0    0    0    0    0    0
# 4    0    1    0    0    0    0    0    0    0    0    0    0
#
# [5 rows x 12 columns]
#    0  1
# 0  0  1
# 1  0  1
# 2  0  1
# 3  0  1
# 4  0  1
#
# [5 rows x 2 columns]
# print (pd.concat([x, dummies_sex, dummies_city, dummies_constellation], axis=1).dtypes)
# sex                int64
# city               int64
# constellation     object
# report_date        int64
# Interest_O_N     float64
# Interest_1_W     float64
# Interest_2_W     float64
# Interest_1_M     float64
# Interest_3_M     float64
# Interest_6_M     float64
# Interest_9_M     float64
# Interest_1_Y     float64
# 0                float64
# 1                float64
# 6081949          float64
# 6281949          float64
# 6301949          float64
# 6411949          float64
# 6412149          float64
# 6481949          float64
# 6581949          float64
# 双子座              float64
# 双鱼座              float64
# 处女座              float64
# 天秤座              float64
# 天蝎座              float64
# 射手座              float64
# 巨蟹座              float64
# 摩羯座              float64
# 水瓶座              float64
# 狮子座              float64
# 白羊座              float64
# 金牛座              float64
X = pd.concat([x, dummies_sex, dummies_city, dummies_constellation], axis=1)
X = X.loc[:,
    ['report_date', 'Interest_O_N', 'Interest_1_W', 'Interest_2_W', 'Interest_1_M', 'Interest_3_M', 'Interest_6_M',
     'Interest_9_M', 'Interest_1_Y',
     0, 1,
     6081949, 6281949, 6301949, 6411949, 6412149, 6481949, 6581949,
     '双子座', '双鱼座', '处女座', '天秤座', '天蝎座', '射手座', '巨蟹座', '摩羯座', '水瓶座', '狮子座', '白羊座', '金牛座'
     ]]  # 30列
# print (X.head())
#    report_date  Interest_O_N  Interest_1_W  Interest_2_W  Interest_1_M  \
# 0          231         2.951        3.8790         4.483         5.365
# 1          367         2.960        3.3930         3.500         4.132
# 2          318         2.350        3.1355         3.202         3.651
# 3          218         0.000        0.0000         0.000         0.000
# 4          236         0.000        0.0000         0.000         0.000
#
#    Interest_3_M  Interest_6_M  Interest_9_M  Interest_1_Y  0  1  6081949  \
# 0        5.6000        4.9984        5.0000        5.0001  0  1        0
# 1        4.7500        4.9001        4.9654        5.0000  0  1        0
# 2        5.2665        5.0000        5.0000        5.0000  0  1        0
# 3        0.0000        0.0000        0.0000        0.0000  0  1        0
# 4        0.0000        0.0000        0.0000        0.0000  0  1        0
#
#    6281949  6301949  6411949  6412149  6481949  6581949  双子座  双鱼座
# 0        0        0        1        0        0        0    0    0 ...
# 1        0        0        0        1        0        0    0    0 ...
# 2        0        0        1        0        0        0    1    0 ...
# 3        0        0        1        0        0        0    0    1 ...
# 4        0        0        1        0        0        0    0    1 ...
#
# [5 rows x 30 columns]


y = df.loc[:, ['total_purchase_amt', 'total_redeem_amt']]
# print (y.head())
#    total_purchase_amt  total_redeem_amt
# 0                   1                 0
# 1                  31                 0
# 2                   6                 0
# 3                   7                 0
# 4                   0                 0
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.8, random_state=5)
# train target data
y_purchase_train = y_train['total_purchase_amt']
y_redeem_train = y_train['total_redeem_amt']
# test target data
y_purchase_test = y_test['total_purchase_amt']
y_redeem_test = y_test['total_redeem_amt']

# DecisionTree
regr_1 = DecisionTreeRegressor(max_depth=20)
regr_2 = DecisionTreeRegressor(max_depth=15)
regr_1.fit(X_train, y_purchase_train)
regr_2.fit(X_train, y_purchase_train)

print ('DecisionTree score')
print(regr_1.score(X_test, y_purchase_test))
print(regr_2.score(X_test, y_purchase_test))

regr_3 = DecisionTreeRegressor(max_depth=20)
regr_4 = DecisionTreeRegressor(max_depth=15)
regr_3.fit(X_train, y_redeem_train)
regr_4.fit(X_train, y_redeem_train)

print (regr_3.score(X_test, y_redeem_test))
print (regr_4.score(X_test, y_redeem_test))

# LinearRegression
from sklearn import linear_model

regr_5 = linear_model.LinearRegression()
regr_5.fit(X_train, y_purchase_train)
regr_6 = linear_model.LinearRegression()
regr_6.fit(X_train, y_redeem_train)

print ('LinearRegression score')
print (regr_5.score(X_test, y_purchase_test))
print (regr_6.score(X_test, y_redeem_test))

# predict
dummies_city = pd.get_dummies(df_val['city'])
dummies_constellation = pd.get_dummies(df_val['constellation'])
dummies_sex = pd.get_dummies(df_val['sex'])

X_val = pd.concat([df_val, dummies_sex, dummies_city, dummies_constellation], axis=1)
X_val = X_val.loc[:,
        ['mfd_date', 'O/N', '1W', '2W', '1M', '3M', '6M',
         '9M', '1Y',
         0, 1,
         6081949, 6281949, 6301949, 6411949, 6412149, 6481949, 6581949,
         '双子座', '双鱼座', '处女座', '天秤座', '天蝎座', '射手座', '巨蟹座', '摩羯座', '水瓶座', '狮子座', '白羊座', '金牛座'
         ]]

# max_depth 20
y_purchase_predict20 = regr_1.predict(X_val)
y_redeem_predict20 = regr_3.predict(X_val)
getResult(X_val, y_purchase_predict20, y_redeem_predict20)
# # max_depth 15
# y_purchase_predict15 = regr_2.predict(X_val)
# y_redeem_predict15 = regr_4.predict(X_val)
#
# # linear
# y_purchase_predict = regr_5.predict(X_val)
# y_redeem_predict = regr_6.predict(X_val)
