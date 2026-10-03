try:
    #Команда для ввода числа
    number = int(input("Введите двузначное число:"))
    #Проверка двузначное число ли
    if not (10 <= abs(number) <= 99):
        raise "Число не является двузначным!"
    #Извлекаем цифры
    a = abs(number) // 10 #Десятки
    b = abs(number) % 10 #Единицы

    #Ищем сумму и произведение
    digit_sum = a + b
    digit_product = a * b

    #Выводим результаты
    print(f"Число: {number}")
    print(f"Сумма цифр: {digit_sum}")
    print(f"Произведение цифр: {digit_product}")

except ValueError as e:
     print ("Ошибка ввода:", e)
