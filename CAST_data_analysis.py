#!/usr/bin/env python
# coding: utf-8

# In[28]:


###############################################################################
###############################################################################

## MN50759 - Dissertation in Business Analytics

#------------------------------------------------------------------------------------------------------
########################################## Installing Packages #######################################
#------------------------------------------------------------------------------------------------------

import pandas as pd
import numpy as np
import pyreadstat

#------------------------------------------------------------------------------------------------------
########################################## Loading Data ##############################################
#------------------------------------------------------------------------------------------------------

# Read the .sav file
Data_Wave1, metadata = pyreadstat.read_sav('./CAST wave 1 2020_o.sav')
Data_Wave2, metadata = pyreadstat.read_sav('./CAST wave 2 2021_o.sav')
Data_Wave3, metadata = pyreadstat.read_sav('./CAST wave 3 2022_o.sav')

# Convert the data to a pandas DataFrame
DataWave1 = pd.DataFrame(Data_Wave1)
DataWave2 = pd.DataFrame(Data_Wave2)
DataWave3 = pd.DataFrame(Data_Wave3)

print(DataWave1.info())
print(DataWave2.info())
print(DataWave3.info())

# Append the 3 data frames
DataWave = pd.concat([DataWave1, DataWave2, DataWave3], ignore_index=True)


# In[29]:


#------------------------------------------------------------------------------------------------------
########################################## Installing Packages #######################################
#------------------------------------------------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#------------------------------------------------------------------------------------------------------
########################################## Data Manipulation ##############################################
#------------------------------------------------------------------------------------------------------

# Check for null values in the 'CODERESP' column
is_null_CODERESP = DataWave['CODERESP'].isnull().sum()
DataWave['CODERESP'] = DataWave['CODERESP'].astype(str)
#--------------------------------------------------------------------------
# Check for null values in the 'DATE' column
is_null_Date = DataWave['DATE'].isnull()
# Extract the year into a new column
DataWave['DATE'] = pd.to_datetime(DataWave['DATE'], format='%Y-%m-%d')
DataWave['Year'] = DataWave['DATE'].dt.year
DataWave['Year'] = DataWave['Year'].astype(int)
#Delete the 'Date' Column
del DataWave['DATE']
#---------------------------------------------------------------------------
# Check for null values in the 'QCOUNTRY' column
is_null_qcountry = DataWave['QCOUNTRY'].isnull()
# print('number of null values in QCOUNTRY')
# print(is_null_qcountry)
#----------------------------------------------------------------------------
# Split the datasets into 4 based on the country
data_1 = DataWave[DataWave['QCOUNTRY'] == 1]
data_2 = DataWave[DataWave['QCOUNTRY'] == 2]
data_3 = DataWave[DataWave['QCOUNTRY'] == 3]
data_4 = DataWave[DataWave['QCOUNTRY'] == 4]
#------------------------------------------------------------------------------
print(data_1.info())
print(data_2.info())
print(data_3.info())
print(data_4.info())


# In[30]:


#------------------------------------------------------------------------------------------------------
########################################## Installing Packages #######################################
#------------------------------------------------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#------------------------------------------------------------------------------------------------------
########################################## Data Cleaning ##############################################
#------------------------------------------------------------------------------------------------------
# Check for number of null values column and row wise
#COUNTRY = 1
null_count_data_1 = data_1.isnull().sum()
null_count_data_1_rec = data_1.isnull().sum(axis=1)
#COUNTRY = 2
null_count_data_2 = data_2.isnull().sum()
null_count_data_2_rec = data_2.isnull().sum(axis=1)
#COUNTRY = 3
null_count_data_3 = data_3.isnull().sum()
null_count_data_3_rec = data_3.isnull().sum(axis=1)
#COUNTRY = 4
null_count_data_4 = data_4.isnull().sum()
null_count_data_4_rec = data_4.isnull().sum(axis=1)
# Replace all invalid and null values with null values
dataset = [data_1, data_2, data_3, data_4]
for data in dataset:
    data['Q018'] = data['Q018'].replace(87.0,6.0)
    data['Q018'] = data['Q018'].replace(7.0,6.0)
    data['Q029'] = data['Q029'].replace(87.0,6.0)
    data['Q031'] = data['Q031'].replace(87.0,6.0)
    data['Q049_1'] = data['Q049_1'].replace(6.0,99.0)
    data['Q049_2'] = data['Q049_2'].replace(6.0,99.0)
    data['Q049_3'] = data['Q049_3'].replace(6.0,99.0)
    for column in data.columns:
        data[column].fillna(99, inplace = True)
        data[column] = data[column].replace(85.0,99.0)
        data[column] = data[column].replace(86.0,99.0)
        data[column] = data[column].replace(87.0,99.0)
        data[column] = data[column].replace(98.0,99.0)
        data[column] = data[column].replace(999.0,99.0)
        data[column] = data[column].replace(997.0,99.0)
        data[column] = data[column].replace(997.0,99.0)
        data[column] = data[column].replace(99.0, np.nan)
# Filter out rows with more than 24 missing values (~ 5% Of rows containing null values)
print(data_1['Year'].value_counts())
print(data_2['Year'].value_counts())
print(data_3['Year'].value_counts())
print(data_4['Year'].value_counts())
# COUNTRY = 1
print('null values')
print((null_count_data_1_rec > 22).sum()) #283
data_1 = data_1[null_count_data_1_rec <23]
# COUNTRY = 2
print((null_count_data_2_rec > 24).sum()) #198
data_2 = data_2[null_count_data_2_rec <25]
# COUNTRY = 3
print((null_count_data_3_rec > 22).sum()) #221
data_3 = data_3[null_count_data_3_rec <23]
# COUNTRY = 4
print((null_count_data_4_rec > 23).sum()) #149
data_4 = data_4[null_count_data_4_rec <24]
print(data_1['Year'].value_counts())
print(data_2['Year'].value_counts())
print(data_3['Year'].value_counts())
print(data_4['Year'].value_counts())
# Copy the data into another one
datimp_1 = data_1.copy()
datimp_2 = data_2.copy()
datimp_3 = data_3.copy()
datimp_4 = data_4.copy()
# Combine the columns Q055_15, Q055_16, Q055_17 and Q055_18 to Q055_peer
data_1.loc[:,'Q055_peer'] = data_1['Q055_15'].copy()
data_2.loc[:,'Q055_peer'] = data_2['Q055_16'].copy()
data_3.loc[:,'Q055_peer'] = data_3['Q055_17'].copy()
data_4.loc[:,'Q055_peer'] = data_4['Q055_18'].copy()
datimp_1.loc[:,'Q055_peer'] = datimp_1['Q055_15'].copy()
datimp_2.loc[:,'Q055_peer'] = datimp_2['Q055_16'].copy()
datimp_3.loc[:,'Q055_peer'] = datimp_3['Q055_17'].copy()
datimp_4.loc[:,'Q055_peer'] = datimp_4['Q055_18'].copy()
# Delete for all the datset
dataset = [data_1, data_2, data_3, data_4]
dataimpSet = [datimp_1, datimp_2, datimp_3, datimp_4]
for data in dataset:
    del data['Q055_15']
    del data['Q055_16']
    del data['Q055_17']
    del data['Q055_18']
