import random 

class Situation:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.options = []

    def add_option(self, optionName, option):
        self.options.append((optionName, option))

    def run(self, **kwargs):
        print(self.description)
        if len(self.options) == 0:
            return
        # print('What do you do?')
        for i in range(len(self.options)):
            print(f'{i+1}: {self.options[i][0]}')
        choice = int(input()) - 1
        print()
        desc, decisionResult = self.options[choice][1].run(**kwargs)
        print(desc)
        print('Result: ', decisionResult)
        decisionResult.run(**kwargs)

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name


class Decision:
    def __init__(self, option, desc = ''):
        self.options = option
        self.desc = desc

    def run(self, **kwargs):
        return self.desc, self.options # Return no description and next node
    
    def __str__(self):
        return self.options
    
    def __repr__(self):
        return self.options


class RandomDecision(Decision):
    def __init__(self, *args, t=0, **kwargs):
        super().__init__(args)
        self.options = args
        self.probabilities = []
        total = 0
        for option in self.options:
            prob = option[0]
            if callable(option[0]):
                prob = option[0](t=t, **kwargs)
            total += prob
            self.probabilities.append(total)

    def run(self, **kwargs):
        # Option Type
        if any([callable(i[0]) for i in self.options]):
            # Recalculate probabilities
            self.probabilities = []
            total = 0
            for option in self.options:
                prob = option[0]
                if callable(option[0]):
                    prob = option[0](**kwargs)
                total += prob
                self.probabilities.append(total)

        # Random number between 0 and 1
        random_number = random.random() * 100

        # Find the first probability that is greater than the random number
        for i in range(len(self.probabilities)):
            if random_number < self.probabilities[i]:
                return self.options[i][1], self.options[i][2]


if __name__ == '__main__':
    # A simple graph with 4 nodes, 3 edges, and 2 decisions, one of which is random.
    # Nodes
    start = Situation('start', 'You are in a dark room. There is a door to the left and right, which one do you take?')
    a = Situation('a', 'You find a room full of spiders. You lose!')
    b = Situation('b', 'You find a room full of gold. You win!')
    c = Situation('c', 'You get lost. You find a room full of snakes. You lose!')

    # Decisions/Edges
    left = Decision(a) # Completely certain event
    right = RandomDecision((50, b), (50, c)) # 50% chance of b, 50% chance of c

    # Add decisions to nodes
    start.add_option('Left', left)
    start.add_option('Right', right)

    # Run the game
    start.run()