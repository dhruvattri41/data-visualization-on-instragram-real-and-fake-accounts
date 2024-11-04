import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


sns.set(style="whitegrid")

np.random.seed(42)  

data = {
    'AccountType': np.random.choice(['Real', 'Fake'], size=200),
    'Followers': np.random.randint(100, 10000, size=200),
    'Following': np.random.randint(50, 5000, size=200),
    'Posts': np.random.randint(1, 300, size=200)
}

df = pd.DataFrame(data)


print(df.head())

plt.figure(figsize=(8, 6))
sns.countplot(x='AccountType', data=df, palette='pastel')
plt.title('Count of Fake vs Real Instagram Accounts', fontsize=16)
plt.xlabel('Account Type', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.show()


plt.figure(figsize=(10, 6))
sns.boxplot(x='AccountType', y='Followers', data=df, palette='pastel')
plt.title('Distribution of Followers by Account Type', fontsize=16)
plt.xlabel('Account Type', fontsize=14)
plt.ylabel('Number of Followers', fontsize=14)
plt.yscale('log')  
plt.show()


plt.figure(figsize=(10, 6))
sns.scatterplot(x='Followers', y='Posts', hue='AccountType', data=df, palette='pastel', alpha=0.7)
plt.title('Followers vs. Posts by Account Type', fontsize=16)
plt.xlabel('Number of Followers', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.xscale('log')  
plt.show()
