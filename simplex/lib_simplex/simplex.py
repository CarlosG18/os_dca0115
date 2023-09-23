import numpy as np

def linha_base_calc(matriz_base, col_base):
  #obtendo a dimensão da matriz_base
  (lin,col) = matriz_base.shape
  vetor_fatorP = np.zeros(lin)
  vetor_altera = np.zeros(lin)
  #calculando os valores dos fatores P - apenas para valores dos elementos da coluna_base > 0
  for i in range(lin):
    print(f'fatorP{i} = {matriz_base[i,col-1]}/{matriz_base[i,col_base]} = {matriz_base[i,col-1] / matriz_base[i,col_base]}')
    if matriz_base[i,col_base] > 0:
      vetor_fatorP[i] = matriz_base[i,col-1] / matriz_base[i,col_base]
      #atualizando o vetor_altera para indicar qual valor foi alterado no vetor_fatorP
      vetor_altera[i] = 1

  #obtendo o menor valor do vetor_fatorP
  #definindo o valor inicial para a variavel menor valor
  for i in range(lin):
    if vetor_altera[i] != 0 and vetor_fatorP[i] != 'inf':
      menor_valor = vetor_fatorP[i]
      break
  #verificando qual o menor valor e trocando com a var menor_valor
  for i in range(lin):
    if vetor_fatorP[i] < menor_valor and vetor_altera[i] != 0:
      menor_valor = vetor_fatorP[i]
  linha_base = np.where(vetor_fatorP == menor_valor)
  print(f'menor valor = {menor_valor}')
  return linha_base[0][0]

def isNegative(array):
  return np.any(array < 0)

def simplex(matriz_base, FOB, var_Nbasic, var_basic, vars):
  iteracoes = 0

  (lin, col) = matriz_base.shape

  while(isNegative(FOB)):
    print(f'iteração de numero {iteracoes+1}\n')

    #encontrar a coluna base
    ajustFOB = np.zeros(col-1)
    ajustFOB = FOB[:-1]
    col_base = np.where(FOB == ajustFOB.min())
    print(f'menor numero na FOB/base = {ajustFOB.min()}')
    print(f'candidato a entrar na base = {vars[col_base[0][0]]}')

    #encontrar a linha base
    linha_base = linha_base_calc(matriz_base, col_base[0][0])
    print(f'variavel a sair da base = {var_basic[linha_base]}\n\n')

    #troca das variaves basicas e não basicas
    new_varBasic = vars[col_base[0][0]]
    out_varBasic = var_basic[linha_base]
    index_Nbasic = np.where(var_Nbasic == new_varBasic)
    index_basic = np.where(var_basic == out_varBasic)
    var_Nbasic[index_Nbasic[0][0]] = out_varBasic
    var_basic[index_basic[0][0]] = new_varBasic

    #fazendo a eliminação de gaus-jordan
    print(f'L{linha_base} = L{linha_base} / {matriz_base[linha_base,col_base[0][0]]}')
    matriz_base[linha_base, :] = matriz_base[linha_base, :] / matriz_base[linha_base, col_base[0][0]]
    FOB = matriz_base[linha_base, :] * -FOB[col_base[0][0]] + FOB
    print(matriz_base,'\n\n')

    for i in range(lin):
      if i != linha_base:
        print(f'l{i} = -{matriz_base[i, col_base[0][0]]}L{linha_base}+L{i}')
        matriz_base[i, :] = matriz_base[linha_base, :] * -matriz_base[i, col_base[0][0]] + matriz_base[i, :]
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
  print(f'- valor otimo da função objetivo = {FOB[col-1]} \n\n')
  print(f'variaveis basicas = {var_basic}')
  print(f'variaveis não basicas = {var_Nbasic}')
  print(f'função objetivo/base {FOB} \n')