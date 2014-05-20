class LSystem(object):
    def __init__(self, alphabet, rules, initial, singlechars=False):
        if singlechars:
            alphabet = alphabet.split()
            rules = dict((key, rules[key].split()) for key in rules)
            initial = initial.split()

        self.alphabet = alphabet
        self.rules = rules
        self.initial = initial
        self.singlechars = singlechars

    def generate(self, num_steps=1000):
        output = []
        if num_steps == 0:
            output = self.initial
        else:
            # FIXME Recursive, this isn't great performance wise
            # TODO if a char isn't in rules, it's presumed to be a constant and
            # always included, other option is to delete
            current_step = self.generate(num_steps-1)

            # apply one step
            output = []
            for char in current_step:
                output.extend(self.rules.get(char, char))


        if self.singlechars:
            output = ''.join(output)
        return output

