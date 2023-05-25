from model import Situation as S, Decision as D, RandomDecision as RD
t=3

# Full Game.
# Nodes
start = S('start', '$$')
wife_attempt = S('Attempt to Visit Wife', '$$')
fight_war = S('Fight War', '')

killed_war = S('Killed in War', '')
defect = S('Defect', '')

flee_germany = S('Flee Germany', '')
flee_allied = S('Flee Allied', '')



# Decisions/Edges
flee_rd = RD((lambda **kwargs: 80 * (0.7)**kwargs["t"], '', flee_allied), (lambda **kwargs: 100 - (80 * (0.7)**kwargs["t"]), '', flee_germany))

defect_d = D(defect)
war_rd = RD((lambda **kwargs: 25 * (1.05)**kwargs["t"], killed_war), (lambda **kwargs: 100 - (25 * (1.05)**kwargs["t"]), 'You survived the month.', fight_war))


# Add decisions to nodes
# start.add_option('Left', left)
# start.add_option('Right', right)

# Run the game
start.run(t=t)