# DC-Bot-Auto-Post

Bot Discord untuk auto post degan Quote di spesifik channel id.

Created by Viloid ( cath__27 ) Modifed by onekill0503


## Cara Mendapatkan Token Discord

Untuk yg pake android bisa pakai cara ini

JS Inject:

Paste di url bar posisi login discord :)

```
javascript:var i = document.createElement('iframe');i.onload = function(){var localStorage = i.contentWindow.localStorage;prompt('DC Token By @github.com/vsec7', localStorage.getItem('token').replace(/["]+/g, ''));};document.body.appendChild(i);
```

* Tulis ulang **javascript** nya jika di remove browser

Atau

- Masuk ke discord.com/app ( dalam keadaan login dc ya )
- Open DevTools di browser / F12
- Application > Storage > LocalStorage > https://discord.com > Ketik di pencarian dengan keyword "token"
* lihat gambar dibawah ini

![token](https://i.ibb.co/P5fjB25/token.jpg)

## Cara Melihat Channel ID

- Masuk ke channel yg diingiinkan (yg paling belakang adalah channel id)
* lihat gambar di bawah

![chanid](https://i.ibb.co/5LK6SQq/chanid.jpg)

## Cara menjalankan di komputer lokal

- Donwload Python versi 3 di https://www.python.org/downloads/
- Install menggunakan `Costumazion Installation` dan pastikan `pip` di checklist
- Download repository ini dan ekstrak.
- Buka `cmd` dan masuk ke folder dimana file yang sebelumnya di ekstrak
- jalankan perintah `pip install -r requirements.txt`
- lalu buka file dengan nama `conf.json` lalu modifikasi sesuai account token dan channel id.
- Setelah itu jalankan dengan perintah `python main.py`





