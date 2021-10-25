# import Libcplx as lc
import EspaVectCplx as lct
# import SaltoClásicoAQuantico as lst
# import Estados_cuanticos as qs
# import math
import unittest

class TestCplxOperations(unittest.TestCase):


    # def test_adVector(self):
    #    suma = lct.adVector([(1, -2.5), (2, 1)], [(3, 0), (7, -3.8)])
    #    self.assertEqual(suma, [(4, -2.5), (9, -2.8)])
    
    ##def test_invVector(self):
      ##  invAd = lct.invVector([(6, -4), (7, 3)])
        ##self.assertEqual(invAd, [(-6, 4), (-7, -3)])
    # #
    # # def test_MultEscalarVector(self):
    # #     Msv = lct.MultEscalarVector((3,2),[(6,3),(5,1)])
    # #     self.assertEqual(Msv,[(12,21),(13,13)])
    # #
    # def test_sumaMatrix(self):
    #    sumatx = lct.adVector([(1,2),(3,4)],[(4,3),(2,1)])
    #    self.assertEqual(sumatx,[(5,5),(5,5)])
    # #
    # # def test_invAdMtx(self):
    # #     InvAdM = lct.invAdMtx([[(4, 3), (2, 1)],[(9, 8), (7, 5)]])
    # #     self.assertEqual(InvAdM, [[(-4, -3), (-2, -1)],[(-9, -8), (-7, -5)]])
    # #
    # # def test_MultEscMtx(self):
    # #     MultEscMtx = lct.MultEscMtx((3, 2), [[(6, 3), (5, 1)], [(0, 0), (4, 0)]])
    # #     self.assertEqual(MultEscMtx, [[(12, 21), (13, 13)], [(0, 0), (12, 8)]])
    # #
    # # def test_trMtx(self):
    # #     trMt = lct.trMtx([[(1,0),(2,3)],[(4,5),(1,0)]])
    # #     self.assertEqual(trMt,[[(1,0),(4,5)],[(2,3),(1,0)]])
    # #
    # # def test_conjMtx(self):
    # #     conjM = lct.conjMtx([[(1, 0), (2, 3)], [(4, 5), (1, 0)]])
    # #     self.assertEqual(conjM, [[(1, 0), (2, -3)], [(4, -5), (1, 0)]])
    # #
    # # def test_adjMtx(self):
    # #     HMt = lct.adjMtx([[(6,-3),(2,12),(0,-19)],[(0,0),(5,2.1),(17,0)],[(1,0),(2,5),(3,-4.5)]])
    # #     self.assertEqual(HMt,[[(6,3),(0,0),(1,0)],[(2,-12),(5,-2.1),(2,-5)],[(0,19),(17,0),(3,4.5)]])
    # #
    # # def test_ProdMtx(self):
    # #     PrMtx = lct.ProdMtx([[(4,0),(-1,0)],[(2,0),(-1,0)]], [[(1,0)],[(2,0)]])
    # #     self.assertEqual(PrMtx,[[(2,0)],[(4,0)]])
    #
    # # def test_MtxVec(self):
    # #     Mv = lct.MtxVec([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,1,0,0],[0,0,1,0,0,0],[1,0,0,0,1,0]],[[6],[2],[1],[5],[3],[10]])
    # #     self.assertEqual(Mv, [[0],[0],[12],[5],[1],[9]])
    # #
    # # def test_vectorPrInt(self):
    # #     VPI = lct.vectorPrInt([3,1,2])
    # #     self.assertEqual(VPI, 14)
    # #
    # # def test_vectorNorm(self):
    # #     vNorm = lct.vectorNorm([3,5,8,1,1])
    # #     self.assertEqual(vNorm, 10)
    # #
    # # def test_disV(self):
    # #     dv = lct.disV([3,1,2],[2,2,-1])
    # #     self.assertEqual(dv, sqrt(11))
    # #
    # # def test_hermMtx(self):
    # #     hm = lct.hermMtx([[(7,0),(6,5)],[(6,-5),(-3,0)]])
    # #     self.assertEqual(hm, True)
    # #
    # # def test_Unitaria(self):
    # #     mtxu = lct.Unitaria([[cos(90),-sin(90),0],[sin(90),cos(90),0],[0,0,1]])
    # #     self.assertEqual(mtxu, True)
    # #
    # # def test_vectorTsorProduct(self):
    # #     Tp = lct.vectorTsorProduct([2,3],[4,6,3])
    # #     self.assertEqual(Tp, [[8],[12],[6],[12],[18],[9]])
    # #
    # def test_multiplicar_matrices(self):
    #     mm = lst.multiplicar_matrices([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,1,0,0],[0,0,1,0,0,0],[1,0,0,0,1,0]],[[6],[2],[1],[5],[3],[10]])
    #     self.assertEqual(mm, [[0],[0],[12],[5],[1],[9]])
    #
    # # def test_multiplicar_matrices_n(self):
    # #     n = lst.multiplicar_matrices_n([[0,0,0,0,0,0,0,0],[1/2,0,0,0,0,0,0,0],[1/2,0,0,0,0,0,0,0],[0,1/3,0,0,0,0,0,0],[0,1/3,0,1,0,0,0,0],[0,1/3,1/3,0,0,1,0,0],[0,0,1/3,0,0,0,1,0],[0,0,1/3,0,0,0,0,1]],2)
    # #     self.assertEqual(n, [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[1/6,1/3,0,1,0,0,0,0],[1/6,1/3,0,0,1,0,0,0],[1/3,1/3,1/3,0,0,1,0,0],[1/6,0,1/3,0,0,0,1,0],[1/6,0,1/3,0,0,0,0,1]])
    #
    # def test_multiplicar_matrices_fr(self):
    #     mmfr = lst.multiplicar_matrices_fr([[0,1/6,5/6],[1/3,1/2,1/6],[2/3,1/3,0]],[[1/6],[1/6],[2/3]])
    #     self.assertEqual(mmfr, [[21/36],[9/36],[6/36]])
    #
    # # def test_multiplicar_matrices_pr(self):
    # #     pr = lst.multiplicar_matrices_pr([[0,1/6,5/6],[1/3,1/2,1/6],[2/3,1/3,0]],[[1/6],[1/6],[2/3]])
    # #     self.assertEqual(pr, )
    #
    # def test_multiplicar_matrices_cplx(self):
    #     mmc = lst.multiplicar_matrices_cplx([[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[(-1,1)/sqrt(12),(-1,1)/sqrt(6),0,1,0,0,0,0],[(-1,1)/sqrt(12),(-1,-1)/sqrt(6),0,0,1,0,0,0],[0,(-1,1)/sqrt(6),(1,-1)/sqrt(6),0,0,1,0,0],[(-1,-1)/sqrt(12),0,(-1,-1)/sqrt(6),0,0,0,1,0],[(-1,1)/sqrt(12),0,(1,-1)/sqrt(6),0,0,0,0,1]],[[1],[0],[0],[0],[0],[0],[0],[0]])
    #     self.assertEqual(mmc, [[0],[0],[0],[(-1,1)/sqrt(12)],[(-1,1)/sqrt(12)],[0],[(-1,-1)/sqrt(12)],[(-1,1)/sqrt(12)]])

    # def test_probParticleInLine(self):
    #     PPIL = qs.probParticleInLine(3, [(-3,-1),(0,-2),(0,1),(2,0)])
    #     self.assertEqual(PPIL, 1/19)

    # def test_probTransition(self):
    #    pt = qs.probTransition([(1,0),(0,-1)],[(0,1),(1,0)])
    #    self.assertEqual(pt, (0,-2))

if __name__ == '__main__':
    unittest.main()
