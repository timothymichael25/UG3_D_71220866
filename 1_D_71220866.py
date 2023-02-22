cuaca = float(input('Masukkan Cuaca: '))

if cuaca >= 0 and cuaca <= 0.4:
    print("Cuaca terang / berawan")
elif cuaca >= 0.5 and cuaca <= 20:
    print("Cuaca hujan ringan")
elif cuaca >=21 and cuaca <= 50:
    print("Cuaca hujan sedang")
elif cuaca >= 51 and cuaca < 100:
    print("Cuaca hujan lebat")
elif cuaca >= 100:
    print("Cuaca hujan ekstrem")

# cuaca = float(input('Masukkan Cuaca: ')).lower().split(' ')
# a = ('cuaca >= 0' and 'cuaca <= 0.4' if cuaca[0] == 'Cuaca terang / berawan'else(print('cuaca >= 0.5' and 'cuaca <= 20' if cuaca[0] == 'Cuaca hujan ringan')))
# print(a)