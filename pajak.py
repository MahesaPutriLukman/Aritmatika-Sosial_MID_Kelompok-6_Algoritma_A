def ppn(transaksi, tarif_ppn=0.11):
    """
    Menghitung pajak pertambahan nilai atau PPN

    Args:
        transaksi (float): Jumlah transaksi yang dikenakan PPN
        tarif_ppn (float): tarif PPN (deafult 11%)

    Returns:
        float: Nilai PPN yang harus dibayarkan
    """
    jumlah_ppn = transaksi  * tarif_ppn
    return jumlah_ppn

def total_bayar(transaksi, tarif_ppn=0.11):
    """
    Menghitung total yang harus dibayar setelah PPN

    Args:
        transaksi (float): Jumlah transaksi yang dikenakan PPN
        tarif_ppn (float): tarif PPN (deafult 11%)

    Returns:
        float: jumlah total PPN yang harus dibayarkan
    """
    nilai_ppn = ppn(transaksi, tarif_ppn)
    total_bayar = transaksi + nilai_ppn
    return total_bayar

def njkp(njop):
    """
    Menghitung NJKP untuk dipakai menghitung PBB

    Args:
    njop (float): Nilai jual Objek Pajak

    Returns:
        float: Nilai Jual Kena Pajak (NJKP)
    """
    if njop <= 1000000000:
        persen_njkp = 20
    else:
        persen_njkp = 40

    nilai_njkp = njop * (persen_njkp / 100)
    return nilai_njkp

def pbb(njop, persen_pbb=0.5):
    """
    Menghitung Pajak Bumi dan Bangunan (PBB)

    Args:
    njop (float): Nilai Jual Objek Pajak
    persen_pbb (float): Presentase tarif PBB (deafult 0.5%)

    Returns:
        float: Nilai PBB yang harus dibayar
    """
    njkp_value= njkp(njop)
    pbb_value = njkp_value * (persen_pbb / 100)
    return pbb_value

def hitung_pph(penghasilan, status_pernikahan, jumlah_tanggungan):
    """
    Fungsi untuk menghitung PPH (Pajak Penghasilan).
    :param penghasilan: total penghasilan setahun
    :param status_pernikahan: 'lajang' atau 'menikah'
    :param jumlah_tanggungan: jumlah tanggungan yang dimiliki
    :return: jumlah pajak yang harus dibayar
    """

    if status_pernikahan == 'lajang':
        ptkp = 54000000  
    elif status_pernikahan == 'menikah':
        ptkp = 58500000 + (4500000 * min(jumlah_tanggungan, 3)) 

    pkp = penghasilan - ptkp


    if pkp <= 0:
        return 0

    if pkp <= 50000000:
        pajak = pkp * 0.05
    elif pkp <= 250000000:
        pajak = (50000000 * 0.05) + ((pkp - 50000000) * 0.15)
    elif pkp <= 500000000:
        pajak = (50000000 * 0.05) + (200000000 * 0.15) + ((pkp - 250000000) * 0.25)
    else:
        pajak = (50000000 * 0.05) + (200000000 * 0.15) + (250000000 * 0.25) + ((pkp - 500000000) * 0.30)
    return pajak 