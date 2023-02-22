nama = input("Masukkan Nama Lengkap Anda: ")
prodi = input("Masukkan Prodi Anda: ")
nilai = input("Masuklan Nilai (harus hruf) yang Anda Dapat: ")
try:   
    if nilai == 'A':
        print("Nilai kamu 4.00, Mantaplah kamu")
    elif nilai == 'A-':
        print("Nilai kamu 3.75, kamu keren!")
    elif nilai == 'B+':
        print("Nilai kamu 3.25, Lumayan bang")
    elif nilai == 'B':
        print("Nilai kamu 3.0, semngt")
    elif niali == 'B-':
        print("Nilai kamu 2.75, belajar lah")
    elif nilai == 'C+':
        print("Nilai kamu 2.25, masih oke")
    elif nilai == 'C':
        print("Nilai kamu 2.0, mumet")
    elif nilai == 'D':
        print("Nilai kamu 1.0, angell")
    elif nilai == 'E':
        print("Nilai kmau 0, jelek")
    else:
        print("inputan kamu ga valid")
except:
    ()
