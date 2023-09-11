import numpy as np

def isNegative(array):
  return np.any(array < 0)

matriz_base = np.array([
    [0, 2, 3, 1, 1, 0, 0, 0, 100],
    [0, 1, 1, 2, 0, 1, 0, 0, 120],
    [0, 1, 2, 3, 0, 0, 1, 0, 176],
    [0, 1, 2, 1, 0, 0, 0, 1, 132],
  ])

FOB = np.array([1, -10, -15, -20, 0, 0, 0, 0, 0])

matriz_base = np.array([
    
])

(lin, col) = matriz_base.shape

while(isNegative(FOB)):
  #encontrar a coluna base
  col_base = np.where(FOB == FOB.min())
  print(f'coluna base = {col_base[0]}')

  #encontrar a linha base
  vetor_fatorP = np.zeros(lin-1)
  for i in range(lin-1):
    vetor_fatorP[i] = matriz_base[i,col-1] / matriz_base[i,col_base[0][0]]
  linha_base = np.where(vetor_fatorP == vetor_fatorP.min())
  print(f'linha base = {linha_base[0][0]}')

  #fazendo a eliminação de gaus-jordan
  matriz_base[linha_base[0][0], :] = matriz_base[linha_base[0][0], :] / matriz_base[linha_base[0][0], col_base[0][0]]
  FOB = matriz_base[linha_base[0][0], :] * -FOB[col_base[0][0]] + FOB

  print(f'linha {linha_base[0][0]} pivotizada \n {matriz_base}')
  for i in range(lin):
    if i != linha_base[0][0]:
      matriz_base[i, :] = matriz_base[linha_base[0][0], :] * -matriz_base[i, col_base[0][0]] + matriz_base[i, :]  

  print(f'função objetivo {FOB}')
  print(isNegative(FOB))
  print(f'depois da primeira lapada \n {matriz_base}')