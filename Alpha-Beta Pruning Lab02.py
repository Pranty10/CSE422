# Part 1: Mortal Kombat
import math

a = math.inf

def abPruning(depthNode, indexNodes, maximization, leafNodesGiven, alPha, B, highestDepthReach):
    if depthNode == highestDepthReach:
        return leafNodesGiven[indexNodes]
    if maximization:
        x = -a
        for i in range(2):
            value = abPruning(depthNode + 1, indexNodes * 2 + i, False, leafNodesGiven, alPha, B, highestDepthReach)
            x = max(x, value)
            alPha = max(alPha, x)
            if B <= alPha:
                break
        return x
    else:
        x = a
        for i in range(2):
            value = abPruning(depthNode + 1, indexNodes * 2 + i, True, leafNodesGiven, alPha, B, highestDepthReach)
            x = min(x, value)
            B = min(B, x)

            # Alpha Beta Pruning
            if B <= alPha:
                break
        return x

def Simulation(startingPlayer, highestDepthReach):
    leafNodesGiven = [-1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1,
                      1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1]
#each round winner
   
    xd = []
#final winner    
    new = []
    round_num = 1
    current_player = startingPlayer
    while round_num <= highestDepthReach:
        finalResult = abPruning(0, 0, current_player == 0, leafNodesGiven, -a, a, highestDepthReach)
        if finalResult == -1:
            xd.append("Scorpion")
        else:
            xd.append("Sub-Zero")#Sub-Zero
        current_player = 1 - current_player
        round_num += 1
    if finalResult == -1:
        new.append("Scorpion")
    else:
        new.append("Sub-Zero")
    print("Game Winner:", new[0])
    print("Total Rounds Played:", round_num - 1)
    for i in range((highestDepthReach)):
        print(f"Winner of Round {i+1}: {xd[i]}")

startingPlayer = int(input(" 0 for Scorpion, 1 for Sub-Zero: "))
x = 3  
Simulation(startingPlayer, x)

# Part 2: Games with Magic
import math

a = math.inf

def abPruning(depthNode, indexNodes, pacmanMaximizing, leafNodesGiven, a_pa, B, highestDepthReach):
    if depthNode == highestDepthReach:
        return leafNodesGiven[indexNodes]

    if pacmanMaximizing:
        nodeValueReturning = -a
        for i in range(2):
            recursion_value = abPruning(depthNode + 1, indexNodes * 2 + i, False, leafNodesGiven, a_pa, B, highestDepthReach)
            nodeValueReturning = max(nodeValueReturning, recursion_value)
            a_pa = max(a_pa, nodeValueReturning)
            if B <= a_pa:
                break
        return nodeValueReturning
    else:
        nodeValueReturning = a
        for i in range(2):
            recursion_value = abPruning(depthNode + 1, indexNodes * 2 + i, True, leafNodesGiven, a_pa, B, highestDepthReach)
            nodeValueReturning = min(nodeValueReturning, recursion_value)
            B = min(B, nodeValueReturning)
            if B <= a_pa:
                break
        return nodeValueReturning

def pacmanGame(c):
    leafNodes_left = [3, 6, 2, 3, 7, 1, 2, 0]
    withoutDarkMagic = abPruning(0, 0, True, leafNodes_left, -a, a, highestDepthReach=3)
    lef_ts_idevalue = max(leafNodes_left[0], leafNodes_left[1])
    right_value = max(leafNodes_left[4], leafNodes_left[5])

    left_v = lef_ts_idevalue - c
    r_value_mgc = right_value - c

    if r_value_mgc > withoutDarkMagic and r_value_mgc > left_v:
        return f"The new minimax value is {r_value_mgc}. Pacman goes right and uses dark magic."
    else:
        return f"The minimax value is {withoutDarkMagic}. Pacman does not use dark magic."

print(pacmanGame(int(input("Enter cost or penalty value : "))))
