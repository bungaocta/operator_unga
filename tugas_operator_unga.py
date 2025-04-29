# =============================
# 1. Jenis Operator dalam Python
# =============================
print("1. Jenis Operator dalam Python:")
print("""
- Operator Aritmatika: +, -, *, /, //, %, **
- Operator Perbandingan: ==, !=, >, <, >=, <=
- Operator Logika: and, or, not
- Operator Penugasan: =, +=, -=, *=, /=, %=, //=, **=
- Operator Bitwise: &, |, ^, ~, <<, >>
- Operator Keanggotaan: in, not in
- Operator Identitas: is, is not
""")

# =============================
# 2. Penyelesaian Ekspresi Matematika
# =============================
print("2. Hasil Perhitungan:")
hasil2 = 200 / (20 - 30) + (100 * (21.9**2)) / (100 + (10 / 20))
print("Hasil perhitungan: {:.2f}".format(hasil2))

# =============================
# 3. Operasi Biner
# =============================
print("\n3. Operasi Biner:")
x = 100      # 0b01100100
y = 10       # 0b00001010
z = 68       # 0b01000100

# a. x & y & z
hasil3a = x & y & z
print("a. x & y & z = {} (bin: {})".format(hasil3a, bin(hasil3a)))

# b. x ^ y << 5 >> 2
hasil3b = (x ^ y) << 5 >> 2
print("b. x ^ y << 5 >> 2 = {} (bin: {})".format(hasil3b, bin(hasil3b)))

# c. ~x & ~y | ~z
hasil3c = (~x & ~y) | ~z
print("c. ~x & ~y | ~z = {} (bin: {})".format(hasil3c, bin(hasil3c)))

# =============================
# 4. Operasi Biner dengan Angka Biner
# =============================
print("\n4. Operasi Biner dari Bilangan Biner:")
x = 0b1100100   # 100
y = 0b110010    # 50
z = 0b101       # 5

# a. (x - y) / z
hasil4a = (x - y) / z
print("a. (x - y) / z = {} (bin: {})".format(hasil4a, bin(int(hasil4a))))

# b. (x + y + z) / (x - z + z)
hasil4b = (x + y + z) / (x - z + z)
print("b. (x + y + z) / (x - z + z) = {} (bin: {})".format(hasil4b, bin(int(hasil4b))))
