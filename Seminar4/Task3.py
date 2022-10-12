lst = list(map(int, input("Введите числа через пробел: ").split()))
print(f"Исходный список: {lst}")
newlst = [newlst.append (i) for i in lst if i not in newlst]
print(f"Список из неповторяющихся элементов: {newlst}")