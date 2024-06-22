"""
This module defines the data needed to run the program and the abstract class to get it
Author: Sela
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from ipaddress import IPv4Network
from typing import Tuple


@dataclass
class NeededData:
    protocol: Tuple[str]
    network: IPv4Network
    port: int
    output_method: Tuple[str]


class UserData(ABC):
    """
    Class with abstract method to define how to get user input
    """

    def __init__(self):
        self.user_data = self._get_user_input()

    @abstractmethod
    def _get_user_input(self) -> NeededData:
        """
        Get the needed user data to run this program
        """

    def __str__(self):
        return (f"The protocols used are: {self.user_data.protocol}, the network is {self.user_data.network}, "
                f"the port is {self.user_data.port} and the output method is {self.user_data.output_method}")
