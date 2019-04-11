""" Module responsible for providing a base class for system data collecting.

    Classes:
        BaseSystemInfo
"""
import os

from abc import ABC
from abc import abstractmethod

from src.exceptions import SystemFileReadError


class BaseSystemInfo(ABC):
    """ Abstract class for system data collecting.

        Remember to always implement property abstract methods with
        property decorator.
    """
    @abstractmethod
    def __init__(self):
        """ Abstract constructor method for the BaseSystemInfo class
            Needs to be implemented in child class, always with invoking
            mothers class constructor method.
        """
        self._proc_path = os.path.join('/', 'proc')

    @property
    def data(self):
        """ Property method for obtaining a data from system file

            Returns:
                parsed_data(dict): system data ready to convert to json
        """
        info_file = self._get_info_file()
        parsed_data = self._parse_info_file(info_file)
        return parsed_data

    @property
    @abstractmethod
    def file_path(self):
        """ Abstract method, which have to provide a system file
            absolute path.
        """
        pass

    def _get_info_file(self):
        """ Open selected file and save its content in a variable.

            Returns:
                data(list): lines from the file

            Raises:
                SystemFileReadError: if error occurred during reading a file.
        """
        try:
            with open(self.file_path, 'r') as data_file:
                data = data_file.readlines()
        except IOError:
            raise SystemFileReadError(
                f'Error during reading file: {self.file_path}'
            )
        return data

    @abstractmethod
    def _parse_info_file(self, info_file):
        """ Abstract method which have to provide a data from system file
            transformed into a proper dictionary.

            Args:
                info_file(list)
        """
        pass
