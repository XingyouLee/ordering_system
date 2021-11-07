import csv
import pandas as pd
import numpy as np
# #
# # headers = ["id", "time", "items", "total_price"]
# #
# # rows = [[100,100,100,100,110]]
# #
# # with open('order_record.csv', 'w') as f:
# #     f_csv = csv.writer(f)
# #     f_csv.writerow(headers)
# #     f_csv.writerows(rows)
# #
# import time
# payment_id = round(time.time())
# date = time.strftime("%Y-%m-%d %H:%M:%S")
#
#
# storage_data = pd.read_csv('order_record.csv')
#
# df4 = pd.DataFrame([payment_id,date,["aa","b","vv"],6]).T
# # 修改df4的column和df3的一致
# df4.columns = storage_data.columns
# # 把两个dataframe合并，需要设置 ignore_index=True
# df_new = pd.concat([storage_data,df4],ignore_index=True)
#
#
# df_new.to_csv("order_record.csv", index=0)
#
# print(df_new)
# item_data = pd.read_csv('material_storage.csv')
# item_data = np.array(item_data)
# # for i in item_data:
# #     if i[0] == "Americano":
# #         i[1] = 100
# # item_data = pd.DataFrame(item_data)
# # item_data.columns = ["name","price","water","coco","milk","sugar","cheese"]
# print(item_data)
# a = np.array([[1,1,1,1]])
# print(a)

#  record = pd.read_csv('order_record.csv')
# record = np.array(record)

from Crypto.Cipher import AES
obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
message = "The answer is no"
ciphertext = obj.encrypt(message)


id,username,password,level
148_,208_207_231_142_,208_207_231_142_101_,148_
1,tkx,0,1
2,ppy,0,1
3,pzy,0,1

