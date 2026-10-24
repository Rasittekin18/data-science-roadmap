# 🛒 Süpermarket Fiyat Trendleri & Bütçe Tasarruf Analizi (To-Do & Uygulama Planı)

Bu proje, **Data Science ve Python Sıfırdan Uzmanlığa Veri Bilimi** kursunda öğrenilen tüm tekniklerin gerçek hayata uyarlandığı, **uçtan uca dinamik bir veri bilimi projesidir**.

---

## 🎯 Projenin Temel İlkeleri

1. **Hazır Veri Seti Desteği:** Varsayılan olarak 12 aylık, 4 farklı marketi, 20 temel tüketim ürününü ve gerçekçi fiyat trendlerini içeren zengin bir veri seti (`supermarket_data.csv`) kullanılır.
2. **Dinamik & Tak-Çalıştır Mimari (Plug & Play):** Başka bir kullanıcı kendi verisini (örneğin kendi fiş/market listesini) getirdiğinde kodları değiştirmek zorunda kalmaz; tek bir `CONFIG` sözlüğü üzerinden kendi sütun isimlerini tanımlayarak tüm analiz hattını çalıştırabilir.
3. **Format Esnekliği:** Kullanıcının verisi ister geniş formatta (marketler sütunlarda: `Migros`, `BIM`, `A101`), ister uzun/düzenli formatta (`Market`, `Fiyat`) olsun; sistem bunu otomatik algılar ve Tidy formata dönüştürür.

---

## 📌 Canlı İlerleme Takip Listesi (To-Do List)

Her aşama tamamlandıkça bu liste güncellenerek işaretlenecektir (`[x]`).

- [x] **Aşama 1: Dinamik Veri Altyapısı & Hazır Veri Seti Oluşturma**
  - [x] 12 aylık, 4 marketli, 20 ürünlü gerçekçi veri üretecinin hazırlanması (`create_supermarket_dataset.py`).
  - [x] Kursa uygun eksik değerler (`NaN`) ve aykırı değerler (`outliers`) içeren `supermarket_data.csv` dosyasının üretilmesi.
  - [x] Dinamik kullanıcı yapılandırma sözlüğünün (`CONFIG`) tanımlanması.

- [x] **Aşama 2: Veri Yükleme, Muayene & Tip Dönüşümleri (Diagnose Data)**
  - [x] Verinin dinamik fonksiyon ile yüklenmesi (`pd.read_csv`).
  - [x] İlk muayene araçları: `head()`, `tail()`, `info()`, `shape`, `describe()`.
  - [x] Tarih sütununun `pd.to_datetime()` ile dönüştürülmesi.
  - [x] Metin sütunlarının (`Kategori`, `Market`, `Urun`) `astype('category')` yapılarak bellek optimizasyonu (%52.2 tasarruf).

- [x] **Aşama 3: Otomatik Format Dönüştürücü (Tidy Data - Melt/Pivot) & Eksik Veri Yönetimi**
  - [x] Geniş format kontrolü: Market sütunları yataysa `pd.melt()` ile dikey uzun formata çekme (240x7 -> 960x5).
  - [x] Eksik fiyatların tespiti (12 adet NaN değer bulundu).
  - [x] Eksik fiyatların aynı ürün ve ayın medyanı ile dinamik doldurulması (`fillna` & `transform('median')`).
  - [x] `assert` ifadeleriyle veri bütünlüğünün otomatik doğrulanması (`assert df['Fiyat'].notnull().all()`).

- [x] **Aşama 4: Aykırı Değer (Outlier) Dedektörü (Tukey IQR Metodu)**
  - [x] Ürün bazında $IQR = Q3 - Q1$ ve $1.5 \times IQR$ adım formülü ile alt/üst sınır tespiti.
  - [x] Kutu grafikleri (`boxplot`) ile 950 TL ve 12 TL gibi hatalı uç fiyatların görselleştirilmesi.
  - [x] Hatalı fiyatların o ürünün ve ayın gerçekçi medyanı ile ikame edilerek temizlenmesi (0 aykırı değer kaldı).

