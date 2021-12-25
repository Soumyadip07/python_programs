#TWO-WAY ANOVA
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols

#create DataFrame in Pandas
df=pd.read_csv(r'https://raw.githubusercontent.com/Soumyadip07/python_datasets/main/ToothGrowth.csv')
print("TWO-WAY ANOVA calculation Methods:-","\n1.By using library functions","\n2.By manually executing every steps of univariate ANOVA")
n=int(input("Enter you choice:-"))
if(n==1):
    print("\nTHE DATA:-","\n",df)
    #USING STATSMODEL LIBRARY FUNCTIONS
    model=ols('len ~ C(supp) + C(dose) + C(supp):C(dose)', data=df).fit()
    anov_res=sm.stats.anova_lm(model, typ=2)
    print("TWO WAY ANOVA Result(using library):-","\n",anov_res)
elif(n==2):
    print("\nTHE DATA:-","\n",df)
    #MANUAL CALCULATION
    data=df.copy()
    c1=df['len'].isnull().sum()
    c2=df['supp'].isnull().sum()
    c3=df['dose'].isnull().sum()
    if(c1==0 and c2==0 and c3==0):
        N = len(data.len)
        grp1=data.groupby("supp")
        grp2=data.groupby("dose")
        #Degree of Freedom
        df_a = len(grp1) - 1
        df_b = len(grp2) - 1
        df_ab = df_a*df_b 

        df_w = N - (len(grp1)*len(grp2))

        #Grand Mean
        grand_mean = data['len'].mean()
        #print(grand_mean)

        #Sum of square
        ssq_a=0
        for i in data.supp:
            ssq_a+=(data[data.supp==i].len.mean()-grand_mean)**2
        ssq_b=0
        for i in data.dose:
            ssq_b+=(data[data.dose==i].len.mean()-grand_mean)**2
        #print("ssq_a:",ssq_a,"\nssq_b:",ssq_b)
        ssq_t=0
        for i in data.len:
            ssq_t+=(i-grand_mean)**2
        #print("ssq_t:",ssq_t)
        vc = data[data.supp == 'VC']
        oj = data[data.supp == 'OJ']
        vc_dose_means=[]
        oj_dose_means=[]

        for i in vc.dose:
            vc_dose_means.append(vc[vc.dose==i].len.mean())
        for j in oj.dose:
            oj_dose_means.append(oj[oj.dose==j].len.mean())   
        
        ssq_w = sum((oj.len - oj_dose_means)**2) +sum((vc.len - vc_dose_means)**2)
        #print(vc[vc.dose==i])

        #print("ssq_w:",ssq_w) 
        ssq_ab = ssq_t-ssq_a-ssq_b-ssq_w
        #print("ssq_a:b:",ssq_ab)

        #MEAN SQUARE
        ms_a = ssq_a/df_a
        ms_b = ssq_b/df_b
        ms_ab = ssq_ab/df_ab
        ms_w = ssq_w/df_w

        #F-value
        f_a = ms_a/ms_w
        f_b = ms_b/ms_w
        f_ab = ms_ab/ms_w

        #Creating Table
        table_data={'sum_sq':[ssq_a, ssq_b, ssq_ab, ssq_w],
                   'df':[df_a, df_b, df_ab, df_w],
                   'F':[f_a, f_b, f_ab, np.nan]}
        
        t_dta=pd.DataFrame(table_data,index=['C(supp)','C(dose)',
                                             'C(supp):C(dose)','Residual'])
        print(t_dta)
         