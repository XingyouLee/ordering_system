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
item_data = pd.read_csv('items_category.csv')
print(item_data[0]["name"])