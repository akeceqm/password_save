import accounts


def variant_print():

    input_variant_print = int(input(
        " 1. Создать аккаунт\n 2. Внести изменения в аккаунт \n 3. Удалить аккаунт\n 4. Посмотреть список аккаунтов\n 5. Выйти\nВаш вариант действий: "))
    global select_input
    select_input = input_variant_print


while True:
    variant_print()
    if select_input == 0 or select_input > 5:
        print("Вы вели не правильную команду!!!")
        print("Введите снова!!!")
        select_input = int(input("Ввод: "))
    else:
        if select_input == 1:
            account_pass_check=""
            accounts.create_account(account_society=input("Введите вашу социльную сеть: "),
                                    account_name=input(
                                        "Введите ваш никнейм: "),
                                    account_password=input("Введите ваш пароль: "))

        elif select_input == 2:
            accounts.change_account(change_value=int(input("Введите id аккаунта: ")),account_society=input("Введите вашу социльную сеть: "), account_name=input(
                "Введите ваш никнейм: "), account_password=input("Введите ваш пароль: "))

        elif select_input == 3:
            accounts.del_account(account_id=int(
                input("Введите id аккаунта: ")))
        elif select_input == 4:
            accounts.print_list()

        elif select_input == 5:
            break
        else:
            "Ошибка в выборе варианта действия"
