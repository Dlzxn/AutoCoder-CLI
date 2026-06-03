from src.core import Tool
from src.scripts import ProjectTree


class WriteFile(Tool):
    def __init__(self):
        self.name = 'write_file'

    def __call__(self, file_path, filling, **kwargs) -> str:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(filling)
            return 'File successfully written.'
        except Exception as e:
            return f"Error writing file: {str(e)}"

    def _desc(self) -> dict:
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": "Create a new file or overwrite an existing one with specific text content.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_path": {
                            "type": "string",
                            "description": "Path and file name from the project root (e.g., 'src/main.py')",
                        },
                        "filling": {
                            "type": "string",
                            "description": "The actual text content to write into the file.",
                        }
                    },
                    "required": ["file_path", "filling"],
                },
            }
        }


class Tree(Tool):
    def __init__(self, root: str):
        self.name = 'get_project_tree'
        self.tree = ProjectTree(root)

    def __call__(self, **kwargs):
        return self.tree.generate()

    def _desc(self) -> dict:
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": (
                    "Returns the current project structure as a visual tree. "
                    "Use this tool to discover existing files, folders, and project architecture "
                    "before reading, writing, or modifying any code."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                },
            }
        }



class EditLine(Tool):
    def __init__(self):
        self.name = 'edit_line'

    def __call__(self, file_path: str, line_number: int, new_content: str, **kwargs) -> str:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            if 1 <= line_number <= len(lines):
                if not new_content.endswith('\n'):
                    new_content += '\n'

                lines[line_number - 1] = new_content

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.writelines(lines)

                return f"Successfully updated line {line_number} in {file_path}."
            else:
                return f"Error: Line {line_number} is out of range. File has {len(lines)} lines."

        except Exception as e:
            return f"Error editing line: {str(e)}"

    def _desc(self) -> dict:
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": "Replace a specific line in a file with new content using the line number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_path": {
                            "type": "string",
                            "description": "Path to the file relative to project root.",
                        },
                        "line_number": {
                            "type": "integer",
                            "description": "The 1-based index of the line to be replaced.",
                        },
                        "new_content": {
                            "type": "string",
                            "description": "The new text that will replace the old line.",
                        }
                    },
                    "required": ["file_path", "line_number", "new_content"],
                },
            }
        }

