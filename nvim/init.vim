set number
set relativenumber
set cursorline
set expandtab
set tabstop=4
set shiftwidth=4
set autoindent
set smartindent

nnoremap <C-o> :NERDTreeToggle<CR>

call plug#begin('~/.config/nvim/plugged')

" Nicer status line
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

" Code navigation and search
Plug 'preservim/nerdtree'
Plug 'junegunn/fzf',{ 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
Plug 'easymotion/vim-easymotion'

" Git integration
Plug 'tpope/vim-fugitive'
Plug 'airblade/vim-gitgutter'

" Syntax highlighting and auto-completion
"Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'nvim-treesitter/nvim-treesitter'

call plug#end()
