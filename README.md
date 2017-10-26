### BOT LIKE V2

1x Login = 100 Like ( Ubah Pengaturan Timeline dengan cara menghilangkan ceklis pada Post Populer dulu )

Bisa Input sendiri SC yang kalian inginkan di Line 161

Bot ini hanya berfungsi untuk nge-LIKE semua post/status yang ada di timeline secara otomatis dan memberikan komentar secara otomatis
Jika terdapat Post/Status baru, bot ini tidak bisa langsung nge-LIKE post/status tersebut, tetapi kalian harus login ulang bot tersebut, saya sarankan kalian merubah cara loginnya menggunakan "authtoken"

### Cara ubah login versi authtoken ( Login Otomatis )
Ubah script dibawah ini
```bash
cl = LINETCR.LINE()
cl.login(qr=True)
cl.loginResult()
```
menjadi
```bash
cl = LINETCR.LINE()
cl.login(token="authtoken-ente")
cl.loginResult()
```

### Cara mendapatkan authtoken
Saat pertama login, pada terminal / termux kalian, kalian akan diberi authtoken kalian, contohnya
```bash
authToken -> EmGxXwhjizYIReLFxxxx.eFtfXEQQ9zeBAclHFogALq.3sv5woAxxxxHYXBJFxxxxxxxPToPfzUNv2VYvSXXXX=
```

### Catatan
Jika kalian mengerti bahasa pemograman, tolong untuk jangan merubah result komentar-nya, tetapi jika kalian memaksa ingin merubahnya, tolong jangan hapus URL Channel Youtube saya :) Terima Kasih

### Created By Farzain - zFz
