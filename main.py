"""
This program scans a network in IPv4 to see which addresses are alive in a port specified by th user
Author: Sela
"""

from exporter import Exporter

from input_from_cmd import CMDInput
from scanner import Scanner


def main():
    user_parameters = CMDInput()
    networks = Scanner(user_parameters.user_data)
    Exporter(user_parameters.user_data, networks.living_networks)


if __name__ == '__main__':
    main()
