from install.plugins import Plugins
import sys

class Exit():
    def __init__(self) -> None:
        self.safe()


    def safe(self):
        print("[!] If you installed any plugin, open Neovim and type :PackerSync, this will solve the problems!")
        sys.exit()
