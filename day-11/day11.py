# return to monke
#                 _
#             ,.-" "-.,
#            /   ===   \
#           /  =======  \
#        __|  (o)   (0)  |__      
#       / _|    .---.    |_ \         
#      | /.----/ O O \----.\ |       
#       \/     |     |     \/        
#       |                   |            
#       |                   |           
#       |                   |          
#       _\   -.,_____,.-   /_         
#   ,.-"  "-.,_________,.-"  "-.,
#  /          |       |          \  
# |           l.     .l           | 
# |            |     |            |
# l.           |     |           .l             
#  |           l.   .l           | \,     
#  l.           |   |           .l   \,    
#   |           |   |           |      \,  
#   l.          |   |          .l        |
#    |          |   |          |         |
#    |          |---|          |         |
#    |          |   |          |         |
#    /"-.,__,.-"\   /"-.,__,.-"\"-.,_,.-"\
#   |            \ /            |         |
#   |             |             |         |
#    \__|__|__|__/ \__|__|__|__/ \_|__|__/ 

with open("input.txt", "r") as file:
    data = file.read().split('\n\n')
    monkeyboi, monkeybois = {}, {}
    for e, monkey in enumerate(data):
        
        monkey = monkey.splitlines()[1:]
        items = [int(x) for x in monkey[0].split(": ")[1].split(", ")]

        def monkey_ops(x, y): 
            return (x + (int(y[1]) if y[1].isdigit() else x)) if y[0] == "+" else (x * (int(y[1]) if y[1].isdigit() else x))

        def test(x, y): 
            return [y[1], y[0]][not x % y[2]]


        oppa = monkey[1].split(" ")[-2:]
        zzz = [int(monkey[3].split(" ")[-1]), int(monkey[4].split(" ")[-1]), int(monkey[2].split(" ")[-1])]

        monkeyboi[e] = {"i": items, "o": monkey_ops,"t": test, "op": oppa, "bool": zzz}

        monkeybois[e] = {"i": items[:], "o": monkey_ops,"t": test, "op": oppa[:], "bool": zzz[:]}

mod = 1
for e in monkeyboi:
    mod *= monkeyboi[e]["bool"][-1]

inspects1 = {e: 0 for e in monkeyboi}
inspects2 = {**inspects1}

for x in range(10000):
    for i, monkeys, inspects in [(0, monkeyboi, inspects1), (1, monkeybois, inspects2)]:
        if (x < 20 and i == 0) or i == 1:
            for e, monkey in monkeys.items():
                while monkey["i"]:
                    inspects[e] += 1
                    item = monkey["i"].pop(0)
                    item = monkey["o"](item, monkey["op"])
                    item = item // 3 if not i else item % mod
                    monkeys[monkey["t"](item, monkey["bool"])]["i"].append(item)

p1 = sorted(inspects1.values())
p2 = sorted(inspects2.values())

print("Day 11: ", p1[-2] * p1[-1], p2[-2] * p2[-1])
