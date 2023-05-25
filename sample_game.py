from model import Situation as S, Decision as D, RandomDecision as RD
t=3

# A simple graph with 4 nodes, 3 edges, and 2 decisions, one of which is random.
# Nodes
start = S('start', 'You are in a dark room. There is a door to the left and right, which one do you take?')
a = S('a', 'You find a room full of spiders. You lose!')
b = S('b', 'You find a room full of gold. You win!')
c = S('c', 'You find a room full of snakes. You lose!')

# Decisions/Edges
left = D(a) # Completely certain event
right = RD((lambda **kwargs: 80 * (0.9)**kwargs["t"], 'You successfully navigate the room.', b), (lambda **kwargs: 100 - (80 * (0.9)**kwargs["t"]), 'You get lost.', c)) # 50% chance of b, 50% chance of c

# Add decisions to nodes
start.add_option('Left', left)
start.add_option('Right', right)

# Run the game
start.run(t=t)