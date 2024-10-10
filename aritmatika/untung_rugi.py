def hitung_untung(harga_beli, harga_jual):
  """Hitung keuntungan dari suatu transaksi jual beli.

  Returns:
    Keuntungan dari transaksi tersebut.
  """

  return harga_jual - harga_beli

def hitung_rugi(harga_beli, harga_jual):
  """Hitung kerugian dari suatu transaksi jual beli.

  Return:
    Kerugian dari transaksi tersebut.
  """

  return harga_beli-harga_jual


def persentase_untung(harga_beli, harga_jual):
    """
    Menghitung persentase keuntungan.
    """
    if harga_jual > harga_beli:
        untung = harga_jual - harga_beli
        return print(f"{(untung/harga_beli) * 100}%")
    else:
        return 0

def persentase_rugi(harga_beli, harga_jual):
    """
    Menghitung persentase kerugian.
    """
    if harga_jual < harga_beli:
        rugi = harga_beli - harga_jual
        return print(f"{(rugi / harga_beli) * 100}%")
    else:
        return 0