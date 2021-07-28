import re


class Board:
    def __init__(self):
        self.data_list = list(' ' * 9)
        self.win_pattern = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        self.regex = r'^[0-8]$'

    def play(self, index, sym_choice):
        self.data_list[index] = sym_choice

    def user_choice_validation(self, index):
        if re.match(self.regex, index) is None:
            print(
                "Your choice should be in between 0 to 8.")
            return False
        elif self.data_list[int(index)] != ' ':
            print("This place has already been filled.")
            return False
        else:
            return True

    @staticmethod
    def display_help():
        s = "Please select a number from 0 to 8 according to below scenario\n"
        for i in range(0, 9, 3):
            s += "{} | {} | {}\n".format(i, i + 1, i + 2)
            if i != 6:
                s += "----------\n"
        return s
