from numpy.linalg import LinAlgError
from sympy.core.sympify import SympifyError
from sympy.ntheory.generate import prime
from functions import Functions
from sympy import symbols, integrate
import math
import numpy as np
import re
import sys


class ServiceFunction():
    def __init__(self, matrix_a=[], matrix_b=[]):
        self.matrix_a = matrix_a
        self.matrix_b = matrix_b

    def calculate_matrix_a(self, polinomic_function, w_p, symbol, inf, sup):
        try:
            symbol_to_integrate = symbols(symbol)
            j = 0
            i = 0
            lenght = (len(polinomic_function)*len(polinomic_function)) - 1
            print(polinomic_function)
            while len(self.matrix_a) <= lenght:
                integrate_func = integrate((polinomic_function[i]+'*'+polinomic_function[j]+'*'+w_p), (symbol_to_integrate, inf, sup)).evalf()
                i += 1
                self.matrix_a.append(float(integrate_func))
                if i == len(polinomic_function):
                    i = 0
                    j += 1
            return self.matrix_a
        except SyntaxError as err:
            return (f'Expresion mal ingresada (error computacional: {err}')
            sys.exit()
        except ValueError as err:
            return (f'Expresion mal ingresada (error computacional: {err}')
            sys.exit()
        except SympifyError as err:
            return (f'Expresion mal ingresada (error computacional: {err}')
            sys.exit()

    def calculate_matrix_b(self, function, polinomic_function, symbol, inf, sup):
        try:
            for i in range(len(polinomic_function)):
                integrate_func = integrate((polinomic_function[i]+'*'+function), (symbol, inf, sup)).evalf()
                self.matrix_b.append(integrate_func)
            return self.matrix_b
        except SyntaxError as err:
            print(f'Expresion mal ingresada (error computacional: {err}')
            sys.exit()
        except ValueError as err:
            print(f'Expresion mal ingresada (error computacional: {err}')
            sys.exit()
        except SympifyError as err:
            print(f'Expresion mal ingresada (error computacional: {err}')
            sys.exit()

    def regex_func(self, any_function, symbol, result):
        expre = any_function
        sym = symbol
        pat1 = re.compile(r'[**]?[*]?'+sym+r'[+-]?(?![**])')
        exponente_uno = pat1.findall(expre)
        pat = re.compile(sym+r'[**]+[0-9]+')
        exponentes = pat.findall(expre)
        pat2 = re.compile(r'[*]?\d[+-]?[/]?(?![*]+)')
        constantes = pat2.findall(expre)
        lista = []
        largo_const = len(constantes)
        while largo_const > 0:
            for i in constantes:
                if '*' in i or '/' in i:
                    constantes.remove(i)
            largo_const-=1
        expre_expo = ''.join(exponentes)
        for i in expre_expo:
            if i.isdigit():
                lista.append(i)
        if len(exponente_uno) !=0:
            lista.append(str(len(exponente_uno)))
        se = result
        lista2 = []
        if len(constantes) > 0:
            lista.append(str(len(constantes)))
            lista = sorted(lista)
            for i, val in enumerate(lista):
                if i == 0:
                    lista2.append(str(se[i]))
                elif '-' in str(se[i]) and i != 0:
                    lista2.append(str(se[i])+'*'+sym+'**'+val)
                else:
                    lista2.append('+'+str(se[i])+'*'+sym+'**'+val)
        else:
            lista.sort()
            for i, val in enumerate(lista):
                if '-' in str(se[i]):
                    lista2.append(str(se[i])+'*'+sym+'**'+val)
                else:
                    lista2.append('+'+str(se[i])+'*'+sym+'**'+val)
        lista3 = ''.join(lista2)
        return(lista3)

    def calculate_se(self, polinomic_function, symbol):
        try:
            sqr_root = int(math.sqrt(len(self.matrix_a)))
            list_a = []
            i = 0
            j = sqr_root
            while True:
                if j > len(self.matrix_a):
                    break
                list_a.append(self.matrix_a[i:j])
                i = j
                j += sqr_root
            mtx_a = []
            print('MATRIZ A: ', list_a)
            for i in list_a:
                mtx_a.append(np.array(i))
            mtx_a = np.array(mtx_a, dtype = float)
            mtx_b = np.array(self.matrix_b, dtype=float)
            print('MATRIZ B: ', self.matrix_b)
            result = np.linalg.solve(mtx_a, mtx_b)
            result_a = []
            for i in result:
                result_a.append(float(i))
            fun = self.regex_func(polinomic_function, symbol, result_a)
            print('Resultado del Sistema de Ecuaciones: ', result_a)
            print('Funcion a aproximar: ', fun)
            return result_a
        except LinAlgError as err:
            print('Error: ',err)
            sys.exit()
        except TypeError as err:
            print(f'Parece que la funcion se anula en esos limites, mejor cambiarlos? (error computacional: {err})')
            sys.exit()
        except SympifyError as err:
            print(f'Expresion mal ingresada (error computacional: {err}')
            sys.exit()
        except SyntaxError as err:
            print(f'Expresion mal ingresada (error computacional: {err}')
            sys.exit()

    def error(self, function, w_p, symbol, inf, sup, result_se):
        try:
            function_sqr = '('+function+')'+'**2'
            integrate_calc = integrate(
                (function_sqr+'*'+w_p), (symbol, inf, sup)).evalf()
            print('Valor de (f)^2: ',integrate_calc)
            
            calc_err = math.sqrt(
                integrate_calc - sum(list(map(lambda x, y: x*y, result_se, self.matrix_b))))
            return calc_err
        except ValueError as err:
            print(f'No a sido posible calcular el error, error negativo! (error computacional de tipo: {err})')

    '''def function_graph(self, function, polinomic_function, se, inf, sup, symbol):
        inf = str(inf)
        sup = str(sup)
        x = np.linspace(int(inf),int(sup),50)
        fun1 = eval(func_obt)
        fun2 = eval(function)
        plt.plot(x,fun1,x,fun2)
        return plt.show()'''
