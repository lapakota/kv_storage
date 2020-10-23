from arg_parser import ArgParser
from storage import Storage


def execute_command(storage, input_data):
    print(input_data)
    str_command, arg1, arg2 = ArgParser.parse_args(input_data)
    try:
        command = COMMANDS[str_command]
    except KeyError:
        return 'Error with command'
    else:
        return command(storage, arg1, arg2)


def add_pair(storage, key, value):
    try:
        storage.add(key, value)
        return f"Pair {key}:{value} was added"
    except Exception as e:
        return e


def delete_pair(storage, key, arg=None):
    try:
        value = storage.data[key]
        storage.delete(key)
        return f"{key}:{value} was deleted"
    except KeyError:
        return 'Key not found'


def get_value(storage, key, arg=None):
    try:
        return storage.get(key)
    except KeyError:
        return 'Key not found'


def save_storage(storage, arg1=None, arg2=None):
    try:
        storage.save()
        return "State was saved"
    except Exception as e:
        return e


def load_storage(storage):
    try:
        storage.load()
        return 'Storage was loaded'
    except Exception as e:
        return e


def change_storage(storage, name, arg=None):
    try:
        storage.change_storage(name)
        return f'Storage {name} selected'
    except Exception as e:
        return e


def get_all_data(storage, arg1=None, arg2=None):
    return storage.data


def close_app(storage=None, arg1=None, arg2=None):
    print('Good bye')
    exit(0)


def clone_storage(storage, arg1=None, arg2=None):
    try:
        new_name = storage.name + '-clone'
        new_storage = Storage(new_name)
        new_storage.data = storage.data
        new_storage.save()
        return f"Clone {new_name} was created"
    except Exception as e:
        return e


COMMANDS = {
    'add': add_pair,
    'del': delete_pair,
    'get': get_value,
    'save': save_storage,
    'load': load_storage,
    'change': change_storage,
    'all': get_all_data,
    'exit': close_app,
    'clone': clone_storage,
}
