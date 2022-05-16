

def val_checker(func):
    def wrapper(perem):
        if type(perem) == int or type(perem) == float:
            if perem > 0:
                result = func(perem)
                return result
            else:
                raise ValueError(f'wrong value: {perem}')  # исключение на значение аргумента
        else:
            raise TypeError(f'wrong type: {perem}')  # исключение на тип аргумента
    return wrapper


@val_checker  # эх, я немного не понял как работать с аргумент-функцией, поэтому сделал втупую, если так можно сказать
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube(12412.2))
    print(calc_cube(124141414897192847))
    print(calc_cube('OMG'))
