import numpy as np

matriz_base = np.array([
    [1, -10, -15, -20, 0, 0, 0, 0, 0],
    [0, 2, 3, 1, 1, 0, 0, 0, 100],
    [0, 1, 1, 2, 0, 1, 0, 0, 120],
    [0, 1, 2, 3, 0, 0, 1, 0, 176],
    [0, 1, 2, 1, 0, 0, 0, 1, 132],
  ])
  
vetorB = np.array([0, 100, 120, 176, 132])
vetor_fatorP = np.zeros(5)
candidato_base = {
  "value": 0,
  "index": 0,
  "line": 0,
}
index_base = 0

for i in matriz_base[0, :]:
  if i < candidato_base["value"]:
    candidato_base["value"] = i
    candidato_base["index"] = index_base
  index_base += 1
 
cont = 0
for i in matriz_base[:, 8]:
    vetor_fatorP[cont] = (i/matriz_base[cont, candidato_base["index"]])
    cont += 1


#primeira lapada
matriz_base[3, :] = matriz_base[3, :] / 3

matriz_base[0, :] = matriz_base[3, :] * 20 + matriz_base[0, :]
matriz_base[1, :] = matriz_base[3, :] * -1 + matriz_base[1, :]
matriz_base[2, :] = matriz_base[3, :] * -2 + matriz_base[2, :]
matriz_base[4, :] = matriz_base[3, :] * -1 + matriz_base[4, :]

linha_base = 1
col_base = 2
matriz_base[linha_base, :] = matriz_base[linha_base, :] / matriz_base[linha_base,col_base]

matriz_base[0, :] = matriz_base[linha_base, :] *  + matriz_base[0, :]
matriz_base[1, :] = matriz_base[linha_base, :] * -1 + matriz_base[1, :]
matriz_base[2, :] = matriz_base[linha_base, :] * -2 + matriz_base[2, :]
matriz_base[4, :] = matriz_base[linha_base, :] * -1 + matriz_base[4, :]

print(matriz_base)