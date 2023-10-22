import json


def convert_cl(cl):
    """ Returns milliliters"""
    return int(cl * 10)


def draw_line():
    print('\n' + '-' * 40)

with open('recipes.json', 'r', encoding='utf-8') as file:
    content = file.read()

recipes = json.loads(content)

menu = ['1. Search by name', '2. Search by ingredient', '3. Print out all the cocktails (alphabetically)', '4. Exit']
print("Welcome to the cocktail database.")

while True:

    print('Type a number to navigate through the menu:')
    for line in menu:
        print(line)
    user_action = input()
    user_action = user_action.strip().strip(".")

    match user_action:
        case '1':
            name = input('Type the name of the cocktail: ')
            name = name.lower()
            for cocktail in recipes:
                if name == cocktail['name'].lower():
                    draw_line()
                    if cocktail['glass'].startswith("o"):
                        print(f"{cocktail['name']} is typically served in an {cocktail['glass']} glass.\n\n"
                          f"Ingredients:")
                    else:
                        print(f"{cocktail['name']} is typically served in a {cocktail['glass']} glass.\n\n"
                              f"Ingredients:")
                    for item in cocktail["ingredients"]:
                        try:
                            print(f"{convert_cl(item['amount'])}ml of {item['ingredient']}")
                        except KeyError:
                            pass
                    for item in cocktail["ingredients"]:
                        try:
                            print(item['special'])
                        except KeyError:
                            pass
                    print('\n')
                    try:
                        print(f"Usually garnished with {cocktail['garnish'].lower()}")
                    except KeyError:
                        pass

                    try:
                        print(f"Preparation: {cocktail['preparation']}")
                    except KeyError:
                        pass

                    draw_line()
                    again = input("Search again? (yes / no)")
                    if again == 'yes':
                        continue
                    else:
                        exit()


        case '2':
            ingredient = input('Type the name of the ingredient: ')
            ingredient = ingredient.lower()
            found_matches = []

            for cocktail in recipes:
                for item in cocktail['ingredients']:
                    try:
                        if ingredient in item['ingredient'].lower():
                            found_matches.append(cocktail['name'])
                    except KeyError:
                        continue
            draw_line()
            print(f"{len(found_matches)} matches found for '{ingredient}':")
            for index, item in enumerate(found_matches):
                print(f"{index + 1} - {item}")

            draw_line()

        case '3':
            alphabet = []
            for cocktail in recipes:
                alphabet.append(cocktail['name'])
            alphabet = sorted(alphabet)
            for index, item in enumerate(alphabet):
                print(f"{index + 1}.{item}")
            draw_line()


        case '4':
            exit()
