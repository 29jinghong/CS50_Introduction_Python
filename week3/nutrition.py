food = input("Enter here: ").lower()

nutrition ={"apple" : 130, "bannana" : 110, "avocado" : 50, "sweet cherries" : 100, "cantaloupe" : 50, "grapefruit" : 60, "grapes" : 90, "honeydew melon" : 50, "kiwifruit" : 90, "lemon" : 15, "lime" : 20, "nectarine" : 60, "orange" : 80, "peach" : 60, "pear" : 100, "pineapple" : 50, "plums" : 70, "tangerine" : 50, "watermelon" : 80} 

for frit in nutrition:
    if food == frit:
        print(nutrition[food])
