# markdown_convert_explorer

_Add Markdown to PDF conversion to the right click menu of Windows File Explorer._

## Requirements

- The [markdown-convert](https://github.com/Julynx/markdown_convert) Python package: `pip install markdown-convert`.
- The [GTK-3 Runtime](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases) for Windows: (Required by `weasyprint`, a dependency of `markdown-convert`).

## Installation

1. Download [<kbd> ↓ generate_reg_keys.py </kbd>](https://github.com/Julynx/markdown_convert_explorer/releases/download/1.0/generate_reg_keys.py) and run it:
   
    This will create a file called `markdown-convert.reg` that contains the registry keys to add the right click menu entries for your system.

3. Double click the `markdown-convert.reg` file and accept the UAC prompt to merge the new keys to the Windows Registry.

## Usage

> [!NOTE]
> If you just installed the `markdown-convert` package, you may need to log out and log back in for the command to be registered to your PATH.

- Right click any Markdown file, then click `Convert to PDF`.
- For real-time conversion to PDF, click `Convert to PDF (live)`.

If you don't see the new menu entries when right clicking on a file, please ensure it has the `.md` extension.
Because Windows **hides file extensions** by default, it might actually be a `.md.txt` file. 
Check out [this link](https://lazyadmin.nl/win-11/show-file-extension-windows-11/) if you wish to disable this behavior.

## Uninstalling

To remove the entries from the right click menu, download [<kbd> ↓ uninstall.reg </kbd>](https://github.com/Julynx/markdown_convert_explorer/releases/download/1.0/uninstall.reg) from this repository and double click it.

If you also wish to uninstall `markdown-convert`, run the following command:

```bash
pip uninstall markdown-convert -y
```
