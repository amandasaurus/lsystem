import random

def expand_weighted(weights):
    output = []
    for repeat, value in weights:
        output.extend([value] * repeat)
    return output


def convert_rules(rules, singlechars):
    if singlechars:
        return convert_rules_singlechars(rules)
    return rules


def convert_rules_singlechars(rules):
    new_rules = {}
    if all(isinstance(value, basestring) for value in rules.values()):
        new_rules = dict((key, list(rules[key])) for key in rules)
    else:
        # weighted dict
        for key in rules:
            if all(isinstance(value, basestring) for value in rules[key]):
                new_rules[key] = list(rules[key])
            else:
                new_rules[key] = expand_weighted(rules[key])

    return new_rules

class LSystem(object):
    def __init__(self, rules, initial, singlechars=False):
        if singlechars:
            if all(isinstance(value, basestring) for value in rules.values()):
                rules = dict((key, [rules[key].split()]) for key in rules)
            else:
                # weighted randoms
                rules = dict((key, [x.split() for x in expand_weighted(rules[key])]) for key in rules)
            initial = initial.split()

        self.rules = rules
        self.initial = initial
        self.singlechars = singlechars
        self.seed = None

    def generate(self, num_steps=1000):
        random.seed(self.seed)
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
                if char not in self.rules:
                    output.append(char)
                else:
                    this_replacement = self.rules[char]
                    if isinstance(this_replacement, list):
                        output.extend(this_replacement)
                    else:
                        # dict so get calculations
                        pass



        if self.singlechars:
            output = ''.join(output)
        return output

