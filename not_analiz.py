import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class OgrenciNotAnalizi:
    def __init__(self, csv_dosyasi):
        self.csv_dosyasi = csv_dosyasi
        self.df = pd.read_csv(csv_dosyasi)

    def not_analizi(self):
        try:
            self.df = pd.read_csv(self.csv_dosyasi)
            
            gerekli_sütunlar = ['isim', 'yas', 'bolum', 'not']
            if not all(sutun in self.df.columns for sutun in gerekli_sütunlar):
                print("CSV dosyasında gerekli sütunlar bulunamadı.")
                return

            self.df['not'] = pd.to_numeric(self.df['not'], errors='coerce')
            print("Not sütunu sayısal değerlere dönüştürüldü.")
            print(self.df['not'].describe())
            
            self.df.dropna(subset=['not'], inplace=True)
            
        except FileNotFoundError:
            print("CSV dosyası bulunamadı.")
        except Exception as e:
            print(f"Bir hata oluştu: {e}")

    def numpy_ilehesapla(self):
        try:
            notlar = self.df['not'].to_numpy()
            ortalama = np.mean(notlar)
            medyan = np.median(notlar)
            std_sapma = np.std(notlar)

            print(f"Ortalama: {ortalama}")
            print(f"Medyan: {medyan}")
            print(f"Standart Sapma: {std_sapma}")

        except Exception as e:
            print(f"Bir hata oluştu: {e}")

    def pandas_ilefiltreleme(self):
        try:
            filtrelenmis_df = self.df[self.df['not'] > 80]
            print("80'den büyük notlar:")
            print(filtrelenmis_df)
                  
            yapayzekaoregncileri = self.df[self.df['bolum'].str.contains('Yapay Zeka', case=False, na=False)]
            print("Yapay Zeka bölümü öğrencileri:") 
            print(yapayzekaoregncileri)

            yasi_22_buyuk_ogrenciler = self.df[self.df['yas'] > 22]
            print("Yaşı 22'den büyük öğrenciler:")
            print(yasi_22_buyuk_ogrenciler)

        except Exception as e:
            print(f"Bir hata oluştu: {e}")



    def grafik_ciz(self):
        try:
            plt.hist(self.df['not'], bins=10, edgecolor='black')
            plt.title('Öğrenci Not Dağılımı')
            plt.xlabel('Notlar')
            plt.ylabel('Öğrenci Sayısı')
            plt.grid(axis='y', alpha=0.75)
            plt.show()
        except Exception as e:
            print(f"Bir hata oluştu: {e}")

    def tum_analizleri_yap(self):
        self.not_analizi()
        if self.df is  None :
            print("analiz durdurdu çünkü CSV dosyası yüklenemedi veya gerekli sütunlar eksik.")
            return
        self.numpy_ilehesapla()
    
        self.pandas_ilefiltreleme()

        self.grafik_ciz()
if __name__ == "__main__":
    csv_dosyasi = "ogrenci_notlari.csv"
    analiz = OgrenciNotAnalizi(csv_dosyasi)
    analiz.tum_analizleri_yap()
