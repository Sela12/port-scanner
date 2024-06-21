import argparse
from ipaddress import IPv4Network

from user_data import UserData, NeededData


class UserInput(UserData):
    def get_user_input(self) -> NeededData:
        parser = argparse.ArgumentParser()
        parser.add_argument("-u", "--UDP", help="Use UDP", action="store_true")
        parser.add_argument("-t", "--TCP", help="Use TCP", action="store_true")
        parser.add_argument("Network", help="The IP range you want to test. example: 0.0.0.0/24",
                            type=IPv4Network)
        parser.add_argument("Port", help="The port you want to try", type=int)
        parser.add_argument("-p", "--print", help="print to screen", action="store_true")
        parser.add_argument("-j", "--json", help="Export to jason file: -j <filename>")
        args = parser.parse_args()
        self.protocol = [args.UDP, args.TCP]
        self.network = args.Network
        self.port = args.Port
        self.output_method = [args.print, args.json]
        return NeededData([args.UDP, args.TCP], args.Network, args.Port, [args.print, args.json])

    def __str__(self):
        return (f"The protocols used are: {self.protocol}, the network is {self.network}, "
                f"the port is {self.port} and the output method is {self.output_method}")
