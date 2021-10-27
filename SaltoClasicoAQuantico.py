from matplotlib.pyplot import bar, show
import EspaVectCplx as lct
import math

# 1. Los experimentos de la canicas con coeficiente booleanos.
def boolMtx(m):
    n = len(m)
    for i in range(n):
        for j in range(len(m[0])):
            if m[j][i]:
                m[j][i] = (1, 0)
            elif not m[j][i]:
                m[j][i] = (0, 0)
            else:
                m[j][i] = False
    if False in m:
        return 'No es posible realizar esta operación'
    else:
        return m 


def clics(m,vec,n):
    a = []
    for i in range(n):
        a = lct.ProdMtx(m, m)
    if n != 1:
        return lct.MtxVec(a,vec)
    else:
        return lct.MtxVec(m,vec)


# 3.1.1
def momentoMatrix(m,vec,n):
    m = boolMtx(m)
    if not m:
        return 'No es posible realizar esta operación'
    else:
        return clics(m,vec,n)


# 3.2.1
def momentoMatrixFr(m,vec,n):
    return clics(m,vec,n)


# 3.2.2
def rendijasPro(nr,nb,n):
    num = (nb*nr)+nr
    m = [[(0, 0) for i in range(num)] for j in range(num)]
    for i in range(1, int(nr)+1):
        m[i][0] = (1/int(nr), 0)
    x = int(nr)+1
    for j in range(1, int(nr)+1):
        m[x][j] = (1/nb, 0)
        m[x+1][j] = (1/nb, 0)
        m[x+2][j] = (1/nb, 0)
        x += 2
    for k in range(nr+1, num):
        m[k][k] = (1, 0)
    vec = [(0, 0) for i in range(num)]
    vec[0] = (1, 0)
    return m, clics(m,vec,n)


# 3.3.1
def momentoMatrixFr(m,vec,n):
    return clics(m,vec,n)


# 3.3.2
def transCplxInterf(nr, nb, n):
    num = (nb*nr)+nr
    m = [[(0, 0) for i in range(num)] for j in range(num)]
    for i in range(1, int(nr)+1):
        m[i][0] = (math.sqrt(0.5), 0)
    x = int(nr) + 1
    for j in range(1, int(nr)+1):
        m[x][j] = ((-1)/(math.sqrt(6)), 1/(math.sqrt(6)))
        m[x + 1][j] = ((-1)/(math.sqrt(6)), (-1)/(math.sqrt(6)))
        m[x + 2][j] = (1/math.sqrt(6), (-1)/math.sqrt(6)
        x += 2
    for k in range(int(nr)+1, (nb*nr)+nr):
        m[k][k] = (1, 0)
    vec = [(0, 0) for i in range(num)]
    vec[0] = (1, 0)
    return m, clics(m,vec,n)


# Graficar con un diagrama de barras que muestre las probabilidades de un vector de estados
def diagramBarr(vec):
    n = len(vec)
    prob = [i for i in range(n)]
    matplotlib.bar(p, vec, color="14000a")
    matplotlib.show()

def diagramaCuantico(vec):
    vec = [(compl.module(v[i]))**2 for i in range(len(v))]
    prob = [i for i in range(len(vec))]
    plt.bar(prob,vec,color="14000a")
    plt.show()


# c = multiplicar_matrices(a, b)
#
# if c == None:
#     print('No se pueden multiplicar')
# else:
#     for fila in c:
#         print("[", end=" ")
#         for elemento in fila:
#             print(elemento, end=" ")
#         print("]")

# def multiplicar_matrices_n(m1,n):
#     m3 = []
#     for i in range(n):
#         m3 += lct.ProdMtx(m1, m1)
#     if n != 1:
#         res = lct.ProdMtx(m1, m1)
#     else:
#         res = lct.ProdMtx(m1, m1)
#     return res


# 2. Experimentos de las múltiples rendijas clásico probabilístico, con más de dos rendijas.

# def multiplicar_matrices_fr(m1, m2):
 #   if len(m1[0]) == len(m2):
 #       m3 = []
 #       for i in range(len(m1)):
  #          m3.append([])
   #        for j in range(len(m2[0])):
    #            m3[i].append(0)

    #    for i in range(len(m1)):
     #       for j in range(len(m2[0])):
      #          for k in range(len(m1[0])):
       #             m3[i][j] += m1[i][k] * m2[k][j]
        #return m3
    #else:
     #   return None


#def multiplicar_matrices_pr(m1, m2):
 #   if len(m1[0]) == len(m2):
  #      m3 = []
   #     for i in range(len(m1)):
    #        m3.append([])
     #       for j in range(len(m2[0])):
      #          m3[i].append(0)
#
 #       for i in range(len(m1)):
  #          for j in range(len(m2[0])):
   #             for k in range(len(m1[0])):
    #                m3[i][j] += m1[i][k] * m2[k][j]
     #   return m3
    #else:
     #   return None

# 3. Experimento de las múltiples rendijas cuántico.
#def multiplicar_matrices_cplx(m1, m2):
 #   if len(m1[0]) == len(m2):
  #      m3 = []
   #     for i in range(len(m1)):
    #        m3.append([])
     #       for j in range(len(m2[0])):
      #          m3[i].append(0)

       # for i in range(len(m1)):
        #    for j in range(len(m2[0])):
         #       for k in range(len(m1[0])):
          #          m3[i][j] += lc.cplxproduct(m1[i][k], m2[k][j])
        # return m3
    #else:
     #   return None

# 4. Cree una función para graficar con un diagrama de barras que muestre las probabilidades de un vector de estados. La imagen se debe poder guardar en el computador con un formato de imagen.
