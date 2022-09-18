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