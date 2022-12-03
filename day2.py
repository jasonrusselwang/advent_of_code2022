opp_shapes = {"a": "rock", "b": "paper", "c": "scissors"}
my_shapes = {"x": "rock", "y": "paper", "z": "scissors"}
shape_scores = {"x": 1, "y": 2, "z": 3}
score = 0

with open("inputs/day2data.txt", "r") as file:
    for line in file:
        curr_round = [i.replace("\n", "").lower() for i in line.split(" ")]
        # print(f"Opponent: {opp_shapes[curr_round[0]]}, You: {my_shapes[curr_round[1]]}")
        # rock beats scissors
        if curr_round[1] == "x":
            score += shape_scores[curr_round[1]]
            if curr_round[0] == "a":
                score += 3
            elif curr_round[0] == "b":
                score += 0
            elif curr_round[0] == "c":
                score += 6
            else:
                print(f"invalid input {curr_round[1]}")
        # paper beats rock
        if curr_round[1] == "y":
            score += shape_scores[curr_round[1]]
            if curr_round[0] == "a":
                score += 6
            elif curr_round[0] == "b":
                score += 3
            elif curr_round[0] == "c":
                score += 0
            else:
                print(f"invalid input {curr_round[1]}")

        # scissors beats paper
        if curr_round[1] == "z":
            score += shape_scores[curr_round[1]]
            if curr_round[0] == "a":
                score += 0
            elif curr_round[0] == "b":
                score += 6
            elif curr_round[0] == "c":
                score += 3
            else:
                print(f"invalid input {curr_round[1]}")
print(score)

# part 2
results = {"x": "lose", "y": "draw", "z": "win"}
score = 0

with open("inputs/day2data.txt", "r") as file:
    for line in file:
        curr_round = [i.replace("\n", "").lower() for i in line.split(" ")]
        # print(f"Opponent: {opp_shapes[curr_round[0]]}, You need to: {results[curr_round[1]]}")
        # they pick rock
        if curr_round[0] == "a":
            if curr_round[1] == "x":
                pick = 3
                score += 0
            elif curr_round[1] == "y":
                pick = 1
                score += 3
            elif curr_round[1] == "z":
                pick = 2
                score += 6
            else:
                print(f"invalid input {curr_round[1]}")
            score += pick
        # they pick paper
        if curr_round[0] == "b":
            if curr_round[1] == "x":
                pick = 1
                score += 0
            elif curr_round[1] == "y":
                pick = 2
                score += 3
            elif curr_round[1] == "z":
                pick = 3
                score += 6
            else:
                print(f"invalid input {curr_round[1]}")
            score += pick
        # they pick scissors
        if curr_round[0] == "c":
            if curr_round[1] == "x":
                pick = 2
                score += 0
            elif curr_round[1] == "y":
                pick = 3
                score += 3
            elif curr_round[1] == "z":
                pick = 1
                score += 6
            else:
                print(f"invalid input {curr_round[1]}")
            score += pick
print(score)