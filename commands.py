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

    def add_pair(self, storage, key, value):
        try:
            storage.add(key, value)
            return f"Pair {key}:{value} was added"
        except Exception as e:
            return e

    def delete_pair(self, storage, key, arg=None):
        try:
            value = storage.data[key]
            storage.delete(key)
            return f"{key}:{value} was deleted"
        except KeyError:
            return 'Key not found'

    def get_value(self, storage, key, arg=None):
        try:
            return storage.get(key)
        except KeyError:
            return 'Key not found'

    def save_storage(self, storage, arg1=None, arg2=None):
        try:
            storage.save()
            return "State was saved"
        except Exception as e:
            return e

    def change_storage(self, storage, name, arg=None):
        try:
            storage.change_storage(name)
            return f'Storage {name} selected'
        except Exception as e:
            return e

    def get_all_data(self, storage, arg1=None, arg2=None):
        return storage.data

    def close_app(self, storage=None, arg1=None, arg2=None):
        print('Good bye')
        exit(0)

    def clone_storage(self, storage, arg1=None, arg2=None):
        try:
            new_name = storage.name + '-clone'
            new_storage = Storage(new_name)
            new_storage.data = storage.data
            new_storage.save()
            return f"Clone {new_name} was created"
        except Exception as e:
            return e
