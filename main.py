import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn as ml
import statistics as st
import scipy.stats as ss


xlsx = pd.ExcelFile('imdb_veri_excel_ham.xlsx') # exceldeki verileri okuyup değişkene attık
df = pd.read_excel(xlsx) # verileri dataframe'e attık
#print(df.columns) #Sütun adlarını görmek için 
df[['KATEGORİ1', 'KATEGORİ2','KATEGORİ3']] = df['KATEGORİ'].str.split(',', n=2, expand=True )
df[['BAŞROL1', 'BAŞROL2']] = df['BAŞROL OYUNCULAR'].str.split(',', n=1, expand=True )
df = df.dropna(subset=['KATEGORİ'], how='all') # Boş sütunlara sahip satırları kaldırdık
df = df.dropna(subset=['BAŞROL1','BAŞROL2'], how='all')
df = df.dropna(subset=['IMDB_PUANI'], how='all')
df = df.dropna(subset=['KATEGORİ','BAŞROL1','BAŞROL2', 'IMDB_PUANI'], how='all')

# Tekrar eden satırları kaldırma
df.drop_duplicates(inplace=True)

# Hatalı değeri düzeltmek için döngü kullanma
for i in range(len(df)):
    deger = df.loc[i, 'IMDB_PUANI']
    if deger > 10:  # Hatalı değeri kontrol etmek için örneğin 10'dan büyükse düzelt
        df.loc[i, 'IMDB_PUANI'] = deger / 10

df.to_excel('veriler.xlsx', index=False) # Düzeltme yapıldıktan sonra dataframe'i kaydetme
print(df) 

film_adlari = df['FİLM ADI'].astype(str)
imdb_puanlari = df['IMDB_PUANI'].astype(str) #imdb puanıın veri tipini str'ye çevir
#Bar çubuğunda verileri görselleştirme
fig, ax = plt.subplots()
ax.bar(imdb_puanlari,film_adlari)
ax.set_ylabel('Film Adları')
ax.set_xlabel('İmdb Puanları')
plt.show()

imdb_puanlari = df['IMDB_PUANI'].astype(float) 
print('\n')
print('Fimlerin İmdb Puan MODU = ',st.mode(df.IMDB_PUANI),'\n')
print('Fimlerin İmdb Puan MEDYANI = ',st.median(df.IMDB_PUANI),'\n')
print('Fimlerin İmdb Puan MERKEZİ EĞİLİM ÖLÇÜLERİ =','\n',imdb_puanlari.describe(),'\n') 


print('Fimlerin İmdb Puan VARYANSI= ',st.variance(df.IMDB_PUANI),'\n')
print('Fimlerin İmdb Puan STANDART SAPMASI= ',st.stdev(df.IMDB_PUANI),'\n')
print('Fimlerin İmdb Puan ARALIĞI= ',np.ptp(df.IMDB_PUANI),'\n')


carpiklik=ss.skew(df.IMDB_PUANI)
print("IMDB PUAN ÇARPIKLIK",carpiklik,'\n')
if (-0.5<carpiklik<0.5):
    print("simetrik",'\n')
elif carpiklik<0:
    print("sola çarpık",'\n')
elif carpiklik:
    print("sağa çarpık",'\n')

basiklik = ss.kurtosis(df.IMDB_PUANI)
print("IMDB PUAN BASIKLIK",basiklik,'\n')
if(-1<basiklik<1):
    print("normal dağılım",'\n')
elif basiklik>0:
    print("sivri dağılım",'\n')
elif basiklik<0:
    print("basık dağılım",'\n')

df_sorted = df.sort_values(by=['IMDB_PUANI'], ascending=True) # dataframe'i IMDB PUANI sütununa göre küçükten büyüğe doğru sıraladı

df_sorted.to_excel('veriler.xlsx', index=False) # sıralanan dataframe'i veriler adlı excel dosyasıne kaydetti
veriler_okudu = pd.read_excel('veriler.xlsx')  # verileri "veriler.xlsx" dosyasından okudu

#Sıralanmış veriyi bar çubuğunda verileri görselleştirme
film_adlari1 = df_sorted['FİLM ADI'].astype(str)
imdb_puanlari1 = df_sorted['IMDB_PUANI'].astype(str) #imdb puanıın veri tipini str'ye çevir
fig1, ax1 = plt.subplots()
ax1.bar(imdb_puanlari1,film_adlari1)
ax1.set_ylabel('Film Adları')
ax1.set_xlabel('İmdb Puanları')
plt.ylim()  
plt.xlim()
plt.show()

#histogram
plt.hist(imdb_puanlari1, bins=69, edgecolor='black')  # histogramı çizdirin
plt.xlabel('IMDB Puanı')
plt.ylabel('Frekans')
plt.title('IMDB Puanı Dağılımı')
plt.ylim(0, 5)  # frekans sınırı
plt.show()




