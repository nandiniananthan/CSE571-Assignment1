# CSE571-Assignment1

The datasets
a) from the Continuous Glucose Sensor (CGMData.csv) 
              b) from the insulin pump (InfusionData.csv)

The output of the CGM sensor consists of three columns: a) data time stamp, 
							b) the 5 minute filtered CGM reading in mg/dL, 
							c) the Sensor Glucose (SG) value which is the raw sensor output every 5 mins. 

The output of the pump has the following information: a) data time stamp, 
						      b) Basal setting, 
						      c) Micro bolus every 5 mins, 
						      d) Meal intake amount in terms of grams of carbohydrate, 
						      e) Meal bolus, 
						      f) correction bolus, 
						      g) correction factor, 
						      h) CGM calibration or insulin reservoir related alarms,
						      i) auto mode exit events and unique codes representing reasons.


Metrics that were extracted:
a) Percentage time in hyperglycemia (CGM > 180 mg/dL), 
b) percentage of time in hyperglycemia critical (CGM > 250 mg/dL), 
c) percentage time in range (CGM >= 70 mg/dL and CGM <= 180 mg/dL), 
d) percentage time in range secondary (CGM >= 70 mg/dL and CGM <= 150 mg/dL), 
e) percentage time in hypoglycemia level 1 (CGM < 70 mg/dL),
f) percentage time in hypoglycemia level 2 (CGM < 54 mg/dL).

Each of the above mentioned metrics were extracted in three different time intervals: 
a) daytime (6 am to midnight), 
b) overnight (midnight to 6 am),
c) whole day (12 am to 12 am).

Hence there were 18 metrics to be extracted. The metrics were computed for two cases: 
Case A: Manual mode
Case B: Auto mode


Expected Outcome of the Assignment:
A python or matlab script that accepts two csv files: CGMData.csv and InsulinData.csv and runs the analysis procedure and outputs the metrics discussed in the metrics section in another csv file using the format described in Results.csv.
