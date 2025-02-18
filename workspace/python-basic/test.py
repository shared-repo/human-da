import pickle

# from custom_type import TestClass
from mypkg import mymodule

class TestClass:
    def __init__(self):
        self.data = 0

    def increase_value(self, v):
        self.data += v

    def get_value(self):
        return self.data

# with open('test.pickle', 'rb') as f:
#     tc = pickle.load(f)

# print(tc.get_value())

# print("=" * 50)

mymodule.do_test()



