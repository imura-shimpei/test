class osakana():
    def __init__(self, name):
        self.name = name


class fish(osakana):
    def __init__(self, name):
        super(fish, self).__init__(name)
        self.name = "味噌汁にすると美味しい" + name

    def place(self):
        print(self.name + "は根魚")


kasago = fish("カサゴ")
kasago.place()




