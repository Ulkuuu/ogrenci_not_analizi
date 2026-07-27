# Öğrenci Not Analizi 🎓📊

Bu proje, bir öğrenci veri setini (CSV formatında) okuyarak **Pandas**, **NumPy** ve **Matplotlib** kütüphaneleri aracılığıyla veri temizleme, istatistiksel hesaplama ve veri filtreleme işlemleri gerçekleştiren temel bir Python uygulamasıdır.

## 🚀 Özellikler

- **Veri Kontrolü ve Temizleme:** CSV dosyasında eksik sütun olup olmadığını kontrol eder. Sayısal olmayan hatalı verileri temizler ve eksik değerleri (NaN) veri setinden çıkarır.
- **NumPy ile İstatistiksel Analiz:** Sınıfın genel başarı durumunu ölçmek için notlara ait **ortalama**, **medyan** ve **standart sapma** değerlerini hesaplar.
- **Pandas ile Veri Filtreleme:**
  - Sınavdan 80'in üzerinde not alan başarılı öğrencileri listeler.
  - "Yapay Zeka" bölümünde okuyan öğrencileri tespit eder.
  - Yaşı 22'den büyük olan öğrencileri süzer.
- **Görselleştirme:** Matplotlib kullanılarak analiz sonuçlarına dayalı grafik çizimi yapar.

## 📂 Dosya Yapısı

- `not_analiz.py`: Sınıf yapısını (Object-Oriented Programming) temel alan ve tüm analiz işlemlerini yürüten ana Python dosyasıdır.
- `ogrenci_notlari.csv`: Projenin çalışması için gereken örnek veri setidir (İçerisinde `isim`, `yas`, `bolum`, `not` sütunlarını barındırır).

## 🛠️ Kurulum ve Çalıştırma

Projeyi kendi bilgisayarınızda veya yerel ortamınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1. **Projeyi İndirin:**
   Projeyi (repository) bilgisayarınıza zip olarak indirin veya git ile klonlayın. Terminali açarak projenin bulunduğu dizine gidin.

2. **Gerekli Kütüphaneleri Yükleyin:**
   Python ortamınızda projenin bağımlılıklarının yüklü olduğundan emin olun. Yüklü değilse şu komutu çalıştırarak yükleyebilirsiniz:
   ```bash
   pip install pandas numpy matplotlib



   Terminal üzerinden veya kullandığınız IDE (VS Code, PyCharm vb.) aracılığıyla ana kod dosyasını çalıştırın:

      python not_analiz.py
