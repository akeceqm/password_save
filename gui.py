import accounts

# Выводится после входа в аккаунт
def variant_print():
    input_variant_print = int(input(
        " 1. Создать аккаунт\n 2. Внести изменения в аккаунт \n 3. Удалить аккаунт\n 4. Посмотреть список аккаунтов\n 5. Выйти\nВаш вариант действий: "))
    global select_input
    select_input = input_variant_print


while True:
    variant_print()
        # def создания 
    if select_input == 1:
        # Нужны для проверки на пусыте строки!
        account_society = ""
        account_name = ""
        account_password = ""

        # Проверка на пустые строки
        while account_society == "":
            account_society = input("Введите вашу социальную сеть: ")
            if account_society!="":
                break

        while account_name == "":
            account_name = input("Введите ваш никнейм: ")
            if account_name!="":
                break

        while account_password == "":
            account_password = input("Введите ваш пароль: ")
            if account_password!="":
                break
        
        accounts.create_account(account_society,
                                account_name,
                                account_password)
    # def изменения
    elif select_input == 2:
        accounts.change_account(change_value=int(input("Введите id аккаунта: ")),account_society=input("Введите вашу социльную сеть: "), account_name=input(
            "Введите ваш никнейм: "), account_password=input("Введите ваш пароль: "))
    # def удаления
    elif select_input == 3:
        accounts.del_account(account_id=int(
            input("Введите id аккаунта: ")))
    # Вывод словаря
    elif select_input == 4:
        accounts.print_list()
    # Выход в окно
    elif select_input == 5:
        break
    else:
        print("Вы вели не правильную команду!!!")
        print("Введите снова!!!")
        select_input = int(input("Ввод: "))