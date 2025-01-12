# waterpotabilityproject

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
