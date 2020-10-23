from storage import Storage
from commands import Commands


def main():
    storage_name = input("Write storage name: ")
    storage = Storage(storage_name)
    storage.load()
    while True:
        input_data = input("Write command: ")
        commands = Commands()
        result = commands.execute_command(storage, input_data)
        print(result, '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


if __name__ == '__main__':
    main()
