def vklad():
    a=int(input("Введите первичную сумму вклада "))
    b=int(input("Введите желательный срок вклада "))
    s=0.1
    c=a*(1+s)**b
    print("Возвращаемая сумма")
    print(c)
vklad()