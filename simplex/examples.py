import numpy as np
from lib_simplex.simplex import simplex 

#questão 2 da prova 1 - periodo 2021.2

matriz_base = np.array([
    [1.,0,1,0,0,0,6],
    [0,1,0,1,0,0,5],
    [2,3,0,0,1,0,18],
    [1,-1,0,0,0,1,2]
  ])

FOB = np.array([-1., -2, 0, 0, 0, 0, 0])
var_Nbasic = np.array(['x1','x2'])
var_basic = np.array(['s1','s2','s3','s4'])
vars = np.array(['x1','x2','s1','s2','s3','s4'])

simplex(matriz_base, FOB, var_Nbasic, var_basic, vars)

'''
#questao 2 da lista

matriz_base = np.array([
    [2,3,4,1,0,10],
    [5,6,2,0,1,12],
  ])

FOB = np.array([-3,-2,-5,0,0,0])
var_Nbasic = np.array(['x1','x2','x3'])
var_basic = np.array(['s1','s2'])
vars = np.array(['x1','x2','x3','s1','s2'])

simplex(matriz_base, FOB, var_Nbasic, var_basic, vars)

#questao do slide

matriz_base = np.array([
    [1.,0,1,0,0,0,3],
    [0,1,0,1,0,0,4],
    [1,1,0,0,1,0,6],
    [1,3,0,0,0,1,13],
  ])

FOB = np.array([-12.,-15,0,0,0,0,0])
var_Nbasic = np.array(['x1','x2'])
var_basic = np.array(['x3','x4','x5','x6'])
vars = np.array(['x1','x2','x3','x4','x5','x6'])

simplex(matriz_base, FOB, var_Nbasic, var_basic, vars)

#outra questao do slide

matriz_base = np.array([
    [1.,0,1,0,0,3],
    [0,1,0,1,0,4],
    [1,3,0,0,1,13],
  ])

FOB = np.array([-1.,-3,0,0,0,0])
var_Nbasic = np.array(['x1','x2'])
var_basic = np.array(['x3','x4','x5'])
vars = np.array(['x1','x2','x3','x4','x5'])

simplex(matriz_base, FOB, var_Nbasic, var_basic, vars)

#questao 7 da lista

matriz_base = np.array([
    [-1.,2,1,0,0,4],
    [1,1,0,1,0,6],
    [1,3,0,0,1,9],
  ])

FOB = np.array([-1.,-3,0,0,0,0])
var_Nbasic = np.array(['x1','x2'])
var_basic = np.array(['x3','x4','x5'])
vars = np.array(['x1','x2','x3','x4','x5'])

simplex(matriz_base, FOB, var_Nbasic, var_basic, vars)

#questao 12 da lista

matriz_base = np.array([
    [1,0,1,0,0,0,8],
    [0,1,0,1,0,0,12],
    [6,4,0,0,-1,1,36],
  ])

FOB = np.array([-36,-30,0,0,5,0,-180])
var_Nbasic = np.array(['x1','x2','s3'])
var_basic = np.array(['s1','s2','a1'])
vars = np.array(['x1','x2','s1','s2','s3','a1'])

simplex(matriz_base, FOB, var_Nbasic, var_basic, vars)

#questao do video

matriz_base = np.array([
    [1,1,0,1,0,0,0,20],
    [1,0,1,0,0,1,0,5],
    [0,1,1,0,-1,0,1,10],
  ])

FOB = np.array([-21,-19,-43,0,20,0,0,-300])
var_Nbasic = np.array(['x1','x2','x3','s2'])
var_basic = np.array(['s1','a1','a2'])
vars = np.array(['x1','x2','x3','s1','s2','a1','a2'])

simplex(matriz_base, FOB, var_Nbasic, var_basic, vars)

#prova de 2023.1 questao 1

#max
matriz_base = np.array([
    [1.,0,1,0,0,0,0,6],
    [0,1,0,1,0,0,0,5],
    [2,3,0,0,-1,0,1,5],
    [1,-1,0,0,0,1,0,2],
  ])

FOB = np.array([-3.,-5,0,0,1,0,0,-5])
var_Nbasic = np.array(['x1','x2','x5'])
var_basic = np.array(['x3','x4','a1','x6'])
vars = np.array(['x1','x2','x3','x4','x5','x6','a1'])

simplex(matriz_base, FOB, var_Nbasic, var_basic, vars)

#questao 2

matriz_base = np.array([
    [1.,0,1,0,0,0,0,6],
    [0,1,0,1,0,0,0,5],
    [2,3,0,0,1,0,0,12],
    [1,-1,0,0,0,-1,1,1],
  ])

FOB = np.array([-2.,-1,0,0,0,1,0,-1])
var_Nbasic = np.array(['x1','x2','x6'])
var_basic = np.array(['x3','x4','x5','a1'])
vars = np.array(['x1','x2','x3','x4','x5','x6','a1'])

simplex(matriz_base, FOB, var_Nbasic, var_basic, vars)

#questao 3

matriz_base = np.array([
    [2.,1,-1,1,0,0,2],
    [2,-1,5,0,1,0,6],
    [4,1,1,0,0,1,6],
  ])

FOB = np.array([-1.,-2,1,0,0,0,0])
var_Nbasic = np.array(['x1','x2','x3'])
var_basic = np.array(['x4','x5','x6'])
vars = np.array(['x1','x2','x3','x4','x5','x6'])

simplex(matriz_base, FOB, var_Nbasic, var_basic, vars)

#questao 1 da lista

matriz_base = np.array([
    [-1,1,1,0,0,0,0,2],
    [3,5,0,-1,0,1,0,15],
    [5,4,0,0,-1,0,1,20],
  ])

FOB = np.array([-15.,-18,0,1,1,0,0,-35])
var_Nbasic = np.array(['x1','x2','x4','x5'])a
var_basic = np.array(['x3','a1','a2'])
vars = np.array(['x1','x2','x3','x4','x5','a1','a2'])

simplex(matriz_base, FOB, var_Nbasic, var_basic, vars)

#questao 5

matriz_base = np.array([
    [1.,1,2,1,0,4],
    [4,-5,3,0,1,30],
  ])

FOB = np.array([-4.,-2,-2,0,0,0])
var_Nbasic = np.array(['x1','x2','x3'])
var_basic = np.array(['x4','x5'])
vars = np.array(['x1','x2','x3','x4','x5'])

simplex(matriz_base, FOB, var_Nbasic, var_basic, vars)
'''