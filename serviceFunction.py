from functions import Functions
from sympy import symbols, integrate
import math
import numpy as np
import matplotlib.pyplot as plt
import re


class ServiceFunction():
    def __init__(self, matrix_a=[], matrix_b=[]):
        self.matrix_a = matrix_a
        self.matrix_b = matrix_b

    def calculate_matrix_a(self, polinomic_function, w_p, symbol, inf, sup):
        symbol_to_integrate = symbols(symbol)
        j = 0
        i = 0
        lenght = (len(polinomic_function)*len(polinomic_function)) - 1
        while len(self.matrix_a) <= lenght:
            integrate_func = integrate(
                (polinomic_function[i]+'*'+polinomic_function[j]+'*'+w_p), (symbol_to_integrate, inf, sup)).evalf()
            i += 1
            self.matrix_a.append(integrate_func)
            if i == len(polinomic_function):
                i = 0
                j += 1
        return self.matrix_a

    def calculate_matrix_b(self, function, polinomic_function, symbol, inf, sup):
        for i in range(len(polinomic_function)):
            for val in function:
                integrate_func = integrate(
                    (polinomic_function[i]+'*'+val), (symbol, inf, sup)).evalf()
                self.matrix_b.append(integrate_func)
        return self.matrix_b

    def calculate_se(self, polinomic_function, symbol):
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
        for i in list_a:
            mtx_a.append(np.array(i))
        mtx_a = np.array(mtx_a)
        mtx_b = np.array(self.matrix_b)
        result = np.linalg.solve(mtx_a, mtx_b)
        expre = polinomic_function
        sym = symbol
        pat1 = re.compile(r'[**]?[*]?'+sym+r'[+-]?(?![**])')
        exponente_uno = pat1.findall(expre)
        pat = re.compile(sym+r'[**]+[0-9]+')
        exponentes = pat.findall(expre)
        pat2 = re.compile(r'[*]?\d[+-]?(?![*]+)')
        constantes = pat2.findall(expre)
        lista = []
        largo_const = len(constantes)
        while largo_const > 0:
            for i in constantes:
                if '*' in i:
                    constantes.remove(i)
            largo_const-=1
        expre_expo = ''.join(exponentes)
        for i in expre_expo:
            if i.isdigit():
                lista.append(i)
        if len(exponente_uno) !=0:
            lista.append(str(len(exponente_uno)))
        lista = sorted(lista)
        se = result
        lista2 = []
        if len(constantes) > 0:
            lista.append(str(len(constantes)))
            lista = sorted(lista)
            print('lista con 1?: ', lista)
            for i, val in enumerate(lista):
                if i == 0:
                    lista2.append(str(se[i]))
                if '-' in str(se[i]) and i != 0:
                    lista2.append(str(se[i])+'*'+sym+'**'+val)
                elif i != 0:
                    lista2.append('+'+str(se[i])+'*'+sym+'**'+val)
        else:
            for i, val in enumerate(lista):
                if '-' in str(se[i]):
                    lista2.append(str(se[i])+'*'+sym+'**'+val)
                else:
                    lista2.append('+'+str(se[i])+'*'+sym+'**'+val)
        lista3 = ''.join(lista2)
        print('Funcion obtenida para aproximar: ',lista3)
        return result

    def error(self, function, w_p, symbol, inf, sup, result_se):
        try:
            function_sqr = '('+function+')'+'**2'
            integrate_calc = integrate(
                (function_sqr+'*'+w_p), (symbol, inf, sup)).evalf()
            calc_err = math.sqrt(
                integrate_calc - sum(list(map(lambda x, y: x*y, result_se, self.matrix_b))))
            return calc_err
        except ValueError as err:
            print(f'No a sido posible calcular el error (error de tipo: {err}')

    def function_graph(self, function, polinomic_function, se, inf, sup, symbol):
        inf = str(inf)
        sup = str(sup)
        sym = symbol
        pat1 = re.compile(r'[**]?[*]?'+sym+r'[+-]?(?![**])')
        exponente_uno = pat1.findall(polinomic_function)
        pat = re.compile(sym+r'[**]+[0-9]+')
        exponentes = pat.findall(polinomic_function)
        pat2 = re.compile(r'[*]?\d[+-]?(?![*]+)')
        constantes = pat2.findall(polinomic_function)
        print(exponente_uno)
        lista = []
        pp = len(constantes)
        while pp > 0:
            for i in constantes:
                if '*' in i:
                    constantes.remove(i)
            pp-=1
        print('const: ',constantes)
        s = ''.join(exponentes)
        for i in s:
            if i.isdigit():
                print(i)
                lista.append(i)
        if len(exponente_uno) !=0:
            lista.append(str(len(exponente_uno)))
        lista = sorted(lista)
        print('lista',lista)
        lista2 = []
        if len(constantes) > 0:
            lista.append(str(len(constantes)))
            lista = sorted(lista)
            print('lista con 1?: ', lista)
            for i, val in enumerate(lista):
                if i == 0:
                    lista2.append(str(se[i]))
                if '-' in str(se[i]) and i != 0:
                    lista2.append(str(se[i])+'*'+sym+'**'+val)
                elif i != 0:
                    lista2.append('+'+str(se[i])+'*'+sym+'**'+val)
        else:
            for i, val in enumerate(lista):
                if '-' in str(se[i]):
                    lista2.append(str(se[i])+'*'+sym+'**'+val)
                else:
                    lista2.append('+'+str(se[i])+'*'+sym+'**'+val)
        func_obt = ''.join(lista2)
        x = np.linspace(inf,sup,50)
        fun1 = eval(func_obt)
        fun2 = eval(function)
        plt.plot(x,fun1,x,fun2)
        return plt.show()
