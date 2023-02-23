# Nvim-PlugMan

# Install and configure Neovim Plugins via a python CLI

## Install

```bash
# Requires
sudo apt install -y python3 git curl 

# Optional for the Mason-lspconfig
sudo apt install python3-pip npm

git clone https://github.com/Diogo1457/nvim-plugman.git

# Run
python3 nvim_plugman/src/main.py
```

## After installing a plugin, when you open neovim you will probably get an error. Run :PackerSync in neovim to fix the error.

## Develop
- ### Some functions, like 'Repair Plugin Config' and 'Uninstall Plugin' are not ready yet.
- ### If you want to test the app you can do it using the Dockerfile provided
```bash
# Build Image
docker build -t test_nvim_plug .
# Run Docker Container
docker run -d -t --name nvim_plugman test_nvim_plug
# Container Shell
docker exec -it nvim_plugman bash
``` 

## Data Structure
- ### *Current Plugins Supported*
- ### category: {plugin: [use_command, [config.split("\n")]} 
```json
{
    "Autocomplete and Linting": {
        "Mason": [
            "use {'williamboman/mason.nvim', requires = { {'williamboman/mason-lspconfig.nvim'} }}", 
            ["require('mason').setup()", "require('mason-lspconfig').setup({", "\tensure_installed = {}", "})"]
        ],
        "LSP": [
            "use 'neovim/nvim-lspconfig'",
            ["local on_attach = function(client, bufnr)", 
            "  vim.api.nvim_buf_set_option(bufnr, 'omnifunc', 'v:lua.vim.lsp.omnifunc')", 
            "  local bufopts = { noremap=true, silent=true, buffer=bufnr }", 
            "  vim.keymap.set('n', 'gD', vim.lsp.buf.declaration, bufopts)", 
            "  vim.keymap.set('n', 'gd', vim.lsp.buf.definition, bufopts)", 
            "  vim.keymap.set('n', 'K', vim.lsp.buf.hover, bufopts)", 
            "  vim.keymap.set('n', 'gi', vim.lsp.buf.implementation, bufopts)", 
            "  vim.keymap.set('n', '<C-k>', vim.lsp.buf.signature_help, bufopts)", 
            "  vim.keymap.set('n', '<space>wa', vim.lsp.buf.add_workspace_folder, bufopts)", 
            "  vim.keymap.set('n', '<space>wr', vim.lsp.buf.remove_workspace_folder, bufopts)", 
            "  vim.keymap.set('n', '<space>wl', function()", 
            "    print(vim.inspect(vim.lsp.buf.list_workspace_folders()))", "  end, bufopts)", 
            "  vim.keymap.set('n', '<space>D', vim.lsp.buf.type_definition, bufopts)", 
            "  vim.keymap.set('n', '<space>rn', vim.lsp.buf.rename, bufopts)", 
            "  vim.keymap.set('n', '<space>ca', vim.lsp.buf.code_action, bufopts)", 
            "  vim.keymap.set('n', 'gr', vim.lsp.buf.references, bufopts)", 
            "  vim.keymap.set('n', '<space>f', function() vim.lsp.buf.format { async = true } end, bufopts)", 
            "end",
            "local lspconfig = require('lspconfig')", 
            "local servers = {}", 
            "for _, lsp in ipairs(servers) do", 
            "  lspconfig[lsp].setup {", 
            "    -- on_attach = my_custom_on_attach,", 
            "    capabilities = capabilities,",
            "}", 
            "end"
        ]
        ],
        "Nvim-CMP": [
            "use {'hrsh7th/nvim-cmp', requires={ {'hrsh7th/nvim-cmp'}, {'hrsh7th/cmp-nvim-lsp'}, {'saadparwaiz1/cmp_luasnip'}, {'L3MON4D3/LuaSnip'} }}", 
            ["local capabilities = require('cmp_nvim_lsp').default_capabilities()",
            "local luasnip = require 'luasnip'",
            "local cmp = require 'cmp'",
            "cmp.setup {",
            "  snippet = {",
            "    expand = function(args)",
            "      luasnip.lsp_expand(args.body)",
            "    end,",
            "  },",
            "  mapping = cmp.mapping.preset.insert({",
            "    ['<C-u>'] = cmp.mapping.scroll_docs(-4), -- Up",
            "    ['<C-d>'] = cmp.mapping.scroll_docs(4), -- Down",
            "    ['<C-Space>'] = cmp.mapping.complete(),",
            "    ['<CR>'] = cmp.mapping.confirm {",
            "      behavior = cmp.ConfirmBehavior.Replace,",
            "      select = true,",
            "    },",
            "    ['<Tab>'] = cmp.mapping(function(fallback)",
            "      if cmp.visible() then",
            "        cmp.select_next_item()",
            "      elseif luasnip.expand_or_jumpable() then",
            "        luasnip.expand_or_jump()",
            "      else",
            "        fallback()",
            "      end",
            "    end, { 'i', 's' }),",
            "    ['<S-Tab>'] = cmp.mapping(function(fallback)",
            "      if cmp.visible() then",
            "        cmp.select_prev_item()",
            "      elseif luasnip.jumpable(-1) then",
            "        luasnip.jump(-1)",
            "      else",
            "        fallback()",
            "      end",
            "    end, { 'i', 's' }),",
            "  }),",
            "  sources = {",
            "    { name = 'nvim_lsp' },",
            "    { name = 'luasnip' },",
            "  },",
            "}"
            ]
        ]
    },
    "Interface": {
        "Telescope": [
            "use {'nvim-telescope/telescope.nvim', tag = '0.1.1', requires = { {'nvim-lua/plenary.nvim'} }}", 
            ["local builtin = require('telescope.builtin')", 
            "vim.keymap.set('n', '<leader>f', builtin.find_files, {})", 
            "vim.keymap.set('n', '<leader>fg', builtin.live_grep, {})", 
            "vim.keymap.set('n', '<leader>fb', builtin.buffers, {})", 
            "vim.keymap.set('n', '<leader>fh', builtin.help_tags, {})"
            ]
        ], 
        "Nvim-Tree": [
            "use {'nvim-tree/nvim-tree.lua', requires={ {'nvim-tree/nvim-web-devicons'} }}",
            ["require('nvim-tree').setup()", "vim.keymap.set('n', '<leader>b', ':NvimTreeOpen<cr>', opts)", "vim.keymap.set('n', '<leader>c', ':NvimTreeClose<cr>', opts)"]
        ],
        "LuaLine": [
            "use {'nvim-lualine/lualine.nvim', requires={ {'nvim-tree/nvim-web-devicons'} }}", 
            ["require('lualine').setup()"]
        ],
        "WhichKey": ["use 'folke/which-key.nvim'", ["require('which-key').setup()"]]
    },
    "Styles": {
        "Tokyonight": ["use 'folke/tokyonight.nvim'", ["vim.cmd[[colorscheme tokyonight]]"]]
    },
    "Utils": {
        "GitSigns": ["use 'lewis6991/gitsigns.nvim'", ["require('gitsigns').setup()"]],
        "Comment": ["use 'numToStr/Comment.nvim'", ["require('Comment').setup()"]],
        "Indent-Blankline": ["use 'lukas-reineke/indent-blankline.nvim'", []]
    }
}
```

## Please report any bugs
## Feel free to suggest plugins to add
