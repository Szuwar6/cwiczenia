class Parent1:
    def __init__(self):
        super().__init__()
        print("In parent 1 class...")

class Parent2:
    def __init__(self):
        print("In parent 2 class...")

class Derived(Parent1, Parent2):
    def __init__(self):
        super().__init__()
        print("In derived class...")

def main():
    d = Derived()

if __name__ == '__main__':
    main()
    print(Derived.mro())