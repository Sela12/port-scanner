"""
As explained in class documentation
Author: Sela
"""

import argparse
from ipaddress import IPv4Network

from user_data import UserData, NeededData


class CMDInput(UserData):
    """
    This class is in charge of getting input through the command line.
    It inherits from the class UserData.
    """

    def _get_user_input(self) -> NeededData:
        parser = argparse.ArgumentParser()
        parser.add_argument("-u", "--UDP", help="Use UDP", dest='protocols', action="append_const", const='UDP')
        parser.add_argument("-t", "--TCP", help="Use TCP", dest='protocols', action="append_const", const='TCP')
        parser.add_argument("Network", help="The IP range you want to test. example: 0.0.0.0/24",
                            type=IPv4Network)
        parser.add_argument("Port", help="The port you want to try", type=int)
        parser.add_argument("-p", "--print", help="print to screen", dest='output',
                            action="append_const", const="print")
        parser.add_argument("-j", "--json", help="Export to jason file: -j <filename>.json",
                            dest='output', action="append")
        args = parser.parse_args()
        print(args.output)
        return NeededData(args.protocols, args.Network, args.Port, args.output)
