# 📊 Veri Bilimi ve Yapay Zekâ için İstatistik ve Olasılık

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> Veri bilimi, makine öğrenmesi ve yapay zekânın temelini oluşturan istatistik ve olasılık konularının kısa özeti ve Python uygulamaları.

---

## 📌 İçindekiler

1. [Veri ve Betimsel İstatistik](#1-veri-ve-betimsel-istatistik)
2. [Olasılık](#2-olasılık)
3. [Olasılık Dağılımları](#3-olasılık-dağılımları)
4. [Hipotez Testleri](#4-hipotez-testleri)
5. [ANOVA](#5-anova)
6. [Ki-Kare Analizi](#6-ki-kare-analizi)
7. [Python Kütüphaneleri](#7-python-kütüphaneleri)

---

## 1. Veri ve Betimsel İstatistik

### Ölçüm Ölçekleri

- **Nominal:** Sıralanamayan kategorik veriler. Örn: şehir, göz rengi.
- **Ordinal:** Sıralanabilen kategorik veriler. Örn: eğitim seviyesi.
- **Interval:** Doğal sıfır noktası olmayan veriler. Örn: °C sıcaklık.
- **Ratio:** Doğal sıfır noktası bulunan veriler. Örn: yaş, kilo, gelir.

### Temel Kavramlar

- **Popülasyon:** İncelenen tüm veri kümesi.
- **Örneklem:** Popülasyonu temsil etmek için seçilen veri kümesi.
- **Ortalama:** Değerlerin toplamının gözlem sayısına bölünmesi.
- **Medyan:** Sıralanmış verinin ortasındaki değer.
- **Mod:** En sık tekrar eden değer.
- **Aralık:** `Max - Min`
- **Varyans:** Verilerin ortalamadan sapma düzeyi.
- **Standart Sapma:** Varyansın karekökü.

### Aykırı Değer Tespiti

$$
IQR = Q_3 - Q_1
$$

Alt sınır:

$$
Q_1 - 1.5 \times IQR
$$

Üst sınır:

$$
Q_3 + 1.5 \times IQR
$$

### Korelasyon

- **Kovaryans:** İki değişkenin birlikte değişim yönünü gösterir.
- **Pearson:** Doğrusal ilişkinin yönünü ve gücünü ölçer.
- **Spearman:** Sıralı ve monotonik ilişkileri ölçer.

---

## 2. Olasılık

### Sayma Yöntemleri

**Permütasyon:**

$$
P(n,r)=\frac{n!}{(n-r)!}
$$

**Kombinasyon:**

$$
C(n,r)=\frac{n!}{r!(n-r)!}
$$

### Temel Kavramlar

- Kesişim: `A ∩ B`
- Birleşim: `A ∪ B`
- Tümleyen: `Aᶜ`
- Bağımlı ve bağımsız olaylar
- Koşullu olasılık
- Bayes Teoremi

### Koşullu Olasılık

$$
P(A|B)=\frac{P(A\cap B)}{P(B)}
$$

### Bayes Teoremi

$$
P(A|B)=\frac{P(B|A)P(A)}{P(B)}
$$

---

## 3. Olasılık Dağılımları

### Kesikli Dağılımlar

- **Düzgün Dağılım:** Sonuçların eşit olasılığa sahip olması.
- **Binom Dağılımı:** Belirli sayıdaki denemelerde başarı sayısını modeller.
- **Poisson Dağılımı:** Belirli bir zaman veya alandaki olay sayısını modeller.

### Sürekli Dağılımlar

- **Olasılık Yoğunluk Fonksiyonu (PDF)**
- **Kümülatif Dağılım Fonksiyonu (CDF)**
- **Normal Dağılım**
- **Z-Skoru**

### Z-Skoru

$$
Z=\frac{X-\mu}{\sigma}
$$

### Normal Dağılım

**68–95–99.7 kuralı:**

- %68 → `μ ± 1σ`
- %95 → `μ ± 2σ`
- %99.7 → `μ ± 3σ`

---

## 4. Hipotez Testleri

### Örnekleme Yöntemleri

- Rastgele örnekleme
- Tabakalı örnekleme
- Küme örneklemesi

### Merkezi Limit Teoremi

Örneklem sayısı yeterince büyüdüğünde örneklem ortalamalarının dağılımı yaklaşık olarak normal dağılıma yaklaşır.

### Standart Hata

$$
SE=\frac{\sigma}{\sqrt{n}}
$$

### Hipotez Testi Adımları

1. `H₀` sıfır hipotezi belirlenir.
2. `H₁` alternatif hipotezi belirlenir.
3. Anlamlılık düzeyi `α` seçilir.
4. Test istatistiği hesaplanır.
5. `p-değeri` hesaplanır.
6. Sonuç yorumlanır.

Genel karar:

$$
p\text{-değeri}<\alpha
\Rightarrow H_0\text{ reddedilir}
$$

### Hata Türleri

- **Tip I Hata (α):** Doğru olan `H₀` hipotezinin reddedilmesi.
- **Tip II Hata (β):** Yanlış olan `H₀` hipotezinin reddedilememesi.

### t-Testi ve A/B Testi

- **t-Testi:** İki grubun ortalamalarını karşılaştırmak için kullanılır.
- **A/B Testi:** İki farklı seçeneğin performansını karşılaştırmak için kullanılır.

---

## 5. ANOVA

ANOVA, **ikiden fazla grubun ortalamaları arasında anlamlı fark olup olmadığını** test etmek için kullanılır.

### F İstatistiği

$$
F=
\frac{\text{Gruplar Arası Varyans}}
{\text{Gruplar İçi Varyans}}
$$

Anlamlı fark bulunduğunda hangi grupların farklı olduğunu belirlemek için ek testler uygulanabilir.

---

## 6. Ki-Kare Analizi

Ki-kare testi, özellikle **kategorik değişkenler** arasındaki ilişkileri incelemek için kullanılır.

### Ki-Kare İstatistiği

$$
\chi^2=
\sum\frac{(O-E)^2}{E}
$$

- `O` → Gözlenen değer
- `E` → Beklenen değer

### Kullanım Alanları

- **Uyum İyiliği Testi**
- **Bağımsızlık Testi**

Örnek:

> Eğitim seviyesi ile ürün tercihi arasında anlamlı bir ilişki var mı?

---

## 7. Python Kütüphaneleri

Bu çalışmada aşağıdaki kütüphaneler kullanılmaktadır:

| Kütüphane | Kullanım Alanı |
|---|---|
| **NumPy** | Sayısal hesaplamalar |
| **Pandas** | Veri işleme ve analiz |
| **SciPy** | İstatistiksel testler |
| **Matplotlib** | Veri görselleştirme |
| **Seaborn** | İstatistiksel görselleştirme |

---

## 🎯 Öğrenme Hedefleri

Bu çalışma ile:

- Betimsel istatistik
- Olasılık
- Olasılık dağılımları
- Örnekleme
- Merkezi Limit Teoremi
- Hipotez testleri
- Korelasyon
- t-Testi
- A/B Testi
- ANOVA
- Ki-Kare Testi
- Aykırı değer analizi

konularının öğrenilmesi ve Python ile uygulanması hedeflenmektedir.

---

## 👨‍💻 Geliştirici

**Raşit Tekin**

Elektrik-Elektronik Mühendisi | Yapay Zekâ ve Makine Öğrenmesi

🌐 [rasittekin.com](https://rasittekin.com)  
📧 info@rasittekin.com

---

⭐ Faydalı bulduysanız projeye yıldız vermeyi unutmayın.
