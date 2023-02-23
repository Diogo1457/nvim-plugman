import os
from utils.file import File
from constants.constants import Constants
from install.packer import Packer
from install.neovim import Neovim
from utils.colors import colors


class Plugins(Constants):
    def __init__(self) -> None:
        pass


    def __find_plugin_category(self, plugin):
        for category in self.PLUGINS.keys():
            for p in self.PLUGINS[category]:
                if plugin == p:
                    return category


    def __write_repo(self, content, command):
        index = content.index(self.PACKER_START_FUNCTION)
        new_content = []
        for i, c in enumerate(content):
            new_content.append(c)
            if i == index + 1:
                new_content.append("\t" + command)
        return "\n".join(new_content)
    

    def __write_config(self, content, config, plugin):
        config = "\n".join(config)
        if config not in content:
            content += f"\n--{plugin} Config\n{config}"
        return content
    

    def check_installed(self, plugin, category=None):
        if not category:
            category = self.__find_plugin_category(plugin)
        if category:
            avaliable_plugins = self.PLUGINS[category]
            content_list = File.read(self.INIT_LUA_FILE)
            return avaliable_plugins[plugin][0] in content_list
        return "NOT_PLUGIN"
    

    def install(self, category, plugin):
        if not self.check_installed(plugin, category):
            print(colors.green(f"[+] Installing plugin '{plugin}'..."))
            Packer().install() # Make sure packer is installed and if not install it
            plug_command, plug_config = self.PLUGINS[category][plugin]
            content_list = File.read(self.INIT_LUA_FILE).split("\n")
            content_without_config = self.__write_repo(content_list, plug_command)
            content = self.__write_config(content_without_config, plug_config, plugin)
            File.write(self.INIT_LUA_FILE, content)
            print(colors.green(f"[+] Plugin '{plugin}' installed with sucess..."))
        else:
            print(colors.red(f"[!] Plugin '{plugin}' was already installed"))
