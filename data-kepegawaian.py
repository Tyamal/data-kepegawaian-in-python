import pandas as pd
import numpy as np
import random

np.random.seed(42)

num_rows = 100
data = {
    'Nomor Kependudukan': [f'1234567890{str(i).zfill(4)}' for i in range(num_rows)],
    'Nama': [f'Pegawai {i+1}' for i in range(num_rows)],
    'Umur': np.random.randint(20, 60, size=num_rows),
    'Pendapatan (Rupiah)': np.random.randint(3000000, 15000000, size=num_rows),
    'Alamat': [f'Jl. Contoh No.{i+1}' for i in range(num_rows)],
    'Status Perkawinan': [random.choice(['Belum Menikah', 'Menikah']) for _ in range(num_rows)]
}

df_kepegawaian = pd.DataFrame(data)
df_kepegawaian['Perusahaan'] = 'Mala Latihan Python'

print(df_kepegawaian)
