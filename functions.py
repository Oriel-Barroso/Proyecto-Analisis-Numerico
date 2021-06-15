from itertools import chain
import re
import sys


class Functions():
    def __init__(self, f_x=None, g_x=None, w_p=None, symbol=None, inf_limit=0, sup_limit=0):
        self.f_x = f_x
        self.g_x = g_x
        self.w_p = w_p
        self.symbol = symbol
        self.inf_limit = inf_limit
        self.sup_limit = sup_limit

    @property
    def f_x(self):
        return self._f_x

    @f_x.setter
    def f_x(self, value):
        if value == '':
            raise ValueError('Debes proporcionar una funcion')
        else:
            self._f_x = str(value)

    @property
    def g_x(self):
        return self._g_x

    @g_x.setter
    def g_x(self, value):
        if value == '':
            raise ValueError('Debes proporcionar una funcion')
        else:
            self._g_x = str(value)

    @property
    def w_p(self):
        return self._w_p

    @w_p.setter
    def w_p(self, value):
        if value == '':
            self._w_p = '1'
        self._w_p = str(value)

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        self._symbol = value

    @property
    def inf_limit(self):
        return self._inf_limit

    @inf_limit.setter
    def inf_limit(self, value):
        self._inf_limit = value

    @property
    def sup_limit(self):
        return self._sup_limit

    @sup_limit.setter
    def sup_limit(self, value):
        self._sup_limit = value

    def function_construction(self, expre):
        text = expre
        pat_neg = re.compile(r'[exp|sin|cos|tan|ln]+[(][-]?x[**]*[-]?[0-9]*[)](?![**])')
        exp_neg = pat_neg.findall(text)
        if len(exp_neg) != 0:
            euler =''.join(exp_neg)
            text = text.replace(euler, '')
        if '+' in text or '-' in text:
            if '-' in text:
                for i in text:
                    if i == '-':
                        result2 = [i+x for x in text.split(i)]
                        result2[0] = result2[0].strip(i)
                lista = []
                for x in result2:
                    lista.append(x.split('+'))
                lista = list(chain(*lista))
                lista3 = []
                lista4 = []
                numero = 0
                for val in lista:
                    x = 0
                    if val.isdigit() is True:
                        numero=val
                        x+=1
                        if x == 2:
                            sys.exit()
                    if '-' in val:
                        lista3.append(val)
                    else:
                        lista4.append(val)
                if numero != 0:
                    lista4.remove(numero)
                lista3.sort()
                lista5 = []
                lista6 = []
                for i in lista3:
                    lista5.append(i.replace('-', ''))
                for i in lista4:
                    if i.strip():
                        lista6.append(i)
                i = 0
                for j in lista6:
                    while i != len(lista5):
                        if i == len(lista5):
                            break
                        if j < lista5[i]:
                            break
                        elif j > lista5[i]:
                            i+=1
                        else:
                            lista5.append(j)
                    if i == len(lista5):
                        lista5.append(j)
                    if j == 'x':
                        lista5.insert(0,j)
                    else:
                        lista5.insert(i,j)
                lista7 = []
                for j in lista5:
                    lista7.append('-'+j)
                lista8 = []
                for j in lista7:
                    if j not in lista3:
                        lista8.append(j.replace('-', ''))
                    else:
                        lista8.append(j)
                if numero != 0:
                    lista8.insert(0,numero)
                if len(exp_neg) != 0:
                    lista8.insert(0, euler)
                return((lista8))
            else:
                result2 = text.split('+')
                for val in result2:
                    if val.isdigit() is True:
                        j=val
                        result2.remove(val)
                        result2.sort()
                        result2.insert(0,j)
                    else:
                        result2.sort()
                return(result2)
        else:
            list_expre = []
            list_expre.append(text)
            return((list_expre))