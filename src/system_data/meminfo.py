""" Module for processing a /proc/meminfo file."""
import os

from src.system_data.base_systeminfo import BaseSystemInfo


class Meminfo(BaseSystemInfo):
    """ Class responsible for obtaining and processing meminfo system data."""
    def __init__(self):
        """ Constructor method for Meminfo class.
            Loads constructor from base class.
        """
        super().__init__()

    @property
    def file_path(self):
        """ Property method which provides a absolute path to meminfo file.

            Returns:
                file_abspath(str): absolute path to meminfo file
        """
        file_name = 'meminfo'
        file_abspath = os.path.join(self._proc_path, file_name)
        return file_abspath

    def _parse_info_file(self, info_file):
        """ Prepare json-like structure from meminfo system data.

            Args:
                info_file(list): lines from the loaded file

            Returns:
                data(dict): meminfo parameters

            Output structure:
            {'parameter_name': {'value': <number>, 'unit': 'kB'}, ... }
            If there is no unit for the parameter, None is provided.
        """
        split_data = [
            [chunk for chunk in info.split(' ') if chunk]
            for info in info_file
        ]

        data = {
            data_el[0].replace(':', ''):
            {
                'value': data_el[1],
                'unit': data_el[2] if len(data_el) is 3 else None
            }
            for data_el in split_data
        }
        return data
