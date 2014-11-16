import urllib2
import json
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from cross_validation import cross_validation

yummly_app_id = '69189240'
yummply_api_key = '9e160e5cce7ff68eab06dc8b9b99de71'

match_terms = []
match_terms.append("Low Sodium")
match_terms.append("Low Cholesterol")
match_terms.append("Low Sugar")
match_terms.append("High Protein")
match_terms.append("Low Carbs")
match_terms.append("High Fiber")


desired_search_terms = []
desired_search_terms.append("&nutrition.NA.min=0&nutrition.NA.max=140")
desired_search_terms.append("&nutrition.CHOLE.min=0&nutrition.CHOLE.max=20")
desired_search_terms.append("&nutrition.SUGAR.min=0&nutrition.SUGAR.max=10")
desired_search_terms.append("&nutrition.PROCNT.min=20&nutrition.PROCNT.max=100")
desired_search_terms.append("&nutrition.CHOCDF.min=0&nutrition.CHOCDF.max=20")
desired_search_terms.append("&nutrition.FIBTG.min=3&nutrition.FIBTG.max=50")

anti_search_terms = []
anti_search_terms.append("&nutrition.NA.min=141")
anti_search_terms.append("&nutrition.CHOLE.min=21")
anti_search_terms.append("&nutrition.SUGAR.min=11")
anti_search_terms.append("&nutrition.PROCNT.max=19")
anti_search_terms.append("&nutrition.CHOCDF.min=21")
anti_search_terms.append("&nutrition.FIBTG.max=2")

#returns the percent of suitable recipies according to nutrition information
def get_percent_of_nutrition_matches(menu_item, nutrition_array):
    menu_item = menu_item.replace(" ", "+")
    
    yummly_link_desired = "http://api.yummly.com/v1/api/recipes?_app_id=" + str(yummly_app_id) + "&_app_key=" + str(yummply_api_key) + "&q=" + str(menu_item)
    yummly_anti_link = "http://api.yummly.com/v1/api/recipes?_app_id=" + str(yummly_app_id) + "&_app_key=" + str(yummply_api_key) + "&q=" + str(menu_item)

    for nutrition_restriction in nutrition_array:
         nutrition_restriction_search = ""
         nutrition_restriction = nutrition_restriction.replace("\n","")
         for index in range(len(match_terms)):
             if nutrition_restriction == match_terms[index]:
                 nutrition_restriction_search = desired_search_terms[index]
                 yummly_link_desired += nutrition_restriction_search
                 yummly_anti_link += anti_search_terms[index]

    #print yummly_link_desired + "&maxResult=100"
    desired_recipie_search = urllib2.urlopen(yummly_link_desired + "&maxResult=100")
    desired_recipie_search = json.load(desired_recipie_search)
    desired_ingredient_list = []
    desired_category_list = []

    for index in range(len(desired_recipie_search["matches"])):
        desired_ingredient_list.append(desired_recipie_search["matches"][index]["ingredients"])
        desired_category_list.append(1)
        
        
    anti_recipie_search = urllib2.urlopen(yummly_anti_link + "&maxResult=100")
    anti_recipie_search = json.load(anti_recipie_search)
    anti_ingredient_list = []
    anti_category_list = []

    for index in range(len(anti_recipie_search["matches"])):
        anti_ingredient_list.append(anti_recipie_search["matches"][index]["ingredients"])
        anti_category_list.append(0)

    text_clf = Pipeline([('vect', CountVectorizer(stop_words='english')),
                     ('tfidf', TfidfTransformer()),
                     ('clf', MultinomialNB()),])

    restaurant_ingredients = desired_ingredient_list + anti_ingredient_list
    restaurant_ingredients_given = []
    for ingredientList in restaurant_ingredients:
        ingredientList = ' '.join(ingredientList)
        restaurant_ingredients_given.append(ingredientList)
    restaurant_categories = desired_category_list + anti_category_list

    if len(restaurant_ingredients_given) == 0:
        return 0

    text_clf = text_clf.fit(restaurant_ingredients_given, restaurant_categories)

    #print cross_validation(text_clf, restaurant_ingredients_given, restaurant_categories, len(restaurant_ingredients_given)/4)

    yummly_link_test = "http://api.yummly.com/v1/api/recipes?_app_id=" + str(yummly_app_id) + "&_app_key=" + str(yummply_api_key) + "&q=" + str(menu_item)
    recipies = urllib2.urlopen(yummly_link_test + "&maxResult=100")
    recipies = json.load(recipies)
    ingredient_list = []
    for index in range(len(recipies['matches'])):
        ingredient_list.append(''.join(recipies['matches'][index]['ingredients']))

    predicted_categories = text_clf.predict(ingredient_list)
    #print predicted_categories
    #print sum(predicted_categories)
    #print len(predicted_categories)
    if len(predicted_categories) == 0:
        return 0
    
    return float(sum(predicted_categories)) / float(len(predicted_categories))

                       

#print(get_percent_of_nutrition_matches("Ice+Cream", ["Low Sugar"]))
