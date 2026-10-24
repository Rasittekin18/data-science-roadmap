Araç Kiralama Sistemi (Vehicle Rental System)

Python ile geliştirilmiş, terminal tabanlı bir araç kiralama uygulamasıdır.
Kullanıcılar saatlik veya günlük olarak araba/bisiklet kiralayabilir, stok kontrolü yapılır ve iade sonrası fatura hesaplanır.

- Özellikler

      Bisiklet kiralama

      Araba kiralama

      Saatlik ve günlük kiralama seçenekleri

      Stok takibi

      Araç iade ve fatura oluşturma

      Araç sayısına göre indirim

      Kullanıcı giriş kontrolü

      Menü tabanlı terminal uygulaması



- Kullanılan OOP Yapısı

      Proje Nesne Tabanlı Programlama prensipleriyle geliştirilmiştir.

- Kullanılan sınıflar:

          - VehicleRent (Ana sınıf)
          
          stok yönetimi
          
          kiralama zamanı kaydı
          
          saatlik ve günlük kiralama
          
          fatura hesaplama
          
          - CarRent (Alt sınıf)
          
          VehicleRent’ten miras alır
          
          %15 indirim hesaplama fonksiyonu içerir
          
          - BikeRent (Alt sınıf)
          
          VehicleRent’ten miras alır
          
          - Customer
          
          müşteri araç talebi
          
          kiralama/iade bilgilerinin saklanması

- Fiyatlandırma


| Araç     | Saatlik | Günlük |
| -------- | ------- | ------ |
| Bisiklet | $5      | $84    |
| Araba    | $10     | $192   |



- Fatura ve İndirim Mantığı

      Kiralama süresi “datetime” ile hesaplanır
      
      Günlük/saatlik ücret süreye göre çarpılır
      
      Araç sayısına göre otomatik indirim yapılır
      
      - İndirim koşulları:
      
      Araba → en az 2 adet kiralama: %20 indirim
      
      Bisiklet → en az 4 adet kiralama: %20 indirim


- Çalıştırma

      Terminalde proje klasörüne gelip komutu çalıştırın:
      python main.py


- Projenin Öğrettikleri

      Bu projeyi inceleyerek şu konular öğrenilebilir:
      
      inheritance (miras alma)
      
      kapsülleme ve sınıf yapısı
      
      method overriding
      
      datetime ile zaman hesaplama
      
      kullanıcı giriş doğrulama (input kontrolü)
      
      terminal menü tasarımı
      
      gerçek fatura hesaplama mantığı


![Araç kiralama proje ekran görüntüsü](https://github.com/Rasittekin18/Rent_a_car_project/blob/main/Screenshot_2.jpg)
