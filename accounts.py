list_account = {}


class IdGenerator:
    def __init__(self):
        self.id = 0

    def get_new_id(self):
        self.id += 1
        return self.id


id_generator = IdGenerator()


def create_account(account_name, account_password):
    account_id = id_generator.get_new_id()
    list_account[account_id] = {account_name: account_password}
    return list_account


def change_account(change_value, account_name, account_password):
    account_id = change_value
    list_account[account_id] = {account_name: account_password}
    print(list_account)
    if change_value not in list_account:
        print("Такого id не существует")


def del_account(account_id):
    del list_account[account_id]


def print_list():
    print("\n Ваш список аккаунтов")
    for account_id, account_body in list_account.items():
        name = list(account_body.keys())[0]
        password = list(account_body.values())[0]
        print(f"ID {account_id} |name: {name}|: |password{password}|")
