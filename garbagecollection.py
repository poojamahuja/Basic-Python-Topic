class SomeObj:

    def __init__(self):
        print('The object is created.')

    def __del__(self):
        print('The object is destroyed.')

obj1 = SomeObj()
obj2 = obj1
obj3 = obj1
print("Set obj1 to None...")
obj1 = None
print("Set obj2 to None...")
obj2 = None
print("Set obj3 to None...")
obj3 = None
