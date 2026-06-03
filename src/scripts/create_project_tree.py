import os
from pathlib import Path


class ProjectTree:
    def __init__(self, root_dir: str, ignore_dirs: list = None):
        self.root_dir = Path(root_dir)
        self.ignore_dirs = ignore_dirs or ['.git', '__pycache__', '.venv', '.idea', '.vscode', 'dist', 'build']

    def generate(self, directory: Path = None, indent: str = "") -> str:
        if directory is None:
            directory = self.root_dir

        tree = ""
        items = sorted(list(directory.iterdir()), key=lambda x: (x.is_file(), x.name))

        items = [item for item in items if item.name not in self.ignore_dirs]

        for i, item in enumerate(items):
            is_last = (i == len(items) - 1)
            marker = "└── " if is_last else "├── "

            tree += f"{indent}{marker}{item.name}\n"

            if item.is_dir():
                new_indent = indent + ("    " if is_last else "│   ")
                tree += self.generate(item, new_indent)

        return tree
