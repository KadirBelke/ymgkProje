
Zonguldak ilinin veri setini kullanılarak Yapay Sinir Ağı modeli uygulanmıştır. Model kullanılmadan önce elimizde bulunan SO2, PM10, NO2 ve CO değerlerinin hesaplanması ile Hava Kitle İndeksi belirlenmiştir. Belirlenen bu değer verisetimizin değer sınıfı olmuştur. Daha model kullanılarak verisetinin %80’ni eğitim verisi ve %20’si test verisi olarak ayrılmıştır. Bu işlem için Python’da Keras kütüphanesi kullanılmıştır.

Daha sonra belirlenen eğitim ve test verileri Yapay sinir ağı modeline uygulanmıştır. Eğitimin ardından %96 eğitim başarımı ve %91 test başırımı elde edilmiştir.

![](/screenshot/chart.png)

![](/screenshot/result.png)
