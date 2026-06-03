from src.core.tool_abstract import Tool

import subprocess
from src.core import Tool


class Terminal(Tool):
    def __init__(self):
        self.name = 'execute_command'

    def __call__(self, command: str, **kwargs) -> str:
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=30
            )

            output = result.stdout
            if result.stderr:
                output += f"\nErrors:\n{result.stderr}"

            return output if output else "Command executed successfully (no output)."
        except subprocess.TimeoutExpired:
            return "Error: Command timed out after 30 seconds."
        except Exception as e:
            return f"Error: {str(e)}"

    def _desc(self) -> dict:
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": "Execute a bash command in the terminal. Use this to run scripts, tests, or install dependencies.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "command": {
                            "type": "string",
                            "description": "The full command to run, e.g., 'python src/main.py' or 'pytest'.",
                        }
                    },
                    "required": ["command"],
                },
            }
        }


from src.core import Tool

class ReviewResult(Tool):
    def __init__(self):
        super().__init__()
        self.name = 'submit_review'

    def __call__(self, status: str, message: str = "", **kwargs) -> str:
        #TODO: Добавить логирование
        result_prefix = "✅ [REVIEW SUCCESS]" if status.lower() == "ok" else "❌ [REVIEW ERROR]"
        print('Reviewer:', result_prefix, message)
        return f"{result_prefix}: {message}"

    def _desc(self) -> dict:
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": (
                    "Finalizes the review process. Call this tool to submit your final verdict "
                    "on the code changes or the task completion status."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "enum": ["ok", "error"],
                            "description": "The final status of the review. 'ok' if the code is correct, 'error' if issues are found.",
                        },
                        "message": {
                            "type": "string",
                            "description": "Summary of the review. If status is 'error', describe the specific bugs or improvements needed.",
                        }
                    },
                    "required": ["status", "message"],
                },
            }
        }