#   
for data_Imp in dataimpSet:
    del data_Imp['Q055_15']
    del data_Imp['Q055_16']
    del data_Imp['Q055_17']
    del data_Imp['Q055_18']


# In[31]:


#------------------------------------------------------------------------------------------------------
########################################## Installing Packages #######################################
#------------------------------------------------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#------------------------------------------------------------------------------------------------------
########################################## Data Manipulation ##############################################
#------------------------------------------------------------------------------------------------------

#Check the mean of each data
# QCOUNTRY = 1
Mean_data_1 = data_1['Q02'].mean()
#print(Mean_data_1)
# QCOUNTRY = 2
Mean_data_2 = data_2['Q02'].mean()
#print(Mean_data_2)
# QCOUNTRY = 3
Mean_data_3 = data_3['Q02'].mean()
#print(Mean_data_3)
# QCOUNTRY = 4
Mean_data_4 = data_4['Q02'].mean()
#print(Mean_data_4)

#data_1['Q02'] = data_1['Q02'].astype(int)


#Segregate categories for the 'AgeGroup' Column
# QCOUNTRY = 1
conditions_1 = [
    (data_1['Q02'] > 17) & (data_1['Q02'] < 36),
    (data_1['Q02'] > 35) & (data_1['Q02'] < 46),
    (data_1['Q02'] > 45) & (data_1['Q02'] < 56),
    (data_1['Q02'] > 55) & (data_1['Q02'] < 100)
]
values_1 = ['18-35', '35-45', '45-55', '55+']
# QCOUNTRY = 2
conditions_2 = [
    (data_2['Q02'] > 17) & (data_2['Q02'] < 36),
    (data_2['Q02'] > 35) & (data_2['Q02'] < 46),
    (data_2['Q02'] > 45) & (data_2['Q02'] < 56),
    (data_2['Q02'] > 55) & (data_2['Q02'] < 100)
]
values_2 = ['18-35', '35-45', '45-55', '55+']
# QCOUNTRY = 3
conditions_3 = [
    (data_3['Q02'] > 17) & (data_3['Q02'] < 36),
    (data_3['Q02'] > 35) & (data_3['Q02'] < 46),
    (data_3['Q02'] > 45) & (data_3['Q02'] < 56),
    (data_3['Q02'] > 55) & (data_3['Q02'] < 100)
]
values_3 = ['18-35', '35-45', '45-55', '55+']
# QCOUNTRY = 4
conditions_4 = [
    (data_4['Q02'] > 17) & (data_4['Q02'] < 36),
    (data_4['Q02'] > 35) & (data_4['Q02'] < 46),
    (data_4['Q02'] > 45) & (data_4['Q02'] < 56),
    (data_4['Q02'] > 55) & (data_4['Q02'] < 100)
]
values_4 = ['18-35', '35-45', '45-55', '55+']

# Replace na values with mean in 'Q02'
datimp_1['Q02'] = datimp_1['Q02'].fillna(Mean_data_1)
datimp_2['Q02'] = datimp_2['Q02'].fillna(Mean_data_2)
datimp_3['Q02'] = datimp_3['Q02'].fillna(Mean_data_3)
datimp_4['Q02'] = datimp_4['Q02'].fillna(Mean_data_4)

datimp_1['Q02'] = datimp_1['Q02'].astype(int)

# Create a new column based on the conditions
# QCOUNTRY = 1
data_1['AgeGroup'] = np.select(conditions_1, values_1, default='Unknown')
# QCOUNTRY = 2
data_2['AgeGroup'] = np.select(conditions_2, values_2, default='Unknown')
# QCOUNTRY = 3
data_3['AgeGroup'] = np.select(conditions_3, values_3, default='Unknown')
# QCOUNTRY = 4
data_4['AgeGroup'] = np.select(conditions_4, values_4, default='Unknown')

#Segregate categories for the 'AgeGroup' Column
# QCOUNTRY = 1
conditions_imp_1 = [
    (datimp_1['Q02'] > 17) & (datimp_1['Q02'] < 36),
    (datimp_1['Q02'] > 35) & (datimp_1['Q02'] < 46),
    (datimp_1['Q02'] > 45) & (datimp_1['Q02'] < 56),
    (datimp_1['Q02'] > 55) & (datimp_1['Q02'] < 100)
]
values_imp_1 = ['18-35', '35-45', '45-55', '55+']
# QCOUNTRY = 2
conditions_imp_2 = [
    (datimp_2['Q02'] > 17) & (datimp_2['Q02'] < 36),
    (datimp_2['Q02'] > 35) & (datimp_2['Q02'] < 46),
    (datimp_2['Q02'] > 45) & (datimp_2['Q02'] < 56),
    (datimp_2['Q02'] > 55) & (datimp_2['Q02'] < 100)
]
values_imp_2 = ['18-35', '35-45', '45-55', '55+']
# QCOUNTRY = 3
conditions_imp_3 = [
    (datimp_3['Q02'] > 17) & (datimp_3['Q02'] < 36),
    (datimp_3['Q02'] > 35) & (datimp_3['Q02'] < 46),
    (datimp_3['Q02'] > 45) & (datimp_3['Q02'] < 56),
    (datimp_3['Q02'] > 55) & (datimp_3['Q02'] < 100)
]
values_imp_3 = ['18-35', '35-45', '45-55', '55+']
# QCOUNTRY = 4
conditions_imp_4 = [
    (datimp_4['Q02'] > 17) & (datimp_4['Q02'] < 36),
    (datimp_4['Q02'] > 35) & (datimp_4['Q02'] < 46),
    (datimp_4['Q02'] > 45) & (datimp_4['Q02'] < 56),
    (datimp_4['Q02'] > 55) & (datimp_4['Q02'] < 100)
]
values_imp_4 = ['18-35', '35-45', '45-55', '55+']



