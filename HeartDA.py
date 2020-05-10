import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn  as sns

df = pd.read_csv(r"C:\Users\wangrg\Desktop\heartdisease\heart.csv")
# print(df.head(10))
# print(df.info())
print(df.describe())
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(),annot=True,cmap='YlGnBu',fmt='.2f',linewidths=2)
plt.show()
print(df['target'].value_counts())
sns.distplot(df['age'],color='red')
plt.show()

fig,ax=plt.subplots(figsize=(24,6))
plt.subplot(1, 3, 1)
age_bins = [20,30,40,50,60,70,80]
df['bin_age']=pd.cut(df['age'], bins=age_bins)
g1=sns.countplot(x='bin_age',data=df ,hue='target',palette='plasma')
g1.set_title("Age vs Heart Disease")

fig,ax=plt.subplots(figsize=(16,6))
plt.subplot(121)
s1=sns.boxenplot(x='sex',y='age',hue='target',data=df,palette='YlGn')
s1.set_title("Figure 1")

fig,ax=plt.subplots(figsize=(24,6))
plt.subplot(131)
x1=sns.countplot(x='cp',data=df,hue='target',palette='spring')
x1.set_title('Chest pain type')

fig,ax=plt.subplots(figsize=(16,6))
sns.pointplot(x='age',y='cp',data=df,color='Lime',hue='target')
plt.title('Age vs Cp')

fig,ax=plt.subplots(figsize=(24,6))
plt.subplot(1, 3, 2)
cho_bins = [100,150,200,250,300,350,400,450]
df['bin_chol']=pd.cut(df['chol'], bins=cho_bins)
g2=sns.countplot(x='bin_chol',data=df,hue='target',palette='plasma')
g2.set_title("Cholestoral vs Heart Disease")

fig,ax=plt.subplots(figsize=(24,6))
plt.subplot(1, 3, 3)
thal_bins = [60,80,100,120,140,160,180,200,220]
df['bin_thalach']=pd.cut(df['thalach'], bins=thal_bins)
g3=sns.countplot(x='bin_thalach',data=df,hue='target',palette='plasma')
g3.set_title("Thalach vs Heart Disease")

fig,ax=plt.subplots(figsize=(16,6))
sns.lineplot(y='thalach',x='age',data=df,hue="target",style='target',palette='magma',markers=True, dashes=False,err_style="bars", ci=68)
plt.title('Age vs Thalach')

sns.pointplot(x='sex',y='thal',data=df,hue='target',markers=["o", "x"],linestyles=["-", "--"],capsize=.2,palette='coolwarm')

fig,ax=plt.subplots(figsize=(24,6))
plt.subplot(133)
x3=sns.countplot(x='slope',data=df,hue='target',palette='spring')
x3.set_title('slope of the peak exercise ST segment')