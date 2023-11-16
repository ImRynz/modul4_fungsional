# Fungsi untuk membuat pasangan koordinat (x, y)
def point(x, y):
    return x, y

# Fungsi untuk menghitung persamaan garis dengan titik dan gradien yang diberikan
def line_equation_of(p1, M):
    # Inner function untuk menghitung nilai intersep (c)
    def calculate_intercept(p):
        x1, y1 = p
        return y1 - M * x1
    
    # Mendapatkan nilai intersep menggunakan inner function
    get_intercept = calculate_intercept(p1)
    
    # Closure yang mengembalikan nilai y berdasarkan x yang diberikan
    def equation(x):
        return M * x + get_intercept
    
    return equation

# Titik yang diberikan:
titik = point(3,8)
gradien = 8

# Mendapatkan persamaan garis yang melalui titik dan memiliki gradien yang diberikan
equation = line_equation_of(titik, gradien)

# Menampilkan persamaan garis untuk x = 0
print("Persamaan garis yang melalui titik (3,8) dan bergradien 8:")
print(f"y = {gradien:.2f}x + {equation(0):.2f}")