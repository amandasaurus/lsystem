import random
import six

def expand_weighted(weights):
    output = []
    for repeat, value in weights:
        output.extend([value] * repeat)
    return output


def convert_rules(rules, singlechars):
    if singlechars:
        return convert_rules_singlechars(rules)
    else:
        return convert_rules_nonsinglechars(rules)

def convert_rules_nonsinglechars(rules):
    new_rules = {}
    #import pudb; pudb.set_trace()
    for key in rules:
        if all(isinstance(value, six.string_types) for value in rules[key]):
            # This rule is a non-weighted simple one
            new_rules[key] = [list(rules[key])]
        else:
            # This rule is a weighted rule
            new_rules[key] = expand_weighted(rules[key])

    return new_rules


def convert_rules_singlechars(rules):
    new_rules = {}
    for key in rules:
        if all(isinstance(value, six.string_types) for value in rules[key]):
            new_rules[key] = [list(rules[key])]
        else:
            this_values = [(weight, list(char)) for weight, char in rules[key]]
            new_rules[key] = expand_weighted(this_values)

    return new_rules

class LSystem(object):
    def __init__(self, rules, initial, singlechars=False):

        self.initial = initial
        self.singlechars = singlechars
        self.rules = convert_rules(rules, singlechars=singlechars)
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
                    assert isinstance(this_replacement, list)
                    if len(this_replacement) == 1:
                        # deterministic, non-random rule, so just apply that
                        # one
                        output.extend(this_replacement[0])
                    else:
                        # stochastic rule
                        output.extend(random.choice(this_replacement))
                        pass



        if self.singlechars:
            output = ''.join(output)
        return output


