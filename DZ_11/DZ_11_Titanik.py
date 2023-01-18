#!/usr/bin/env python
# coding: utf-8

# In[34]:


import numpy as np
import pandas as pd
from IPython import get_ipython
from pandas import Series, DataFrame
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[35]:


df = pd.read_csv('/DZ_11/train.csv')


# In[36]:


df


# In[37]:


df.head()


# In[38]:


df.columns


# In[39]:


df.info()


# In[40]:


df.groupby('Pclass')['Pclass'].count()


# In[42]:


fg = sns.factorplot('Pclass', data=df, kind='count', aspect=1.5)
fg.set_xlabels('Class')


# In[44]:


df.groupby('Sex')['Sex'].count()


# In[45]:


sns.factorplot('Sex', data=df, kind='count', aspect=1.5)


# In[46]:


df.groupby(['Sex', 'Pclass'])['Sex'].count()


# In[47]:


g = sns.factorplot('Pclass', data=df, hue='Sex', kind='count', aspect=1.75)
g.set_xlabels('Class')


# In[48]:


titanic_df.pivot_table('Survived', 'Sex', 'Pclass', aggfunc=np.sum, margins=True)


# In[51]:


not_survived = df[df['Survived']==0]


# In[53]:


sns.factorplot('Survived', data=df, kind='count')


# In[54]:


len(not_survived)


# In[55]:


not_survived.pivot_table('Survived', 'Sex', 'Pclass', aggfunc=len, margins=True)


# In[57]:


table = pd.crosstab(index=[df.Survived, df.Pclass], columns=[df.Sex,df.Embarked])

table.unstack()


# In[66]:


table.columns,table.index


# In[67]:


table.columns.set_levels(['Female', 'Male'], level=0, inplace=True)
table.columns.set_levels(['Cherbourg','Queenstown','Southampton'], level=1, inplace=True)
table


# In[69]:


age = df['Age'].dropna()


# In[70]:


age_dist = sns.distplot(age)
age_dist.set_title("Distribution of Passengers' Ages")


# In[72]:


df['Age'].hist(bins=50)


# In[74]:


df['Parch'].dtype, df['SibSp'].dtype, len(df.Cabin.dropna())


# In[76]:


def male_female_child(passenger):
    age, sex = passenger
    
    if age < 16:
        return 'child'
    else:
        return sex


df['person'] = df[['Age', 'Sex']].apply(male_female_child, axis=1)


# In[78]:


df[:10]


# In[88]:


sns.catplot('Pclass', data=df, kind='count', hue='person', order=[1,2,3], 
               hue_order=['child','female','male'], aspect=2)


# In[89]:


df['person'].value_counts()


# In[91]:


sns.catplot('Pclass', data=df, kind='count', hue='person', col='Survived', order=[1,2,3], 
               hue_order=['child','female','male'], aspect=1.25, size=5)


# In[93]:


fig = sns.FacetGrid(df, hue='Sex', aspect=4)
fig.map(sns.kdeplot, 'Age', shade=True)
oldest = df['Age'].max()
fig.set(xlim=(0,oldest))
fig.set(title='Распределение возраста по полу')
fig.add_legend()


# In[94]:


fig = sns.FacetGrid(df, hue='person', aspect=4)
fig.map(sns.kdeplot, 'Age', shade=True)
oldest = df['Age'].max()
fig.set(xlim=(0,oldest))
fig.add_legend()


# In[95]:


fig = sns.FacetGrid(df, hue='Pclass', aspect=4)
fig.map(sns.kdeplot, 'Age', shade=True)
oldest = df['Age'].max()
fig.set(xlim=(0,oldest))
fig.set(title='Распределение возраста, сгруппированного по классам')
fig.add_legend()


# ### Из приведенного выше графика видно, что класс 1 имеет нормальное
# распределение. Однако классы 2 и 3 имеют искаженное распределение в
# сторону пассажиры 20 и 30 лет.

# In[97]:


deck = df['Cabin'].dropna()
deck.head()


# In[98]:


d = []
for c in deck:
    d.append(c[0])


# In[ ]:


d[0:10]


# In[99]:


['C', 'C', 'E', 'G', 'C', 'D', 'A', 'C', 'B', 'D']


# In[103]:


from collections import Counter
Counter(d)

Counter({'C': 59, 'B': 47, 'D': 33, 'E': 32, 'A': 15, 'F': 13, 'G': 4, 'T': 1})


# In[106]:


cabin_df = DataFrame(d)
cabin_df.columns=['Cabin']
sns.catplot('Cabin', data=cabin_df, kind='count', order=['A','B','C','D','E','F','G','T'], aspect=2, 
              palette='winter_d')


# In[107]:


cabin_df = cabin_df[cabin_df['Cabin'] != 'T']


# In[108]:


sns.factorplot('Cabin', data=cabin_df, kind='count', order=['A','B','C','D','E','F','G'], aspect=2, 
              palette='Greens_d')


# In[109]:


url = 'http://matplotlib.org/api/pyplot_summary.html?highlight=colormaps#matplotlib.pyplot.colormaps'
import webbrowser
webbrowser.open(url)


# ### Откуда взялись пассажиры, т.Е. Откуда пассажиры попали на корабль?

# In[111]:


sns.catplot('Embarked', data=df, kind='count', hue='Pclass', hue_order=range(1,4), aspect=2,
              order = ['C','Q','S'])


# #### Из приведенного выше рисунка можно сделать вывод, что почти все пассажиры, которые сели из Квинстауна, были в третьем классе. С другой стороны, многие, кто прилетел из Шербура, были в первом классе. Самая большая часть пассажиров кто сел на корабль, прибыл из Саутгемптона, в котором 353 пассажира были в третьем классе, 164 во втором классе и 127 пассажиров были в первом классе. В таких случаях, возможно, потребуется взглянуть на экономическую ситуацию в этих разных городах в тот период времени, чтобы понять, почему большинство пассажиров, которые садились из Квинстауна, были, например, в третьем классе.

# In[113]:


df.Embarked.value_counts()


# In[115]:


port = pd.crosstab(index=[df.Pclass], columns=[df.Embarked])
port.columns = [['Cherbourg','Queenstown','Southampton']]


port


# # Конец xD
