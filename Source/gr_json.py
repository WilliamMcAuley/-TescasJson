import json
import pandas as pd
#
# filename = "C:/Users/William/TescasJson/Data/goodreads_reviews_history_biography.json"
# path = filename
# # data = path.read()
# # data_output = (path.decode("utf-8"))
# # print(data_output)
"""Turning json output into python dictionary"""
# pythonObj = json.loads(data_output)
# json.loads(data.read(data_output))
# print(pythonObj)
# for path as f:

# with open('C:/Users/William/TescasJson/Data/goodreads_reviews_history_biography.json') as json_file:
#     json_data = json.load(json_file)
#     print(json_data)
# dict1 = {}
# dict2 = {}
# json.dumps([dict1, dict2])
# '[{}, {}]'
# json.loads(json.dumps([dict1, dict2]))
# '[{}, {}]'
"""Pandas DF"""
file_handle = open('C:/Users/William/TescasJson/Data/newtest.json', encoding='utf-16', errors='ignore')
df = pd.read_json(file_handle, lines=True)
#df1 = df[df['user_id'].duplicated()]
# df_dup = df.duplicated(subset=['user_id'])
df_dup = df.groupby(['user_id'])
#now do on full dateset and create new dataframe
print(df_dup.size(),'user_id',)
df1 = df_dup.size()
print(df1)
# list_dict = dict()
# df12 = list_dict[df1]
# print(df12)
# df_dup_size = df_dup.size()
#
# df1 = df_dup_size.df(['user_id'])
df1.to_csv('C:/Users/William/TescasJson/Data/New_File_Name.csv', index=None)

# with open('New_File_Name.csv', 'w', newline='') as f:
#     for line in f:
#         f.write(line)
#         f.write('\n')
"""Print data"""

# with open('C:/Users/William/TescasJson/Data/goodreads_reviews_history_biography.json') as f:
#     for line in f:
#         data = json.loads(line)
#         print(data)
#         dict1 = {}
#         dict2 = {}
#         # print(dict1.dat)
#         # print(json.dumps([dict1['review_text']]))
#         dump = json.dumps([dict1['review_text'], dict2])
#         print(dump)
#         pd_data = pd.read_json.data['review_text']
#         #rint(dump)

# review_data = data['review_text']
# print(review_data)
# #jsondata = data.append(json.load(f))
# print(data['review_text'])
# json_file_list = [filename]
# for file in json_file_list:
#     with open(file) as json_file:
#         json_data = json.load(json_file)
#         encode_j = (json_data.decode("utf-8"))
#         write = encode_j.write('\n')
#         print(write)
