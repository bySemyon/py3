def compound_interest(principal, rate, time):
    n = 12
    itog = principal * (1 + rate / n) ** (n * time)
    return itog
#itog - итоговая сумма
#principal - начальная сумма
#n - месяц
#ввод данных пользователем
principal = float(input("Введите начальную сумму: "))
rate = float(input("Введите годовую процентную ставку (в виде десятичной дроби): "))
time = int(input("Введите количество лет: "))

#расчет и результат итоговой суммы
result = compound_interest(principal, rate, time)
print("Через {} лет ваша инвестиция вырастет до: {:.0f}".format(time, result))