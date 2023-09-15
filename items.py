class Item:
    def __init__(self, id, name, useful):
        self.id = id
        self.name = name
        self.useful = useful

    def is_useful(self):
        if self.useful == True:
            return "The object is useful"
        return "The object is not useful"