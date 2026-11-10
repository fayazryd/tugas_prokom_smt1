

import parkir

TARIF = {
    "becak": {"flat": 1000},
    "motor": {"masuk": 2000, "progresif": 1000, "maksimal": 10000, "inap": 15000},
    "mobil": {"masuk": 4000, "progresif": 2000, "maksimal": 15000, "inap": 20000},
    "microbus": {"masuk": 10000, "progresif": 5000},
}

BATAS_JAM_AWAL = 2   # jam pertama yang sudah termasuk tarif masuk
BATAS_INAP = 24      # jam


def daftar_kendaraan():
    """Mengembalikan daftar jenis kendaraan yang tersedia."""
    return list(TARIF.keys())


def hitung_tarif(jenis, durasi_jam):
    """Menghitung biaya parkir.

    jenis      : 'becak', 'motor', 'mobil', atau 'microbus'
    durasi_jam : lama parkir dalam jam (boleh desimal, dibulatkan ke atas)
    """
    jenis = jenis.lower().strip()
    if jenis not in TARIF:
        raise ValueError(f"Jenis kendaraan '{jenis}' tidak dikenal.")
    if durasi_jam < 0:
        raise ValueError("Durasi tidak boleh negatif.")

    t = TARIF[jenis]
    durasi = math.ceil(durasi_jam)

    # Becak: tarif flat
    if "flat" in t:
        return t["flat"]

    # Tarif inap (>= 24 jam), dihitung per 24 jam
    if "inap" in t and durasi >= BATAS_INAP:
        return t["inap"] * math.ceil(durasi / BATAS_INAP)

    # Tarif masuk + progresif setelah 2 jam
    jam_tambahan = max(0, durasi - BATAS_JAM_AWAL)
    total = t["masuk"] + jam_tambahan * t["progresif"]

    # Batasi dengan tarif maksimal (jika ada)
    if "maksimal" in t:
        total = min(total, t["maksimal"])

    return total


def format_rupiah(angka):
    """Format angka menjadi 'Rp 10.000'."""
    return "Rp " + f"{angka:,.0f}".replace(",", ".")