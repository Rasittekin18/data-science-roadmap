# 📚 Data Science & AI Foundations Roadmap

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Scientific-013243?logo=numpy&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?logo=plotly&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4c72b0)
![License](https://img.shields.io/badge/License-MIT-teal)

<br/>

**A step-by-step curriculum and project handbook covering Python Fundamentals, OOP, Data Science (Pandas/NumPy), Interactive Visualization (Seaborn/Plotly), and Statistical Analysis.**  
Developed by **[Raşit Tekin](https://github.com/Rasittekin18)**.

[Müfredat Tablosu](#-müfredat-ve-modüller) • [Kurulum & Çalıştırma](#-kurulum-ve-kullanım) • [Teknolojiler](#-kullanılan-teknolojiler) • [İletişim](#-yazar)

</div>

---

## 📌 Genel Bakış (Overview)

Bu depo; sıfırdan yapay zeka ve veri bilimi kariyerine başlamak isteyenler veya temelleri sağlamlaştırmak için hazırlanmış **adım adım bir yol haritası (roadmap)** ve referans kütüphanesidir:
1. **Python & OOP Temelleri:** Değişkenler, döngüler, hata yönetimi ve Nesne Yönelimli Programlama (OOP).
2. **Uygulamalı OOP Projesi:** Araç kiralama (Rent a Car) simülasyonu ile sınıflar, kalıtım ve metot tasarımı.
3. **Veri Bilimi Çekirdeği:** NumPy ile vektörel hesaplamalar, Pandas ile veri işleme, filtreleme ve temizleme.
4. **Veri Görselleştirme:** Matplotlib, Seaborn ve interaktif Plotly grafikleri, paralel koordinatlar ve nadir görselleştirme araçları.
5. **İstatistiksel Analiz:** Betimsel istatistik, olasılık dağılımları, korelasyon, kovaryans ve aykırı değer (outlier) analizi.

---

## 📂 Müfredat ve Modüller

| # | Modül / Proje | Odak Alanı & İçerik | Kapsam & Araçlar | Klasör Linki |
| :-: | :--- | :--- | :--- | :-: |
| 01 | **Python Programming for AI** | Python sözdizimi, veri tipleri, fonksiyonlar, hata yakalama, NumPy/Pandas temelleri ve OOP mimarisi. | Python 3, OOP, NumPy, Pandas | [`/1-Python_Programming_for_Artificial_Intelligence`](./1-Python_Programming_for_Artificial_Intelligence) |
| 02 | **Data Science Essentials** | Pokemon ve savaş veri setleri üzerinde keşifçi analiz, indeksleme, dilimleme, filtreleme ve eksik veri yönetimi. | Pandas, NumPy, Data Wrangling | [`/2-Data_Science`](./2-Data_Science) |
| 03 | **Advanced Data Visualization** | Dağılım grafikleri, ısı haritaları (heatmaps), interaktif Plotly 3D grafikleri, coğrafi haritalar ve nadir görselleştirme teknikleri. | Matplotlib, Seaborn, Plotly | [`/3-Data_Visualization`](./3-Data_Visualization) |
| 04 | **Statistical Analysis & Probability** | Merkezi eğilim ölçüleri, varyans/standart sapma, normal dağılım, Pearson/Spearman korelasyonu ve hipotez testleri. | Statistics, SciPy, Matplotlib | [`/6-Statistics`](./6-Statistics) |
| 05 | **Rent A Car OOP Project** | Araç ve bisiklet kiralama iş mantığını, envanter yönetimini ve faturalandırmayı yöneten nesne yönelimli Python projesi. | Python Classes, Inheritance, OOP | [`/Rent_a_car_project`](./Rent_a_car_project) |

---

## 🚀 Kurulum ve Kullanım

### 1. Depoyu Klonlayın
```bash
git clone https://github.com/Rasittekin18/data-science-roadmap.git
cd data-science-roadmap
```

### 2. Sanal Ortam Oluşturun
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Gerekli Kütüphaneleri Yükleyin
```bash
pip install numpy pandas matplotlib seaborn plotly scipy jupyter
```

### 4. Modülleri Çalıştırın
```bash
# Jupyter Arayüzü ile Notebook'ları Açma
jupyter notebook

# OOP Rent-a-Car Projesini Çalıştırma
cd Rent_a_car_project
python main.py
```

---

## 🛠️ Kullanılan Teknolojiler

- **Programlama:** Python 3.8+ (Nesne Yönelimli Programlama - OOP)
- **Veri İşleme:** Pandas, NumPy
- **Görselleştirme Kütüphaneleri:** Matplotlib, Seaborn, Plotly Express & Graph Objects
- **İstatistiksel Hesaplama:** SciPy, Statistics
- **Geliştirme Ortamı:** Jupyter Notebook, VS Code

---

## 👨‍💻 Yazar

**Raşit Tekin**  
*Electronics Engineer \| AI & Data Science*  
- GitHub: [@Rasittekin18](https://github.com/Rasittekin18)  
- E-posta: [rasittekin18@gmail.com](mailto:rasittekin18@gmail.com)  
- Konum: İstanbul, Türkiye

---

## 📄 Lisans

Bu repo kapsamındaki tüm içerikler ve kodlar **MIT Lisansı** altında sunulmaktadır.
