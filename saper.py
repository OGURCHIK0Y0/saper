import mylib     
game = True
while game:
    stroka = int(input("Введите номер строки"))
    stolb = int(input("Введите номер столбца"))
    if stroka>12 or stolb>12:
        print("не вводите существующих чисел")
    else:
        mylib.check(stroka-1,stolb-1)
        mylib.vyvodPolya(mylib.vidimost_polya)
        if mylib.isOpen():
            game = False


print("Всё поле открыто!")


