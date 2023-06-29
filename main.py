def word_input(player_name):
    word = input("{} enter a word (or type 'exit' to stop the game): ".format(player_name)).lower()
    return word

def validate_word(word):
    message = {"status": False, "error": None}
    if word == "exit":
        message["status"] = True
    elif not word.isalpha():
        message["error"] = "Invalid input!"
    else:
        message["status"] = True

    return message

def validate_exist_word(word, words):
    message = {"status": False, "error": None}
    if word in words:
        message["error"] = "The word has already been used in the game!"
    else:
        message["status"] = True

    return message

def validate_first_letter(word, words):
    message = {"status": False, "error": None}
    if len(words) > 0:
        last_word = words[-1]
        if last_word[-1] == word[0]:
            message["status"] = True
        else:
            message["error"] = "Entered word must start with the last letter of the previous word!"
    else:
        message["status"] = True

    return message

def validate(word, words):
    message = {"status": True, "error": None}
    result_1 = validate_word(word)
    if not result_1["status"]:
        return result_1

    result_2 = validate_exist_word(word, words)
    if not result_2["status"]:
        return result_2

    result_3 = validate_first_letter(word, words)
    if not result_3["status"]:
        return result_3

    return message

def game(players_num):
    print("Welcome to the word game!")
    words = []
    players = []
    for i in range(1, players_num + 1):
        player_name = input("Enter the name of Player {}: ".format(i))
        players.append(player_name)

    print("Let's play!")
    current_player = 0
    while True:
        word = word_input(players[current_player])
        validation_result = validate(word, words)
        if validation_result["status"]:
            if current_player == players_num - 1:
                current_player = 0
            else:
                current_player += 1
                words.append(word)
                continue

        print(validation_result["error"])

        if word == "exit":
            print("Game stopped.")
            break

if __name__ == '__main__':
    players_num = int(input("Please, enter the number of players: "))
    game(players_num)