# Check for unique values
# QCOUNTRY = 1
print(datimp_1['Q02'].value_counts())
# QCOUNTRY = 2
print(datimp_2['Q02'].value_counts())
# QCOUNTRY = 3
print(datimp_3['Q02'].value_counts())
# QCOUNTRY = 4
print(datimp_4['Q02'].value_counts())

# QCOUNTRY = 1
datimp_1['AgeGroup'] = np.select(conditions_imp_1, values_imp_1, default='Unknown')
# QCOUNTRY = 2
datimp_2['AgeGroup'] = np.select(conditions_imp_2, values_imp_2, default='Unknown')
# QCOUNTRY = 3
datimp_3['AgeGroup'] = np.select(conditions_imp_3, values_imp_3, default='Unknown')
# QCOUNTRY = 4
datimp_4['AgeGroup'] = np.select(conditions_imp_4, values_imp_4, default='Unknown')

# Check for unique values
# QCOUNTRY = 1
print(datimp_1['AgeGroup'].value_counts())
# QCOUNTRY = 2
print(datimp_2['AgeGroup'].value_counts())
# QCOUNTRY = 3
print(datimp_3['AgeGroup'].value_counts())
# QCOUNTRY = 4
print(datimp_4['AgeGroup'].value_counts())



#Check for null Values
# QCOUNTRY = 1
null_count_1 = data_1['AgeGroup'].isnull().sum()
print(null_count_1)
# QCOUNTRY = 2
null_count_2 = data_2['AgeGroup'].isnull().sum()
print(null_count_2)
# QCOUNTRY = 3
null_count_3 = data_3['AgeGroup'].isnull().sum()
print(null_count_3)
# QCOUNTRY = 4
null_count_4 = data_4['AgeGroup'].isnull().sum()
print(null_count_4)

print(datimp_1[datimp_1['AgeGroup'] == 'Unknown'])

#Delete 'Q02' Column
# QCOUNTRY = 1
del data_1['Q02']
del datimp_1['Q02']
# QCOUNTRY = 2
del data_2['Q02']
del datimp_2['Q02']
# QCOUNTRY = 3
del data_3['Q02']
del datimp_3['Q02']
# QCOUNTRY = 4
del data_4['Q02']
del datimp_4['Q02']

# Convert 'Q013_1', 'Q013_2', 'Q013_3', 'Q013_4' into binary values
dataimp = [datimp_1, datimp_2, datimp_3, datimp_4]
Q013_columns = ['Q013_1', 'Q013_2', 'Q013_3', 'Q013_4']
for data in dataimp:
    for column in Q013_columns:
        data[column] = data[column].replace(1.0,0)
        data[column] = data[column].replace(2.0,0)
        data[column] = data[column].replace(3.0,1)
        data[column] = data[column].replace(4.0,1)
#

# Change code to categories in 'Q09'
dataimp = [datimp_1, datimp_2, datimp_3, datimp_4]
for data in dataimp:
    data['Q09'] = data['Q09'].replace(1, 1)
    data['Q09'] = data['Q09'].replace(2, 0)
    data['Q09'] = data['Q09'].replace(3, 0)
    data['Q09'] = data['Q09'].replace(4, 0)
    data['Q09'] = data['Q09'].replace(5, 0)
    data['Q09'] = data['Q09'].replace(6, 0)
    data['Q09'] = data['Q09'].replace(7, 0)
    print(data['Q09'].value_counts())

# Change code to categories in 'Q067_2' - 0-low, 1-high
dataimp = [datimp_1, datimp_2, datimp_3, datimp_4]
for data in dataimp:
    data['Q067_2'] = data['Q067_2'].replace(1, 0)
    data['Q067_2'] = data['Q067_2'].replace(2, 0)
    data['Q067_2'] = data['Q067_2'].replace(3, 0)
    data['Q067_2'] = data['Q067_2'].replace(4, 1)
    data['Q067_2'] = data['Q067_2'].replace(5, 1)
    print(data['Q067_2'].value_counts())

# Change code to categories in 'Q062_1' - 0-low, 1-high
dataimp = [datimp_1, datimp_2, datimp_3, datimp_4]
for data in dataimp:
    data['Q062_1'] = data['Q062_1'].replace(1, 0)
    data['Q062_1'] = data['Q062_1'].replace(2, 0)
    data['Q062_1'] = data['Q062_1'].replace(3, 0)
    data['Q062_1'] = data['Q062_1'].replace(4, 1)
    data['Q062_1'] = data['Q062_1'].replace(5, 1)
    print(data['Q062_1'].value_counts())
    
# Change code to categories in 'Q062_3' - 0-low, 1-high
dataimp = [datimp_1, datimp_2, datimp_3, datimp_4]
for data in dataimp:
    data['Q062_3'] = data['Q062_3'].replace(1, 0)
    data['Q062_3'] = data['Q062_3'].replace(2, 0)
    data['Q062_3'] = data['Q062_3'].replace(3, 0)
    data['Q062_3'] = data['Q062_3'].replace(4, 1)
    data['Q062_3'] = data['Q062_3'].replace(5, 1)
    print(data['Q062_3'].value_counts())


# In[32]:


#------------------------------------------------------------------------------------------------------
########################################## Installing Packages #######################################
#------------------------------------------------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#------------------------------------------------------------------------------------------------------
########################################## Median and mode Imputation #######################################
#------------------------------------------------------------------------------------------------------


