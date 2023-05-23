def zagadka1():
    a=print("загадка №1\nСтрану чудес откроем мы И встретимся с героями В строчках,На листочках,Где станции на точках ? \n у вас есть пять попыток")
    answer=input("введите ответ ")
    answer=answer.lower()
    n=0
    while n<5:
        if answer=="книга":
            print("правильный ответ")
            break 
        else:
            print("ответ неверный попробуйте еще раз")
            i=4-n
            n += 1
            print(i)
            answer=input("Выше написано кол-во оставшихся попыток \n введите ответ:")
            continue
    if n == 0:
        print('Game over')
        break
            
    
    b=print("загадка №2\nНа раскрашенных страницах Много праздников хранится? \n у вас есть пять попыток")
    answers=input("введите ответ ")
    answers=answers.lower()
    n=0
    while n<5:
        if answers=="календарь":
            print("правильный ответ")
            break
        else:
            print("ответ неверный попробуйте еще раз")
            i=4-n
            n += 1
            print(i)
            answers=input("Выше написано кол-во оставшихся попыток \n введите ответ:")
            continue

    
    c=print("загадка №3\nМаленькие домики по улице бегут,Мальчиков и девочек домики везут \n у вас есть пять попыток")
    answerk=input("введите ответ ")
    answerk=answerk.lower()
    n=0
    while n<5:
        if answerk=="машина":
            print("правильный ответ")
            break
        else:
            print("ответ неверный попробуйте еще раз")
            i=4-n
            n += 1
            print(i)
            answerk=input("Выше написано кол-во оставшихся попыток \n введите ответ:")
            continue
zagadka1()

