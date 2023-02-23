import os
from constants.constants import Constants
from utils.colors import colors
from utils.file import File


class Packer(Constants):
    def __init__(self) -> None:
        pass


    def checkInstalled(self, content):
        return self.INSTALL_PACKER in content
    

    def install(self):
        content = File.read(self.INIT_LUA_FILE)
        if self.checkInstalled(content):
            print(colors.red("[!] Packer is already installed"))
        else:
            print(colors.green("[+] Installing packer..."))
            content = self.INSTALL_PACKER + self.PACKER_CONFIG_FUNCTION + content
            File.write(self.INIT_LUA_FILE, content)
            print(colors.green("[+] Packer Installed with sucess"))
