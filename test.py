class Bound:
    def __init__(self):
        id = 1
        food = 455

class Law(Bound):

    __tablename__ = "law"
    id = Column(String(80), default=Law.id)
    food = (Column(String(80), default=Law.food))
    name = ""

    def __init__(self):
        super().__init__()





law = Law("John")