Nama = str(input('Nama: '))
Jenis_Kelamin = str(input('Jenis Kelamin (L/P, Menggunakan huruf kapital): '))
Umur = int(input('Umur: '))

if Jenis_Kelamin == 'L' and Umur <= 20:
    print("Selamat datang, Saudara %s" % Nama)
elif Jenis_Kelamin == 'L' and Umur > 20:
    print("Selamat datang, Bapak %s" % Nama)
elif Jenis_Kelamin == 'P' and Umur <= 20:
    print("Selamat datang, Saudari %s" % Nama)
elif Jenis_Kelamin == 'P' and Umur > 20:
    print("Selamat datang, Ibu %s" % Nama)
else:
    pass
print()