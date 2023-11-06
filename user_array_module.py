print("Здравуствуйте это программа для записи и хранения [соц сетй] !")

# Словарь с данными user для входа
user_profile_array = {"akeceqm": "qwerty"}

# def регистрация
def register_user():
    print("Окно регистрации")
    new_login = input("Придумайте логин: ")
    while True:
        if new_login in user_profile_array:
            print("Такой логин уже занят")
            new_login = input("Придумайте логин: ")
        else:
            break

    new_password = input("Придумайте пароль: ")
    confirm_password = input("Повторите пароль: ")

    if new_password != confirm_password:
        while True:
            print("Пароли не совпадают")
            confirm_password = input("Повторите пароль: ")
            if confirm_password == new_password:
                break
            else:
                confirm_password = input("Повторите пароль: ")

    user_profile_array[new_login] = new_password
    print("Регистрация прошла успешна!")

# def проверка лоигна
def check_login():
    print("Такого логина не существует")
    while True:
        login = input("Введите логин: ")
        if login in user_profile_array:
            print("Проверка пароля!!")
            password = input("Введите пароль: ")
            if user_profile_array[login] == password:
                break
        else:
            login = input("Введите логин: ")
            password = input("Введите пароль: ")


# def проверка аккаунта на существование в списке
def login_user(login, password):
    print("Окно входа")
    if login in user_profile_array and user_profile_array[login] == password:
        print("Вы успешно вошли в систему")
    elif login in user_profile_array and user_profile_array[login] != [password]:
        print("Неверный пароль!!!")
        while True:
            password = input("Введите пароль: ")
            if user_profile_array[login] == password:
                break
            else:
                password = input("Введите пароль: ")
    else:
        check_login()

# def так тута намучился в самом начале.
# Проверка на умение читать, что от тебя хотят
def check_variant_user_login():
    print("Вы уверены?\nЕсли хотите вернуться введите 0\nЕсли хотите продолжить то введите 1")
    resp = (input("Ввод: "))

    while True:
        if resp == "0":
            user_logs_in_and_checks_database()
            break
        elif resp == "1":
            login_user(login=input("Введите логин: "),
                       password=input("Введите пароль: "))
            break
        else:
            print("Вы вели некоректный ввод")
            resp = (input("Ввод: "))
            if resp == "0":
                user_logs_in_and_checks_database()
            elif resp == "1":
                login_user(login=input("Введите логин: "),
                           password=input("Введите пароль: "))

                break


# def так тута намучился в самом начале.
# Проверка на умение читать, что от тебя хотят
# ctrl+c and ctrl+v наше все
def check_variant_register_user():
    print("Вы уверены?\nЕсли хотите вернуться введите 0\nЕсли хотите продолжить то введите 1")
    resp = (input("Ввод: "))

    while True:
        if resp == "0":
            user_logs_in_and_checks_database()
            break
        elif resp == "1":
            register_user()
            break
        else:
            print("Вы вели некоректный ввод")
            resp = (input("Ввод: "))
            if resp == "0":
                user_logs_in_and_checks_database()
            elif resp == "1":
                register_user()
                break

# def выбор на вход или же регистрацию 
def user_logs_in_and_checks_database():
    print("У вас уже есть аккаунт? y/n")
    response = input("Ваш ответ: ")

    while True:
        if response == "y" or response == "n":
            if response == "y":
                check_variant_user_login()
                break
            else:
                check_variant_register_user()
                break
        else:
            print("Введите корректный ответ!!!")
            response = input("Ваш ответ: ")

user_logs_in_and_checks_database()
