# Aritmatika

Aritmatika adalah package Python yang berfungsi untuk menyelesaikan masalah aritmatika sosial seperti untung dan rugi, bunga, pajak, diskon dan rabat, serta bruto, netto, dan tara.

Aritmatika is a Python Package for dealing with social arithmetic problems such as profit and loss, interest, tax, discount and rebate, and also gross, net, and tare.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install aritmatika.

```bash
pip install aritmatika
```

## Penggunaan
#### 1. Fungsi Gaji

```python
from aritmatika import gaji

# Menghitung gaji pokok
gaji_pokok = gaji.hitung_gaji_pokok(50000, 40)
print(f"Gaji pokok: {gaji_pokok}")

# Menghitung gaji bersih
gaji_bersih = gaji.hitung_gaji_bersih(gaji_pokok, 500000, 300000)
print(f"Gaji bersih: {gaji_bersih}")

# Menghitung gaji lembur
gaji_lembur = gaji.hitung_gaji_lembur(5, 75000)
print(f"Gaji lembur: {gaji_lembur}")

# Menghitung total gaji
total_gaji = gaji.hitung_total_gaji(1000000, 200000, 500000)
print(f"Total gaji karyawan: {total_gaji}")

# Menghitung rata-rata gaji
list_gaji = [5000000, 6000000, 4500000, 5500000]
rata_rata_gaji = gaji.hitung_rata_rata_gaji(list_gaji)
print(f"Rata-rata gaji karyawan: {rata_rata_gaji}")
```

#### 2. Fungsi Bruto-Tara-Netto

```python
from aritmatika import bruto_tara_netto

# Menghitung bruto
bruto = bruto_tara_netto.hitung_bruto(500, 50)
print(f"Bruto: {bruto}")

# Menghitung tara
tara = bruto_tara_netto.hitung_tara(550, 500)
print(f"Tara: {tara}")

# Menghitung netto
netto = bruto_tara_netto.hitung_netto(550, 50)
print(f"Netto: {netto}")
```

#### 3. Fungsi Pajak

```python
from aritmatika import pajak

# Menghitung PPN
ppn = pajak.ppn(1000000)
print(f"PPN: {ppn}")

# Total bayar PPN
ppn = pajak.total_bayar(1000000)
print(f"Harga total setelah PPN: {ppn}")

#Menghitung NJKP
njkp = pajak.njkp(1200000)
print(f"NJKP: {njkp}")

# Menghitung PBB
pbb = pajak.pbb(1200000)
print(f"PBB: {pbb}")

# Menghitung PPh
pph = pajak.hitung_pph(120000000, 'lajang', 0)
print(f"PPH: {pph}")
```

#### 4. Fungsi Bunga

```python
from aritmatika import bunga

# Menghitung bunga tunggal
bunga_tunggal = bunga.bunga_tunggal(1000000, 0.05, 2)
print(f"Bunga tunggal: {bunga_tunggal}")

# Menghitung bunga majemuk
bunga_majemuk = bunga.bunga_majemuk(1000000, 0.05, 12, 2)
print(f"Bunga majemuk: {bunga_majemuk}")
```

#### 5. Fungsi Rabat dan Diskon

```python
from aritmatika import rabat_diskon

# Menghitung harga setelah diskon
harga_diskon = rabat_diskon.hitung_diskon(200000, 10)
print(f"Harga setelah diskon: {harga_diskon}")

# Menghitung rabat
total_setelah_rabat = rabat_diskon.hitung_rabat(50000, 10, 5)
print(f"Total setelah rabat: {total_setelah_rabat}")

# Menghitung Persen Diskon
 persen_diskon = rabat_diskon.hitung_persen_diskon(20000, 19000)
    print(f"Persentase diskon: {persen_diskon}%")
```

#### 6. Fungsi Untung dan Rugi

```python
from aritmatika import untung_rugi

# Menghitung untung
untung = untung_rugi.hitung_untung(10000, 15000)
print(f"Keuntungan: {untung}")

# Menghitung rugi
rugi = untung_rugi.hitung_rugi(10000, 15000)
print(f"keuntungan: {untung}")

# Menghitung persentase keuntungan
persen_untung = untung_rugi.persentase_untung(10000, 15000)
print(f"Persentase keuntungan: {persen_untung}%")

# Menghitung persentase kerugian
persen_rugi = untung_rugi.persentase_rugi(10000, 15000)
print(f"persentase kerugian: {persen_rugi}%")

```
## Dokumentasi Fungsi

