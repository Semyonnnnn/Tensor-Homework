import lib
import int_num

def func_1():
    #  площадь прямоугольника
    a = int_num.int_number()
    b = int_num.int_number()
    rect = lib.Rectangle()
    print(f'Площадь прямоугольника = {rect.area(a,b)}')

def func_2():
    # площадь круга
    r = int_num.int_number()
    circ = lib.Circle()
    print(f'Площадь круга = {circ.area(r)}')

def func_3():
    # площадь трегуольника
    a = int_num.int_number()
    b = int_num.int_number()
    triag = lib.Triangle()
    print(f'Площадь треугольника = {triag.area(a,b)}')

def func_4():
    # Площадь прямоугольного параллелепипеда
    a = int_num.int_number()
    b = int_num.int_number()
    c = int_num.int_number()
    parall = lib.Parallelepiped()
    print(f'Объем прямоугольного параллелепипеда = {parall.area3d(a, b, c)}')

def func_5():
    # Площадь поверхности сферы
    r = int_num.int_number()
    spher = lib.Sphere()
    print(f'Площадь поверхногсти сферы = {spher.area3d(r)}')

def menu():
    while True:
        menu = input(
    """
    Выберите задачу.
    Площадь прямоугольника:...............1
    Площадь круга.........................2
    Площадь треугольника..................3
    Объем прямоугольного параллелепипеда..4
    Площадь поверхности сферы.............5
    Выход:............................Enter
    """
        )
        if not menu:
            print("До свидания...")
            break
        elif menu == '1':
            func_1()
        elif menu == '2':
            func_2()
        elif menu == '3':
            func_3()
        elif menu == '4':
            func_4()
        elif menu == '5':
            func_5()
        else:
            print("Повторите ввод...")
menu()