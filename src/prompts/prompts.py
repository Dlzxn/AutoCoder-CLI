TODO_PROMPT = """
Role: Lead Systems Architect.
Task: Decompose the project into a strict, exhaustive implementation sequence.

Format: Single string. Tasks separated ONLY by a semicolon (;).
Strict Rule: Each task is a "Technical Specification". You MUST specify for every file:
1. Exact File Path.
2. Necessary Imports (standard and project-specific).
3. Class/Function Definitions: Exact names, inheritance (e.g., from ABC), and decorators.
4. Method Signatures: Arguments with types, return types (e.g., def __call__(self, path: str) -> str).
5. Internal Logic: Describe the algorithmic core of the method.

Instructions:
- Order: src/core/ (interfaces) -> src/services/ (logic) -> app entrypoints.
- No tests.
- No fluff: Only technical requirements.
- Avoid semicolons inside task descriptions to prevent parsing errors.

Example:
mkdir -p src/core; create src/core/tool.py: imports [from abc import ABC, abstractmethod], class Tool(ABC) with @abstractmethod __init__(self, name: str) and @abstractmethod __call__(self, *args, **kwargs) -> str; create src/core/engine.py: imports [from typing import List; from src.core.tool import Tool], class Engine with attributes [tools: List[Tool]] and method run(self) -> None;

Input Project:
"""

SUMMARY_PROMPT = """
Role: Senior System Architect.
Task: Based on the generated TODO list, create a "Single Source of Truth" (SSOT) for the project.

Structure your response as follows:
1. Core Concept: Briefly define the goal and main logic of the system.
2. Technical Architecture: Describe the stack (Python, Pydantic, etc.) and global constraints (e.g., all interfaces in src/core/).
3. Detailed File-by-File Blueprint: For EVERY file in the project, provide:
   - Full path.
   - Purpose: What this file does.
   - Contents: Class names, methods, and specific logic.
   - Boundaries: What MUST NOT be in this file (to avoid code bloating).
4. Full Project Tree: A visual representation of the final structure.

Constraint: Write everything in a concise, technical style. This summary will be the ONLY context for a developer agent. Avoid fluff.

Input TODO list:
"""

CODER_PROMPT = """

"""