import python_db_sql
# Здесь будут храниться аккаунты, которые добавил
list_account = {}

# Генерирует id для словаря
class IdGenerator:
    def __init__(self):
        self.id = 0

    def get_new_id(self):
        self.id += 1
        return self.id


id_generator = IdGenerator()


# Создание самого аккаунта
def create_account(account_society, account_name, account_password):
    account_id = id_generator.get_new_id()
    # Чтобы словарь можно было использовать в других def 
    global account_data
    account_data = {
        "society": account_society,
        "username": account_name,
        "password": account_password
    }
    list_account[account_id] = account_data
    python_db_sql.insert_into_db(account_society,account_name,account_password)
 
# Изменение аккаунта
# Я не знаю, почему он токо после вводы данных говорит, что такого id нету
def change_account(change_value,account_society,account_name,account_password):
    # Вот этот глобальный снова нужен, чтобы избежать ошибки
    global account_data
    account_id = change_value
    list_account[account_id] = account_data
    account = list_account[change_value]
    account["society"] = account_society
    account["username"] = account_name 
    account["password"] = account_password
    print(list_account)
    

# Удаляет аккаунт по id
def del_account(account_id):
    del list_account[account_id]
    

# Выводит сам словарь
def print_list():
    global society,name,password
    if len(list_account)==0:
        print("У вас отсутствуют аккаунты")
    else:
        print("Ваш список аккаунтов")
        
        for account_id, account in list_account.items():
            # Создаем переменные и присваевываем значения из словаря
            society = account["society"]
            name = account ["username"]
            password = account  ["password"]

            print(f"ID {account_id} |society: {society}| |name: {name}| |password: {password}|")
             
