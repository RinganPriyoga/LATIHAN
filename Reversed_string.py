while True:
    isi = input("Masukkan sebuah data atau kalimat:")
    print(f"\nisi yang dimasukkan: {isi}")

    stack = []
    print("\n[1] menyimpan karakter ke dalam stack")

    for char in isi:
        stack.append(char)
        print(f" Push: {char} -> Stack sekarang: {stack}")

    reversed_string = ""
    print ("\n[2] mengeluarkan karakter dari stack (pop): ")
    while stack:
        popped_char = stack.pop()
        reversed_string += popped_char
        print(f" Pop: {popped_char} -> Hasil sementara: {reversed_string}")

    print(f"\n[3] isi stack setelah dibalik: {reversed_string}")


    pilihan_lanjut = input("\nApakah Anda ingin melakukan pembalik lagi? (y/n): ")
    if pilihan_lanjut.lower() != 'y':
        print("Terima kasih telah menggunakan program pembalik.")
        break
