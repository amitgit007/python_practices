import pandas as pd
import matplotlib.pyplot as plt

#store the excels in variables

excel_file_1='shift-data.xlsx'
excel_file_2='third-shift-data.xlsx'

#read excel in pandas

df_first_shift= pd.read_excel(excel_file_1,sheet_name='first')
df_second_shift=pd.read_excel(excel_file_1,sheet_name='second')
df_third_shift=pd.read_excel(excel_file_2)

#print(df_first_shift)
#print(df_first_shift['Product'])
#print(df_first_shift['Name'])
# combine the data frames
df_all=pd.concat([df_first_shift,df_second_shift,df_third_shift])
#print(df_all)
#do calculations
pivot=df_all.groupby(['Shift']).mean()
shift_productivity=pivot.loc[:,"Production Run Time (Min)":"Products Produced (Units)"]
print(shift_productivity)
#plot graph
#shift_productivity.plot(kind='bar')
#plt.show()
df_all.to_excel("output.xlsx")
