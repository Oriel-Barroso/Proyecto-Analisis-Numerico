from functions import Functions
from serviceFunction import ServiceFunction

def main():
    fun = Functions()
    service = ServiceFunction()
    print('Para empezar a trabajar deberas indicar las funciones de la siguiente manera\n'
          'Para indicar las potencias debes ingresar --> x**2\n'
          'Para indicar que una constante multiplica a una variable --> 2*x\n'
          'Para indicar raices --> x**(1/2)\n'
          'Para indicar divisiones --> 1/2*x, ó, --> 1*x/2\n'
          'Para indicar el valor "pi", con tan solo escribir: pi, pi/2, sera suficiente\n'
          'Para indicar el seno debes ingresar --> sin(x)\n'
          'Se te pedira el simbolo para usar como diferencial en la integral, recuerda: el simbolo debe coincidir con las variables usadas en las funciones\n'
          'Ejemplo de funciones a ingresar: f(x) = sin(x), g(x) = x**2 + x + 1\n'
          'A veces el error no podra ser calculado debido a que la cantidad de decimales no es suficiente\n'
          'Comencemos...')

    i = 0
    while True:
        try:
            fun.f_x = input('Ingrese la funcion: ')
            fun.g_x = input('Ingrese la funcion a trabajar: ')
            i +=1
        except ValueError as err:
            print(err)
        if i == 1:
            break
    
    while True:
        try:
            func_p = input('Deseas ingresar un funcion peso?(s/n): ')
            if func_p == 's' or func_p == 'n':
                break
            else:
                raise ValueError('Las opciones validas son "s" o "n"')
        except ValueError as err:
            print(err)
        
    if func_p == 's':
        fun.w_p = input('Ingresa la funcion peso')
    else:
        fun.w_p = '1'

    while True:
        try:
            fun.symbol = (input('Ingresa el simbolo a utilizar como diferencial: '))
            if fun.symbol.isalpha():
                break
            else:
                raise TypeError
        except TypeError:
            print('Ingresa una letra')

    i = 0
    while True:
        try: 
            fun.inf_limit = int(input('Ingrese el limite inferior: '))
            fun.sup_limit = int(input('Ingrese el limite superior: '))
            i +=1
        except ValueError:
            print('ERROR! Debes ingresar un numero')
        if i == 1:
            break

    func_x = fun.function_construction(fun.f_x)
    func_g = fun.function_construction(fun.g_x)
    mtx_a = service.calculate_matrix_a(func_g, fun.w_p, fun.symbol, fun.inf_limit, fun.sup_limit)
    mtx_b = service.calculate_matrix_b(fun.f_x, func_g, fun.symbol, fun.inf_limit, fun.sup_limit)
    system_ecuation = service.calculate_se(fun.g_x, fun.symbol)
    error_cal = service.error(fun.f_x, fun.w_p, fun.symbol, fun.inf_limit, fun.sup_limit, system_ecuation)
    #graph = service.function_graph(fun.f_x, fun.g_x, system_ecuation,fun.inf_limit, fun.sup_limit, fun.symbol)

    print('Error: ',error_cal)


if __name__ == '__main__':
    main()