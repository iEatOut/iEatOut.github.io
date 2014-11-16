
#recipe = json file
#allergy_array = array of user's allergies
#returns 1 if recipe satisfies allergy restrictions, 0 otherwise
def calculate_match(recipe_ingredients, allergy_array):

    dairy = ["milk"]
    egg = ["egg","eggs"]
    gluten = ["wheat", "wheatberries", "durum", "emmer", "semolina", "spelt", "farina", "farro", "graham", "einkorn wheat"
              , "rye", "barley", "triticale", "malt", "malted barley flour", "malted milk", "malt extract", "malt syrup", "malt flavoring", "malt vinegar", "salad dressings", "self-basting turkey", "soy sauce"]
    peanut = ["peanut", "peanuts", "nut", "nuts"]
    seafood = ["fish", "shrimp", "salmon", "catfish", "lobster", "crab", "tilapia", "oyster"] 
    sesame = ["sesame"]
    soy = ["soy","soymilk"]
    wheat = ["wheat","grain","whole wheat"]

    for allergy in allergy_array:
        if allergy == "Dairy-Free":
            for ingredient in dairy:
                for recipe_ingredient in recipe_ingredients:
                    if ingredient == recipe_ingredient:
                        return 0
        if allergy == "Egg-Free":
            for ingredient in egg:
                for recipe_ingredient in recipe_ingredients:
                    if ingredient == recipe_ingredient:
                        return 0
        if allergy == "Gluten-Free":
            for ingredient in gluten:
                for recipe_ingredient in recipe_ingredients:
                    if ingredient == recipe_ingredient:
                        return 0
        if allergy == "Peanut-Free":
            for ingredient in peanut:
                for recipe_ingredient in recipe_ingredients:
                    if ingredient == recipe_ingredient:
                        return 0
        if allergy == "Seafood-Free":
            for ingredient in seafood:
                for recipe_ingredient in recipe_ingredients:
                    if ingredient == recipe_ingredient:
                        return 0
        if allergy == "Sesame-Free":
            for ingredient in sesame:
                for recipe_ingredient in recipe_ingredients:
                    if ingredient == recipe_ingredient:
                        return 0
        if allergy == "Soy-Free":
            for ingredient in soy:
                for recipe_ingredient in recipe_ingredients:
                    if ingredient == recipe_ingredient:
                        return 0
        if allergy == "Wheat-Free":
            for ingredient in wheat:
                for recipe_ingredient in recipe_ingredients:
                    if ingredient == recipe_ingredient:
                        return 0
    return 1
                                
            

    

