# This is the link to this Python Coding Challenge from codewars.com
# https://www.codewars.com/kata/57a0e5c372292dd76d000d7e/train/python
class Repeater:

    def __init__(self, string, repeat):
        self.string = string
        self.repeat = repeat

    def run(self):

        repeated_str = ''
        for i in range(0, self.repeat):
            # print(i)
            repeated_str += self.string
        print(repeated_str)

        # print(self.string)
        # print(type(self.repeat))
