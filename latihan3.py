nilai = 82
kehadiran = 90

syarat_nilai = nilai >= 75
syarat_kehadiran = kehadiran >= 80

print("--- Kondisi Awal ---")
print(f"Nilai ({nilai}) >= 75 : {syarat_nilai}")
print(f"Kehadiran ({kehadiran}%) >= 80% : {syarat_kehadiran}")
print(f"Status Lulus (AND) : {syarat_nilai and syarat_kehadiran}")

# Mengubah nilai menjadi 70
nilai = 70
syarat_nilai = nilai >= 75

print("\n--- Setelah Nilai Diubah Jadi 70 ---")
print(f"Nilai ({nilai}) >= 75 : {syarat_nilai}")
print(f"Status Lulus dengan AND : {syarat_nilai and syarat_kehadiran}")
print(f"Status Lulus dengan OR : {syarat_nilai or syarat_kehadiran}")