exclude_Columns = ['QWAVE2Q4', 'Q02', 'Q041', 'Q043', 'Q053_9', 'Q053_10', 'Q053_11', 'Q053_12', 
                   'Q053_14', 'Q055_1', 'Q055_5', 'Q055_6', 'Q055_11', 'Q055_12', 'Q055_13', 
                   'Q055_15', 'Q055_16', 'Q055_17', 'Q055_18', 'Q055_19', 'Q055_20', 'Q055_22', 'Q060_6', 'Q018', 'Q029', 'Q031', 'Q044', 'Q049_1', 
                  'Q049_2', 'Q049_3', 'Q053_1', 'Q053_2', 'Q053_3', 'Q053_4', 'Q053_5', 'Q053_6', 'Q053_7', 'Q053_8', 
                  'Q053_13', 'Q054', 'Q064', 'Q055_2', 'Q055_3', 'Q055_4', 'Q055_7', 'Q055_8', 'Q055_9', 'Q055_10', 
                  'Q055_14', 'Q055_peer']

default_Columns = ['CODERESP', 'QCOUNTRY', 'Year', 'AgeGroup']

mode_Columns = ['Q01', 'Q09', 'Q013_1', 'Q013_2', 'Q013_3', 'Q013_4',
                'Q014_01', 'Q014_02', 'Q014_03', 'Q062_1', 'Q062_3', 'Q067_2', 'Q072']

median_Columns = ['Q07', 'Q011', 'Q010_1', 'Q010_2', 'Q010_3', 'Q012', 'Q063_1', 'Q063_2', 'Q063_3', 'Q063_4']


#Generalize for all the columns
dataset = [data_1, data_2, data_3, data_4]
dataimpSet = [datimp_1, datimp_2, datimp_3, datimp_4]

# # Calculations before imputation
# for data in dataset:
#     for column in data.columns:
#         if column not in exclude_Columns and column not in default_Columns:
#             # Values before Imputation
#             print('values before imputation')
#             print(data[column].value_counts())

# Calculations after imputation           
for data_Imp in dataimpSet:
    for column in median_Columns:
        # Replace 99 with a mode value
        print('median :')
        print(data_Imp[column].median())
        print('#####################################################################')
        data_Imp[column] = data_Imp[column].fillna(value = data_Imp[column].median())
        # Values after Imputation
        print('values after imputation')
        print(data_Imp[column].value_counts())
    for column in mode_Columns:
        # Replace 99 with a mode value
        data_Imp[column] = data_Imp[column].fillna(value = data_Imp[column].mode()[0])
        # Values after Imputation
        print('values after imputation')
        print(data_Imp[column].value_counts())
            
            

# Delete the exclude_Columns           
for data_Imp in dataimpSet:
    for column in data_Imp.columns:
        if column in exclude_Columns:
            del data_Imp[column]
            print("deleted")
            
datimp_1.info()
datimp_2.info()
datimp_3.info()
datimp_4.info()
print(datimp_1['Year'].value_counts())
print(datimp_2['Year'].value_counts())
print(datimp_3['Year'].value_counts())
print(datimp_4['Year'].value_counts())

# print skewness of entire dataset
#data_1.skew()
#datimp_1.skew()

# Append the 4 data frames
Survey_Data = pd.concat([datimp_1, datimp_2, datimp_3, datimp_4], ignore_index=True)
print(Survey_Data.info())
                


# In[33]:


#------------------------------------------------------------------------------------------------------
########################################## Installing Packages #######################################
#------------------------------------------------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#------------------------------------------------------------------------------------------------------
########################################## labeling the categories #######################################
#------------------------------------------------------------------------------------------------------

# # One-hot encode the 'Category' column
# one_hot_encoded = pd.get_dummies(Survey_Data['AgeGroup'])

# print(one_hot_encoded)


# # Conversion of AgeGroup to 0 and 1
# Survey_Data['18-35'] = one_hot_encoded['18-35'].copy()
# Survey_Data['35-45'] = one_hot_encoded['35-45'].copy()
# Survey_Data['45-55'] = one_hot_encoded['45-55'].copy()
# Survey_Data['55+'] = one_hot_encoded['55+'].copy()

Climate_Change_Belief = ['QCOUNTRY', 'Q01', 'AgeGroup', 'Year', 'Q07', 'Q09', 'Q010_1', 
                         'Q010_2', 'Q010_3','Q012', 'Q011', 'Q013_1', 'Q013_2', 'Q013_3', 'Q013_4','Q014_01', 
                         'Q014_02', 'Q014_03', 'Q062_1', 'Q062_3', 'Q067_2', 'Q072']

Lifestyle_Changes = [ 'Q018', 'Q029', 'Q031', 'Q044', 'Q049_1', 'Q049_2', 'Q049_3']

Policy_Support = ['Q053_4', 'Q053_5', 'Q053_6', 'Q053_7', 'Q053_8', 'Q053_13', 'Q054', 'Q064']

Behavioural_Intentions = ['Q055_2', 'Q055_3', 'Q055_4', 'Q055_7', 'Q055_8', 'Q055_9', 'Q055_10', 'Q055_14', 
                          'Q055_peer', 'Q063_1', 'Q063_2', 'Q063_3', 'Q063_4']




