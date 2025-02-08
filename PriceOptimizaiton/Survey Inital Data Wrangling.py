#!/usr/bin/env python
# coding: utf-8

# ## Data Wrangling ##

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


def ltci(text):
    new_text = text.lower()
    
    d = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17','r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'}

    result = int(d[new_text[-1]]) 
    if len(new_text) > 1:
        result += 26*(int(d[new_text[0]]))
    return result - 1

def replace_gender1():
    size = df.loc[df['gender'] == "Prefer not to say", 'gender'].size
    male = df.loc[df['gender'] == "Male", "gender"].size
    female = df.loc[df['gender'] == "Female", "gender"].size
    male_th = male/(male+female)
    result = []
    for i in range(size):
        u = np.random.rand()
        if u<=male_th:
            result.append("Male")
        else:
            result.append("Female")  
    return pd.DataFrame(result)

def replace_gender2():
    size = df.loc[df['gender'] == "Non-binary / third gender", 'gender'].size
    male = df.loc[df['gender'] == "Male", "gender"].size
    female = df.loc[df['gender'] == "Female", "gender"].size
    male_th = male/(male+female)
    result = []
    for i in range(size):
        u = np.random.rand()
        if u<=male_th:
            result.append("Male")
        else:
            result.append("Female")   
    return pd.DataFrame(result)

def replace_age():
    values = ["Less than 18 years old", "19 - 25 years old", "26 - 35 years old", "36 - 55 years old", "55+"]
    size = df.loc[df['age'] == "Prefer not to say", 'age'].size
    freq = []
    for v in values: 
        freq.append(df.loc[df['age'] == v].size)
    freq = np.array(freq)
    dist = freq / freq.sum()
    cum_dist = np.array([dist[0:i].sum() for i in range(1,6)])
    result = []
    for i in range(size):
        u = np.random.rand()
        for j in range(len(cum_dist)):
            if u <= cum_dist[j]:
                result.append(cum_dist[j])
    return pd.DataFrame(result)

def replace_education():
    values = ["Some High School", "High School", "Bachelor's Degree", "Master's Degree", "Ph.D. or higher"]
    size = df.loc[df['education'] == "Prefer not to say", 'education'].size
    freq = []
    for v in values: 
        freq.append(df.loc[df['education'] == v].size)
    freq = np.array(freq)
    dist = freq / freq.sum()
    cum_dist = np.array([dist[0:i].sum() for i in range(1,6)])
    result = []
    for i in range(size):
        u = np.random.rand()
        for j in range(len(cum_dist)):
            if u <= cum_dist[j]:
                result.append(cum_dist[j])
    return pd.DataFrame(result)

def replace_employment():
    values = ["Student", "Employed Full-Time", "Employed Part-Time", "Seeking opportunities", "Retired"]
    size = df.loc[df['employment'] == "Prefer not to say", 'employment'].size
    freq = []
    for v in values: 
        freq.append(df.loc[df['employment'] == v].size)
    freq = np.array(freq)
    dist = freq / freq.sum()
    cum_dist = np.array([dist[0:i].sum() for i in range(1,6)])
    result = []
    for i in range(size):
        u = np.random.rand()
        for j in range(len(cum_dist)):
            if u <= cum_dist[j]:
                result.append(cum_dist[j])
    return pd.DataFrame(result)

def replace_income():
    values = ['Less than â‚¬25,000', 'More than â‚¬100,000', 'â‚¬25,000 - â‚¬50,000', 'â‚¬50,000 - â‚¬100,000']
    size = df.loc[df['income'] == "Prefer not to say", 'income'].size
    freq = []
    for v in values: 
        freq.append(df.loc[df['income'] == v].size)
    freq = np.array(freq)
    dist = freq / freq.sum()
    cum_dist = np.array([dist[0:i].sum() for i in range(1,5)])
    result = []
    for i in range(size):
        u = np.random.rand()
        for j in range(len(cum_dist)):
            if u <= cum_dist[j]:
                result.append(cum_dist[j])
    return pd.DataFrame(result)
    
