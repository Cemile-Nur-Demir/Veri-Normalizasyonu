# PYTHON

Elimizde filmlerin özelliklerini barındıran bir excel dosyası bulunmaktadır. Verimizde FİLM ADI, KATEGORİ, IMDB_PUANI, BAŞROL OYUNCULAR sütunları bulunmaktadır. 

![image](https://github.com/Cemile-Nur-Demir/Veri-Normalizasyonu-Python-/assets/101366821/74b15dd0-5bad-44cf-a1ab-92c0d0d5fbaa)

Veri Normaliasyonu için Uygulanmış Adımlar:
1) Verileri işleyebilmek için normalizasyon işlemi yapmamız gerekmektedir. KATEGORİLER ve BAŞROL OYUNCULAR sütunumuzda birden fazla değer vardır.
2) IMDB_PUANI sütunumuzda verileri 1-10 değer olması gerekirken virgül hatası kaynaklı 1-100 arasındadır.
3) Verinin önemli değerlerinin boş olması durumunda veri doğruluğunu etkilememesi için o filmin veri setinden kaldırılması.
4)Tekrarlanan filmlerin olması durumunda tekrarlan satırın kaldırılma işlemi.
5) Bar plot ile veri görselleştirme.
6) Filmlerin İMDB_PUANI'na göre sıralanması ve bar plot ile görselleştirilmesi.
7) Değişkenlik Ölçülerinin hesaplanması; Varyans, Standart Sapma, Aralık, Mod, Medyan, Basıklık, Çarpıklık
