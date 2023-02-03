temp = int(input("Введите год: "))
answer = 0
wholePart = 0
remains = 0
i = 1
while i <= 12:
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
        ii = 1
        while ii <= 31:
            wholePart = ii // 10
            remains =  ii % 10
            answer += wholePart + remains
            ii += 1
    elif i == 2:
        ii = 1
        if temp % 4 == 0:
            if temp % 100 == 0 and temp % 400 == 0 or temp % 100 != 0:
                while ii <= 29:
                    wholePart = ii // 10
                    remains =  ii % 10
                    answer += wholePart + remains
                    ii += 1
            elif temp % 100 == 0 and temp % 400 != 0:
                while ii <= 28:
                    wholePart = ii // 10
                    remains =  ii % 10
                    answer += wholePart + remains
                    ii += 1
        else:
            while ii <= 28:
                wholePart = ii // 10
                remains =  ii % 10
                answer += wholePart + remains
                ii += 1
    elif i == 4 or i == 6 or i == 9 or i == 11:
        ii = 1
        while ii <= 30:
            wholePart = ii // 10
            remains =  ii % 10
            answer += wholePart + remains
            ii += 1
    i += 1
print(f"Сумма дней в году {temp}: {answer}")