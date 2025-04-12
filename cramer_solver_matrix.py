
import sympy
from sympy import Matrix, latex

try:
    from IPython.display import display, Math
    JUPYTER = True
except ImportError:
    JUPYTER = False

def cramer_solver_matrix(A, b, symbolic=True):
    if not A.is_square:
        raise ValueError("Matriks A harus persegi.")
    if A.rows != b.rows:
        raise ValueError("Jumlah baris A dan b tidak cocok.")

    det_A = A.det()
    if det_A == 0:
        hasil = r"\text{Sistem tidak memiliki solusi tunggal karena } \det(A) = 0"
        return display(Math(hasil)) if JUPYTER else print(hasil)

    n = A.cols
    solusi = []
    solusi_latex = [r"\begin{aligned}"]

    for i in range(n):
        A_i = A.copy()
        A_i[:, i] = b
        det_Ai = A_i.det()
        x_i = det_Ai / det_A

        # Jika tidak simbolik, konversi ke float
        x_display = x_i.evalf() if not symbolic else x_i

        solusi.append(x_display)
        solusi_latex.append(
            fr"x_{{{i+1}}} &= \frac{{\det(A_{{{i+1}}})}}{{\det(A)}} = \frac{{{latex(det_Ai)}}}{{{latex(det_A)}}} = {latex(x_display)} \\"
        )

    solusi_latex.append(r"\end{aligned}")
    solusi_final = "\n".join(solusi_latex)

    if JUPYTER:
        return display(Math(solusi_final))
    else:
        print("Solusi LaTeX:\n" + solusi_final)
        return solusi  # Kembalikan juga list solusi untuk pemakaian lanjut
