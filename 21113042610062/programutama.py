

import tarif_parkir as tp


def main():
    print("=== HITUNG TARIF PARKIR ===")
    print("Jenis kendaraan:", ", ".join(tp.daftar_kendaraan()))

    jenis = input("Masukkan jenis kendaraan: ")
    try:
        durasi = float(input("Masukkan lama parkir (jam): "))
        total = tp.hitung_tarif(jenis, durasi)
    except ValueError as e:
        print("Error:", e)
        return

    print(f"\nJenis kendaraan : {jenis.title()}")
    print(f"Lama parkir     : {durasi} jam")
    print(f"Total bayar     : {tp.format_rupiah(total)}")


if __name__ == "__main__":
    main()