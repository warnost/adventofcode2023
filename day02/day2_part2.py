file = open("day2_input.txt","r")
data = file.read().splitlines()

def process_game(game):
    game_parts = game.split(":")
    draws = game_parts[1].split(";")
    min_counts = {"red": 0, "green": 0, "blue": 0}
    for draw in draws:
        colors = draw.split(",")
        for color in colors:
            pair = color.strip().split(" ")
            if (int(pair[0]) > min_counts.get(pair[1])):
                min_counts.update({pair[1]:int(pair[0])})
      
    return min_counts.get("red") * min_counts.get("green") * min_counts.get("blue")

game_powers = []                
for game in data:
    game_powers.append(process_game(game))
        
sum(game_powers)