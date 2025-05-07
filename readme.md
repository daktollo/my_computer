# Oyun ve Steam Projesi

Bu proje, ortaokul ve lise çağındaki öğrencilerin Nesne Yönelimli Programlama (OOP) kavramlarını öğrenmeleri ve pratik yapmaları için hazırlanmıştır. Projede, bilgisayar oyunları ve bir oyun platformu (Steam) simüle edilmiştir. Öğrenciler, oyunların özelliklerini tanımlayabilir ve bu oyunların oluşturulan bilgisayarda çalışıp çalışamayacağını kontrol edebilir.

## Proje Yapısı

Proje aşağıdaki dosya yapısına sahiptir:

```
oyun.py
steam.py
__pycache__/
```

### `oyun.py`

Bu dosyada, bir oyun sınıfı (`Oyun`) tanımlanmıştır. Her oyun, şu özelliklere sahiptir:
- `isim`: Oyunun adı
- `depolama`: Oyunun gerektirdiği depolama alanı (GB)
- `ram`: Oyunun gerektirdiği RAM miktarı (GB)

Örnek kullanım:
```python
cs = Oyun("Counter-Strike", 20, 8)
print(cs.isim)  # Counter-Strike
print(cs.depolama)  # 20
print(cs.ram)  # 8
```

### `steam.py`

Bu dosyada, bir oyun platformu sınıfı (`Steam`) tanımlanmıştır. Platform, oyunları bir liste olarak saklar ve varsayılan oyunları eklemek için bir yöntem içerir.

Örnek kullanım:
```python
steam = Steam()
steam.varsayilan_oyunlari_ekle()
print(steam.oyunlar)  # Varsayılan oyunların listesi
```

## Nasıl Kullanılır?

1. Projeyi çalıştırmak için Python 3.12 veya daha yeni bir sürümünün yüklü olduğundan emin olun.
2. `oyun.py` ve `steam.py` dosyalarını aynı dizinde bulundurun.
3. `steam.py` dosyasını çalıştırarak varsayılan oyunları ekleyebilir ve listeleyebilirsiniz.

## Geliştirme Fikirleri

Bu projeyi genişletmek için aşağıdaki fikirleri uygulayabilirsiniz:
- Bir `Bilgisayar` sınıfı ekleyerek bilgisayarın depolama ve RAM özelliklerini tanımlayın.
- Bir oyun için bilgisayarın yeterli olup olmadığını kontrol eden bir yöntem ekleyin.
- Kullanıcıdan oyun bilgilerini alarak dinamik olarak oyun ekleme özelliği ekleyin.
