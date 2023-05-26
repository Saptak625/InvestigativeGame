from model import Situation as S, Decision as D, RandomDecision as RD
t=1
max_t = 10

# Full Game.
# Nodes
start = S('start', 'You are working in a factory in Poland before the start of WWII. Germany invades, marking the start of the war. You get a letter from the government that says that you have been drafted to fight in the war. While this is happening, your wife is admitted to a mental hospital. What do you do?')

fight_war = S('Fight War', 'You join the army to fight in the war for Poland. You go through a few weeks of training, and then are put on the frontline of the war. You fight in the Battle of Westerplatte against the Germans. What happens to you?')

killed_war = S('Killed in War', 'Unfortunately, you were killed in war. Those close to you are very traumatized by this, but they forever remember you as a hero.')
defect = S('Defect', 'You spend a few days scouring the site for openings and ultimately decide to try your hand at escaping. What heppens?')

visit_wife = S('Visit Wife', 'You have decided to attempt visiting your wife in Poland')
stopped_nazi = S('Stopped by Nazi Soldiers', 'You are stopped by a group of Nazi soldiers, who ask you for identification. What happens to you?')

find_family = S('Find Family', 'You attempt to find your family in Poland. What happens to you?')
hiding_solitary = S('Hiding Solitary', 'You decide it is best to hide in solitary until it is safe enough to move freely.')

concentration_camp = S('Concentration Camp', 'You have been sent to a concentration camp, where the chances of survival are slim. Do you have what it takes to survive?')

executed = S('Executed', 'Unfortunately, you are executed by the Nazis. You never live past the war, and are never able to build a family. Those close to you are extremely traumatized by your death, even years after the war.')

real_papers = S('Real Papers', 'You decide to get registered and show real papers to the Nazis.')
PoW = S('Prisoner of War', 'During your time in the army, you get captured by the Germans and are now a prisoner of war')

rescued_allies = S('Rescued by Allies', 'Luckily, a group of allied soldiers infiltrate the imprisonment site and rescue you. You have been taken back to the allied soldiers’ base and live a good life')

escape_pow_sucess = S('Succesfully Escaped PoW', 'You have successfully escaped imprisonment! CONGRATULATIONS Soldier!')

immigrate_allied = S('Immigrate to Allied Country', 'Henri Guisan has accepted you as a refugee! Congratulations. Enjoy your life. ')
immigrate_reject = S('Immigration Rejected', 'Guisan does not want you. Too bad, so sad.')
wait_war_allied = S('Wait for War to End in Allied Country', 'You are able to settle in Switzerland and live a happy life with your family. Now, you just sit back and wait until the war ends.')

stopped_nazi_2 = S('Stopped by Nazi Soldiers while returning to Poland', 'You are stopped by a group of Nazi soldiers, who ask you for identification. What happens to you?')

guard_friend = S('Befriend Guard', 'You are able to make friends with a guard, who you think might be able to help you in the future.')

escape = S('Successful Escape', 'You successfully escape the concentration camp. However, you are unable to find complete safety, and instead spend the rest of the war in meticulous hiding. ')

find_family_success = S('Find Family', 'You are able to successfully find your family. ')
keep_family_together = S('Keep Family Together', 'You decide to prioritize keeping the family together, even if it is much riskier than splitting up.')
lose_grandparents = S('Lose Parents and Grandparents', 'Parents and Grandparents are sent regardless of your decision. You never hear from them again. However, you do not know that your decision did not affect their fate, and you regret your decision for the rest of your life. What do you do next?')
family_intact = S('Protect Your Family', 'You decide to protect your family by taking them to hide in the attic of a neighbor\'s house. What happens next?')

kids_executed = S('Kids are Executed', 'Your kids are unfortunately executed, which leaves you with an intense amount of guilt and depression, even years after the war.')

neighbors_executed = S('Neighbors Executed', 'Your neighbors are unfortunately executed, which leaves you with an intense amount of guilt and depression, even years after the war. You still do not know where your kids are.$$')

# Decisions/Edges
flee_rd = RD((lambda **kwargs: 80 * (0.7)**kwargs["t"], 'You are able to successfully make it safely to the border of an allied country. You are approached by a border patrol agent. What happens to you?', immigrate_allied), (lambda **kwargs: 100 - (80 * (0.7)**kwargs["t"]), 'You have been caught by the Nazis on your mission to flee the country. You have been taken back to mainland Germany, specifically the Flossenburg concentration camp.', concentration_camp))
wife_rd = RD((40, 'Visit wife in hospital. You have successfully reached your wife and reconnect with her in the hospital.', visit_wife), (35, 'Caught by Polish government for evading draft. You have been captured and held in hostage by the Polish government for evading the draft', fight_war), (25, 'Stopped by Nazi soldiers. You are stopped by a group of Nazi soldiers, who ask you for identification. What happens to you?', stopped_nazi))
fight_war_d = D(fight_war)

