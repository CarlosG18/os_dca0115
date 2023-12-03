from lib_pnl_rest_equals.master import pnl_res_equals
import sympy as sp

'''
#questão do material
# definindo as variaves do problema
x1, x2, lambda1, w = sp.symbols('x1 x2 lambda1 w') 

func_obj = 4 - x1**2 - x2**2
func_res = 1 - x1**2 + x2

eq = one_res(func_obj, func_res)
eq.calcular()
'''
#-------------------------------------------------------------------------------------------------
'''
#questão do material
# definindo as variaves do problema
x1, x2, lambda1, w = sp.symbols('x1 x2 lambda1 w') 

func_obj = x1**2 + x2**2 + 3*x1*x2 + 6*x1 + 19*x2
func_res = 3*x2 + x1 - 5

eq = Pnl_Equals(func_obj, func_res)
eq.calcular()


#-------------------------------------------------------------------------------------------------

#questão 4 da lista
# definindo as variaves do problema
x1, x2, x3 = sp.symbols('x1 x2 x3') 

func_obj = x2 + x3
func_res1 = x1 + x2 + x3 -1
func_res2 = x1**2 + x2**2 + x3**2 -1

eq = more_res(func_obj, func_res1, func_res2)
eq.calcular()
'''

x1, x2, x3 = sp.symbols('x1 x2 x3') 

func_obj = x2 + x3
func_res1 = 2*x1**2 + 3*x1*x2 + 7*x2
func_res2 = x1**2 + x2**2 + x3**2 -1

problema = pnl_res_equals(func_obj,func_res1,num_variaveis=2)
problema.calcular()