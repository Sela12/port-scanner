"""
This module is in charge of the way the data is shown.
Author: Sela
"""

import json

from user_data import NeededData


class Exporter:
    def __init__(self, output_method: NeededData, living_networks: dict):
        self.methods = output_method.output_method
        self.protocols = output_method.protocol
        self.networks = living_networks
        self.exporter()

    def exporter(self):
        """
        Handles the exporting
        :return:
        """
        for method in self.methods:
            if method == 'print':
                self._print_to_screen()
            elif '.jason' in method:
                self._export_to_json(method)

    def _print_to_screen(self):
        """
        Prints the networks to the screen.
        :return:
        """
        for protocol in self.protocols:
            print(f"The networks alive in protocol {protocol} are {self.networks[protocol]}")

    def _export_to_json(self, filename: str):
        """
        Exports the data to a json file specified by the user
        :param filename: The filename to  export into
        """
        with open(filename, 'w') as f:
            for protocol in self.protocols:
                json.dump(f"The networks alive in protocol {protocol} are {self.networks[protocol]}", f)
            print(f"Results saved to {filename}")
