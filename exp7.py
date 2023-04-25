P1 = True
P2 = True
P3 = True
P4 = False
P5 = False

rule1 = P1 and P2
rule2 = P1 and P2 and P3 and not P4
rule3 = P1 and P2 and P3 and not P4 and P5

if (rule3):
    print("The customer can rent SUV")
elif(rule2):
    print("Customer can rent Sedan")
elif(rule2):
    print("The Customer is not elligible")
