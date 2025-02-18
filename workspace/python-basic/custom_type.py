class TestClass:
    def __init__(self):
        self.data = 0

    def increase_value(self, v):
        self.data += v

    def get_value(self):
        return self.data