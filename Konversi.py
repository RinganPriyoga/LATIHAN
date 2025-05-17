def desimal_ke_biner(n):
    if n == 0:
        print("0 dibagi 2 = 0 sisa 0")
        return "0"
    hasil = ""
    langkah = []
    angka_awal = n
    while n > 0:
        sisa = n % 2
        hasil = str(sisa) + hasil
        langkah.append(f"{n} dibagi 2 = {n // 2} sisa {sisa}")
        n = n // 2
    print(f"\nLangkah-langkah konversi {angka_awal} ke biner:")
    for i in langkah:
        print(i)
    print("hasil konversi biner:", hasil)
    return hasil

def desimal_ke_oktal(n):
    if n == 0:
        print("0 dibagi 8 = 0 sisa 0")
        return "0"
    hasil = ""
    langkah = []
    angka_awal = n
    while n > 0:
        sisa = n % 8
        hasil = str(sisa) + hasil
        langkah.append(f"{n} dibagi 8 = {n // 8} sisa {sisa}")
        n = n // 8
    print(f"\nLangkah-langkah konversi {angka_awal} ke okta:")
    for i in langkah:
        print(i)
    print("hasil konversi okta:", hasil)
    return hasil

def desimal_ke_heksadesimal(n):
    if n == 0:
        print("0 dibagi 16 = 0 sisa 0")
        return "0"
    hasil = ""
    langkah = []
    angka_awal = n
    hexa_map = "0123456789ABCDEF"
    while n > 0:
        sisa = n % 16
        hasil = hexa_map[sisa] + hasil
        langkah.append(f"{n} dibagi 16 = {n // 16} sisa {hexa_map[sisa]}")
        n = n // 16
    print(f"\nLangkah-langkah konversi {angka_awal} ke heksadesimal:")
    for i in langkah:
        print(i)
    print("hasil konversi heksadesimal:", hasil)
    return hasil

#Program Utama
while True:
    print("\nPilih jenis konversi:")
    print("1. Desimal ke Biner")
    print("2. Desimal ke Oktal")
    print("3. Desimal ke Heksadesimal")

    pilihan = input("Masukkan pilihan (1-3): ")

    if pilihan == '1':
        n = int(input("Masukkan angka desimal: "))
        desimal_ke_biner(n)
    elif pilihan == '2':
        n = int(input("Masukkan angka desimal: "))
        desimal_ke_oktal(n)
    elif pilihan == '3':
        n = int(input("Masukkan angka desimal: "))
        desimal_ke_heksadesimal(n)

    pilihan_lanjut = input("\nApakah Anda ingin melakukan konversi lagi? (y/n): ")
    if pilihan_lanjut.lower() != 'y':
        print("Terima kasih telah menggunakan program konversi.")
        break
    print("Program dilanjutkan.")