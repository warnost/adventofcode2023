file = open("day2_input.txt","r")
data = file.read().splitlines()

def process_game(game):
    possible = {"red": 12, "green": 13, "blue": 14}
    game_success = True

    game_parts = game.split(":")
    game_num = int(game_parts[0].replace("Game ",""))
    draws = game_parts[1].split(";")
    for draw in draws:
        colors = draw.split(",")
        counts = {}
        for color in colors:
            pair = color.strip().split(" ")
            counts.update({pair[1]:int(pair[0])})
        for key in counts.keys():
            if (counts.get(key) > possible.get(key)):
                game_success = False
      
    return [game_num, game_success]

winning_games = []                
for game in data:
    result = process_game(game)
    if (result[1]):
        winning_games.append(result[0])
        
sum(winning_games)
