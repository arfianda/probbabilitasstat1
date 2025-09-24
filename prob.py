import pandas as pd

# Data mahasiswa
data = {
    'A': 329, 'B': 186, 'C': 295,
    'AB': 83, 'AC': 217, 'BC': 63,
    'ABC': 53, 'Total': 500
}

df = pd.Series(data)

# Hitung jumlah hanya di masing-masing bagian
only_A  = df.A - (df.AB - df.ABC) - (df.AC - df.ABC) - df.ABC
only_B  = df.B - (df.AB - df.ABC) - (df.BC - df.ABC) - df.ABC
only_C  = df.C - (df.AC - df.ABC) - (df.BC - df.ABC) - df.ABC

AB_only = df.AB - df.ABC
AC_only = df.AC - df.ABC
BC_only = df.BC - df.ABC

# Probabilitas
p_a = df.ABC / df.Total
p_b = (only_A + AB_only) / df.Total
p_c = (only_B + BC_only) / df.Total
p_d = (only_C + AC_only) / df.Total

# Tampilkan hasil
result = pd.Series({
    'Ketiga MK': p_a,
    'Aljabar tapi bukan Kalkulus': p_b,
    'Statistika tapi bukan Aljabar': p_c,
    'Kalkulus tapi bukan Statistika': p_d
})

print(result.apply(lambda x: f"{x:.3f}"))
