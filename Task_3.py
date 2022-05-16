

def type_logger(func):
    def wrapper(listik):
        func(listik)
        for i in range(len(listik)):
            listik[i] = str(f'\n{func.__name__}({listik[i]}: {type(listik[i])})')
        return listik
    return wrapper


@type_logger
def calc_cube(first):
    for i in range(len(first)):
        yield first[i] ** 3


bebrik = [4, 2, 4.5, 4124, 682.4234, 419028436, -1, 312.97816]
#Будем использовать список, чтобы можно было использовать "несколько" аргументов, но по факту он один - список, но в списке может быть много других значений
#А ещё можно вручную заполнять список и указывать кол-во "аргументов"
a = calc_cube(bebrik)
print(*a)
