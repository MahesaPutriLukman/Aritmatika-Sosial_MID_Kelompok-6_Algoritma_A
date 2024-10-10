def hitung_gaji_pokok(gaji_per_jam, jam_kerja):
    """
    Menghitung gaji pokok berdasarkan gaji per jam dan jam kerja.

    Args:
        gaji_per_jam (float): Gaji per jam karyawan.
        jam_kerja (float): Jumlah jam kerja dalam satu periode.

    Returns:
        float: Gaji pokok karyawan.
    """
    return gaji_per_jam * jam_kerja

def hitung_gaji_bersih(gaji_pokok, potongan_pajak, potongan_bpjs, potongan_lain=0):
  """
  Menghitung gaji bersih setelah dikurangi berbagai potongan.

  Args:
    gaji_pokok (float): Gaji pokok karyawan.
    potongan_pajak (float): Potongan pajak penghasilan.
    potongan_bpjs (float): Potongan BPJS Kesehatan dan Ketenagakerjaan.
    potongan_lain (float, optional): Potongan lainnya (misal, cicilan). Defaults to 0.

  Returns:
    float: Gaji bersih karyawan.
  """

  return gaji_pokok - potongan_pajak - potongan_bpjs - potongan_lain

def hitung_gaji_lembur(jam_lembur, tarif_lembur):
  """
  Menghitung gaji lembur.

  Args:
    jam_lembur (float): Jumlah jam lembur.
    tarif_lembur (float): Tarif gaji lembur per jam.

  Returns:
    float: Gaji lembur.
  """

  return jam_lembur * tarif_lembur

def hitung_total_gaji(gaji_pokok, gaji_lembur, tunjangan):
  """
  Menghitung total gaji yang diterima karyawan.

  Args:
    gaji_pokok (float): Gaji pokok karyawan.
    gaji_lembur (float): Gaji lembur karyawan.
    tunjangan (float): Total tunjangan yang diterima.

  Returns:
    float: Total gaji karyawan.
  """

  return gaji_pokok + gaji_lembur + tunjangan

def hitung_rata_rata_gaji(list_gaji):
  """
  Menghitung rata-rata gaji dari sebuah list gaji.

  Args:
    list_gaji (list): List berisi nilai-nilai gaji.

  Returns:
    float: Rata-rata gaji.
  """

  return sum(list_gaji) / len(list_gaji)