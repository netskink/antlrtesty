# Notes on vim in github code space

```
filetype plugin indent on
set expandtab
set tabstop=2
set softtabstop=2
set shiftwidth=2
```

# To get tabs in place of spaces momentariliy

Do this to avoid changing your .vimrc

```
:set paste
:set noexpandtab
:set tabstop=8
```

# To get multiple files with tabs 

Open user settings.json.  cmd-shift-p "Preferences: Open User Settings (JSON)

Add this line

```
"workbench.editor.showTabs":"multiple"
```

# notes on python settings deprecated

[stack overflow](https://stackoverflow.com/questions/77498238/vs-code-you-have-deprecated-linting-or-formatting-settings-for-python)
[vscode](https://code.visualstudio.com/docs/getstarted/settings#_settingsjson)


I installed the pylint extension
