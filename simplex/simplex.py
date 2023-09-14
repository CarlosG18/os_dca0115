import numpy as np

def isNegative(array):
  return np.any(array < 0)

def simplex(matriz_base, FOB, var_Nbasic, var_basic, vars):
  iteracoes = 0

  (lin, col) = matriz_base.shape

  while(isNegative(FOB)):
    print(f'iteração de numero {iteracoes+1}\n')

    #encontrar a coluna base
    col_base = np.where(FOB == FOB.min())
    print(f'menor numero na FOB/base = {FOB.min()}')
    print(f'candidato a entrar na base = {vars[col_base[0][0]]}')

    #encontrar a linha base
    tam_vetor_fatorP = 0

    for i in range(lin):
      if matriz_base[i,col_base[0][0]] >= 0:
        tam_vetor_fatorP += 1
    vetor_fatorP = np.zeros(tam_vetor_fatorP)
    #print(f'tam vetorp ={tam_vetor_fatorP}, lin = {lin}')

    cont_vetorP = 0
    #calculando o fator p
    for i in range(lin):
      #print(f'valor de i = {i}')
      #print(f'valor de matriz_base[{i},{col-1}] = {matriz_base[i,col-1]}')
      #print(f'valor da coluna base = {col_base[0][0]}')
      print(f'fatorP{i} = {matriz_base[i,col-1]}/{matriz_base[i,col_base[0][0]]} = {matriz_base[i,col-1] / matriz_base[i,col_base[0][0]]}')
      #print(f'contador do vetor p = {cont_vetorP}')
      if matriz_base[i,col_base[0][0]] >= 0:
        vetor_fatorP[cont_vetorP] = matriz_base[i,col-1] / matriz_base[i,col_base[0][0]]
        cont_vetorP += 1
    print(f'vetor de fator p = {vetor_fatorP}')
    print(f'menor valor do vetor_fatorP = {vetor_fatorP.min()}')
    linha_base = np.where(vetor_fatorP == vetor_fatorP.min())
    print(f'variavel a sair da base = {var_basic[linha_base[0][0]]}')

    #troca das variaves basicas e não basicas
    new_varBasic = vars[col_base[0][0]]
    out_varBasic = var_basic[linha_base[0][0]]
    index_Nbasic = np.where(var_Nbasic == new_varBasic)
    index_basic = np.where(var_basic == out_varBasic)
    var_Nbasic[index_Nbasic[0][0]] = out_varBasic
    var_basic[index_basic[0][0]] = new_varBasic

    #fazendo a eliminação de gaus-jordan
    matriz_base[linha_base[0][0], :] = matriz_base[linha_base[0][0], :] / matriz_base[linha_base[0][0], col_base[0][0]]
    FOB = matriz_base[linha_base[0][0], :] * -FOB[col_base[0][0]] + FOB

    print(f'L{linha_base[0][0]} = L{linha_base[0][0]} / {matriz_base[linha_base[0][0],col_base[0][0]]}')
    print(matriz_base,'\n\n')
    
    for i in range(lin):
      if i != linha_base[0][0]:
        print(f'l{i} = -{matriz_base[i, col_base[0][0]]}L{linha_base[0][0]}+L{i}')
        matriz_base[i, :] = matriz_base[linha_base[0][0], :] * -matriz_base[i, col_base[0][0]] + matriz_base[i, :]
        print(matriz_base, '\n\n')

    print(f'depois da {iteracoes+1}ª lapada \n {matriz_base}')
    print(f'variaveis basicas = {var_basic}')
    print(f'variaveis não basicas = {var_Nbasic}')
    print(f'função objetivo/base {FOB} \n')
    print('-'*100)
    iteracoes += 1

  #imprimindo o valor final
  print(f'resultado final: \n - resultado das variaveis basicas:\n')
  for i in range(lin):
    print(f'- {var_basic[i]} = {matriz_base[i, col-1]:.2f}\n')
    
    
  #questao 2 da prova
matriz_base = np.array([
    [1.,0,1,0,0,0,6],
    [0,1,0,1,0,0,5],
    [2,3,0,0,1,0,18],
    [1,-1,0,0,0,1,2]
  ])

FOB = np.array([-1, -2, 0, 0, 0, 0, 0])
var_Nbasic = np.array(['x1','x2'])
var_basic = np.array(['s1','s2','s3','s4'])
vars = np.array(['x1','x2','s1','s2','s3','s4'])

simplex(matriz_base, FOB, var_Nbasic, var_basic, vars)