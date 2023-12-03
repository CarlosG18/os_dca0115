from lib_pnl_rest_equals.generic import pnl_res_equals
from lib_pnl_rest_equals.especific import one_res_two_vars, three_res_three_vars, two_res_three_vars
import sympy as sp

'''
#questão do material
# definindo as variaves do problema
x1, x2, lambda1, w = sp.symbols('x1 x2 lambda1 w') 

func_obj = 4 - x1**2 - x2**2
func_res = 1 - x1**2 + x2

eq = one_res_two_vars(func_obj, func_res)
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


x1, x2, x3 = sp.symbols('x1 x2 x3') 

func_obj = x2 + x3
func_res1 = 2*x1**2 + 3*x1*x2 + 7*x2
func_res2 = x1**2 + x2**2 + x3**2 -1

problema = pnl_res_equals(func_obj,func_res1,num_variaveis=2)
problema.calcular()
'''
'''
#questao 7 da lista 
x1, x2, x3 = sp.symbols('x1 x2 x3')

func_obj = -x1**2 - 4*x2**2 - 16*x3**2
func_res1 = x1 - 1
func_res2 = x1*x2 - 1
func_res3 = x1*x2*x3 - 1

problema = three_res_three_vars(func_obj, func_res1, func_res2, func_res3)
problema.calcular()
'''

x1, x2, x3 = sp.symbols('x1 x2 x3')

func_obj = x2 + x3
func_res1 = x1 + x2 + x3 -1
func_res2 = x1**2 + x2**2 + x3**2 -1

problema = two_res_three_vars(func_obj, func_res1, func_res2)
problema.calcular()
