from __future__ import print_function
from copy import deepcopy


def check_is_end(i, j, N, M, block):
    if(i < 0):
        return True
    if(j < 0):
        return True
    if(i >= N):
        return True
    if(j >= M):
        return True
    if(block[i][j] == 1):  # If There is a wall at that particular coordinate
        return True

    return False


def compute_value(i, j, N, M, block, previous_utility):
    val1, val2, val3, val4 = 0.0, 0.0, 0.0, 0.0

    if(check_is_end(i+1, j, N, M, block)) == False:
        val1 += 0.8 * previous_utility[i+1][j]
    else:
        val1 += 0.8 * previous_utility[i][j]
    if (check_is_end(i, j-1, N, M, block)) == False:
        val1 += 0.1 * previous_utility[i][j-1]
    else:
        val1 += 0.1 * previous_utility[i][j]
    if (check_is_end(i, j+1, N, M, block)) == False:
        val1 += 0.1 * previous_utility[i][j+1]
    else:
        val1 += 0.1 * previous_utility[i][j]

    if(check_is_end(i-1, j, N, M, block)) == False:
        val2 += 0.8 * previous_utility[i-1][j]
    else:
        val2 += 0.8 * previous_utility[i][j]
    if (check_is_end(i, j-1, N, M, block)) == False:
        val2 += 0.1 * previous_utility[i][j-1]
    else:
        val2 += 0.1 * previous_utility[i][j]
    if (check_is_end(i, j+1, N, M, block)) == False:
        val2 += 0.1 * previous_utility[i][j+1]
    else:
        val2 += 0.1 * previous_utility[i][j]

    if(check_is_end(i, j+1, N, M, block)) == False:
        val3 += 0.8 * previous_utility[i][j+1]
    else:
        val3 += 0.8 * previous_utility[i][j]
    if (check_is_end(i-1, j, N, M, block)) == False:
        val3 += 0.1 * previous_utility[i-1][j]
    else:
        val3 += 0.1 * previous_utility[i][j]
    if (check_is_end(i+1, j, N, M, block)) == False:
        val3 += 0.1 * previous_utility[i+1][j]
    else:
        val3 += 0.1 * previous_utility[i][j]

    if(check_is_end(i, j-1, N, M, block)) == False:
        val4 += 0.8 * previous_utility[i][j-1]
    else:
        val4 += 0.8 * previous_utility[i][j]
    if (check_is_end(i-1, j, N, M, block)) == False:
        val4 += 0.1 * previous_utility[i-1][j]
    else:
        val4 += 0.1 * previous_utility[i][j]
    if (check_is_end(i+1, j, N, M, block)) == False:
        val4 += 0.1 * previous_utility[i+1][j]
    else:
        val4 += 0.1 * previous_utility[i][j]

    return max(val1, val2, val3, val4)


def main():
    iterations = 0
    N, M = raw_input().split(" ")
    N = int(N)
    M = int(M)
    previous_utility = [[float(0) for j in range(M)] for i in range(N)]
    utility = [[float(0) for j in range(M)] for i in range(N)]

    block = [[int(0) for j in range(M)] for i in range(N)]
    reward = [[]for i in range(N)]

    for i in range(N):
        x = raw_input()
        reward[i] = [float(j) for j in x.split(" ")]

    E, W = raw_input().split(" ")

    # Defining terminal-end states to be 2
    E = int(E)
    for i in range(E):
        x = raw_input()
        y = [int(j) for j in x.split()]
        block[y[0]][y[1]] = 2
        utility[y[0]][y[1]] = reward[y[0]][y[1]]

    # Defining walls to be 1
    W = int(W)
    for i in range(W):
        x = raw_input()
        y = [int(j) for j in x.split()]
        block[y[0]][y[1]] = 1

    start = [0, 0]
    start[0], start[1] = raw_input().split(" ")
    start[0] = int(start[0])
    start[1] = int(start[1])
    step_reward = raw_input()
    step_reward = float(step_reward)

    error = 0.01
    discount_factor = 1
    delta = 1
    print(error*((1-discount_factor)/(discount_factor)))
    while (delta > (error*(1-discount_factor)/(discount_factor))):

        iterations += 1
        delta = 0
        previous_utility = deepcopy(utility)
        for i in range(N):
            for j in range(M):
                if(block[i][j] == 1 or block[i][j] == 2):
                    continue
                value = compute_value(i, j, N, M, block, previous_utility)
                utility[i][j] = step_reward + discount_factor*value
                if(previous_utility[i][j]) != 0:
                    delta = max(delta, abs(abs(utility[i][j]-previous_utility[i][j]) /
                                           previous_utility[i][j]))
                else:
                    delta = max(delta, abs(
                        utility[i][j]-previous_utility[i][j]))

        print("Iteration %d" % iterations, end='\n')
        for i in range(N):
            for j in range(M):
                print("%.3f" % utility[i][j], end=" ")
            print("", end='\n')
        print("")


main()
