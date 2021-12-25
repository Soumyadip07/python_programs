#ONE WAY ANOVA
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

df1=pd.read_csv('https://raw.githubusercontent.com/Soumyadip07/python_datasets/main/machine.csv')
print("ONE-WAY ANOVA calculation Methods:-","\n1.By using library functions","\n2.By manually executing every steps of univariate ANOVA")
n=int(input("Enter you choice:-"))


if(n==1):
    print("\nTHE DATA:-","\n",df1)
    #USING STATSMODEL LIBRARY FUNCTIONS'
    model=ols('score ~ company',data=df).fit()
    anov_res=sm.stats.anova_lm(model)
    print("ONE WAY ANOVA Result(using library):-","\n",anov_res)
elif(n==2):
    print("\nTHE DATA:-","\n",df1)
    #MANUAL CALCULATION
    df=df1.copy()
    c1=df['company'].isnull().sum()
    c2=df['score'].isnull().sum()
    if(c1==0 and c2==0):
        mn=df['score'].mean()
        df['overall_mean']=mn
        #SUM OF SQUARE
        #SS_Total
        ss_total=sum((df['score'] - df['overall_mean'])**2)
        #print("Sum of Square total:",ss_total)
        #SS_Within
        group_mean=df.groupby('company').mean()
        group_mean=group_mean.rename(columns={'score':'group_mean'})
        df=df.merge(group_mean,left_on='company',right_index=True)
        ss_within=sum((df['score'] - df['group_mean'])**2)
        #print("Sum of Square within:",ss_within)
        #SS_Between
        ss_between=ss_total-ss_within
        #print("Sum of Square between:",ss_between)
        
        #Degree of freedom
        n_grp=len(set(df['company']))
        n_obs=len(df['company'])
        df_b=n_grp-1
        df_w=n_obs-n_grp
        #print("df between:-",df_b,"\ndf within:-",df_w)
        #Mean Square
        ms_b=ss_between/df_b
        ms_w=ss_within/df_w
        #print("Mean Square between:",ms_b,"\nMean Square within:",ms_w)
      
        #F-value
        f=ms_b/ms_w
        #print("F-value:-",f)
        
        #Creating Table
        table_data={'df':[df_b,df_w],
                    'sum_sq':[ss_between,ss_within],
                    'mean_sq':[ms_b,ms_w],
                    'F value':[f]}
        t_dta=pd.DataFrame(table_data,index=['Between/company','Within/residual'])
        print("ONE WAY ANOVA Result(manual calculation):-","\n",t_dta,"\nSum of Square total:",ss_total)
    else:
        print('One way ANOVA not possible as there is some missing value')
else:
    print("Please enter a correct option!")
