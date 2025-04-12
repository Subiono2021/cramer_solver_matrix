# **fungsi `cramer_solver_matrix`** 

### 🎯 **Tujuan Fungsi**
Menyelesaikan sistem persamaan linear $A\mathbf{x} = \mathbf{b}$ menggunakan **Aturan Cramer** (Cramer's Rule), dan menampilkan langkah-langkah penyelesaian dalam **notasi $\LaTeX$**.

---

## 🧩 **Struktur Program**

### 1. **Import dan Setup**
```python
import sympy
from sympy import Matrix, latex
try:
    from IPython.display import display, Math
    JUPYTER = True
except ImportError:
    JUPYTER = False
```
- Mengimpor pustaka `sympy` untuk manipulasi simbolik.
- Mengecek apakah berjalan di Jupyter (agar bisa menggunakan tampilan $\LaTeX$ interaktif via `display(Math(...))`).

---

### 2. **Parameter Baru: `symbolic=True`**
```python
def cramer_solver_matrix(A, b, symbolic=True):
```
- Menambahkan opsi `symbolic`:  
  - Jika `True` → hasil simbolik (pecahan biasa).
  - Jika `False` → hasil numerik (desimal, float).

---

### 3. **Validasi Masukan**
```python
if not A.is_square:
    raise ValueError("Matriks A harus persegi.")
if A.rows != b.rows:
    raise ValueError("Jumlah baris A dan b tidak cocok.")
```
- Memastikan bahwa:
  - Matriks `A` **harus persegi**.
  - Dimensi vektor kolom `b` **harus cocok** dengan jumlah baris `A`.

---

### 4. **Determinasi Solusi Unik**
```python
det_A = A.det()
if det_A == 0:
    hasil = r"\text{Sistem tidak memiliki solusi tunggal karena } \det(A) = 0"
    return display(Math(hasil)) if JUPYTER else print(hasil)
```
- Jika determinan \( \det(A) = 0 \), maka sistem **tidak punya solusi tunggal**.

---

### 5. **Perhitungan Solusi Cramer**
```python
for i in range(n):
    A_i = A.copy()
    A_i[:, i] = b
    det_Ai = A_i.det()
    x_i = det_Ai / det_A
    x_display = x_i.evalf() if not symbolic else x_i
```
- Untuk setiap variabel \( x_i \):
  - Membuat salinan matriks \( A \) dan mengganti kolom ke-\( i \) dengan \( b \).
  - Menghitung determinan \( A_i \) dan menghitung solusi \( x_i \).
  - Jika `symbolic=False`, konversi ke **float** menggunakan `.evalf()`.

---

### 6. **Penyusunan Langkah LaTeX**
```python
solusi_latex.append(
    fr"x_{{{i+1}}} &= \frac{{\det(A_{{{i+1}}})}}{{\det(A)}} = \frac{{{latex(det_Ai)}}}{{{latex(det_A)}}} = {latex(x_display)} \\"
)
```
- Setiap baris LaTeX mencantumkan langkah penyelesaian dari \( x_i \).
- Hasil akhir digabung dengan `"\n".join(...)`.

---

### 7. **Output Akhir**
```python
if JUPYTER:
    return display(Math(solusi_final))
else:
    print("Solusi LaTeX:\n" + solusi_final)
    return solusi
```
- Di lingkungan Jupyter Notebook → ditampilkan langsung dalam bentuk persamaan matematika.
- Di luar Jupyter (misal terminal) → hasil ditampilkan sebagai string LaTeX biasa.

---

## 🎁 **Fitur Tambahan dan Keunggulan**

| Fitur                         | Keterangan                                                                 |
|------------------------------|----------------------------------------------------------------------------|
| ✅ Symbolic / Numeric Output  | Fleksibel untuk keperluan presisi (simbolik) atau estimasi (float)        |
| ✅ LaTeX Step-by-Step         | Penjabaran lengkap dan elegan dalam format matematika standar              |
| ✅ Kompatibel dengan Jupyter  | Menggunakan `display(Math(...))` bila tersedia                            |
| ✅ Struktur modular & rapi    | Dapat dijadikan modul Python (.py) dan diimpor                            |
| ❗ Validasi input lengkap     | Memastikan struktur matriks dan vektor sesuai sebelum melanjutkan         |

---

## 🧪 **Contoh Penggunaan**
```python
A = Matrix([[1, 1, -2],
            [2, -1, -1],
            [1, 2, 3]])
b = Matrix([[-3], [0], [13]])

cramer_solver_matrix(A, b, symbolic=False)  # hasil dalam float
```

<hr>
