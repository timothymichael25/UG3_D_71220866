awal_deret = int(input("Masukkan awal deret: "))
akhir_deret = int(input("Masukkan akhir deret: "))
for i in range(awal_deret, akhir_deret+1):
    print("" if i%6 == 0 or i%8 == 0 else f"{i} ", end="")