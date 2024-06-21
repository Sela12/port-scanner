from abc import ABC
from dataclasses import dataclass
from ipaddress import IPv4Network
from typing import List


@dataclass
class NeededData:
    protocol: List[str]
    network: IPv4Network
    port: int
    output_method: List[str]


class UserData(ABC):
    def __init__(self):
        # self.protocols: List[str]
        # self.network: IPv4Network
        # self.port: int
        # self.output_method: list
        user_data: NeededData
        user_data = self.get_user_input()

    def get_user_input(self) -> NeededData:
        """
        Get the needed user data to run this program
        """
