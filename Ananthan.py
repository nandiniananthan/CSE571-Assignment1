# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 18:57:32 2020

@author: nandini.ananthan
"""

import pandas as pd

# Importing the Insulin csv file #
insulin_df = pd.read_csv('InsulinData.csv')
rows_insulin_df = len(insulin_df)

insulin_df['Alarm'] = insulin_df['Alarm'].astype('string')
insulin_df['Time'] = insulin_df['Time'].astype('string')
insulin_df['Date'] = insulin_df['Date'].astype('string')

i = rows_insulin_df-1
while i > 0:
    a = insulin_df.at[i, 'Alarm']
    if str(a) == "AUTO MODE ACTIVE PLGM OFF":
        date_stamp = insulin_df.at[i, 'Date']
        time_stamp = insulin_df.at[i, 'Time']
        break_row_value = i
        break
    i-=1

time_stamp = time_stamp.replace(':','')

# Importing the CGM csv file #
cgm_df = pd.read_csv('CGMData.csv')
rows_cgm_df = len(cgm_df)

#######3          Executing the Manual mode           #########

v1= v2= v3= v4= v5= v6 =v7= v8= v9= v10= v11= v12 =v13= v14= v15= v16= v17= v18 =0
count = 0
no_of_days_manual= 1

cgm_df['Time'] = cgm_df['Time'].astype('string')
cgm_df['Date'] = cgm_df['Date'].astype('string')

i = rows_cgm_df-1
while i > 0:
    a = cgm_df.at[i, 'Date']
    d = cgm_df.at[i-1, 'Date']
    if a != d:
        no_of_days_manual += 1
    b = cgm_df.at[i, 'Time']
    c = cgm_df.at[i-1, 'Time']
    b = b.replace(':','')
    if date_stamp == str(a) and str(c) >= time_stamp >= str(b):
        transfer_index = i
        break
    i-=1
    b = cgm_df.at[i, 'Time']


    #####        Day time           #####
    count += 1
    if '06:00:00' <= str(b) <= '23:59:59':
        d = cgm_df.at[i, 'Sensor Glucose (mg/dL)']
        if d > 180:
            v7 += 1
            v13 += 1
        if d > 250:
            v8 += 1
            v14 += 1
        if d >=70 and d <=180:
            v9 += 1
            v15 += 1
        if d >=70 and d <=150:
            v10 += 1
            v16 += 1
        if d < 70:
            v11 += 1
            v17 += 1
        if d < 54:
            v12 += 1
            v18 += 1
            
    #####        Night time           #####
    else:
        c = cgm_df.at[i, 'Sensor Glucose (mg/dL)']
        if c > 180:
            v1 += 1
            v13 += 1
        if c > 250:
            v2 += 1
            v14 += 1
        if c >=70 and c <=180:
            v3 += 1
            v15 += 1
        if c >=70 and c <=150:
            v4 += 1
            v16 += 1
        if c < 70:
            v5 += 1
            v17 += 1
        if c < 54:
            v6 += 1
            v18 += 1
          
    #####        finding the percentage values for manual mode          #####
            
                    # whole day time #
whole_day_total = no_of_days_manual * 288

v13_percent= v14_percent= v15_percent= v16_percent= v17_percent= v18_percent = 0

v13_percent = (v13 / whole_day_total)*100
v14_percent = (v14 / whole_day_total)*100
v15_percent = (v15 / whole_day_total)*100
v16_percent = (v16 / whole_day_total)*100
v17_percent = (v17 / whole_day_total)*100
v18_percent = (v18 / whole_day_total)*100

                  # day time alone#
day_time_total = no_of_days_manual * 288

v7_percent= v8_percent= v9_percent= v10_percent= v11_percent= v12_percent =0
v7_percent = (v7 / day_time_total)*100
v8_percent = (v8 / day_time_total)*100
v9_percent = (v9 / day_time_total)*100
v10_percent = (v10 / day_time_total)*100
v11_percent = (v11 / day_time_total)*100
v12_percent = (v12 / day_time_total)*100

                # night time alone#
night_time_total = no_of_days_manual * 288

v1_percent= v2_percent= v3_percent= v4_percent= v5_percent= v6_percent =0
v1_percent = (v1 / night_time_total)*100
v2_percent = (v2 / night_time_total)*100
v3_percent = (v3 / night_time_total)*100
v4_percent = (v4 / night_time_total)*100
v5_percent = (v5 / night_time_total)*100
v6_percent = (v6 / night_time_total)*100

#######3          Executing the auto mode          #########

v19= v20= v21= v22= v23= v24 =v25= v26= v27= v28= v29= v30 =v31= v32= v33= v34= v35= v36 =0
count = 0
no_of_days_auto=1

for i in range(transfer_index,0,-1):
    a = cgm_df.at[i, 'Date']
    c = cgm_df.at[i-1, 'Date']
    b = cgm_df.at[i, 'Time']
    count += 1
    if a!=c:
        no_of_days_auto += 1
        
    #####        Day time           #####
    if '06:00:00' <= str(b) <= '23:59:59':
        d = cgm_df.at[i, 'Sensor Glucose (mg/dL)']
        if d > 180:
            v25 += 1
            v31 += 1
        if d > 250:
            v26 += 1
            v32 += 1
        if d >=70 and d <=180:
            v27 += 1
            v33 += 1
        if d >=70 and d <=150:
            v28 += 1
            v34 += 1
        if d < 70:
            v29 += 1
            v35 += 1
        if d < 54:
            v30 += 1
            v36 += 1

    #####        Night time           #####
    else:
        c = cgm_df.at[i, 'Sensor Glucose (mg/dL)']
        if c > 180:
            v19 += 1
            v31 += 1
        if c > 250:
            v20 += 1
            v32 += 1
        if c >=70 and c <=180:
            v21 += 1
            v33 += 1
        if c >=70 and c <=150:
            v22 += 1
            v34 += 1
        if c < 70:
            v23 += 1
            v35 += 1
        if c < 54:
            v36 += 1
            v24 += 1

                # whole time alone#
whole_day_total = no_of_days_auto * 288

v31_percent= v32_percent= v33_percent= v34_percent= v35_percent= v36_percent =0

v31_percent = (v31 / whole_day_total)*100
v32_percent = (v32 / whole_day_total)*100
v33_percent = (v33 / whole_day_total)*100
v34_percent = (v34 / whole_day_total)*100
v35_percent = (v35 / whole_day_total)*100
v36_percent = (v36 / whole_day_total)*100

                # day time alone#
day_time_total = no_of_days_auto * 288

v25_percent= v26_percent= v27_percent= v28_percent= v29_percent= v30_percent =0

v25_percent = (v25 / day_time_total)*100
v26_percent = (v26 / day_time_total)*100
v27_percent = (v27 / day_time_total)*100
v28_percent = (v28 / day_time_total)*100
v29_percent = (v29 / day_time_total)*100
v30_percent = (v30 / day_time_total)*100

                # night time alone#
night_time_total = no_of_days_auto * 288

v19_percent= v20_percent= v21_percent= v22_percent= v23_percent= v24_percent =0
v19_percent = (v19 / night_time_total)*100
v20_percent = (v20 / night_time_total)*100
v21_percent = (v21 / night_time_total)*100
v22_percent = (v22 / night_time_total)*100
v23_percent = (v23 / night_time_total)*100
v24_percent = (v24 / night_time_total)*100


# initialize list of lists 
data = [[v1_percent,v2_percent,v3_percent,v4_percent,v5_percent,v6_percent,v7_percent,v8_percent,v9_percent,v10_percent,v11_percent,v12_percent,v13_percent,v14_percent,v15_percent,v16_percent,v17_percent,v18_percent], [v19_percent,v20_percent,v21_percent,v22_percent,v23_percent,v24_percent,v25_percent,v26_percent,v27_percent,v28_percent,v29_percent,v30_percent,v31_percent,v32_percent,v33_percent,v34_percent,v35_percent,v36_percent]] 
  
# Create the pandas DataFrame 
result_df = pd.DataFrame(data, columns = ['Percentage time in hyperglycemia (CGM > 180 mg/dL)(over night)', 'percentage of time in hyperglycemia critical (CGM > 250 mg/dL)(over night)', 'percentage time in range (CGM >= 70 mg/dL and CGM <= 180 mg/dL)(over night)', 'percentage time in range secondary (CGM >= 70 mg/dL and CGM <= 150 mg/dL)(over night)','percentage time in hypoglycemia level 1 (CGM < 70 mg/dL)(over night)', 'percentage time in hypoglycemia level 2 (CGM < 54 mg/dL)(over night)', 'Percentage time in hyperglycemia (CGM > 180 mg/dL)(day_time)', 'percentage of time in hyperglycemia critical (CGM > 250 mg/dL)(day_time)', 'percentage time in range (CGM >= 70 mg/dL and CGM <= 180 mg/dL)(day_time)', 'percentage time in range secondary (CGM >= 70 mg/dL and CGM <= 150 mg/dL)(day_time)','percentage time in hypoglycemia level 1 (CGM < 70 mg/dL)(day_time)', 'percentage time in hypoglycemia level 2 (CGM < 54 mg/dL)(day_time)',  'Percentage time in hyperglycemia (CGM > 180 mg/dL)(whole_day)', 'percentage of time in hyperglycemia critical (CGM > 250 mg/dL)(whole_day)', 'percentage time in range (CGM >= 70 mg/dL and CGM <= 180 mg/dL)(whole_day)', 'percentage time in range secondary (CGM >= 70 mg/dL and CGM <= 150 mg/dL)(whole_day)','percentage time in hypoglycemia level 1 (CGM < 70 mg/dL)(whole_day)', 'percentage time in hypoglycemia level 2 (CGM < 54 mg/dL)(whole_day)'], index =['Manual Mode', 'Auto Mode']) 

  
# print dataframe. 
result_df.to_csv('D:/desktop_sep_13/Data_Mining/Assignment_1/Ananthan_Results.csv')