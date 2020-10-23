class ArgParser:
    @staticmethod
    def parse_args(input_data):
        input_data = input_data.split(maxsplit=2)
        command = input_data[0]
        arg1 = None
        arg2 = None

        if len(input_data) == 2:
            arg1 = input_data[1]

        if len(input_data) > 2:
            arg1 = input_data[1]
            arg2 = input_data[2]

        return command, arg1, arg2
