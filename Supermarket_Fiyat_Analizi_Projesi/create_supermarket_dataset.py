"""
Süpermarket Fiyat Trendleri & Bütçe Tasarruf Analizi - Gerçekçi Veri Seti Üreteci
Bu script, 12 aylık, 4 farklı marketi, 20 temel tüketim ürününü içeren
gerçekçi piyasa fiyatlarını, fiyat artış trendini ve veri temizleme pratiği
için bilinçli eksik (NaN) / aykırı (outlier) değerleri üretir.
"""

import pandas as pd
import numpy as np
import random

# Tekrarlanabilirlik için tohum
np.random.seed(42)
random.seed(42)

# 1. Tarihler (2024 Yılı 12 Ay)
dates = pd.date_range(start="2024-01-01", end="2024-12-01", freq="MS").strftime("%Y-%m-%d").tolist()

# 2. Ürünler, Kategoriler ve Ocak 2024 Baz Fiyatları (TL)
products = [
    # Süt ve Kahvaltılık
    {"Urun": "Süt (1L)", "Kategori": "Süt & Kahvaltılık", "Baz_Fiyat": 30.0},
    {"Urun": "Beyaz Peynir (500g)", "Kategori": "Süt & Kahvaltılık", "Baz_Fiyat": 110.0},
    {"Urun": "Kaşar Peyniri (400g)", "Kategori": "Süt & Kahvaltılık", "Baz_Fiyat": 135.0},
    {"Urun": "Yumurta (10'lu)", "Kategori": "Süt & Kahvaltılık", "Baz_Fiyat": 42.0},
    {"Urun": "Tereyağı (250g)", "Kategori": "Süt & Kahvaltılık", "Baz_Fiyat": 85.0},
    {"Urun": "Siyah Zeytin (500g)", "Kategori": "Süt & Kahvaltılık", "Baz_Fiyat": 95.0},
    
    # Temel Gıda
    {"Urun": "Ekmek (Adet)", "Kategori": "Temel Gıda", "Baz_Fiyat": 8.0},
    {"Urun": "Ayçiçek Yağı (1L)", "Kategori": "Temel Gıda", "Baz_Fiyat": 48.0},
    {"Urun": "Zeytinyağı (1L)", "Kategori": "Temel Gıda", "Baz_Fiyat": 260.0},
    {"Urun": "Makarna (500g)", "Kategori": "Temel Gıda", "Baz_Fiyat": 16.0},
    {"Urun": "Pirinç (1kg)", "Kategori": "Temel Gıda", "Baz_Fiyat": 52.0},
    {"Urun": "Un (1kg)", "Kategori": "Temel Gıda", "Baz_Fiyat": 22.0},
    {"Urun": "Toz Şeker (1kg)", "Kategori": "Temel Gıda", "Baz_Fiyat": 34.0},
    
    # İçecek
    {"Urun": "Çay (1kg)", "Kategori": "İçecek", "Baz_Fiyat": 140.0},
    {"Urun": "Türk Kahvesi (100g)", "Kategori": "İçecek", "Baz_Fiyat": 32.0},
    {"Urun": "Maden Suyu (6'lı)", "Kategori": "İçecek", "Baz_Fiyat": 28.0},
    
    # Manav
    {"Urun": "Domates (1kg)", "Kategori": "Manav", "Baz_Fiyat": 28.0},
    {"Urun": "Patates (1kg)", "Kategori": "Manav", "Baz_Fiyat": 18.0},
    {"Urun": "Kuru Soğan (1kg)", "Kategori": "Manav", "Baz_Fiyat": 15.0},
    {"Urun": "Elma (1kg)", "Kategori": "Manav", "Baz_Fiyat": 25.0}
]

# Market Fiyat Katsayıları (Piyasa Çarpanları)
# Market_A: Süpermarket Zinciri (Daha geniş ürün yelpazesi, hafif primli)
# Market_B: İndirim Marketi 1 (En uygun fiyat odaklı)
# Market_C: İndirim Marketi 2 (Rekabetçi fiyat)
# Market_D: Hipermarket (Orta-üst segment)
market_multipliers = {
    "Market_A": 1.05,
    "Market_B": 0.95,
    "Market_C": 0.97,
    "Market_D": 1.02
}

rows = []

# Aylık ortalama enflasyon artış faktörü (~%2.5 - %4.0 arası aylık artış)
cumulative_inflation = 1.0

for month_idx, date in enumerate(dates):
    if month_idx > 0:
        monthly_inflation_rate = np.random.uniform(0.025, 0.042)
        cumulative_inflation *= (1.0 + monthly_inflation_rate)
    
    for item in products:
        urun = item["Urun"]
        kategori = item["Kategori"]
        baz = item["Baz_Fiyat"] * cumulative_inflation
        
        row = {
            "Tarih": date,
            "Urun": urun,
            "Kategori": kategori
        }
        
        for m_name, m_mult in market_multipliers.items():
            # Market fiyatında küçük rastgele dalgalanma (+/- %3)
            fluctuation = np.random.uniform(0.97, 1.03)
            price = round(baz * m_mult * fluctuation, 2)
            row[m_name] = price
            
        rows.append(row)

df = pd.DataFrame(rows)

# 3. Bilinçli Olarak Veri Temizleme Pratiği Ekleyelim (Kurs Bölüm 5 paralelinde)
# A) Birkaç eksik değer (NaN) enjekte edelim (yaklaşık 12 adet rastgele hücreye)
for _ in range(12):
    r_idx = np.random.randint(0, len(df))
    m_col = np.random.choice(["Market_A", "Market_B", "Market_C", "Market_D"])
    df.loc[r_idx, m_col] = np.nan

# B) 2 adet bariz Aykırı Değer (Outlier / Veri Giriş Hatası) ekleyelim (Tukey IQR testi için)
# Hata 1: 35 TL yerine 950 TL yazılmış bir ürün
df.loc[15, "Market_A"] = 950.0
# Hata 2: 120 TL yerine 12.0 TL yazılmış eksik basamaklı bir ürün
df.loc[45, "Market_C"] = 12.0

# CSV Olarak Kaydet
output_filename = "supermarket_data.csv"
df.to_csv(output_filename, index=False, encoding="utf-8")
print(f"Başarılı! '{output_filename}' dosyası oluşturuldu.")
print(f"Toplam Satır: {len(df)}, Toplam Sütun: {len(df.columns)}")
print("Sütunlar:", list(df.columns))
print("İlk 3 Satır:")
print(df.head(3))
