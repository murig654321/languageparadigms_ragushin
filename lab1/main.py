from math import *
import sys
def calculate_root(a, b, c):
    roots = []
    d = b**2 - 4*a*c
    if d < 0:
        print("Корней нет")
        return roots
    else:
        x1 = (-b+sqrt(d))/(2*a)
        x2 = (-b-sqrt(d))/(2*a)
        if x1>0:
            roots.append(sqrt(x1))
            roots.append(-sqrt(x1))
        if x1 == 0:
            roots.append(0.0)
        if x2>0:
            roots.append(sqrt(x2))
            roots.append(-sqrt(x2))
        if x2==0:
            roots.append(0)
        return list(set(roots))

def get_abc(name, can_be_0=True):
    while True:
        try :
            vl = float(input(f"Введите коэффициент {name}: "))
            if not can_be_0 and vl == 0:
                print(f"Ошибка. Коэффициент {name} не может быть равен 0")
                continue
            return vl
        except ValueError:
            print("Ошибка. Введите число")

def get_pref_abc(index, can_be_0=True):
    if len(sys.argv)>index:
        try:
            val = float(sys.argv[index])
            if not can_be_0 and val == 0:
                return None
            return val
        except ValueError:
            return None
    return None
    

if __name__ == "__main__":
    a = get_pref_abc(1, can_be_0=False)
    b = get_pref_abc(2)
    c = get_pref_abc(3)

    contin = True
    while contin:
        if a is None:
            a = get_abc("a", can_be_0=False)
        if b is None:
            b = get_abc("b")
        if c is None:
            c = get_abc("c")
        roots = calculate_root(a, b, c)
        if not roots:
            print("Корней нет")
        else:
            roots.sort()
            for r in roots:
                print(f" {r} ")
        a, b, c = None, None, None
        print("Продолжить? (y/n)")
        if input() == "n":
            contin = False