# Define a dictionary to map values to labels
label_QCOUNTRY = {1: 'UK', 2: 'China', 3: 'Sweden', 4: 'Brazil'}
label_Q01 = {1: 'Male', 2: 'Female', 3: 'Other'}
label_Q07 = {1: 'Not at all worried', 2: 'Not very worried', 3: 'Fairly worried', 4: 'Very worried', 5: 'Extremely worried'}
label_Q09 = {1: 'Already feeling the effects', 0: 'Have not felt any effects till date'}
label_Q010_1 = {1: 'Not at all serious', 2: 'Not very serious', 3: 'Fairly serious', 4: 'Very serious', 5: 'Extremely serious'}
label_Q010_2 = {1: 'Not at all serious', 2: 'Not very serious', 3: 'Fairly serious', 4: 'Very serious', 5: 'Extremely serious'}
label_Q010_3 = {1: 'Not at all serious', 2: 'Not very serious', 3: 'Fairly serious', 4: 'Very serious', 5: 'Extremely serious'}
label_Q012 = {1: 'Little or no urgency', 2: 'A low level of urgency', 3: 'A moderate level of urgency', 4: 'A high level of urgency', 5: 'An extremely high level of urgency'}
label_Q011 = {1: 'Entirely negative', 2: 'More negative than positive', 3: 'Neither positive nor negative', 4: 'More positive than negative', 5: 'Entirely positive'}
label_Q013_1 = {0: 'We don’t need to do this at all/We don’t really need to do this', 1: 'We should probably do this/We should definetly do this'}
label_Q013_2 = {0: 'We don’t need to do this at all/We don’t really need to do this', 1: 'We should probably do this/We should definetly do this'}
label_Q013_3 = {0: 'We don’t need to do this at all/We don’t really need to do this', 1: 'We should probably do this/We should definetly do this'}
label_Q013_4 = {0: 'We don’t need to do this at all/We don’t really need to do this', 1: 'We should probably do this/We should definetly do this'}
label_Q014_01 = {1: 'Walk, cycle or use public transport more instead of using a car', 2: 'Eat less red meat', 3: 'Minimise throwing away food', 4: 'Drive an electric car', 5: 'Minimise the amount of energy we use at home', 6: 'Use a low-carbon heating/cooling system in our home', 7: 'Minimise air travel', 8: 'Reduce the amount of new things we buy'}
label_Q014_02 = {1: 'Walk, cycle or use public transport more instead of using a car', 2: 'Eat less red meat', 3: 'Minimise throwing away food', 4: 'Drive an electric car', 5: 'Minimise the amount of energy we use at home', 6: 'Use a low-carbon heating/cooling system in our home', 7: 'Minimise air travel', 8: 'Reduce the amount of new things we buy'}
label_Q014_03 = {1: 'Walk, cycle or use public transport more instead of using a car', 2: 'Eat less red meat', 3: 'Minimise throwing away food', 4: 'Drive an electric car', 5: 'Minimise the amount of energy we use at home', 6: 'Use a low-carbon heating/cooling system in our home', 7: 'Minimise air travel', 8: 'Reduce the amount of new things we buy'}
label_Q062_1 = {1: 'High', 0: 'Low'}
label_Q062_3 = {1: 'High', 0: 'Low'}
label_Q067_2 = {1: 'High', 0: 'Low'}
label_Q072 = {1: 'large City', 2: 'Large Town', 3: 'Small city', 4: 'Suburb', 5: 'rural area'}

# Use the map() function to replace values with labels
Survey_Data['QCOUNTRY'] = Survey_Data['QCOUNTRY'].map(label_QCOUNTRY)
Survey_Data['Q01'] = Survey_Data['Q01'].map(label_Q01)
Survey_Data['Q07'] = Survey_Data['Q07'].map(label_Q07)
Survey_Data['Q09'] = Survey_Data['Q09'].map(label_Q09)
Survey_Data['Q010_1'] = Survey_Data['Q010_1'].map(label_Q010_1)
Survey_Data['Q010_2'] = Survey_Data['Q010_2'].map(label_Q010_2)
Survey_Data['Q010_3'] = Survey_Data['Q010_3'].map(label_Q010_3)
Survey_Data['Q011'] = Survey_Data['Q011'].map(label_Q011)
Survey_Data['Q012'] = Survey_Data['Q012'].map(label_Q012)
Survey_Data['Q013_1'] = Survey_Data['Q013_1'].map(label_Q013_1)
Survey_Data['Q013_2'] = Survey_Data['Q013_2'].map(label_Q013_2)
Survey_Data['Q013_3'] = Survey_Data['Q013_3'].map(label_Q013_3)
Survey_Data['Q013_4'] = Survey_Data['Q013_4'].map(label_Q013_4)
Survey_Data['Q014_01'] = Survey_Data['Q014_01'].map(label_Q014_01)
Survey_Data['Q014_02'] = Survey_Data['Q014_02'].map(label_Q014_02)
Survey_Data['Q014_03'] = Survey_Data['Q014_03'].map(label_Q014_03)
Survey_Data['Q062_1'] = Survey_Data['Q062_1'].map(label_Q062_1)
Survey_Data['Q062_3'] = Survey_Data['Q062_3'].map(label_Q062_3)
Survey_Data['Q067_2'] = Survey_Data['Q067_2'].map(label_Q067_2)
Survey_Data['Q072'] = Survey_Data['Q072'].map(label_Q072)
Survey_Data['Year'] = Survey_Data['Year'].astype(str)

Climate_Belief_Data = Survey_Data[Climate_Change_Belief].copy()


print(Climate_Belief_Data.info())

print(Survey_Data.describe())


# In[34]:


#------------------------------------------------------------------------------------------------------
########################################## Installing Packages #######################################
#------------------------------------------------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#------------------------------------------------------------------------------------------------------
########################################## Exploratory Data Analysis #######################################
#------------------------------------------------------------------------------------------------------

#EDA
# Select data to Climate_Change_Belief and the demographics

wave_1 = Climate_Belief_Data[(Climate_Belief_Data['Year'] == '2020')]
wave_2 = Climate_Belief_Data[(Climate_Belief_Data['Year'] == '2021')]
wave_3 = Climate_Belief_Data[(Climate_Belief_Data['Year'] == '2022')]
print(wave_1.info())
print(wave_2.info())
print(wave_3.info())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[35]:


#------------------------------------------------------------------------------------------------------
########################################## Installing Packages #######################################
#------------------------------------------------------------------------------------------------------

import pandas as pd
import numpy as np
from kmodes.kmodes import KModes
from kmodes import kprototypes
from scipy.spatial import distance

#------------------------------------------------------------------------------------------------------
########################################## Find optimum number of K #######################################
#------------------------------------------------------------------------------------------------------
Public_Belief = ['Q07', 'Q09', 'Q010_1', 'Q010_2', 'Q010_3','Q012', 'Q011', 'Q013_1', 'Q013_2', 'Q013_3', 'Q013_4','Q014_01', 
                         'Q014_02', 'Q014_03']
data_wave_1 = wave_1[Public_Belief].copy()
data_wave_2 = wave_2[Public_Belief].copy()
data_wave_3 = wave_3[Public_Belief].copy()

