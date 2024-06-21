from input_from_cmd import UserInput


def main():
    user_parameters = UserInput()
    received = ScanNetworks(user_parameters.protocol, user_parameters.network, user_parameters.port)
    export = Exporter(user_parameters.output_method, received.results)


if __name__ == '__main__':
    main()
