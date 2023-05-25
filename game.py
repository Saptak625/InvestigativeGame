from model import Situation as S, Decision as D, RandomDecision as RD
t=1

# Full Game.
# Nodes
start = S('start', '$$')

fight_war = S('Fight War', '$$')

killed_war = S('Killed in War', '$$')
defect = S('Defect', '$$')

flee_germany = S('Flee Germany', '$$')
flee_allied = S('Flee Allied', '$$')

visit_wife = S('Visit Wife', '$$')
stopped_nazi = S('Stopped by Nazi Soldiers', '$$')

find_family = S('Find Family', '$$')
hiding_solitary = S('Hiding Solitary', '$$')

concentration_camp = S('Concentration Camp', '$$')


# Decisions/Edges
flee_rd = RD((lambda **kwargs: 80 * (0.7)**kwargs["t"], '$$', flee_allied), (lambda **kwargs: 100 - (80 * (0.7)**kwargs["t"]), '$$', flee_germany))
wife_rd = RD((40, 'Visit wife in hospital. $$', visit_wife), (35, 'Caught by Polish government for evading draft. $$', fight_war), (25, 'Stopped by Nazi soldiers. $$', stopped_nazi))
fight_war_d = D(fight_war)

defect_d = D(defect)
continue_war_rd = RD((lambda **kwargs: 25 * (1.05)**kwargs["t"], '$$', killed_war), (lambda **kwargs: 100 - (25 * (1.05)**kwargs["t"]), 'You survived the month.', fight_war))
hiding_solitary_d = D(hiding_solitary)
find_family_d = D(find_family)

continue_hiding_solitary_rd = RD((lambda **kwargs: 35 * (1.05)**kwargs["t"], '$$', concentration_camp), (lambda **kwargs: 100 - (35 * (1.05)**kwargs["t"]), 'You survived the month.', hiding_solitary))


# Add decisions to nodes
# start.add_option('Left', left)
start.add_option('Flee Country', flee_rd)
start.add_option('Visit Wife', wife_rd)
start.add_option('Fight War', fight_war_d)

fight_war.add_option('Continue', continue_war_rd)
fight_war.add_option('Defect', defect_d)

defect.add_option('Flee Country', flee_rd)
defect.add_option('Find Family', find_family_d)
defect.add_option('Hiding Solitary', hiding_solitary_d)

hiding_solitary.add_option('Continue', continue_hiding_solitary_rd)
hiding_solitary.add_option('Find Family', find_family_d)

# Run the game
start.run(t=t)