def extract_choice(row):
    if row['choice_set'] == 'C1' and (row['option'] == 'choice_opt_1'):
        return row[64], row[66], row[68]
    if row['choice_set'] == 'C1' and (row['option'] == 'choice_opt_2'):
        return row[70], row[72], row[74]
    if row['choice_set'] == 'C2' and (row['option'] == 'choice_opt_1'):
        return row[76], row[78], row[80]
    if row['choice_set'] == 'C2' and (row['option'] == 'choice_opt_2'):
        return row[82], row[84], row[86]
    if row['choice_set'] == 'C3' and (row['option'] == 'choice_opt_1'):
        return row[88], row[90], row[92]
    if row['choice_set'] == 'C3' and (row['option'] == 'choice_opt_2'):
        return row[94], row[96], row[98]
    if row['choice_set'] == 'C4' and (row['option'] == 'choice_opt_1'):
        return row[100], row[102], row[104]
    if row['choice_set'] == 'C4' and (row['option'] == 'choice_opt_2'):
        return row[106], row[108], row[110]
    
    return 0, 0, 0

def extract_competitors(row):
    if row['choice_set'] == 'C1' and (row['option'] == 'choice_opt_1'):
        return row[70], row[72], row[74], 0, 0, 0
    if row['choice_set'] == 'C1' and (row['option'] == 'choice_opt_2'):
        return row[64], row[66], row[68], 0, 0, 0
    if row['choice_set'] == 'C1' and (row['option'] == 'choice_opt_3'):
        return row[64], row[66], row[68], row[70], row[72], row[74]
    if row['choice_set'] == 'C2' and (row['option'] == 'choice_opt_1'):
        return row[82], row[84], row[86], 0, 0, 0
    if row['choice_set'] == 'C2' and (row['option'] == 'choice_opt_2'):
        return row[76], row[78], row[80], 0, 0, 0
    if row['choice_set'] == 'C2' and (row['option'] == 'choice_opt_3'):
        return row[76], row[78], row[80], row[82], row[84], row[86]
    if row['choice_set'] == 'C3' and (row['option'] == 'choice_opt_1'):
        return row[94], row[96], row[98], 0, 0, 0
    if row['choice_set'] == 'C3' and (row['option'] == 'choice_opt_2'):
        return row[88], row[90], row[92], 0, 0, 0
    if row['choice_set'] == 'C3' and (row['option'] == 'choice_opt_3'):
        return row[88], row[90], row[92], row[94], row[96], row[98]
    if row['choice_set'] == 'C4' and (row['option'] == 'choice_opt_1'):
        return row[106], row[108], row[110], 0, 0, 0
    if row['choice_set'] == 'C4' and (row['option'] == 'choice_opt_2'):
        return row[100], row[102], row[104], 0, 0, 0
    if row['choice_set'] == 'C4' and (row['option'] == 'choice_opt_3'):
        return row[100], row[102], row[104], row[106], row[108], row[110] 
    
    return 0, 0, 0, 0, 0, 0


# In[ ]:



#import file as extracted from Qualtrics
df = pd.read_excel("../Final Project/Data Survey - Early.xlsx", header = None)

#Drop columns not needed for analysis
cols_to_drop = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",                "K", "L", "M", "N", "O", "P", "Q", "AL", "AN", "AP",                "BE", "BG", "BL", "BN", "BP", "BR", "BT", "BV", "BX", "BZ",                "CB", "CD", "CF", "CH", "CJ", "CL", "CN", "CP", "CR",                "CT", "CV", "CX", "CZ", "DB", "DD", "DF", "DH", "DJ", 'DI']
indeces_to_drop = [ltci(x) for x in cols_to_drop]
df.drop(df.columns[indeces_to_drop], axis=1, inplace=True)

#Drop state rows
df.drop(index = range(11), inplace = True)
df.dropna(how = 'all', inplace = True)
df.reset_index(inplace = True)

#Rename columns for analysis
cp = {ltci("R") : "gender", ltci("S") : "age", ltci("T") : "country",       ltci("U") : "region", ltci("V") : "education", ltci("W") : "employment",      ltci("X") : "income", ltci("Y") : "strug_enter_attion", ltci("Z") : "strug_keep_attion",       ltci("AA") : "lack_of_control", ltci("AB") : "lack_of_efficacy", ltci("AC") : "stress_1",       ltci("AD") : "stress_2", ltci("AE") : "stress_3", ltci("AF") : "stress_4",       ltci("AG") : "meditated", ltci("AH") : "want_to_try", ltci("AI") : "exp_benefits",       ltci("AJ") : "exp_time_for_benefits", ltci("AK") : "further_incentive", ltci("AM") : "starting_place",       ltci("AO") : "reason_not_want_try", ltci("AQ") : "des_relieve_stress", ltci("AR") : "des_to_impr_concent",      ltci("AS") : "meditation_duration", ltci("AT") : "meditation_frequency", ltci("AU") : "life_impr_from_meditation",      ltci("AV") : "first_improved_ability", ltci("AW") : "second_improved_ability", ltci("AX") : "third_improved_ability",      ltci("AY") : "fourth_improved_ability", ltci("AZ") : "fith_improved_ability", ltci("BA") : "sixth_improved_ability",       ltci("BB") : "seventh_improved_ability", ltci("BC") : "time_before_seeing_impr",ltci("BD") : "usual_meditation_medium",      ltci("BF") : "reason_for_start", ltci("BH") : "C1", ltci("BI") : "C2", ltci("BJ") : "C3", ltci("BK") : "C4"}
df.rename(columns = cp, inplace = True)

# Wide to Long Format 

id_variables = df.loc[:, ~df.columns.isin(['C1', 'C2', 'C3', 'C4'])]
df = pd.melt(df, id_vars = id_variables.columns, value_vars = ['C1', 'C2', 'C3', 'C4'],         var_name = 'choice_set', value_name = 'choice')
df.dropna(how = 'any', subset = ['choice'], inplace = True)
df['choice'].astype(np.int64, copy = True)

df['choice_opt_1'] = (df['choice'] == 1).astype(np.int64, copy = True)
df['choice_opt_2'] = (df['choice'] == 2).astype(np.int64, copy = True)
df['choice_opt_3'] = (df['choice'] == 3).astype(np.int64, copy = True)
#df.iloc[:, -5::]

id_variables = df.loc[:, ~df.columns.isin(['choice_opt_1', 'choice_opt_2', 'choice_opt_3'])]
df = pd.melt(df, id_vars = id_variables.columns, value_vars = ['choice_opt_1', 'choice_opt_2', 'choice_opt_3'],         var_name = 'option', value_name = 'choosed')


# In[234]:


df[['group', 'location', 'price']] = df.apply(extract_choice, axis=1, result_type="expand")
df[['group_comp1', 'location_comp1', 'price_comp1', 'group_comp2', 'location_comp2', 'price_comp2']] = df.apply(extract_competitors, axis = 1, result_type = "expand")

#Dropping residual variables
indeces_to_drop = [(x) for x in range(38, 62, 1)]
df.drop(df.columns[indeces_to_drop], axis=1, inplace=True)
df.drop('choice', axis = 1, inplace = True)

# Complete variables to facilitate analysis
df.loc[df['gender'] == 'Prefer not to say', 'gender'] = pd.DataFrame(replace_gender1())
df.loc[df['gender'] == 'Non-binary / third gender', 'gender'] = replace_gender2()
df.loc[df['age'] == 'Prefer not to say', 'age'] = replace_age()
df.loc[df['education'] == 'Prefer not to say', 'education'] = replace_education()
df.loc[df['employment'] == 'Prefer not to say', 'employment'] = replace_employment()
df.loc[df['income'] == 'Prefer not to say', 'income'] = replace_income()

for col in df.columns[0:16].values:
    df.drop(df[df[col].isna()].index, inplace = True)

for col in  df.columns[-12::].values:
    df.drop(df[df[col].isna()].index, inplace = True)


# In[238]:


grp = pd.get_dummies(df['group'])
lc = pd.get_dummies(df['location'])
prc = pd.get_dummies(df['price'])

df = df.loc[:, ~df.columns.isin(['group', 'location', 'price'])].join(grp.iloc[:, 1::]).join(lc.iloc[:, 1::]).join(prc.iloc[:, 1::])
df.to_csv('C:\\Users\\User\\Dropbox\\My PC (HP-16340)\\Desktop\\Bocconi\\Semester II\\Innovation and Marketing Analytics\\Final Project\\CleredDF.csv')


# In[ ]:





# In[ ]:





# In[ ]:




