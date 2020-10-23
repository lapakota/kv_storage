from arg_parser import ArgParser
from storage import Storage


class Commands:
    def __init__(self):
        self.COMMANDS = {
            'add': self.add_pair,
            'del': self.delete_pair,
            'get': self.get_value,
            'save': self.save_storage,
            'change': self.change_storage,
            'all': self.get_all_data,
            'exit': self.close_app,
            'clone': self.clone_storage,
        }

    def handle_command(self, command, *args):
        return self.COMMANDS[command](*args)

    def execute_command(self, storage, input_data):
        str_command, arg1, arg2 = ArgParser.parse_args(input_data)
        try:
            return self.handle_command(str_command, storage, arg1, arg2)
        except KeyError:
            return 'Error with input data'

    @staticmethod
    def add_pair(*args):
        storage = args[0]
        key = args[1]
        value = args[2]
        try:
            storage.add(key, value)
            return f"Pair {key}:{value} was added"
        except Exception as e:
            return e

    @staticmethod
    def delete_pair(*args):
        storage = args[0]
        key = args[1]
        try:
            value = storage.data[key]
            storage.delete(key)
            return f"{key}:{value} was deleted"
        except KeyError:
            return 'Key not found'

    @staticmethod
    def get_value(*args):
        storage = args[0]
        key = args[1]
        try:
            return storage.get(key)
        except KeyError:
            return 'Key not found'

    @staticmethod
    def save_storage(*args):
        storage = args[0]
        try:
            storage.save()
            return "State was saved"
        except Exception as e:
            return e

    @staticmethod
    def change_storage(*args):
        storage = args[0]
        name = args[1]
        try:
            storage.change_storage(name)
            return f'Storage {name} selected'
        except Exception as e:
            return e

    @staticmethod
    def get_all_data(*args):
        storage = args[0]
        return storage.data

    @staticmethod
    def clone_storage(*args):
        storage = args[0]
        try:
            new_name = storage.name + '-clone'
            new_storage = Storage(new_name)
            new_storage.data = storage.data
            new_storage.save()
            return f"Clone {new_name} was created"
        except Exception as e:
            return e

    @staticmethod
    def close_app(*args):
        print('Good bye')
        exit(0)