# WAVE 1
# Find the optimum number of clusters
cs_1 = []
kvalues = range(2, 10)
# wave - 1
print('#################### wave 1######################')
for i in kvalues:
    kmode_1 = KModes(n_clusters=i, n_init = 1)
    fit_kmode_1 = kmode_1.fit(data_wave_1) # wave 1
    cs_1.append(kmode_1.cost_)
    

    
# wave - 2  
cs_2 = []
print('#################### wave 1######################')
for i in kvalues:  
    kmode_2 = KModes(n_clusters=i, n_init = 1)
    fit_kmode_2 = kmode_2.fit(data_wave_2) # wave 2
    cs_2.append(kmode_2.cost_)
   
    
# wave - 3  
cs_3 = []
print('#################### wave 1######################')
for i in kvalues: 
    kmode_3 = KModes(n_clusters=i, n_init = 1)
    fit_kmode_3 = kmode_3.fit(data_wave_3) # wave 3
    cs_3.append(kmode_3.cost_)
    
    
# WAVE 1
# Elbow method
plt.plot(kvalues, cs_1, 'bx-')
plt.title('The Elbow Method - Wave 1') #k=4
plt.xlabel('Number of clusters')
plt.ylabel('Cost')
plt.show()


# WAVE 2
# Elbow method
plt.plot(kvalues, cs_2, 'bx-')
plt.title('The Elbow Method - Wave 2')#k=5
plt.xlabel('Number of clusters')
plt.ylabel('Cost')
plt.show()


# WAVE 3
# Elbow method
plt.plot(kvalues, cs_3, 'bx-')
plt.title('The Elbow Method - Wave 3') #k=5
plt.xlabel('Number of clusters')
plt.ylabel('Cost')
plt.show()





# In[36]:


#------------------------------------------------------------------------------------------------------
########################################## Installing Packages #######################################
#------------------------------------------------------------------------------------------------------

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from kmodes.kmodes import KModes
import openpyxl


#------------------------------------------------------------------------------------------------------
########################################## K - Modes Clustering #######################################
#------------------------------------------------------------------------------------------------------

# WAVE 1
# Found k=4: recode kMeans for k=4
kmode_1 = KModes(n_clusters=4, n_init = 1) 
kmode_1.fit(data_wave_1)
predict_clusters_1 = kmode_1.predict(data_wave_1)
data_wave_1['cluster'] = predict_clusters_1




# Generate and store summary statistics for each cluster
clusters = [0, 1, 2, 3]
summary_statistics = data_wave_1.describe()
print(summary_statistics)


for column in data_wave_1.columns:
    
    # Create a contingency table of categorical feature frequencies within clusters
    contingency_table_1 = pd.crosstab(data_wave_1['cluster'], data_wave_1[column])

    # Normalize the contingency table for better heatmap visualization
    normalized_table_1 = contingency_table_1.div(contingency_table_1.sum(axis=1), axis=0) *100
    print("wave 1")
    #print(normalized_table_1)
    
    # Create a heatmap using seaborn
    print(column)
    normalized_table_1.plot(kind='bar', stacked=True)
    plt.xlabel('Clusters')
    plt.ylabel('Percentage')
    plt.title('Distribution of responses in each cluster')
    plt.legend(title='Types of responses',bbox_to_anchor=(1.05, 0.5), loc='center left')
    plt.show()



# Distribution of clusters
print(data_wave_1['cluster'].value_counts().sort_index())
print(((data_wave_1['cluster'].value_counts().sort_index())/data_wave_1.shape[0])*100)
data_wave_1['cluster'].value_counts(normalize=True).sort_index().plot.bar(rot=0)
plt.xlabel('Clusters')
plt.ylabel('Count')
plt.title('Distribution of clusters - WAVE 1')
plt.show()




# Print the cluster centroids with mapped cluster labels
print("Centroids of K-Modes Clusters - wave 1")
print(kmode_1.cluster_centroids_)


#################################################################################################################


# WAVE 2
# Found k=4: recode kMeans for k=4
kmode_2 = KModes(n_clusters=4, n_init = 1) 
kmode_2.fit(data_wave_2)
predict_clusters_2 = kmode_2.predict(data_wave_2)
data_wave_2['cluster'] = predict_clusters_2


# Generate and store summary statistics for each cluster
clusters = [0, 1, 2, 3]
summary_statistics = data_wave_2.describe()

        
for column in data_wave_2.columns:
    
    # Create a contingency table of categorical feature frequencies within clusters
    contingency_table_2 = pd.crosstab(data_wave_2['cluster'], data_wave_2[column])

    # Normalize the contingency table for better heatmap visualization
    normalized_table_2 = contingency_table_2.div(contingency_table_2.sum(axis=1), axis=0) *100
    print("wave 2")
    #print(normalized_table_2)
    
    # Create a heatmap using seaborn
    print(column)
    normalized_table_2.plot(kind='bar', stacked=True)
    plt.xlabel('Clusters')
    plt.ylabel('Percentage')
    plt.title('Distribution of responses in each cluster')
    plt.legend(title='Types of responses',bbox_to_anchor=(1.05, 0.5), loc='center left')
    plt.show()

# Distribution of clusters
print(data_wave_2['cluster'].value_counts().sort_index())
print(((data_wave_2['cluster'].value_counts().sort_index())/data_wave_2.shape[0])*100)
data_wave_2['cluster'].value_counts(normalize=True).sort_index().plot.bar(rot=0)
plt.xlabel('Clusters')
plt.ylabel('Count')
plt.title('Distribution of clusters - WAVE 2')
plt.show()



# Print the cluster centroids with mapped cluster labels
print("Centroids of K-Modes Clusters - wave 2")
print(kmode_2.cluster_centroids_)

###########################################################################################################

# WAVE 3
# Found k=5: recode kMeans for k=5
kmode_3 = KModes(n_clusters=5, n_init = 1) 
kmode_3.fit(data_wave_3)
predict_clusters_3 = kmode_3.predict(data_wave_3)
data_wave_3['cluster'] = predict_clusters_3


