from sympy import *

# Define the symbols and facts
A, B, C, D = symbols('A B C D')
facts = [A | B, B | C | D, ~C]

# Perform resolution
while True:
    new_facts = set()
    for i, fact1 in enumerate(facts):
        for j, fact2 in enumerate(facts):
            if i < j:
                for literal1 in fact1.args:
                    for literal2 in fact2.args:
                        if literal1 == ~literal2:
                            resolvent = Or(fact1.args.difference({literal1}), fact2.args.difference({literal2}))
                            if resolvent not in facts:
                                new_facts.add(resolvent)
        if ~fact1 in facts:
            print("Contradiction found")
            break
    else:
        if not new_facts:
            print("No new facts found")
            break
        facts = facts.union(new_facts)

# Print the final set of facts
print("Final set of facts:")
for fact in facts:
    print(fact)