import shutil
from utils.colors import colors
from constants.constants import Constants
import os


class Neovim(Constants):
    def __init__(self) -> None:
        pass


    def check_curl(self):
        return shutil.which("curl")
        

    def which(self):
        return shutil.which("nvim")


    def install(self):
        neovim_exists = self.which()
        if not neovim_exists:
            curl_avaliable = self.check_curl()
            if curl_avaliable:
                if not os.path.isdir(self.INSTALL_NEOVIM_DIR):
                    os.makedirs(self.INSTALL_NEOVIM_DIR)
                print(colors.green("[+] Installing Neovim"))
                install_command = f"curl -L -o {self.INSTALL_NEOVIM_PATH} {self.INSTALL_NEOVIM_URL}"
                os.system(install_command)
                os.system(f"chmod u+x {self.INSTALL_NEOVIM_PATH}")
                print(colors.green("[+] Neovim installed"))
                path = os.get_exec_path()
                if self.INSTALL_NEOVIM_DIR in path:
                    print(colors.green(f"{self.INSTALL_NEOVIM_DIR} already in your path."))
                else:
                    print(colors.red(f"Add '{self.INSTALL_NEOVIM_DIR}' this to your path."))
            else:
                print(colors.red("[x] For this you must have 'curl' installed"))
        else:
            print(colors.red("Neovim already installed"))