# Generate and store summary statistics for each cluster
clusters = [0, 1, 2, 3, 4]
summary_statistics = data_wave_3.describe()
print(summary_statistics)

        
for column in data_wave_3.columns:
    # Create a contingency table of categorical feature frequencies within clusters
    contingency_table_3 = pd.crosstab(data_wave_3['cluster'], data_wave_3[column])

    # Normalize the contingency table for better heatmap visualization
    normalized_table_3 = contingency_table_3.div(contingency_table_3.sum(axis=1), axis=0)*100
    print("wave 3")
    #print(normalized_table_3)
    
    # Create a heatmap using seaborn
    print(column)
    normalized_table_3.plot(kind='bar', stacked=True)
    plt.xlabel('Clusters')
    plt.ylabel('Percentage')
    plt.title('Distribution of responses in each cluster')
    plt.legend(title='Types of responses',bbox_to_anchor=(1.05, 0.5), loc='center left')
    plt.show()

# Distribution of clusters
print(data_wave_3['cluster'].value_counts().sort_index())
print(((data_wave_3['cluster'].value_counts().sort_index())/data_wave_3.shape[0])*100)
data_wave_3['cluster'].value_counts(normalize=True).sort_index().plot.bar(rot=0)
plt.xlabel('Clusters')
plt.ylabel('Count')
plt.title('Distribution of clusters - WAVE 3')
plt.show()



# Trendline - wave 1
data_wave_1['cluster'] = data_wave_1['cluster'].replace(0,'Cautious')
data_wave_1['cluster'] = data_wave_1['cluster'].replace(1,'Concerned')
data_wave_1['cluster'] = data_wave_1['cluster'].replace(2,'Alarmed')
data_wave_1['cluster'] = data_wave_1['cluster'].replace(3,'Disengaged')

data_counts_1 = data_wave_1['cluster'].value_counts(normalize=True).sort_index()
plt.figure(figsize=(8, 2))
data_counts_1.plot(kind='line')
plt.xlabel('')
plt.ylabel('')
plt.title('')
plt.xticks(rotation=45)
plt.grid(True) 
plt.show() 


data_wave_2['cluster'] = data_wave_2['cluster'].replace(0,'Concerned')
data_wave_2['cluster'] = data_wave_2['cluster'].replace(1,'Disengaged')
data_wave_2['cluster'] = data_wave_2['cluster'].replace(2,'Alarmed')
data_wave_2['cluster'] = data_wave_2['cluster'].replace(3,'Cautious')

data_counts_2 = data_wave_2['cluster'].value_counts(normalize=True).sort_index()
plt.figure(figsize=(8, 2))
data_counts_2.plot(kind='line')
plt.xlabel('')
plt.ylabel('')
plt.title('')
plt.xticks(rotation=45)
plt.grid(True) 
plt.show() 

# Trendline - wave 3
data_wave_3['cluster'] = data_wave_3['cluster'].replace(0,'Concerned')
data_wave_3['cluster'] = data_wave_3['cluster'].replace(1,'Disengaged')
data_wave_3['cluster'] = data_wave_3['cluster'].replace(2,'Neutral')
data_wave_3['cluster'] = data_wave_3['cluster'].replace(3,'Alarmed')
data_wave_3['cluster'] = data_wave_3['cluster'].replace(4,'Cautious')

data_counts_3 = data_wave_3['cluster'].value_counts(normalize=True).sort_index()
plt.figure(figsize=(8, 2))
data_counts_3.plot(kind='line')
plt.xlabel('')
plt.ylabel('')
plt.title('')
plt.xticks(rotation=45)
plt.grid(True) 
plt.show() 


# Print the cluster centroids with mapped cluster labels
print("Centroids of K-Modes Clusters - wave 3")
print(kmode_3.cluster_centroids_)





# In[42]:


#------------------------------------------------------------------------------------------------------
########################################## Installing Packages #######################################
#------------------------------------------------------------------------------------------------------
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn import metrics
from statsmodels.stats.outliers_influence import variance_inflation_factor
import shap

#------------------------------------------------------------------------------------------------------
################################################ Prediction ###########################################
#------------------------------------------------------------------------------------------------------
Climate_change_Data = pd.concat([wave_1, wave_2, wave_3], ignore_index=True)
print(Climate_change_Data.info())
print(Climate_change_Data['Q09'].value_counts())
Climate_change_Data['Q09'] = Climate_change_Data['Q09'].replace({'Already feeling the effects': 1, 'Have not felt any effects till date': 0})
Climate_change_Data['Q09'] = Climate_change_Data['Q09'].astype('uint8')
# Encode categorical features using one-hot encoding
Climate_Belief_encoded = pd.get_dummies(Climate_change_Data, columns=['QCOUNTRY', 'Q01', 'AgeGroup', 'Year', 'Q07', 'Q010_1', 
                         'Q010_2', 'Q010_3','Q012', 'Q011', 'Q013_1', 'Q013_2', 'Q013_3', 'Q013_4','Q014_01', 
                         'Q014_02', 'Q014_03', 'Q062_1', 'Q062_3', 'Q067_2', 'Q072'], drop_first=True)
print(Climate_Belief_encoded.info())


y = Climate_Belief_encoded['Q09']
X = Climate_Belief_encoded.drop('Q09', axis=1)


# mullti collinearity
# X = Climate_Belief_encoded
# vif = pd.DataFrame()
# vif["Variable"] = Climate_Belief_encoded.columns
# vif["VIF"] = [variance_inflation_factor(Climate_Belief_encoded.values, i) for i in range(Climate_Belief_encoded.shape[1])]
# print(vif)


#vif.to_excel('C:/Users/deept/OneDrive/Desktop/CAST/Report Data/vif.xlsx', index=True)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

##################################

# Fit a logistic regression model
model_1 = LogisticRegression()
model_1.fit(X_train, y_train)
# Make predictions using model_1
y_pred_1 = model_1.predict(X_test)
# Evaluate the model's performance
precision_1 = precision_score(y_test, y_pred_1)
recall_1 = recall_score(y_test, y_pred_1)
accuracy_1 = accuracy_score(y_test, y_pred_1)
fscore_1 = f1_score(y_test, y_pred_1)
print("Accuracy:", accuracy_1)
print("Precision:", precision_1)
print("Recall:", recall_1)
print("F_score:", fscore_1)
# Show confusion matrix
cmap = plt.cm.BuPu
confusion_matrix_1 = metrics.confusion_matrix(y_test, y_pred_1)
print(confusion_matrix_1)
cm_display_1 = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix_1, display_labels = [0, 1])
cm_display_1.plot(cmap = cmap)
plt.show()

