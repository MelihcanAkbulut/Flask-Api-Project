# Malware Baazar API Project

## Proje Ayrıntıları

* Projenin amacı, aşağıda linki verilen bazaar.abuse.ch sitesindeki hashleri parse edip veritabanına kaydetmek ve kullanıcı istekte bulunduğunda veritabanındaki bu bilgileri kullanıcıya döndürmektir.
* Proje API altyapısında olacak ve döndürdüğü bilgiler JSON formatında olacak.
* MD5 hashleri kontrol edilecek (1. link) ve veritabanında olmayan hashlerin ayrıntıları 2. linkten çekilerek veritabanına kaydedilecek. Kullanıcı  POST isteği attığında güncelleme arka planda başlayacak ve güncellemenin başladığına dair kullanıcıya bilgi döndürülecek.
* GET metoduyla hash bilgileri çekildiğinde sayfalama ve search özelliği olması tercih edilir. 
* Proje katmanlı mimaride yazılacak. Business kodları (günceleme yapan ve database CRUD işlemleri yapan kodlar) ayrı bir dosyada yazılacak, Flask kodları ile karıştırılmayacak. Ayrıca database tablolarının olduğu kısım da ayrı bir dosyaya yazılacak.

## Linkler

- Recent MD5 Hashes : https://bazaar.abuse.ch/export/txt/md5/recent/
- MD5 Information API Endpoint : https://bazaar.abuse.ch/api/#query_hash 
    - İlgili endpoint şu başlık altında bulunabilir : "Query a malware sample (hash)"

## Endpointler

* `GET api/v1/malware` : Veritabanındaki tüm malware bilgilerini döndürür.
* `POST api/v1/malware` : Kaynakları tarayarak yeni malware varsa veritabanına kaydeder.
* `GET api/v1/malware/<id>` : ID'si verilen malware bilgisini döndürür. 
* `DELETE api/v1/malware/<id>` : ID'si verilen malware kaydını veritabanından siler. 
* `GET api/v1/malware/count` : Veritabanındaki malware kaydı sayısını döndürür.

## Database Tablo İçeriği

* Yukarıdaki linklerden (2. link) gelen aşağıdaki bilgiler veritabanına kaydedilmelidir.
    * sha256_hash
    * sha1_hash
    * md5_hash
    * first_seen (datetime yapısında olmalıdır.)
    * tags
    * signature

## Kullanılması gereken Python kütüphaneleri

* Flask ve Flask-Restful (Endpointler için)
* Celery (Post metoduyla gelen istekte arka planda güncelleme yapmak için)
* Peewee veya SqlAlchemy (Database bağlantısını sağyalan ORM olarak)
* Requests (API isteklerini gönderip cevaplarını almak için)
* PostgreSQL, MongoDB veya SQLite (Veritabanı olarak)
