from FirstDemo import Calculator


class ChildImpl(Calculator):
    num2=200

    def __init__(self):
        Calculator.__init__(self,2,10)


    def getData(self):
        return ChildImpl.num2 + self.num + self.sum()


obj3 = ChildImpl()

print(obj3.getData())

