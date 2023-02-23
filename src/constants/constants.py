import os
from utils.json import Json


class Constants():
    def __init__(self) -> None:
        pass

    
    INSTALL_FILENAME = os.path.join(os.path.dirname(__file__), "install.json")
    PLUGINS = Json.read(INSTALL_FILENAME)
    USER_DIR = os.path.expanduser("~")
    NVIM_CONFIG_DIR = os.path.join(USER_DIR, ".config/nvim")
    INIT_LUA_FILE = os.path.join(NVIM_CONFIG_DIR, "init.lua")
    PACKER_DIRECTORY = os.path.join(USER_DIR, ".local/share/nvim/site/pack/packer")
    PACKER_START_FUNCTION = "require('packer').startup(function(use)"
    PACKER_END_FUNCTION = "end)"
    INSTALL_PACKER = """local ensure_packer = function()
    local fn = vim.fn
    local install_path = fn.stdpath('data')..'/site/pack/packer/start/packer.nvim'
    if fn.empty(fn.glob(install_path)) > 0 then
        fn.system({'git', 'clone', '--depth', '1', 'https://github.com/wbthomason/packer.nvim', install_path})
        vim.cmd [[packadd packer.nvim]]
        return true
    end
    return false
end
local packer_bootstrap = ensure_packer()
"""
    PACKER_CONFIG_FUNCTION = """
require('packer').startup(function(use)
	use "wbthomason/packer.nvim"
end)
"""
    
    INSTALL_NEOVIM_URL = "https://github.com/neovim/neovim/releases/latest/download/nvim.appimage"
    INSTALL_NEOVIM_DIR = os.path.join(USER_DIR, ".local/bin")
    INSTALL_NEOVIM_PATH = os.path.join(INSTALL_NEOVIM_DIR, "nvim")
