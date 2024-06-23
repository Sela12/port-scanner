"""
This module contains the class in charge of scanning the network for live ports
Author: Sela
"""

import socket
from random import randint

from scapy import all as scapy

from user_data import NeededData


class Scanner:
    def __init__(self, user_parameters: NeededData):
        self.user_data = user_parameters
        self.optional_protocols = {'u': self._scan_socket,
                                   't': self._scan_socket,
                                   's': self._scan_scapy,
                                   'w': self._scan_scapy}
        self.living_networks = {'u': [], 't': [], 's': [], 'w': []}
        self._scan_all_ports()

    def _scan_all_ports(self):

        for protocol in self.user_data.protocol:
            self.optional_protocols[protocol](protocol)

    def _scan_socket(self, protocol: str):
        """
        Scans networks using sockets, TCP or UDP depending on user input
        :param protocol: Which protocol the user wants to use
        """
        socket_protocols = {'u': socket.SOCK_DGRAM,
                            't': socket.SOCK_STREAM}
        for network in self.user_data.network:
            sock = socket.socket(socket.AF_INET, socket_protocols[protocol])
            sock.settimeout(1)
            data = None
            try:
                if protocol == 'u':
                    sock.sendto('ping'.encode(), (str(network), self.user_data.port))
                    data, server = sock.recvfrom(1024)
                elif protocol == 't':
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
        src_port = randint(5000, 6000)
        for network in self.user_data.network:
            packet = scapy.IP(dst=network) / scapy.TCP(dport=self.user_data.port, sport=src_port,
                                                       flags=protocol.capitalize())
            received_packet = scapy.sr1(packet, timeout=2)
            if protocol == 's' and "S" in received_packet.TCP(flags):
                self.living_networks[protocol].append(network)
            elif protocol == 'w' and received_packet.TCP(window) is not None:
                self.living_networks[protocol].append(network)
