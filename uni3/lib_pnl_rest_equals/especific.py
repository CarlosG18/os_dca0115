import sympy as sp

x1, x2, x3, lambda1, lambda2, lambda3, w = sp.symbols('x1 x2 x3 lambda1 lambda2 lambda3 w')

class one_res_two_vars:
    def __init__(self, func_obj, func_res):
        self.func_obj = func_obj
        self.res = func_res

    def calcular(self):
        print(f'condições de primeira ordem:\n')
        
        #vetor gradiente da restrição
        der_res_x1 = sp.diff(self.res, x1)
        der_res_x2 = sp.diff(self.res, x2)
        vetor_grad_res = sp.Matrix([der_res_x1, der_res_x2])
        print(f'- vetor gradiente da funçao de restrição = [{vetor_grad_res[0]} , {vetor_grad_res[1]}]\n')
        
        #montando a funcao aumentada do sistema
        func_aum = self.func_obj + lambda1*(self.res)
        print(f'- função aumentada = {func_aum}\n')

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
        resposta = sp.solve((der_f_x1, der_f_x2,der_f_lb1),(x1, x2, lambda1))
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

class three_res_three_vars:
    def __init__(self, func_obj, func_res1, func_res2, func_res3):
        self.func_obj = func_obj
        self.res1 = func_res1
        self.res2 = func_res2
        self.res3 = func_res3

    def calcular(self):
        print(f'condições de primeira ordem:\n')
        
        #vetor gradiente da restrição 1
        der_res1_x1 = sp.diff(self.res1, x1)
        der_res1_x2 = sp.diff(self.res1, x2)
        der_res1_x3 = sp.diff(self.res1, x3)
        vetor_grad_res1 = sp.Matrix([der_res1_x1, der_res1_x2, der_res1_x3])
        print(f'- vetor gradiente da funçao de restrição 1 = [{vetor_grad_res1[0]} , {vetor_grad_res1[1]}, {vetor_grad_res1[2]}]\n')
        
        #vetor gradiente da restrição 1
        der_res2_x1 = sp.diff(self.res2, x1)
        der_res2_x2 = sp.diff(self.res2, x2)
        der_res2_x3 = sp.diff(self.res2, x3)
        vetor_grad_res2 = sp.Matrix([der_res2_x1, der_res2_x2, der_res2_x3])
        print(f'- vetor gradiente da funçao de restrição 2 = [{vetor_grad_res2[0]} , {vetor_grad_res2[1]}, {vetor_grad_res2[2]}]\n')

        #vetor gradiente da restrição 1
        der_res3_x1 = sp.diff(self.res3, x1)
        der_res3_x2 = sp.diff(self.res3, x2)
        der_res3_x3 = sp.diff(self.res3, x3)
        vetor_grad_res3 = sp.Matrix([der_res3_x1, der_res3_x2, der_res3_x3])
        print(f'- vetor gradiente da funçao de restrição 3 = [{vetor_grad_res3[0]} , {vetor_grad_res3[1]}, {vetor_grad_res3[2]}]\n')

        #montando a funcao aumentada do sistema
        func_aum = self.func_obj + lambda1*(self.res1) + lambda2*(self.res2) + lambda3*(self.res3)
        print(f'- função aumentada = {func_aum}\n')

        #derivada da funcao aumentada em relação a x1
        der_f_x1 = sp.diff(func_aum, x1)
        print(f'- derivada da função aumentada em relação a x1 = {der_f_x1}\n')

        #derivada da funcao aumentada em relação a x2
        der_f_x2 = sp.diff(func_aum, x2)
        print(f'- derivada da função aumentada em relação a x2 = {der_f_x2}\n')

        #derivada da funcao aumentada em relação a x3
        der_f_x3 = sp.diff(func_aum, x3)
        print(f'- derivada da função aumentada em relação a x3 = {der_f_x3}\n')

        #derivada da funcao aumentada em relação a lambda1
        der_f_lb1 = sp.diff(func_aum, lambda1)
        print(f'- derivada da função aumentada em relação a lambda1 = {der_f_lb1}\n')

        #derivada da funcao aumentada em relação a lambda2
        der_f_lb2 = sp.diff(func_aum, lambda2)
        print(f'- derivada da função aumentada em relação a lambda2 = {der_f_lb2}\n')

        #derivada da funcao aumentada em relação a lambda3
        der_f_lb3 = sp.diff(func_aum, lambda3)
        print(f'- derivada da função aumentada em relação a lambda1 = {der_f_lb3}\n')

        #resolvendo o sistema de equações das derivadas:
        resposta = sp.solve((der_f_x1, der_f_x2, der_f_x3, der_f_lb1, der_f_lb2, der_f_lb3),(x1, x2, x3, lambda1, lambda2, lambda3))
        print(f'resposta = {resposta}')

        
        print(f'{"-"*100}\n - condições de segunda ordem\n')

        #aplicando a condição de segunda ordem
        #calculando a hessiana da função aumentada
        hessiana = sp.hessian(func_aum, (x1,x2,x3))
        print(f'- matriz hessiana = {hessiana}\n')

        
        identidade = sp.eye(3)
        m = hessiana - w*identidade
        print(f'matriz m = {m}\n')
        matriz_seg_ord = sp.Matrix([
            [m[0], m[1], m[2], der_res1_x1, der_res1_x2, der_res1_x3],
            [m[3], m[4], m[5], der_res2_x1, der_res2_x2, der_res2_x3],
            [m[6], m[7], m[8], der_res3_x1, der_res3_x2, der_res3_x3],
            [der_res1_x1, der_res2_x1, der_res3_x1,  0, 0, 0],
            [der_res1_x2, der_res2_x2, der_res3_x2, 0, 0, 0],
            [der_res1_x3, der_res2_x3, der_res3_x3, 0, 0, 0]
        ])
        print(f'- matriz de segunda ordem = {matriz_seg_ord}\n')

        #calculando o determinante da matriz de segunda ordem
        det = sp.det(matriz_seg_ord)
        print(f'- determinante da matriz de segunda ordem = {det}\n')

        #valor de w usando o resposta[0]
        equacao0_w = det.subs({x1:resposta[0][0], x2:resposta[0][1], lambda1:resposta[0][2]})
        valor0_w = sp.solve(equacao0_w, w)
        print(f'- valor de w usando o vetor de resposta[0] = {valor0_w}\n')


