username = input('Masukkan Username Anda :')
password = input('Masukkan Password Anda :')

if username == 'admin' and password == 'admin123':
    print('Selamat Anda Berhasil Login dengan akses Admin')
elif username == 'user' and password == 'user123':
    print('Selamat Anda Berhasil Login Dengan Akses Terbatas')
elif username == 'guest' and password == "" :
    print('Selamat Anda Berhasil Login Dengan Akses Minimal')
else:
    print('Akses di tolak')