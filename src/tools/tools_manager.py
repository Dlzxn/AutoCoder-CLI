


class ToolManager:
    def __init__(self, tools: list):
        self.tools = [x() for x in tools]
        self._create_map()

    def _create_map(self):
        self._functions = {x.name: x for x in self.tools}

    def get_list_desc(self):
        return [x._desc() for x in self.tools]

    def __getitem__(self, item: str):
        return self._functions[item]


