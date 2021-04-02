Nama = str(input('Nama: '))
Nilai = float(input('NIlai Ujian: '))

if Nilai < 60:
  Nilai_Konversi = 'E'
elif 60 <= Nilai <= 64:
    Nilai_Konversi = 'C'
elif 65 <= Nilai <= 69:
    Nilai_Konversi = 'C+'
elif 70 <= Nilai <= 74:
    Nilai_Konversi = 'B'
elif 75 <= Nilai <= 79:
    Nilai_Konversi = 'B+'
elif 80 <= Nilai <= 84:
    Nilai_Konversi = 'A-'
elif 85 <= Nilai <= 100:
    Nilai_Konversi = 'A'
else:
    Nilai_Konversi = "(Maaf, Nilai yang anda masukkan tidak valid)"

print("Hallo, %s ! Nilai anda setelah dikonversi adalah " %Nama, Nilai_Konversi)