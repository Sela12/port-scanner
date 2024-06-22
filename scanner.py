"""
This module contains the class in charge of scanning the network for live ports
Author: Sela
"""

import socket

from user_data import NeededData


class Scanner:
    def __init__(self, user_parameters: NeededData):
        self.user_data = user_parameters
        self.optional_protocols = {'UDP': self._scan_socket,
                                   'TCP': self._scan_socket}
        self.socket_protocols = {'UDP': socket.SOCK_DGRAM,
                                 'TCP': socket.SOCK_STREAM}
        self.living_networks = {'UDP': [], 'TCP': []}
        self._scan_all_ports()

    def _scan_all_ports(self):

        for protocol in self.user_data.protocol:
            self.optional_protocols[protocol](protocol)

    def _scan_socket(self, protocol: str):
        """
        Scans networks using sockets, TCP or UDP depending on user input
        :param protocol: Which protocol the user wants to use
        """
        for network in self.user_data.network:
            sock = socket.socket(socket.AF_INET, self.socket_protocols[protocol])
            sock.settimeout(1)
            data = None
            try:
                if protocol == 'UDP':
                    sock.sendto('ping'.encode(), (str(network), self.user_data.port))
                    data, server = sock.recvfrom(1024)
                elif protocol == 'TCP':
                    sock.connect((str(network), self.user_data.port))
                    data, server = sock.recvfrom(1024)
                sock.close()
            except (TimeoutError, OSError):
                continue
            self.living_networks[protocol].append(network)

    def _scan_scapy(self, protocol):
        """
                Scans networks using sockets, TCP or UDP depending on user input
                :param protocol: Which protocol the user wants to use
        """
        pass
    # TODO: Implement this function
