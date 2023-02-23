from install.plugins import Plugins
from constants.constants import Constants

class PluginsCategories(Plugins, Constants):

    def __init__(self) -> None:
        pass


    def parse_functions(self, function):
        # Prevent Import Error
        self.main_menu = function


    def __list(self, options, title, back_func):
        options = sorted(options)
        value = self.input(options, title, back_func)
        return value, options


    def list_plugins_categories(self):
        value, options = self.__list(self.PLUGINS.keys(), "Plugins Categories", self.main_menu)
        if value:
            self.__list_category(options[value - 1])
        

    def __list_category(self, category):
        value, options = self.__list(self.PLUGINS[category].keys(), f"{category} Plugins", self.list_plugins_categories)
        if value:
            self.install(category, options[value - 1])
            self.__list_category(category)