defect_d = D(defect)
continue_war_rd = RD((lambda **kwargs: 25 * (1.05)**kwargs["t"], 'Unfortunately, you were killed in war. Those close to you are very traumatized by this, but they forever remember you as a hero.', killed_war), (lambda **kwargs: 0.7 * (100 - (25 * (1.05)**kwargs["t"])), 'Days keep passing as you face your fate in the imprisonment site. You await a fearless, god-sent soldier to come and save you', fight_war), (lambda **kwargs: 0.3 * (100 - (25 * (1.05)**kwargs["t"])), 'During your time in the army, you get captured by the Germans and are now a prisoner of war', PoW))
hiding_solitary_d = D(hiding_solitary)
find_family_d = D(find_family)

continue_hiding_solitary_rd = RD((lambda **kwargs: 35 * (1.05)**kwargs["t"], 'You have been sent to a concentration camp, where the chances of survival are slim. Do you have what it takes to survive?', concentration_camp), (lambda **kwargs: 100 - (35 * (1.05)**kwargs["t"]), 'Days keep passing as you face your fate in the imprisonment site. You await a fearless, god-sent soldier to come and save you', hiding_solitary))

fake_papers_rd = RD((lambda **kwargs: 20 * (1.05)**kwargs["t"], 'The soldier realizes that the papers are fake, and you are sent to be immediately executed', executed), (lambda **kwargs: 100 - (20 * (1.05)**kwargs["t"]), 'The soldiers let you pass without suspecting you. What do you do?', visit_wife))
real_papers_d = D(real_papers)

house_seized_d = D(concentration_camp, desc='Your house was seized for redistricting reasons. You were relocated to a Labor Camp.')

face_fate_rd = RD((lambda **kwargs: 35 * (0.9)**kwargs["t"], 'Luckily, a group of allied soldiers infiltrate the imprisonment site and rescue. You have been taken back to the allied soldiers’ base and live a good life', rescued_allies), (lambda **kwargs: 0.2 * (100 - (35 * (0.9)**kwargs["t"])), 'After a couple of days, you become executed alongside the other prisoners of war', executed), (lambda **kwargs: 0.8 * (100 - (35 * (0.9)**kwargs["t"])), 'Days keep passing as you face your fate in the imprisonment site. You await a fearless, god-sent soldier to come and save you', PoW))
escape_pow_rd = RD((lambda **kwargs: 50 * (0.95)**kwargs["t"], 'You have successfully escaped imprisonment! CONGRATULATIONS Soldier!', escape_pow_sucess), (lambda **kwargs: 100 - (50 * (0.95)**kwargs["t"]), 'Unfortunately, you were unable to escape. Soldiers found you and alerted their leader Hitler. It has been ordered that you are transported to Auscwhitz instantly with maximum security detail', concentration_camp))

help_pows_rd = RD((lambda **kwargs: 35 * (0.9)**kwargs["t"], 'Deciding to serve the poor prisoners of war, you decide to embark on the risky task of helping other prisoners of war escape. Over time, you help a multitude of soldiers escape.', escape_pow_sucess), (lambda **kwargs: 100 - (35 * (0.9)**kwargs["t"]), 'You were caught while trying to rescue other PoWs. You are sent to a concentration camp.', concentration_camp))

apply_immigration_rd = RD((lambda **kwargs: 40 * (0.9)**kwargs["t"], 'Henri Guisan has accepted you as a refugee! Congratulations. Enjoy your life.', wait_war_allied), (lambda **kwargs: 100 - (40 * (0.9)**kwargs["t"]), 'Guisan does not want you. Too bad, so sad.', immigrate_reject))

sent_back_rd = RD((lambda **kwargs: 55 * (0.9)**kwargs["t"], 'You have been sent back to Poland and are now forced to fight in the war. Ready up soldier', fight_war), (lambda **kwargs: 100 - (55 * (0.9)**kwargs["t"]), 'Guisan does not want you. Too bad, so sad.', immigrate_reject))

stopped_nazi_2_rd = RD((lambda **kwargs: 10 * (1.05)**kwargs["t"], 'The soldier realizes that the papers are fake, and you are sent to be immediately executed', executed), (lambda **kwargs: 0.65*(100 - (10 * (1.05)**kwargs["t"])), 'The soldier realizes that the papers are fake, and you are sent a concentration camp.', concentration_camp), (lambda **kwargs: 0.35*(100 - (10 * (1.05)**kwargs["t"])), 'The soldiers let you pass without suspecting you. What do you do?', find_family))

escape_concentration_rd = RD((lambda **kwargs: 35 * (0.8)**kwargs["t"], 'Fortunately, you are able to make it out of the concentration camp. You are finally free!', escape), (lambda **kwargs: 0.9*(100 - (35 * (0.8)**kwargs["t"])), 'You are caught attempting to escape from concentration camp. You are gassed next morning.', executed), (lambda **kwargs: 0.1*(100 - (35 * (0.8)**kwargs["t"])), 'You are caught attempting to escape from concentration camp. You miraculously find allied troops!', rescued_allies))
continue_concentration_rd = RD((75, 'You are another dreaded week closer to your execution. Your time is running out...', concentration_camp), (10, 'You make some friends with fellow prisoners in the concentration camp.', concentration_camp), (10, 'Unfortunately, you are sent to get gassed', executed), (5, 'You are able to make friends with a guard at the concentration camp, who you think might be able to help you in the future.', guard_friend))

