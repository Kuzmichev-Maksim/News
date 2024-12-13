print(" 1 — сложение, 2 — вычитание, 3 — умножение, 4 — деление,"
      " 5 — возведение в степень 6 — остатоток от деления, 7 — целочисленное деление")  
o = int(input("Выберите номер арифметической операции из списка:")) 
a = float(input("Введите первое число:")) 
b = float(input("Введите второе число:")) 

match o:
    case 1: 
        print(a + b) 
    case 2: 
        print(a - b) 
    case 3: 
        print(a * b) 
    case 4: 
        if (a==0 or b==0):
            print("Ошибка") 
        else: 
            print(a / b) 
    case 5:
            print(a ** b) 
    case 6: 
        if (a==0 or b==0): 
            print("Ошибка") 
        else:
            print(a % b) 
    case 7: 
        if (a == 0 or b == 0): 
            print("Ошибка") 
        else:
            print(a // b) 