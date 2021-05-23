from itertools import chain


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
        if '+' in expre or '-' in expre:
            if '-' in text:
                for i in text:
                    if i == '-':
                        result = [i+x for x in text.split(i)]
                        result[0] = result[0].strip(i)
                lista = []
                for x in result:
                    lista.append(x.split('+'))
                y = list(chain(*lista))
                return(list(reversed(y)))
            else:
                result2 = text.split('+')
                return(list(reversed(result2)))
        else:
            return expre