#### 1. Fungsi Gaji

##### `hitung_gaji_pokok(gaji_per_jam, jam_kerja)`
- **Deskripsi**: Menghitung gaji pokok berdasarkan jam kerja.
- **Parameter**:
  - `gaji_per_jam` (*float*): Gaji per jam.
  - `jam_kerja` (*float*): Total jam kerja.
- **Return**: Gaji pokok yang dihasilkan.

##### `hitung_gaji_bersih(gaji_pokok, potongan_pajak, potongan_bpjs, potongan_lain=None)`
- **Deskripsi**: Menghitung gaji bersih setelah potongan pajak, BPJS, dan potongan lainnya.
- **Parameter**:
  - `gaji_pokok` (*float*): Gaji pokok.
  - `potongan_pajak` (*float*): Potongan pajak.
  - `potongan_bpjs` (*float*): Potongan BPJS.
  - `potongan_lain` (*float*, opsional): Potongan lain-lain.
- **Return**: Gaji bersih setelah potongan.

##### `hitung_gaji_lembur(jam_lembur, tarif_lembur)`
- **Deskripsi**: Menghitung gaji lembur berdasarkan jam lembur dan tarif lembur per jam.
- **Parameter**:
  - `jam_lembur` (*float*): Jumlah jam lembur.
  - `tarif_lembur` (*float*): Tarif lembur per jam.
- **Return**: Total gaji lembur.

##### `hitung_total_gaji(gaji_pokok: float, gaji_lembur: float, tunjangan: float)`
- **Deskripsi**: Menghitung total gaji berdasarkan gaji pokok, gaji lembur, dan tunjangan.
- **Parameter**:
  - `gaji_pokok` (*float*): Gaji pokok.
  - `gaji_lembur` (*float*): Gaji lembur.
  - `tunjangan` (*float*): Tunjangan.
- **Return**: Total gaji.

##### `hitung_rata_rata_gaji(list_gaji: list)`
- **Deskripsi**: Menghitung rata-rata gaji berdasarkan list gaji.
- **Parameter**:
  - `list_gaji` (*list*): List gaji.
- **Return**: Rata-rata gaji.

#### 2. Fungsi Bruto-Tara-Netto

##### `hitung_bruto(netto, tara)`
- **Deskripsi**: Menghitung bruto berdasarkan netto dan tara.
- **Parameter**:
  - `netto` (*float*): Berat bersih suatu barang.
  - `tara` (*float*): Berat kemasan barang.
- **Return**: Berat bruto barang.

##### `hitung_netto(bruto, tara)`
- **Deskripsi**: Menghitung netto dari bruto dan tara.
- **Parameter**:
  - `bruto` (*float*): Berat kotor suatu barang.
  - `tara` (*float*): Berat kemasan barang.
- **Return**: Berat netto barang.

##### `hitung_tara(bruto, netto)`
- **Deskripsi**: Menghitung tara dari bruto dan netto.
- **Parameter**:
  - `bruto` (*float*): Berat kotor suatu barang.
  - `netto` (*float*): Berat bersih suatu barang.
- **Return**: Berat tara barang.

#### 3. Fungsi Pajak

##### `ppn(transaksi, tarif_ppn=0.11)`
- **Deskripsi**: Menghitung Pajak Pertambahan Nilai (PPN) berdasarkan nilai transaksi.
- **Parameter**:
  - `transaksi` (*float*): Nilai transaksi.
  - `tarif_ppn` (*float*, opsional): Tarif PPN (default 11% atau 0.11).
- **Return**: Nilai PPN.

#### `total_bayar(transaksi, tarif_ppn=0.11)`
- **Deskripsi**: Menghitung total yang harus dibayar setelah PPN.
- **Parameter**:
  - transaksi (float): Jumlah transaksi yang dikenakan PPN
  - tarif_ppn (float): tarif PPN (deafult 11%)
- **Return**: jumlah total PPN yang harus dibayarkan.

### `def njkp(njop)`
- **Deskripsi**: Menghitung NJKP untuk dipakai menghitung PBB.
- **Parameter**:
  - njop (float): Nilai jual Objek Pajak
- **Return** Nilai jual kena pajak.

