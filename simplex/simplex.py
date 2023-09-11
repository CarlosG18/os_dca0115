import numpy as np

def isNegative(array):
  return np.any(array < 0)

def simplex(matriz_base, FOB, var_Nbasic, var_basic):
  iteracoes = 0

  (lin, col) = matriz_base.shape

  while(isNegative(FOB)):
    print(f'iteração de numero {iteracoes}\n')

    #encontrar a coluna base
    col_base = np.where(FOB == FOB.min())
    print(f'coluna base = {col_base[0][0]} candidato a entrar na base = {var_Nbasic[col_base[0][0]]}')

    #encontrar a linha base
    vetor_fatorP = np.zeros(lin-1)
    for i in range(lin-1):
      vetor_fatorP[i] = matriz_base[i,col-1] / matriz_base[i,col_base[0][0]]
    linha_base = np.where(vetor_fatorP == vetor_fatorP.min())
    print(f'linha base = {linha_base[0][0]} - variavel a sair da base = {var_basic[linha_base[0][0]]}')

    #troca das variaves basicas e não basicas
    new_varBasic = var_Nbasic[col_base[0][0]]
    out_varBasic = var_basic[linha_base[0][0]]
    index_Nbasic = np.where(var_Nbasic == new_varBasic)
    index_basic = np.where(var_basic == out_varBasic)
    var_Nbasic[index_Nbasic[0][0]] = out_varBasic
    var_basic[index_basic[0][0]] = new_varBasic

    #fazendo a eliminação de gaus-jordan
    matriz_base[linha_base[0][0], :] = matriz_base[linha_base[0][0], :] / matriz_base[linha_base[0][0], col_base[0][0]]
    FOB = matriz_base[linha_base[0][0], :] * -FOB[col_base[0][0]] + FOB

    print(f'linha {linha_base[0][0]} pivotizada \n {matriz_base[linha_base[0][0], :]} \n')
    for i in range(lin):
      if i != linha_base[0][0]:
        matriz_base[i, :] = matriz_base[linha_base[0][0], :] * -matriz_base[i, col_base[0][0]] + matriz_base[i, :]

    print(f'depois da {iteracoes+1}ª lapada \n {matriz_base}')
    print(f'variaveis basicas = {var_basic}')
    print(f'variaveis não basicas = {var_Nbasic}')
    print(f'função objetivo {FOB} \n')
    print('-'*80)
    iteracoes += 1

  #imprimindo o valor final
  print(f'resultado final: \n - resultado das variaveis basicas:\n')
  for i in range(lin):
    print(f'- {var_basic[i]} = {matriz_base[i, col-1]:.2f}\n')