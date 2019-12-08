# amcc-desktop-agung-triyadi
Project pelatihan python dan github amcc divisi desktop

# Bagimana clone repository ?
1. pada halaman ini, klik clone repository > copy SSH
2. Buka Terminal (Linux) atau GitBash (Windows), lalu clone Repository dengan cara
"$ git clone git@github.com:dvrg/dp-2019.git"
3. untuk pertamkali clone, fingerprint akan didaftarkan ke komputer kamu dan konfirmasi penambahan itu dengan yes
"Cloning into 'dp-2019'...
The authenticity of host 'github.com (13.229.188.59)' can't be established.
RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes"
4. maka repository akan tercopy ke lokal komputer kamu.

## Bagaimana cara commit dan push
1. patikan perubahan pada file dengan "git status"
2. saat ingin menambahkan perubahan pada git, caranya git commit -am "pesan perubahan"
3. pastikan sudah tecommit dengan "git status"
4. setelah di commit dan sudah benar bisa langsung di push dengan "git push"

### Mengapa lebih baik ssh daripada https ?
alasannya adalah jika menggunakan ssh tidak perlu login saat ingin push ke repository seperti ssh

#### Alasan menggunakan python !
alsannya adalah bahasa python lebih mudah dari pada bahasa lainnya dan lebih manusiawi daripada bahasa yang lain, contoh bahasa laing perlu menggunakan titik koma sedangkan python tidak hanya saja lebih fokus ke inden pada teks (yaitu menjoroknya sebuah teks)

##### Pastikan telah mengintal python !
1. cara memastikannya dengan cara "phyton --version" atau "py --version" dan lihatlah versi python yang telah terinstal

###### Bagaimana jika python belum terinstall ?
ikuti tautan berikut https://www.dicoding.com/academies/86/tutorials/4738?from=4736 (daftar akun dicoding terlebih dahulu)

# Hello World dengan python
Masuk ke direktori folder repository ini dengan cara :
```bash
cd /path/nama-direktori
`
NB : merupakan nama-nama direktori diatas direktori repository ini, seperti misalnya Document

1. Buat sebuah file dengan nama main.py, cara berikut ini
`bash
nano main.py
`
2.
`python
print('Hello World !!!')
`
3. Jalankan file tersebut dengan cara
`python
python main.py
`
4. Hasil output harusnya sesuai dengan inputnya, yaitu :
`python
Hello World !!!
`

## Python Interpreter
1. Python interpreter merupakan program yang dibaca & dieksekusi pada sebuah sesi pada command line. Untuk masuk ke python interpreter, caranya sebagai berikut :
    -Buka CMD (windows) / Terminal (Linux/MacOS) >> Ketikkan 'Python'

## Menggunakan Modul (Function Dasar)
Modul merupakan set program yang sudah disediakan oleh python yang tinggal pakai, contohnya adalah seperti ini :

```Python
>>> import datetime
>>> datetime.datetime.now()
datetime.datetime(2019, 12, 1, 21, 39, 43, 673959)

Untuk menampilkan tanggal dan jam pada saat ini. lalu selanjutnya, kita akan menggunakan modul 'random' untuk mengacak karakter alfabet seperti contoh code dibawah ini :
```
```Python
>>> import random
>>> import string
>>> def randomword(length):
...     letters = string.ascii_lowercase
...     return ''.join(random.choice(letters) for i in range(length))
...
>>> randomword(10)
'ogrpxncyyt'
```
Lalu kita bakal buat program untuk mengacak nama dari seluruh pelatih desktopbprogramming amcc dengan contoh kode berikut ini :
```Python
>>> def random_name():
...     name = ('david', 'sabil', 'peby', 'angung', 'yanuar')
...     return ''.join(random.choice(name) for i in range(1))
...
>>> random_name()
'yanuar'
```

## Variabel
```Python
import datetime
print('Waktu Sekarang adalah ',datetime.datetime.now())

#Variabel
mynow =  datetime.datetime.now()
print(mynow)

print(datetime.datetime.now())

#Menggabungkan INT & STR
number = 10
string = 'Agung Triyadi'
print(number, string)
```

## Simple Type
```Python
a = 10
b = '10'
c = 10.1

sum1 = a+a
sum2 = b+b
sum3 = c+c

print(sum1, sum2, sum3)
print(type(a), type(b), type(c))
```