class Player:
    def __init__(self):
        self.name = None
        self.sym = None

    def set_sym(self, sym):
        if sym in ['O', 'X']:
            self.sym = sym

    def set_name(self, name):
        self.name = name

    def __str__(self):
        return "{} : {}".format(self.name, self.sym)