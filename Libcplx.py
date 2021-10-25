 import math

# Adicion de vectores complejos
def cplxsum(a, b):
    real = a[0] + b[0]
    imag = a[1] + b[1]
    return (real, imag)

# Producto de vectores complejos
def cplxproduct(a, b):
    real = a[0]*b[0] - a[1]*b[1]
    imag = a[0]*b[1] + b[0]*a[1]
    return (real, imag)

# Sustracción de vectores complejos
def cplxsust(a, b):
    real = a[0] - b[0]
    imag = a[1] - b[1]
    return (real, imag)

# Módulo de vectores complejos
def cplxmod(a):
    return round(math.sqrt(a[0]**2 + a[1]**2)),2)

# División de vectores complejos
def cplxcoc(a, b):
    real = (a[0]*b[0] + a[1]*b[1])/(b[0]*b[0] + b[1]*b[1])
    imag = (b[0]*a[1] - a[0]*b[1])/(b[0]*b[0] + b[1]*b[1])
    return (real, imag)

# Conjugado de un vector complejo
def cplxconj(b):
    real = b[0]
    imag = (-1)*(b[1])
    return (real, imag)

# Cambio de coorfenadas de polar a cartesiana
def cplxpolaracartesiana(d):
    return round(d[0]*math.cos(math.radians(d[1])),2),round(d[0]*math.sin(math.radians(d[1])),2)

# Cambio de coorfenadas de cartesiana a polar
def cplxcartesianaapolar(d):
    return round(math.degrees(math.atan(d[1] / d[0])),2)

# Retornar la fase de un número complejo
def cplxfase(d):
    theta = round(math.degrees(math.atan(d[1] / d[0])),2)
    return theta

if __name__ == '__main__':
    print(cplxsum((3,5), (-2.6,6.8)))  # (3 + 5i) + (-2.6 + 6.8i) = (0.4, 11.8i)
    print(cplxproduct((3,-1), (1,4)))  # (3 - i) x (1 + 4i) = (7, 11i)
    print(cplxsust((3,5), (-2.6,6.8)))  # (3 + 5i) - (-2.6 + 6.8i) = (5.6, -1.8i)
    print(cplxcoc((-2,1), (1,2))) # (-2 + i) x (1 + 2i) = (0, i)
    print(cplxmod(2, 1)) # (2 + i) -> sqrt((-2*-2) + (1*1)) = 5
    print(cplxconj(2, 3)) # (2, 3) -> (2, -3)
    print(cplxpolaracartesiana(sqrt(2), 45)) # (sqrt(2), pi/4) --> 1 + i
    print(cplxcartesianaapolar(1, 1)) # 1 + i --> (sqrt(2), pi/4)
    print(cplxfase(1, 1)) # a + i --> atan(1/1) = pi/4