guard_rd = RD((lambda **kwargs: 50 * (0.9)**kwargs["t"], 'You are able to convince the guard to help you escape.', escape), (lambda **kwargs: 100 - (50 * (0.9)**kwargs["t"]), 'The guard does not help you escape and instead reports you, and you will be immediately executed.', executed))
ignore_guard_d = D(concentration_camp, desc='You ignore your friendship with the guard and continue to wait for your execution.')

send_kids_countryside_rd = RD((lambda **kwargs: 45 * (0.9)**kwargs["t"], 'Fortunately, the kids survive, and you get them back.', keep_family_together), (lambda **kwargs: 100 - (45 * (0.9)**kwargs["t"]), 'Your kids are unfortunately executed, which leaves you with an intense amount of guilt and depression, even years after the war.', kids_executed))
give_kids_neighbors_rd = RD((lambda **kwargs: 15 * (1.05)**kwargs["t"], 'Your Neighbors have been taken to a concentration camp. Their lives and ', keep_family_together), (lambda **kwargs: 0.65 * (100 - (15 * (0.9)**kwargs["t"])), 'Kids survived with your neighbors.$$', keep_family_together), (lambda **kwargs: 0.35 * (100 - (15 * (0.9)**kwargs["t"])), 'Kids are killed by neighbors when they find out that they will be sent to Auschwitz. Sorry for your loss bud.', kids_executed))
keep_family_together_d = D(keep_family_together)

find_family_rd = RD((lambda **kwargs: 65 * (0.9)**kwargs["t"], 'You are able to successfully find your family.', find_family_success), (lambda **kwargs: 100 - (65 * (0.9)**kwargs["t"]), 'You are caught by Nazis before you find your family. You are sent to a concentration camp.', concentration_camp))

protect_family_rd = RD((60, 'One of your family members is caught, and they are taken to a concentration camp without you.', family_intact), (15, 'Your entire family is caught, and taken to concentration camp', concentration_camp), (25, 'You are caught, and taken to concentration camp.', concentration_camp))

neighbors_executed_rd = RD((lambda **kwargs: 40 * (1.05)**kwargs["t"], 'Kids are taken to concentration camp as well and are executed. Sorry for your loss bud.', kids_executed), (lambda **kwargs: 100 - (40 * (1.05)**kwargs["t"]), 'Your children are alive and you reunite with them!', keep_family_together))

# Add decisions to nodes
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

stopped_nazi.add_option('Show Fake Papers', fake_papers_rd)
stopped_nazi.add_option('Show Real Papers', real_papers_d)

real_papers.add_option('Stay', house_seized_d)
real_papers.add_option('Flee Country', flee_rd)

PoW.add_option('Escape', escape_pow_rd)
PoW.add_option('Face Fate', face_fate_rd)

escape_pow_sucess.add_option('Help Other PoWs', help_pows_rd)
escape_pow_sucess.add_option('Find Family', find_family_d)
escape_pow_sucess.add_option('Flee Country', flee_rd)

visit_wife.add_option('You are able to find your family along with your wife.', find_family_d)
visit_wife.add_option('You decide to abandon your wife and flee the country for your own safety.', flee_rd)

immigrate_allied.add_option('Find Family', find_family_d)
immigrate_allied.add_option('Apply for Immigration', apply_immigration_rd)

stopped_nazi_2.add_option('Continue', stopped_nazi_2_rd)

concentration_camp.add_option('Escape', escape_concentration_rd)
concentration_camp.add_option('Continue', continue_concentration_rd)

guard_friend.add_option('Confide with Guard', guard_rd)
guard_friend.add_option('Ignore Guard', ignore_guard_d)

find_family.add_option('Continue', find_family_rd)

find_family_success.add_option('Send Kids to Countryside', send_kids_countryside_rd)
find_family_success.add_option('Give Kids to Neighbors', give_kids_neighbors_rd)
find_family_success.add_option('Keep Family Together', keep_family_together_d)

keep_family_together.add_option('You decide to send your parents and grandparents to the mandatory living space', lose_grandparents)
keep_family_together.add_option('You Refuse to send your parents and grandparents to the mandatory living space.', lose_grandparents)

lose_grandparents.add_option('Flee Country', flee_rd)
lose_grandparents.add_option('Protect Family in Hiding', protect_family_rd)

family_intact.add_option('Flee Country', flee_rd)
family_intact.add_option('Protect Family in Hiding', protect_family_rd)

neighbors_executed.add_option('Continue', neighbors_executed_rd)

# Run the game
start.run(t=t, max_t=max_t)