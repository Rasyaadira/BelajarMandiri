print("time converter")
hours = input("Input a number in hours : ")
Pilihan = input("convert into (Second) or (Minutes) or (Days) : ")

if Pilihan == "Second" or Pilihan == "S" :
    final = int(hours) * 3600
    satuan = " Detik"
elif Pilihan == "Minutes" or Pilihan == "M" : 
    final = int(hours) * 60
    satuan = " Menit"
elif Pilihan == "Days" or Pilihan == "D" : 
    final = int(hours) / 24
    satuan = " Hari"
print("Jumlah" +str(satuan)+ " dari " +str(hours)+ " adalah " +str(final) +str(satuan))



