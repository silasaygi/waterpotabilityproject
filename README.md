# Water Potability Project

I worked on a machine learning project to analyze and classify water quality. This project aims to classify potable and non-potable water samples by examining different water parameters.

This project is a project prepared by our instructor Kaan Can Yılmaz from the "Applied Based Machine Learning" training on the "Turkcell Geleği Yazanlar" platform, which I am currently continuing.

Project details:

🔍 Data Analysis and Pre-Processing:

Dataset Features: It consists of 10 columns containing water quality parameters such as pH, Hardness, Solids, Chloramines.

We filled the missing data problem with average values ​​by dividing them into groups based on the target variable "Potability".

We determined the relationships between the parameters by performing correlation analyzes and distribution examinations on the data.

🌳 Machine Learning Models :

We performed modeling using Decision Tree and Random Forest algorithms.

We evaluated the performance of each model with precision score and confusion matrix.

🎯 Hyperparameter Optimization :

We performed hyperparameter optimization for the Random Forest model. We obtained the best results using RandomizedSearchCV and RepeatedStratifiedKFold with the following parameters: n_estimators, max_features, max_depth .

🚀 As a result, the model performed best with 71.7% accuracy.

Dataset link used : https://www.kaggle.com/datasets/adityakadiwal/water-potability


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Water Potability Project

Su kalitesini analiz edip sınıflandırmaya yönelik bir makine öğrenimi Projesi üzerinde çalıştım. Bu proje, farklı su parametrelerini inceleyerek içilebilir (potable) ve içilemez (non-potable) su örneklerini sınıflandırmayı amaçlıyor. 


Bu proje, şuan devam etmekte olduğum Turkcell Geleceği Yazanlar platformunda bulunan "Uygulamalı Tabanlı Makine Öğrenimi" eğitiminden, Kaan Can Yılmaz  hocamızın hazırlamış olduğu bir projedir. 


Proje detayları : 



🔍 Veri Analizi ve Ön İşleme :


Veri Seti Özellikleri:  pH, Sertlik (Hardness), Katı Maddeler (Solids), Kloraminler (Chloramines) gibi su kalitesi parametrelerini içeren 10 sütundan oluşuyor.

Eksik veri problemini, hedef değişken olan "Potability" üzerinden gruplara ayırarak ortalama değerlerle doldurduk.

Veriler üzerinde korelasyon analizleri ve dağılım incelemeleri yaparak parametreler arasındaki ilişkileri belirledik.



🌳 Makine Öğrenimi Modelleri :  

Karar Ağacı (Decision Tree) ve Random Forest algoritmalarını kullanarak modelleme yaptık.

Her modelin performansını, precision score ve confusion matrix ile değerlendirdik. 



🎯 Hiperparametre Optimizasyonu :

Random Forest modeli için hiperparametre optimizasyonu gerçekleştirdik. En iyi sonuçları, RandomizedSearchCV ve RepeatedStratifiedKFold kullanarak şu parametrelerle elde ettik :  n_estimators, max_features, max_depth .

🚀 Sonuç olarak model, %71.7 doğrulukla en iyi performansı sergiledi. 



Kullanılan veri seti linki : https://www.kaggle.com/datasets/adityakadiwal/water-potability
