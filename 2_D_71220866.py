try: 
    plat =int(input("Masukkan nomor plat kendaraan: "))
    if plat >= 0 and plat <= 3000:
        print("Kendaraan ini adalah mobil.")
    elif plat >= 3001 and plat <= 4000:
        print("Kendaraan ini adalah motor.")
    elif plat >= 4001 and plat <= 5000:
        print("Kendaraan ini adalah angkutan umum.")
    elif plat >= 5000:
        print('Plat nomor tidak terindetifikasi ketiga angkutan tersebut')        
except:
    print('Plat nomor tidak teridentifikasi, setelah kode daerah harus berupa nomor kendaraan')