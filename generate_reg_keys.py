#!/usr/bin/env python3

import subprocess
from pathlib import Path


def main():

    try:
        result = subprocess.run(['where', 'markdown-convert'],
                                capture_output=True, text=True, check=True)
        exe_path = result.stdout.strip()
        if not exe_path:
            raise FileNotFoundError

    except Exception as e:
        print("markdown-convert not found.\n"
              "Please run 'pip install markdown-convert' first.")
        return

    exe_path = exe_path.split('\n')[0]
    exe_path = exe_path.replace("\\", "\\\\")

    filled_template = fill_template(exe_path)
    Path('markdown-convert.reg').write_text(filled_template)


def fill_template(exe_path):
    return f"""Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\\SystemFileAssociations\\.md\\shell\\MarkdownConvert]
@="Convert to PDF"

[HKEY_CLASSES_ROOT\\SystemFileAssociations\\.md\\shell\\MarkdownConvert\\command]
@="\\"{exe_path}\\" \\"%1\\""

[HKEY_CLASSES_ROOT\\SystemFileAssociations\\.md\\shell\\MarkdownConvertLive]
@="Convert to PDF (live)"

[HKEY_CLASSES_ROOT\\SystemFileAssociations\\.md\\shell\\MarkdownConvertLive\\command]
@="\\"{exe_path}\\" \\"%1\\" \\"--mode=live\\""
"""


if __name__ == '__main__':
    main()
