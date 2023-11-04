list_account = {}


class IdGenerator:
    def __init__(self):
        self.id = 0

    def get_new_id(self):
        self.id += 1
        return self.id


id_generator = IdGenerator()


def create_account(account_society, account_name, account_password):
    account_id = id_generator.get_new_id()
    global account_data
    account_data = {
        "society": account_society,
        "username": account_name,
        "password": account_password
    }
    list_account[account_id] = account_data
    return list_account


def change_account(change_value):
    account_id = change_value
    list_account[account_id] = account_data
    print(list_account)
    if change_value not in list_account:
        print("Такого id не существует")


def del_account(account_id):
    del list_account[account_id]


def print_list():
    print("\n Ваш список аккаунтов")
    for account_id, account in list_account.items():
        society = account["society"]
        name = account ["username"]
        password = account  ["password"]
        
        print(f"ID {account_id} |society: {society}| |name: {name}|: |password: {password}|")
             
