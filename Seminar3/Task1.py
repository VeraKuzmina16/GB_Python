x = [2, 3, 6, 10, 12, 16, 5]
summ = 0
for i in range(1, len(x), 2):
    if i % 2 == 1:
        summ += x[i]       
print(f"{x} -> Cумма элементов на нечётных позициях: {summ}")