import json


with open('recipes.json', 'r', encoding='utf-8') as file:
    content = file.read()

content = content.replace("Vodka", 'Водка')
content = content.replace("Lemon juice", 'Лимонный сок')
content = content.replace("Syrup", 'Сироп')
content = content.replace("Sugar syrup", 'Сахарный сироп')
content = content.replace("Whiskey", 'Виски')
content = content.replace("Vermouth", 'Вермут')
content = content.replace("Cognac", 'Коньяк')
content = content.replace("Tequila", 'Текила')
content = content.replace("Gin", 'Джин')
content = content.replace("martini", 'мартини')
content = content.replace("Rum", 'Ром')
content = content.replace("Triple Sec", 'Трипл Сек')
content = content.replace("Lime juice", 'Сок лайма')
content = content.replace("Pineapple juice", 'Ананасовый сок')
content = content.replace("Coconut milk", 'Кокосовое молоко')
content = content.replace("Cream", 'Сливки')
content = content.replace("Cherry liqueur", 'Вишневый ликер')
content = content.replace("Cherry liqueur", 'Вишневый ликер')
content = content.replace("Cherry liqueur", 'Вишневый ликер')
content = content.replace("Cherry liqueur", 'Вишневый ликер')
print(content)
