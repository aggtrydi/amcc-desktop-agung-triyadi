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