harga = 12500
jumlah = 4

total_harga = harga * jumlah

sisa_bagi = total_harga % 2000

diskon = 5000
total_setelah_diskon = total_harga - diskon

# Menampilkan hasil perhitungan dengan label yang jelas
print("=== RINCIAN PEMBAYARAN TOKO BUKU ===")
print(f"Harga per buku         : Rp{harga:,}")
print(f"Jumlah buku            : {jumlah} buah")
print(f"Total harga            : Rp{total_harga:,}")
print(f"Sisa pembagian (% 2000): {sisa_bagi}")
print(f"Total setelah diskon   : Rp{total_setelah_diskon:,}")