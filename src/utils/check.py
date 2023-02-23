import os
from constants.constants import Constants


class SystemCheck(Constants):
    def __init__(self) -> None:
        self.__nvim_dir()


    def __nvim_dir(self):
        if not os.path.isdir(self.NVIM_CONFIG_DIR):
            os.makedirs(self.NVIM_CONFIG_DIR)
