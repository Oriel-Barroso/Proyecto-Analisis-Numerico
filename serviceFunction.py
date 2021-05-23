from functions import Functions
from sympy import symbols, integrate
import math
import numpy as np
import matplotlib.pyplot as plt


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

    def calculate_se(self, function, polinomic_function):
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

    def function_graph(self, function, polinomic_function, inf, sup):
        inf = str(inf)
        sup = str(sup)
        sup_a = float(sup+'.'+sup)
        sup_b = float('.'+sup)
        x = np.arange(float(inf), sup_a, sup_b)
        evaluate_function = eval(function)
        evaluate_polinomic_function = eval(polinomic_function)
        plt.plot(x, evaluate_function, x, evaluate_polinomic_function)
        plt.show()
