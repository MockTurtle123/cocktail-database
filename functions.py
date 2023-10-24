def draw_line():
    print('\n' + '-' * 40)

def convert_cl(cl):
    """ Returns milliliters"""
    return int(cl * 10)

def display_info(name, recipe_book):
    info = []
    for cocktail in recipe_book:
        if cocktail['name'] == name:
            article = "an" if cocktail['glass'].startswith("o") else "a"
            info.append(f"{cocktail['name']} is typically served in {article} "
                  f"{cocktail['glass']} glass.\n\n"                  
                          f"Ingredients:")
            for item in cocktail["ingredients"]:
                try:
                    info.append(f"{convert_cl(item['amount'])}ml of {item['ingredient']}")
                except KeyError:
                    pass
            info.append('\n')
            for item in cocktail["ingredients"]:
                try:
                    info.append(item['special'])
                except KeyError:
                    pass
            info.append('\n')
            try:
                info.append(f"Usually garnished with {cocktail['garnish'].lower()}\n")
            except KeyError:
                pass

            try:
                info.append(f"Preparation: {cocktail['preparation']}")
            except KeyError:
                pass

    return info
