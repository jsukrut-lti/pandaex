import pandas as pd
import pandas_read_xml as pdx

# missing_column_str ="cl"
# missing_column_no = 1
# df = pd.read_csv('book1.CSV')
# df1 = pd.read_csv('book2.CSV')
# print(df)
# print(df1)
# file1_columns = list(df.columns)
# file2_columns = list(df1.columns)

# def get_missing_columns(file_columns,missing_column_str,missing_column_no):
# 	missing_columns = {}
# 	for index,column in enumerate(file_columns):
# 		try:
# 			if "Unnamed" in column.split(':'):
# 				missing_columns.update({ index:str(missing_column_str + str(missing_column_no))})
# 				missing_column_no += 1
# 		except Exception as e:
# 			raise
# 	return missing_columns
#
# def update_columns(missing_columns,actual_columns,dataframe1,dataframe2):
# 	if missing_columns and actual_columns:
# 		missing_index = list(missing_columns.keys())
# 		for idx in missing_index:
# 			actual_columns[idx] = missing_columns[idx]
# 		dataframe1.columns = actual_columns
# 		dataframe2.columns = actual_columns
# 		return [dataframe1,dataframe2]


#
# missing_columns = get_missing_columns(file1_columns,missing_column_str,missing_column_no)
# if missing_columns:
# 	dataframes = update_columns(missing_columns,file1_columns,df, df1)
# else:
# 	missing_columns = get_missing_columns(file2_columns, missing_column_str, missing_column_no)
# 	dataframes = update_columns(missing_columns,file2_columns,df, df1)
# print(dataframes)


# using pandas read_xml
def read_xmls(path_or_file):
    df = pd.read_xml(path_or_file)
    print("Columns",df.columns)
    print("DataFrame",df)
    print("-------------")
    print("Accessing Column Data",df['name'])

path_or_file = 'INPUT.XML'
read_xmls(path_or_file)





