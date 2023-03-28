def ritm(a):
    a = a.split()
    lst = []
    for word in a:
        sum_w = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                sum_w += 1
        lst.append(sum_w)
    return len(lst) == lst.count(lst[0])


x = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
if ritm(x):
    print('Парам пам-пам')
else:
    print('Пам парам')