angka = int(input("Masukkan bilangan: "))

# Bilangan prima harus lebih besar dari 1
if angka > 1:
    is_prima = True
    # Cek pembagi dari 2 hingga angka - 1
    for i in range(2, angka):
        if angka % i == 0:
            is_prima = False
            break

    if is_prima:
        print("bilangan prima")
    else:
        print("bukan bilangan prima")
else:
    print("bukan bilangan prima")