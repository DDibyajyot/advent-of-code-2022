# Read input
with open('input.txt') as f:
    data = f.read().splitlines()

# Parse input
# 1. Seperate moves and starting shipping stacks
# 2. Turn 9 shipping stacks into a list of lists
# 3. Turn moves into a list of moves
# 4. Run moves on starting shipping stacks

# 1. Seperate moves and starting shipping stacks
shipping_stacks = data[:8]
moves = data[10:]

# 2. Turn 9 shipping stacks into a list of lists
stacks = [[] for _ in range(9)]
for stack in shipping_stacks:
    # Every four characters is a stack
    # the second letter is the stack container
    for i in range(0, len(stack), 4):
        stack_number = i // 4
        potential_container = stack[i:i+4]
        # If the container is not empty
        if potential_container[1] != ' ':
            stacks[stack_number].append(potential_container[1])
# Reverse the stacks so the top is the first element
# This makes it easier to pop from the stack
stacks = [stack[::-1] for stack in stacks]

# 3. Turn moves into a list of moves
moves_list = []
for move in moves:
    # The first letter is the number of containers to move
    # The second number is the source stack
    # The third number is the destination stack
    # Find numbers in move
    numbers = [int(number) for number in move.split() if number.isdigit()]
    moves_list.append(numbers)

# 4. Run moves on starting shipping stacks
for move in moves_list:
    # Fix index
    move[1] -= 1
    move[2] -= 1
    # Move containers from source stack to destination stack
    for _ in range(move[0]):
        # Check if the source stack is empty
        if stacks[move[1]]:
            # Pop the top container from the source stack
            container = stacks[move[1]].pop()
            # Push the container onto the destination stack
            stacks[move[2]].append(container)
# Print top of each stack
print(''.join([stack[-1] for stack in stacks]))

# Day 5: Part 2
# Supply Stacks
# CrateMover 9001
# Read input
with open('input.txt') as f:
    data = f.read().splitlines()

# Solution
# Parse Input
# Simulate crane movement

# 1. Seperate moves and starting shipping stacks
# 2. Turn 9 shipping stacks into a list of lists
# 3. Turn moves into a list of moves
# 4. Run moves on starting shipping stacks

# 1. Seperate moves and starting shipping stacks
shipping_stacks = data[:8]
moves = data[10:]

# 2. Turn 9 shipping stacks into a list of lists
stacks = [[] for _ in range(9)]
for stack in shipping_stacks:
    # Every four characters is a stack
    # the second letter is the stack container
    for i in range(0, len(stack), 4):
        stack_number = i // 4
        potential_container = stack[i:i+4]
        # If the container is not empty
        if potential_container[1] != ' ':
            stacks[stack_number].append(potential_container[1])
# Reverse the stacks so the top is the first element
# This makes it easier to pop from the stack
stacks = [stack[::-1] for stack in stacks]

# 3. Turn moves into a list of moves
moves_list = []
for move in moves:
    # The first letter is the number of containers to move
    # The second number is the source stack
    # The third number is the destination stack
    # Find numbers in move
    numbers = [int(number) for number in move.split() if number.isdigit()]
    moves_list.append(numbers)

# 4. Run moves on starting shipping stacks
for move in moves_list:
    # Fix index
    move[1] -= 1
    move[2] -= 1
    # Move containers from source stack to destination stack
    # Move containers as a group, not one at a time
    # Check if the source stack is empty
    if stacks[move[1]]:
        # Grab the top containers from the source stack
        containers_to_move = stacks[move[1]][-move[0]:]
        # Remove the containers from the source stack
        stacks[move[1]] = stacks[move[1]][:-move[0]]
        # Push the containers onto the destination stack
        stacks[move[2]] += containers_to_move
# Print top of each stack
print(''.join([stack[-1] for stack in stacks]))
