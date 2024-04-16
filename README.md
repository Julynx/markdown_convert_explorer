# markdown_convert_explorer

_Add Markdown to PDF conversion to the right click menu of Windows File Explorer._

## Requirements

- The [markdown-convert](https://github.com/Julynx/markdown_convert) Python package: `pip install markdown-convert`.
- The GTK-3 Runtime for Windows: [GTK-3 Runtime](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases).

## Installation

1. Download and run `generate_reg_keys.py`.
   
    This will create a file called `markdown-convert.reg` that contains the registry keys to add the right click menu entries for your system.

3. Double click the `markdown-convert.reg` file and accept the UAC prompt to merge the new keys to the Windows Registry.

## Usage

- Right click on any Markdown file, then click `Convert to PDF`.
- For real-time conversion to PDF, click `Convert to PDF (live)`.