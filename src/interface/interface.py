from interface.plugins_categories import PluginsCategories
from install.packer import Packer
from install.neovim import Neovim
import sys
from utils.colors import colors
from utils.check import SystemCheck
from utils.exit import Exit


class Interface(PluginsCategories, SystemCheck):
    def __init__(self) -> None:
        self.parse_functions(self.initial_menu)
        SystemCheck.__init__(self)


    def start(self):
        self.initial_menu()


    def printOptions(self, options, title, back):
        self.header(title)
        length = len(options)
        for i, o in enumerate(options):
            string = f"{i + 1}) {o}"
            if i == length - 1:
                string = colors.blue(string)
            elif (i == length - 2 and back == True):
                string = colors.yellow(string)
            elif self.check_installed(o) == True:
                string = colors.green(string + " (installed)") 
            elif self.check_installed(o) == False:
                string = colors.red(string)
            else:
                string = colors.magenta(string)
            print(string)


    def input(self, options, title, go_back_function=None):
        if go_back_function != None:
            options.append("Back")
        options.append("Exit")
        value = (go_back_function is not None)
        self.printOptions(options, title, value)
        while True:
            try:
                value = int(input(colors.red("Option", bg=True) + ": "))
            except:
                print("[!] Invalid Option - Must be an integer!")
            else:
                length = len(options)
                if (1 <= value < length and go_back_function is None):
                    return value
                elif 1 <= value < length - 1: 
                    return value
                elif value == length:
                    Exit()
                elif value == length - 1 and go_back_function != None:
                    go_back_function()
                    break
                else:
                    print(f"[!] Invalid Option - Integer Between [1-{length}]")


    def header(self, title, num=50):
        print("="*num)
        print(title.center(num))
        print("="*num)


    def initial_menu(self):
        options = ["Install Neovim", "Install Packer", "Install Plugins", "Repair Plugins", "Unistall Plugins"]
        value = self.input(options, "Manage your Neovim Plugins")
        if value == 1:
            Neovim().install()
        if value == 2:
            Packer().install()
        elif value == 3:
            self.list_plugins_categories()
        elif value == 4:
            print("Repair (TODO)")
        elif value == 5:
            print("Uninstall (TODO)")
        self.initial_menu()
