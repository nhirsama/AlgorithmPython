class Abc:
    n = 0
    def __init__(self):
        self.n = int(input())
    def printf(self):
        print(self.n)
        return self.n
if __name__ == "__main__":
    cl = Abc()
    print(cl.printf());
