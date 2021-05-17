#mengimpor modul geometri2D
#yang berada di dalam paket matematika
import matematika.geometri2D

def main():
    #bujur sangkar
    sisi = 5
    luas = matematika.geometri2D.luasBujursangkar(sisi)

    print("BUJURSANGKAR")
    print("Panjag sisi\t: ", sisi)
    print("Luas\t\t= ", luas)

if __name__ == "__main__":
    main()