class two_res_three_vars:
    def __init__(self, func_obj, func_res1, func_res2):
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
        print(f'- vetor gradiente da funçao de restrição 1 = [{vetor_grad_res1[0]} , {vetor_grad_res1[1]}, {vetor_grad_res1[2]}]\n')
        
        #vetor gradiente da restrição 2
        der_res2_x1 = sp.diff(self.res2, x1)
        der_res2_x2 = sp.diff(self.res2, x2)
        der_res2_x3 = sp.diff(self.res2, x3)
        vetor_grad_res2 = sp.Matrix([der_res2_x1, der_res2_x2, der_res2_x3])
        print(f'- vetor gradiente da funçao de restrição 2 = [{vetor_grad_res2[0]} , {vetor_grad_res2[1]}, {vetor_grad_res2[2]}]\n')

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
        print(f'- derivada da função aumentada em relação a x3 = {der_f_x3}\n')

        #derivada da funcao aumentada em relação a lambda1
        der_f_lb1 = sp.diff(func_aum, lambda1)
        print(f'- derivada da função aumentada em relação a lambda1 = {der_f_lb1}\n')

        #derivada da funcao aumentada em relação a lambda2
        der_f_lb2 = sp.diff(func_aum, lambda2)
        print(f'- derivada da função aumentada em relação a lambda2 = {der_f_lb2}\n')

        #resolvendo o sistema de equações das derivadas:
        resposta = sp.solve((der_f_x1, der_f_x2, der_f_x3, der_f_lb1, der_f_lb2),(x1, x2, x3, lambda1, lambda2))
        print(f'resposta = {resposta}')

        
        print(f'{"-"*100}\n - condições de segunda ordem\n')

        #aplicando a condição de segunda ordem
        #calculando a hessiana da função aumentada
        hessiana = sp.hessian(func_aum, (x1,x2,x3))
        print(f'- matriz hessiana = {hessiana}\n')

        identidade = sp.eye(3)
        m = hessiana - w*identidade
        print(f'matriz m = {m}\n')
        matriz_seg_ord = sp.Matrix([
            [m[0], m[1], m[2], der_res1_x1, der_res2_x1],
            [m[3], m[4], m[5], der_res1_x2, der_res2_x2],
            [m[6], m[7], m[8], der_res1_x3, der_res2_x3],
            [der_res1_x1, der_res1_x2, der_res1_x3, 0, 0],
            [der_res2_x1, der_res2_x2, der_res2_x3, 0, 0]
        ])
        print(f'- matriz de segunda ordem = {matriz_seg_ord}\n')

        #calculando o determinante da matriz de segunda ordem
        det = sp.det(matriz_seg_ord)
        print(f'- determinante da matriz de segunda ordem = {det}\n')

        #valor de w usando o resposta[0]
        equacao0_w = det.subs({x1:resposta[0][0], x2:resposta[0][1], lambda1:resposta[0][2], lambda2:resposta[0][3]})
        valor0_w = sp.solve(equacao0_w, w)
        print(f'- valor de w usando o vetor de resposta[0] = {valor0_w}\n')

        #valor de w usando o resposta[1]
        equacao1_w = det.subs({x1:resposta[1][0], x2:resposta[1][1], lambda1:resposta[1][2], lambda2:resposta[1][3]})
        valor1_w = sp.solve(equacao1_w, w)
        print(f'- valor de w usando o vetor de resposta[1] = {valor1_w}\n')
'''
class two_res_two_vars:
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