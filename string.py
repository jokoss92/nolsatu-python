import re
artikel = "NolSatu hadir sebagai usAha untuk merespon masalah bersama yaitu banyak lulusan teknologi informatika atau profesional teknologi informatika yang kemampuannya kuranG sementara perusahaan-perusahaan membutuhkan profesional teknologi informatika terbaik dengan kemampuan terkini. Selain itu, perkembangan teknologi informatika global Berlangsung sangat cepat dan kemampuan profesional teknologi informatika disarankan selaras dengan perkembangan tersebut. Profesional teknologi informatika diharapkan dapat membantu perusahaan dalaM mengadopsi teknologi informatika terkini untuk mendOrong proses bisnis perusahaan. Imbal balik bagi profesional teknologi informatika dari proses ini adalah penghasilan yang cukup dan kesejahteraAN yang baik yang diberikan oleh perusahaaN. NolSatu adalah media untuk Talenta teknologi informatika dilatih agar memiliki kemampuan terkini kemudian disalurkan ke perusahaan yang membutuhkan. NolSatu juga media untuk Profesional teknologi informatika dilatih agar kemampuannya termutakhirkan kemudian disalurkan ke perusahaan baru yang membutuhkan."

print("Jumlah huruf kapital : " + str(sum(1 for c in artikel if c.isupper())))
kata = len(re.findall(r'\w+', artikel))
print("Jumlah kata : " +  str(kata)) 
kalimat = re.split(r'[.!?]+', artikel)
print("Jumlah kalimat : " + str(len(kalimat)))
array = artikel.split(". ")
hitung = 0
for i in artikel:
    if artikel.startswith("NolSatu") and artikel.endswith("membutuhkan"):
        hitung+1
    print(hitung)
kapital = [p.capitalize() for p in array]
join_kapital = ". ".join(kapital)
print("Kapital di tiap kalimat : " + join_kapital)