# Visualization of the correct and wrong predictions as a bar chart
correct_predictions = np.diag(confusion_matrix_1)
total_predictions = np.sum(confusion_matrix_1, axis=1)
wrong_predictions = total_predictions - correct_predictions
class_labels = ['Have not felt any effects till date', 'Already feeling the effects']
bar_width = 0.25
index = np.arange(len(class_labels))
plt.bar(index, correct_predictions, bar_width, label='Correct Predictions')
plt.bar(index + bar_width, wrong_predictions, bar_width, label='Wrong Predictions')
plt.xlabel('')
plt.ylabel('Number of Predictions')
plt.title(' Visualization of the correct and wrong predictions using logistic regression classifier')
plt.xticks(index + bar_width / 2, class_labels)
plt.legend()
plt.show()

# Feature Importance using shap
explainer_1 = shap.Explainer(model_1, X_train)
shap_values_1 = explainer_1.shap_values(X_train)
print(shap_values_1)
shap.summary_plot(shap_values_1, X_test, plot_type="bar")
plt.figure(figsize=(4, 2))
plt.tight_layout() 
plt.show()



#####################################
# Fit a SVM classifier model
model_2 = SVC(kernel='rbf')
model_2.fit(X_train, y_train)
# Make predictions using model_1
y_pred_2 = model_2.predict(X_test)
# Evaluate the model's performance
precision_2 = precision_score(y_test, y_pred_2)
recall_2 = recall_score(y_test, y_pred_2)
accuracy_2 = accuracy_score(y_test, y_pred_2)
fscore_2 = f1_score(y_test, y_pred_2)
print("Accuracy:", accuracy_2)
print("Precision:", precision_2)
print("Recall:", recall_2)
print("F_score:", fscore_2)
# Show confusion matrix
confusion_matrix_2 = metrics.confusion_matrix(y_test, y_pred_2)
print(confusion_matrix_2)
cm_display_2 = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix_2, display_labels = [0, 1])
cm_display_2.plot(cmap = cmap)
plt.show()

# Visualization of the correct and wrong predictions as a bar chart
correct_predictions = np.diag(confusion_matrix_2)
total_predictions = np.sum(confusion_matrix_2, axis=1)
wrong_predictions = total_predictions - correct_predictions
class_labels = ['Have not felt any effects till date', 'Already feeling the effects']
bar_width = 0.25
index = np.arange(len(class_labels))
plt.bar(index, correct_predictions, bar_width, label='Correct Predictions')
plt.bar(index + bar_width, wrong_predictions, bar_width, label='Wrong Predictions')
plt.xlabel('')
plt.ylabel('Number of Predictions')
plt.title('Visualization of the correct and wrong predictions using SVM classifier')
plt.xticks(index + bar_width / 2, class_labels)
plt.legend()
plt.show()


#######################################
# Fit a Random forest classifier model
model_3 = RandomForestClassifier( n_estimators=100, max_depth=None, min_samples_split=2, min_samples_leaf=1, max_features='auto', random_state=42)
model_3.fit(X_train, y_train)
# Make predictions using model_1
y_pred_3 = model_3.predict(X_test)
# Evaluate the model's performance
precision_3 = precision_score(y_test, y_pred_3)
recall_3 = recall_score(y_test, y_pred_3)
accuracy_3 = accuracy_score(y_test, y_pred_3)
fscore_3 = f1_score(y_test, y_pred_3)
print("Accuracy:", accuracy_3)
print("Precision:", precision_3)
print("Recall:", recall_3)
print("F_score:", fscore_3)
# Show confusion matrix
confusion_matrix_3 = metrics.confusion_matrix(y_test, y_pred_3)
print(confusion_matrix_3)
cm_display_3 = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix_3, display_labels = [0, 1])
cm_display_3.plot(cmap = cmap)
plt.show()
# Visualization of the correct and wrong predictions as a bar chart
correct_predictions = np.diag(confusion_matrix_3)
total_predictions = np.sum(confusion_matrix_3, axis=1)
wrong_predictions = total_predictions - correct_predictions
class_labels = ['Have not felt any effects till date', 'Already feeling the effects']
bar_width = 0.25
index = np.arange(len(class_labels))
plt.bar(index, correct_predictions, bar_width, label='Correct Predictions')
plt.bar(index + bar_width, wrong_predictions, bar_width, label='Wrong Predictions')
plt.xlabel('')
plt.ylabel('Number of Predictions')
plt.title('Visualization of the correct and wrong predictions using Random forest classifier')
plt.xticks(index + bar_width / 2, class_labels)
plt.legend()
plt.show()

precision = []
precision.append(precision_1)
precision.append(precision_2)
precision.append(precision_3)


recall = []
recall.append(recall_1)
recall.append(recall_2)
recall.append(recall_3)


accuracy = []
accuracy.append(accuracy_1)
accuracy.append(accuracy_2)
accuracy.append(accuracy_3)


fscore = []
fscore.append(fscore_1)
fscore.append(fscore_2)
fscore.append(fscore_3)

metrics_table = [[precision, recall, accuracy, fscore] for precision, recall, accuracy, fscore in zip(precision, recall, accuracy, fscore)]
print("metrics table")
for row in metrics_table:
    print(row)
    
# Imbalanced data

grouped = Climate_change_Data.groupby('Year')['Q09'].value_counts().unstack(fill_value=0)
print(grouped)

# Plot the grouped bar chart
grouped.plot(kind='bar', stacked=True)
plt.xlabel('Categories')
plt.ylabel('Counts')
plt.title('Counts of responses by Category')
plt.legend(title='y', labels=['Have not felt any effects till date', 'Already feeling the effects'], bbox_to_anchor=(1.05, 0.5), loc='center left')
plt.show()


# In[ ]:





# In[ ]:




