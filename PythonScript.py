import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_excel(r'C:\Users\30694\OneDrive\Έγγραφα\Project Portofolio\Financial Data Analysis for Bank Loans\Bank_Personal_Loan_Modelling.xlsx',1)
df.head()

########## ---------- PERFORM Descriptive ANALYSIS  ---------- ##########

# ---------------------   exploratory data analysis    --------------------------#

# this means drop columns that i do not need, check for null values, in general to summarize their main characteristics
#, often using statistical graphics and other data visualization methods.
df.shape

# check if i have any null values in my data
df.isnull().sum()

# ID and Zipcode might be removed as they may not be useful for our analysis




df.drop(['ID','ZIP Code'],axis=1,inplace=True)
df.columns
import plotly.express as px


## use five porint summary to get description about the data
# means: find the min value which means i have to find: 0% percentile data, 25%,50% percentile (median),75%,100% (max value)
# we are going to do that with boxplots

fig=px.box(df,y=['Age', 'Experience', 'Income', 'Family', 'Education'])
fig.show()


# Five point summary suggest that Experience has negative value(This should be fixed).
# we can see the Min, Max, mean and std deviation for all key attributes of the dataset
# Income has too much noise and slightly skewed right, Age and exp are equally distributed.


# check the skewness
df.skew()

df.hist(figsize=(20,20))


# INFERENCE from Histogram
# 1.Age & Experience are to an extent equally distributed
# 2.Income & Credit card spending are skewed to the left
# 3.We have more Undergraduates than Graduate and Advanced & Professional
# 4.60% of customers have enabled online banking and went digital

import seaborn as sns
sns.distplot(df['Experience']) # exist some negative values, do more analysis


Negative_exp=df[df['Experience']<0]
Negative_exp.head()

Negative_exp['Experience'].mean()
Negative_exp.size
print('There are {} records which has negative values for experience, approx {} %'.format(Negative_exp.size , ((Negative_exp.size/df.size)*100)))

data=df.copy()
data.head()


#### use numpy where function to change the negative values to mean value derived from data with the same age group
data['Experience']=np.where(data['Experience']<0,data['Experience'].mean(),data['Experience'])


df.corr()

plt.figure(figsize=(10,6))
sns.heatmap(df.corr(),annot=True) # annot :  show the values

# We could see that Age & Experience are very strongly correlated,
# Hence it is fine for us to go with Age and drop Experience to avoid multi-colinearity issue.

data=data.drop(['Experience'],axis=1)

data['Education'].unique()


def mark(x):
    if x==1:
        return 'Undergrad'
    elif x==2:
        return 'Graduate'
    else:
        return 'Advanced/Professional'

## to apply the function above, because we do not say to print something or return    
data['Edu_mark']=data['Education'].apply(mark)
data.head()


EDU_dis=data.groupby('Edu_mark')['Age'].count()
EDU_dis

fig=px.pie(data,values=EDU_dis, names=EDU_dis.index,title='Pie CHart')
fig.show()

#### Inference :We could see that We have more Undergraduates 41.92% than graduates(28.06%) & Advanced Professional(30.02%)


# create a custom function to categorize the customers
def Security_CD(row):
    if (row['Securities Account']==1) & (row['CD Account']==1):
        return 'Holds Securites & Deposit'
    elif (row['Securities Account']==0) & (row['CD Account']==0):
        return 'Does not Holds Securites or Deposit'
    elif (row['Securities Account']==1) & (row['CD Account']==0):
        return ' Holds only Securites '
    elif (row['Securities Account']==0) & (row['CD Account']==1):
        return ' Holds only Deposit'


data['Account_holder_category']=data.apply(Security_CD,axis=1)


values=data['Account_holder_category'].value_counts()
values.index

# create a pie chart for the column we create above
fig=px.pie(data,values=values, names=values.index,title='Pie CHart')
fig.show()



################ ANALYSE CUSTOMER ON THE BASIS OF EDUCATION, INCOME AND PERSONAL LOAN STATUS ################
plt.figure(figsize=(12,8))
sns.distplot(data[data['Personal Loan']==0]['Income'],hist=False,label='Income with no personal loan')
sns.distplot(data[data['Personal Loan']==1]['Income'],hist=False,label='Income with personal loan')
plt.legend() #show the legend 

#### Conclusion: Customers Who have availed personal loan seem to have higher income than those who do not have personal loan

# Automate the above process
def plot(col1,col2,label1,label2,title):
    plt.figure(figsize=(12,8))
    sns.distplot(data[data[col2]==0][col1],hist=False,label=label1)
    sns.distplot(data[data[col2]==1][col1],hist=False,label=label2)
    plt.legend()
    plt.title(title)


##### -------- ANALYSE CUSTOMERS BEHAVIOR ON THE BASIS OF VARIOUS ATTRIBUTES ------------ #####

data.columns
col_names=['Securities Account','Online','Account_holder_category','CreditCard']


for i in col_names:
    plt.figure(figsize=(10,5))
    sns.countplot(x=i,hue='Personal Loan',data=data)
    
#From the above graph we could infer that , customers who hold deposit account & customers 
# who do not hold either a securities account or deposit account have aviled personal loan


# --------------- #### Perform Hypothesis Testing  # --------------- #### 

### Q.. How Age of a person is going to be a factor in availing loan ??? Does Income of a person have an impact on availing loan ??? Does the family size makes them to avail loan ???¶

sns.scatterplot(data['Age'],data['Personal Loan'],hue=data['Family'])
import scipy.stats as stats
Ho='Age does not have impact on availing personal loan'
Ha='Age does  have impact on availing personal loan'

Age_no=np.array(data[data['Personal Loan']==0]['Age'])
Age_yes=np.array(data[data['Personal Loan']==1]['Age'])

t,p_value=stats.ttest_ind(Age_no,Age_yes,axis=0)
if p_value<0.05:
    print(Ha,' as the p_value is less than 0.05 with a value of {}'.format(p_value))
else:
    print(Ho,' as the p_value is greater than 0.05 with a value of {}'.format(p_value))
    
    
## Automate the above process
def Hypothesis(col1,col2,HO,Ha):
    arr1=np.array(data[data[col1]==0][col2])
    arr2=np.array(data[data[col1]==1][col2])
    t,p_value=stats.ttest_ind(arr1,arr2,axis=0)
    if p_value<0.05:
        print('{}, as the p_value is less than 0.05 with a value of {}'.format(Ha,p_value))
    else:
        print('{} as the p_value is greater than 0.05 with a value of {}'.format(HO,p_value))
