import sympy as sp

# definindo as variaves do problema
for var in range(1,10):
    exec(f'x{var} = sp.symbols("x{var}")')
    exec(f'lambda{var} = sp.symbols("lambda{var}")')
w = sp.symbols("w")

class pnl_res_equals:

    def __init__(self, func_obj, *func_res, num_variaveis):
        self.func_obj = func_obj
        self.res = list(func_res)       
        self.num_vars = num_variaveis
        
    def calcular(self):
        print(f'condições de primeira ordem:\n')
        derivadas = list()
        
        #derivada de cada restrição
        for i in range(1, self.num_vars+1):
            for index_res in range(len(self.res)):
                exec(f'der_res{index_res}_x{i} = sp.diff(self.res[{index_res}], x{i})')   
                exec('derivada = {{ "restrição": {}, "variavel": {}, "resultado": der_res{}_x{}}}'.format(self.res[index_res], i, index_res, i,))
                exec(f'derivadas.append(derivada)')   
        
        for der in derivadas:
            for key, value in der.items():
                print(f'{key} - {value}')
            print('\n')

        func_aum = self.func_obj
        soma_res = 5
        #montando a funcao aumentada do sistema
        for i in range(len(self.res)):
            exec(f'soma_res += lambda{i+1}*self.res[{i}]')
        func_aum += lambda1*self.res[0]
        print(f'- função aumentada = {func_aum}\n')

        '''
        #derivada da funcao aumentada em relação a x1
        der_f_x1 = sp.diff(func_aum, x1)
        print(f'- derivada da função aumentada em relação a x1 = {der_f_x1}\n')

        #derivada da funcao aumentada em relação a x2
        der_f_x2 = sp.diff(func_aum, x2)
        print(f'- derivada da função aumentada em relação a x2 = {der_f_x2}\n')

        #derivada da funcao aumentada em relação a lambda1
        der_f_lb1 = sp.diff(func_aum, lambda1)
        print(f'- derivada da função aumentada em relação a lambda1 = {der_f_lb1}\n')

        #resolvendo o sistema de equações das derivadas:
        resposta = sp.solve((der_f_x1, der_f_x2, der_f_lb1),(x1, x2, lambda1))
        print(f'resposta = {resposta}')

        print(f'{"-"*100}\n - condições de segunda ordem\n')

        #aplicando a condição de segunda ordem
        #calculando a hessiana da função aumentada
        hessiana = sp.hessian(func_aum, (x1,x2))
        print(f'- matriz hessiana = {hessiana}\n')

        identidade = sp.eye(2)
        m = hessiana - w*identidade
        print(f'matriz m = {m}\n')
        matriz_seg_ord = sp.Matrix([
            [m[0], m[1], der_res_x1],
            [m[2], m[3], der_res_x2],
            [der_res_x1, der_res_x2, 0]
        ])
        print(f'- matriz de segunda ordem = {matriz_seg_ord}\n')

        #calculando o determinante da matriz de segunda ordem
        det = sp.det(matriz_seg_ord)
        print(f'- determinante da matriz de segunda ordem = {det}\n')

        #valor de w usando o resposta[0]
        equacao0_w = det.subs({x1:resposta[0][0], x2:resposta[0][1], lambda1:resposta[0][2]})
        valor0_w = sp.solve(equacao0_w, w)
        print(f'- valor de w usando o vetor de resposta[0] = {valor0_w}\n')

        #valor de w usando o resposta[1]
        equacao1_w = det.subs({x1:resposta[1][0], x2:resposta[1][1], lambda1:resposta[1][2]})
        valor1_w = sp.solve(equacao1_w, w)
        print(f'- valor de w usando o vetor de resposta[1] = {valor1_w}\n')
        '''
