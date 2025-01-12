

# %% Kesifsel Veri Analizi (EDA)

import numpy as np # linear algebra
import pandas as pd # data processing
import seaborn as sns # visualization 
import matplotlib.pyplot as plt # visualization 
import plotly.express as px # visualization 

import missingno as msno  # missing value analysis

from sklearn.tree import DecisionTreeClassifier 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV , 
from sklearn.model_selection import RepeatedStratifiedKFold, train_test_split 
from sklearn.metrics import precision_score, confusion_matrix
from sklearn import tree 

df = pd.read_csv("water_potability.csv")

describe = df.describe() #degerlerimizin temel istatistiksel ozellikleri

df.info()

"""
RangeIndex: 3276 entries, 0 to 3275
Data columns (total 10 columns): 
    
"""

#dependent variable analysis (bagimli degisken analizi)

d = df["Potability"].value_counts().reset_index()
d.columns = ["Potability", "count"]

fig = px.pie(d, values = "count" , names= ["Not Potable", "Potable"], 
             hole =0.35, opacity=0.8, 
             labels = {"label" : "Potability", 
                       "Potability" : "Number of Samples" })

fig.update_layout(title=dict(text = "Pie Chart of Potability Feature"))
fig.update_traces(textposition = "outside", textinfo="percent+label")
fig.show()

fig.write_html("potability_pie_chart.html")


# korelasyon analizi

sns.clustermap(df.corr(), cmap="vlag", dendrogram_ratio = (0.1,0.2), 
               annot = True, linewidths=0.8, figsize=(10,10))
plt.show()


# distribition of features

non_potable = df.query("Potability == 0")
potable = df.query("Potability == 1")

plt.figure()
for ax, col in enumerate(df.columns[:9]):
    plt.subplot(3,3, ax + 1)
    plt.title(col)
    sns.kdeplot(x = non_potable[col],label = "Non Potable")
    sns.kdeplot(x = potable[col],label = "Potable")
    plt.legend()
    
plt.tight_layout()   


# missing value  
msno.matrix(df)
plt.show     ## ph, sulfate ve trihalomethanes 


# %% Veri Ön İşleme Adımı (Preprocessing) , missing value problem, 
#train-test split, normalization

print(df.isnull().sum()) # missing value sayısı 

# sayıları çok fazla olduğu için, bu dağılımları dolduracağız.(ortalamaya göre)

# Eksik değerleri "potability"ye göre ortalama ile doldurmak
# Her grup için ortalamaları hesapla
ph_means = df.groupby('Potability')['ph'].transform('mean')

# Eksik değerleri ortalamalarla doldur
df['ph'] = df['ph'].fillna(ph_means)

print(df['ph'].isnull().sum())  # Çıktı: 0


df["Sulfate"].fillna(value = df["Sulfate"].mean(), inplace= True)
df["Trihalomethanes"].fillna(value = df["Trihalomethanes"].mean(),
                             inplace= True)


# train- test split
X = df.drop("Potability", axis = 1).values # independent degerler
y = df["Potability"].values # target degeri potable or non potable



X_train, X_test, y_train, y_test = train_test_split(X, y , test_size = 0.3, 
                                                    random_state=42)


# min - max normalization 0-1
x_train_max = np.max(X_train)
x_train_min = np.min(X_train)
X_train = (X_train - x_train_min)/(x_train_max - x_train_min)
X_test = (X_test - x_train_min)/(x_train_max - x_train_min)


# %% Modelling

models = models = [("DTC", DecisionTreeClassifier(max_depth=3)), 
                   ["RF", RandomForestClassifier()]]
                   
finalResult = [] #score list
cmList = []  #confusion matrix list    
for name, model in models:
    
    model.fit(X_train, y_train) #training             
                 
    model_result = model.predict(X_test) #prediction

    score = precision_score(y_test, model_result) 
    finalResult.append((name,score))    
    
    cm = confusion_matrix(y_test, model_result)
    cmList.append((name, cm))


print(finalResult)
for name, i in cmList:
    plt.figure()
    sns.heatmap(i, annot=True, linewidths=0.8, fmt= ".0f")
    plt.title(name)
    plt.show





# %% Evulation : decision tree visualization 

dt_clf = models[0][1]

plt.figure(figsize=(25,20))


tree.plot_tree(dt_clf, feature_names = df.columns.tolist()[:-1],
               
                    class_names = ["0","1"],
                    filled = True,
                    precision = 5)
plt.show()


# %% Hyperparameter Tuning: Random Forest

model_params = {
    "Random Forest":
        {
            "model": RandomForestClassifier(),
            "params":
                {
                    "n_estimators": [10,50,100],
                    "max_features" : ["auto","sqrt","log2"],
                    "max_depth" : list(range(1,21,3))
                    }
            }
    
    }

cv = RepeatedStratifiedKFold(n_splits=5, n_repeats=2)
scores = []

for model_name, params in model_params.items():
    
    rs = RandomizedSearchCV(params["model"], params["params"], cv=cv , 
                            n_iter=10)
    rs.fit(X,y)
    scores.append([model_name, dict(rs.best_params_), rs.best_score_])
    

print(scores)

" [['Random Forest', {'n_estimators': 50, 'max_features': 'log2', 
""""'max_depth': 16}, 0.7176470862036866]]"