- [x] **Aşama 5: Fonksiyonel Araçlar & Dinamik Sepet Tanımlama (Feature Engineering)**
  - [x] Kullanıcı tanımlı fonksiyonlar (`def`), docstring ve `lambda` ile KDV/Birim Fiyat hesaplaması (`KDV_Dahil_Fiyat`).
  - [x] Titanic projesi tarzı metin madenciliğiyle ürün adından birim/ambalaj ayıklama (`Birim`).
  - [x] Koşullu List Comprehension ile piyasa durumuna göre fiyat seviyesi etiketleme (`Pahalı` / `Ortalama` / `Uygun`).
  - [x] Kullanıcının `PROJECT_CONFIG["target_basket"]` içinde belirlediği "Temel Tüketim Sepeti"nin filtrelenmesi (`Sepette_Mi`).

- [x] **Aşama 6: Zaman Serisi & Sepet Fiyat Değişim Analizi (Time Series & Resampling)**
  - [x] Tarih sütununun `DatetimeIndex` yapılması ve çeyrek dilimleme (`time slicing`).
  - [x] Aylık bazda yeniden örnekleme (`resample('MS').mean()`) ve aylık artış oranı (`pct_change`).
  - [x] Market bazında aylık toplam sepet maliyetlerinin çıkarılması (`groupby` & `unstack`).
  - [x] Ocak 2024 baz fiyatına göre kümülatif sepet fiyat artış trendi (%) hesaplaması (Piyasa geneli %43.7 artış).

- [x] **Aşama 7: Görsel Keşifsel Veri Analizi (Visual EDA)**
  - [x] **Line Plot:** 12 aylık sepet tutarı ve fiyat trend eğrisi.
  - [x] **Korelasyon Haritası (`sns.heatmap`):** Marketlerin fiyat hareketlerinin birbiriyle korelasyonu.
  - [x] **Bar Plot:** En ucuzdan en pahalıya market ve kategori liderlik tablosu.
  - [x] **Histogram (PDF & CDF):** Fiyat dağılımının kümülatif olasılık eğrileri.

- [x] **Aşama 8: İleri Tablo Raporlama (Pivot, MultiIndex, Groupby) & Karar Raporu**
  - [x] `pivot_table()` ve `unstack()` ile Market $\times$ Kategori fiyat matrisi.
  - [x] `groupby(['Kategori', 'Market'])` ile detaylı istatistiksel özet (`min`, `mean`, `max`).
  - [x] **Sonuç Raporu:** "Hangi marketten ne alınmalı? En çok hangi kategoride fiyat artışı gerçekleşti? Tasarruf rehberi" karar önerileri.

---

## 🛠️ Dinamik Kullanıcı Yapılandırma Şablonu (Config)

Başka bir kullanıcı projeyi kendi CSV dosyasıyla çalıştırmak istediğinde sadece aşağıdaki parametreleri güncelleyecektir:

```python
PROJECT_CONFIG = {
    # 1. Veri Dosyası Yolu
    "file_path": "supermarket_data.csv",
    
    # 2. Sütun Eşlemeleri (Kullanıcının kendi CSV sütun isimleri)
    "columns": {
        "date": "Tarih",          # Tarih içeren sütun adı
        "product": "Urun",        # Ürün adı sütunu
        "category": "Kategori",   # Ürün kategorisi
        "price": "Fiyat",         # Fiyat sütunu (Uzun format için)
        "market": "Market"        # Market adı sütunu (Uzun format için)
    },
    
    # 3. Eğer veri geniş formatta ise (Marketler ayrı sütunlardaysa):
    "is_wide_format": True,
    "market_columns": ["Market_A", "Market_B", "Market_C", "Market_D"],
    
    # 4. Enflasyon Analizinde Takip Edilecek Özel Sepet Ürünleri
    "target_basket": [
        "Süt (1L)",
        "Yumurta (10'lu)",
        "Ekmek (Adet)",
        "Zeytinyağı (1L)",
        "Beyaz Peynir (500g)",
        "Domates (1kg)"
    ]
}
```

---

## 🚀 Proje Dosya Yapısı

* `SUPERMARKET_PROJECT_PLAN_AND_TODO.md`: Bu plan ve canlı ilerleme dosyası.
* `create_supermarket_dataset.py`: Gerçekçi sentetik veri üreteci script'i.
* `supermarket_data.csv`: Projede çalışacağımız hazır market veri seti.
* `Supermarket_Inflation_Analysis.ipynb`: Adım adım uygulayacağımız ana Jupyter Notebook.