'''        
class more_res:
    def __init__(self, func_obj, func_res1 , func_res2):
        self.func_obj = func_obj
        self.res1 = func_res1
        self.res2 = func_res2

    def calcular(self):
        print(f'condições de primeira ordem:\n')
        
        #vetor gradiente da restrição 1
        der_res1_x1 = sp.diff(self.res1, x1)
        der_res1_x2 = sp.diff(self.res1, x2)
        der_res1_x3 = sp.diff(self.res1, x3)
        vetor_grad_res1 = sp.Matrix([der_res1_x1, der_res1_x2, der_res1_x3])
        print(f'- vetor gradiente da funçao de restrição = [{vetor_grad_res1[0]} , {vetor_grad_res1[1]}, {vetor_grad_res1[2]}]\n')
        
        #vetor gradiente da restrição
        der_res2_x1 = sp.diff(self.res2, x1)
        der_res2_x2 = sp.diff(self.res2, x2)
        der_res2_x3 = sp.diff(self.res2, x3)
        vetor_grad_res2 = sp.Matrix([der_res2_x1, der_res2_x2, der_res2_x3])
        print(f'- vetor gradiente da funçao de restrição = [{vetor_grad_res2[0]} , {vetor_grad_res2[1]}, {vetor_grad_res2[2]}]\n')

        #montando a funcao aumentada do sistema
        func_aum = self.func_obj + lambda1*(self.res1) + lambda2*(self.res2)
        print(f'- função aumentada = {func_aum}\n')

        #derivada da funcao aumentada em relação a x1
        der_f_x1 = sp.diff(func_aum, x1)
        print(f'- derivada da função aumentada em relação a x1 = {der_f_x1}\n')

        #derivada da funcao aumentada em relação a x2
        der_f_x2 = sp.diff(func_aum, x2)
        print(f'- derivada da função aumentada em relação a x2 = {der_f_x2}\n')

        #derivada da funcao aumentada em relação a x3
        der_f_x3 = sp.diff(func_aum, x3)
        print(f'- derivada da função aumentada em relação a x2 = {der_f_x3}\n')

        #derivada da funcao aumentada em relação a lambda1
        der_f_lb1 = sp.diff(func_aum, lambda1)
        print(f'- derivada da função aumentada em relação a lambda1 = {der_f_lb1}\n')

        #derivada da funcao aumentada em relação a lambda2
        der_f_lb2 = sp.diff(func_aum, lambda2)
        print(f'- derivada da função aumentada em relação a lambda2 = {der_f_lb2}\n')

        #resolvendo o sistema de equações das derivadas:
        resposta = sp.solve((der_f_x1, der_f_x2,der_f_x3,der_f_lb1,der_f_lb2),(x1, x2, x3, lambda1, lambda2))
        print(f'resposta = {resposta}')

        print(f'{"-"*100}\n - condições de segunda ordem\n')

        #aplicando a condição de segunda ordem
        #calculando a hessiana da função aumentada
        hessiana = sp.hessian(func_aum, (x1,x2))
        print(f'- matriz hessiana = {hessiana}\n')

        identidade = sp.eye(2)
        m = hessiana - w*identidade
        print(f'matriz m = {m}\n')
        matriz_seg_ord = sp.Matrix([
            [m[0], m[1], der_res_x1],
            [m[2], m[3], der_res_x2],
            [der_res_x1, der_res_x2, 0]
        ])
        print(f'- matriz de segunda ordem = {matriz_seg_ord}\n')

        #calculando o determinante da matriz de segunda ordem
        det = sp.det(matriz_seg_ord)
        print(f'- determinante da matriz de segunda ordem = {det}\n')

        #valor de w usando o resposta[0]
        equacao0_w = det.subs({x1:resposta[0][0], x2:resposta[0][1], lambda1:resposta[0][2]})
        valor0_w = sp.solve(equacao0_w, w)
        print(f'- valor de w usando o vetor de resposta[0] = {valor0_w}\n')

        #valor de w usando o resposta[1]
        equacao1_w = det.subs({x1:resposta[1][0], x2:resposta[1][1], lambda1:resposta[1][2]})
        valor1_w = sp.solve(equacao1_w, w)
        print(f'- valor de w usando o vetor de resposta[1] = {valor1_w}\n')
    '''







