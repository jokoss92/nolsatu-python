import re
artikel = "NolSatu hadir sebagai usAha untuk merespon masalah bersama yaitu banyak lulusan teknologi informatika atau profesional teknologi informatika yang kemampuannya kuranG sementara perusahaan-perusahaan membutuhkan profesional teknologi informatika terbaik dengan kemampuan terkini. Selain itu, perkembangan teknologi informatika global Berlangsung sangat cepat dan kemampuan profesional teknologi informatika disarankan selaras dengan perkembangan tersebut. Profesional teknologi informatika diharapkan dapat membantu perusahaan dalaM mengadopsi teknologi informatika terkini untuk mendOrong proses bisnis perusahaan. Imbal balik bagi profesional teknologi informatika dari proses ini adalah penghasilan yang cukup dan kesejahteraAN yang baik yang diberikan oleh perusahaaN. NolSatu adalah media untuk Talenta teknologi informatika dilatih agar memiliki kemampuan terkini kemudian disalurkan ke perusahaan yang membutuhkan. NolSatu juga media untuk Profesional teknologi informatika dilatih agar kemampuannya termutakhirkan kemudian disalurkan ke perusahaan baru yang membutuhkan."

print("1. Jumlah huruf kapital : " + str(sum(1 for c in artikel if c.isupper())))
kata = len(re.findall(r'\w+', artikel))-1
print("2. Jumlah kata : " +  str(kata)) 
kalimat = re.split(r'[.!?]+', artikel)
print("3. Jumlah kalimat : " + str(len(kalimat)-1))
array = artikel.split(". ")
# array = re.sub(".", "", array)
array_kriteria = []
for i in array:
    hitung = 0 
    if i.startswith("NolSatu") and (i.endswith("membutuhkan") or i.endswith("membutuhkan.")):
        array_kriteria.append(i)
print("4. Jumlah kalimat yang diawali dengan kata 'nolsatu' dan diakhiri dengan kata 'membutuhkan' : "
  + str(len(array_kriteria)))
kapital = [p.capitalize() for p in array]
join_kapital = ". ".join(kapital)
print("5. Kapital di tiap kalimat : \n" + join_kapital)