#### `pbb(njop, persen_pbb=0.5)`
- **Deskripsi**: Menghitung Pajak Bumi dan Bangunan (PBB).
- **Parameter**:
  - njop (float): Nilai Jual Objek Pajak
  - persen_pbb (float): Presentase tarif PBB (deafult 0.5%)
**Return**: Nilai PBB yang harus dibayar

##### `hitung_pph(gaji_tahunan, status, tanggungan)`
- **Deskripsi**: Menghitung Pajak Penghasilan (PPH) berdasarkan gaji tahunan, status, dan tanggungan.
- **Parameter**:
  - `gaji_tahunan` (*float*): Total gaji tahunan.
  - `status` (*str*): Status wajib pajak (contoh: 'lajang', 'kawin').
  - `tanggungan` (*int*): Jumlah tanggungan.
- **Return**: Jumlah PPH yang harus dibayar.

#### 4. Fungsi Bunga

##### `bunga_tunggal(p, r, t)`
- **Deskripsi**: Menghitung bunga tunggal berdasarkan pokok, suku bunga, dan periode waktu.
- **Parameter**:
  - `p` (*float*): Pokok pinjaman.
  - `r` (*float*): Suku bunga per periode (dalam desimal, contoh 5% ditulis 0.05).
  - `t` (*float*): Waktu (periode dalam tahun).
- **Return**: Nilai bunga yang dihasilkan.

##### `bunga_majemuk(p, r, n, t)`
- **Deskripsi**: Menghitung bunga majemuk dengan penggabungan bunga setiap periode.
- **Parameter**:
  - `p` (*float*): Pokok pinjaman.
  - `r` (*float*): Suku bunga per periode (dalam desimal).
  - `n` (*int*): Frekuensi penggabungan bunga per periode.
  - `t` (*float*): Waktu (periode dalam tahun).
- **Return**: Total (pokok + bunga) yang dihasilkan.

#### 5. Fungsi Rabat & Diskon

##### `hitung_diskon(harga_awal, diskon_persen)`
- **Deskripsi**: Menghitung harga setelah diskon.
- **Parameter**:
  - `harga_awal` (*float*): Harga sebelum diskon.
  - `diskon_persen` (*float*): Persentase diskon.
- **Return**: Harga setelah diskon.

##### `hitung_rabat(harga_per_barang, jumlah_barang, rabat_persen)`
- **Deskripsi**: Menghitung harga total setelah rabat.
- **Parameter**:
  - `harga_per_barang` (*float*): Harga per barang.
  - `jumlah_barang` (*int*): Jumlah barang.
  - `rabat_persen` (*float*): Persentase rabat.
- **Return**: Total harga setelah rabat.
- 
##### 'hitung_persen_diskon(harga_awal, harga_setelah_diskon)'
- **Deskripsi**: Menghitung Persentase Diskon
- **Parameter**:
  - `harga_awal` (*float*): Harga sebelum diskon
  - `harga_setelah_diskon` (*float*): Harga setelah diskon
-  **Return**: Persentase Diskon


#### 6. Fungsi Untung & Rugi

##### `hitung_untung(harga_beli, harga_jual)`
- **Deskripsi**: Menghitung keuntungan dari suatu transaksi.
- **Parameter**:
  - `harga_beli` (*int*): Harga beli barang.
  - `harga_jual` (*int*): Harga jual barang.
- **Return**: Keuntungan yang diperoleh.

##### `hitung_rugi(harga_beli, harga_jual)`
- **Deskripsi**: Menghitung kerugian dari suatu transaksi.
- **Parameter**:
  - `harga_beli` (*int*): Harga beli barang.
  - `harga_jual` (*int*): Harga jual barang.
- **Return**: Keuntungan yang diperoleh.

##### `persentase_untung(harga_beli, harga_jual)`
- **Deskripsi**: Menghitung persentase keuntungan.
- **Parameter**:
  - `harga_beli` (*float*): Harga beli barang.
  - `harga_jual` (*float*): Harga jual barang.
- **Return**: Persentase keuntungan.

##### `persentase_rugi(harga_beli, harga_jual)`
- **Deskripsi**: Menghitung persentase kerugian.
- **Parameter**:
  - `harga_beli` (*float*): Harga beli barang.
  - `harga_jual` (*float*): Harga jual barang.
- **Return**: Persentase kerugian.


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

