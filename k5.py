def point(x, y):
    return x, y

def line_equation_of(p1, p2):
    # Menggunakan lambda untuk menghitung nilai M (gradien)
    get_gradient = lambda p1, p2: (p2[1] - p1[1]) / (p2[0] - p1[0])

    # Menggunakan lambda untuk menghitung nilai C (intersep)
    get_intercept = lambda p, m: p[1] - m * p[0]

    # Mendapatkan nilai gradien (M) dari dua titik yang diberikan
    M = get_gradient(p1, p2)

    # Mendapatkan nilai intersep (C)
    C = get_intercept(p1, M)

    return f"y = {M:.2f}x + {C:.2f}"

# Dua titik yang diberikan: 
titik_A = point(1, 3)
titik_B = point(5, 2)

print("Persamaan garis yang melalui titik A dan B:")
print(line_equation_of(titik_A, titik_B))