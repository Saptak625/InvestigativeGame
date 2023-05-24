import random 

class Situation:
    def __init__(self, name, description, options):
        self.name = name
        self.description = description
        self.options = options

    def __str__(self):
        return self.name


class RandomDecision:
    def __init__(self, *args):
        self.options = args
        self.probabilities = []
        total = 0
        for option in self.options:
            total += option[0]
            self.probabilities.append(total)

    def run(self):
        # Random number between 0 and 1
        random_number = random.random() * 100

        # Find the first probability that is greater than the random number
        for i in range(len(self.probabilities)):
            if random_number < self.probabilities[i]:
                return self.options[i][1]


if __name__ == '__main__':
    rd1 = RandomDecision((10, 'a'), (50, 'b'), (40, 'c'))	
    print(rd1.run())