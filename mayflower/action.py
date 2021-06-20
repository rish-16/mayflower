class Action:
    def __init__(self, name):
        self.name = name

class ClickAction(Action):
    def __init__(self, name):
        super().__init__(name)

class TypeAction(Action):
    def __init__(self, name):
        super().__init__(name)

class SelectAction(Action):
    def __init__(self, name):
        super().__init__(name)