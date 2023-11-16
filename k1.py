# (HOF)
def perkalian(a):
    def apa(b):
        return a * b
    return apa

hasil = perkalian(5)
print(hasil(3))

# Currying
def perkalian_currying(a):
    return lambda b: a * b

hasil = perkalian_currying(5)
print(hasil(3))