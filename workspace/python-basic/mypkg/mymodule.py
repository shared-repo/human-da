import pickle

# from custom_type import TestClass

def do_test():
    with open('test.pickle', 'rb') as f:
        tc = pickle.load(f)

    print(tc.get_value())