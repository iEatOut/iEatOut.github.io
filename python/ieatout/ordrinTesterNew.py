import ordrin
import urllib2
import json
import allergySearcher
from allergySearcher import calculate_match
from nutritionMatcher import get_percent_of_nutrition_matches

yummly_app_id = '69189240'
yummply_api_key = '9e160e5cce7ff68eab06dc8b9b99de71'



def get_nearby_restaurants(street_address, city, zip_code):
    ordrin_api = ordrin.APIs("SvMY8WkSk78OHhgYSs55FVkUev7FOrdtEXF_1bExeUc", ordrin.TEST)
    data = ordrin_api.delivery_list("ASAP", street_address, city, zip_code)
    return data[0:5]

def get_name(restaurant_id):
    ordrin_api = ordrin.APIs("SvMY8WkSk78OHhgYSs55FVkUev7FOrdtEXF_1bExeUc", ordrin.TEST)
    restaurant_details = ordrin_api.restaurant_details(str(restaurant_id))
    return restaurant_details["name"]

def get_average_menu_item_price(restaurant_id):
    ordrin_api = ordrin.APIs("SvMY8WkSk78OHhgYSs55FVkUev7FOrdtEXF_1bExeUc", ordrin.TEST)
    restaurant_details = ordrin_api.restaurant_details(str(restaurant_id))
    price = float(0)
    for index in range(len(restaurant_details["menu"])):
        for index2 in range(len(restaurant_details["menu"][index]["children"])):
            price += float(restaurant_details["menu"][index]["children"][index2]["price"])

    return float(price) / float(len(restaurant_details["menu"]))
    

def get_menu_items(restaurant_id):
    ordrin_api = ordrin.APIs("SvMY8WkSk78OHhgYSs55FVkUev7FOrdtEXF_1bExeUc", ordrin.TEST)
    restaurant_details = ordrin_api.restaurant_details(str(restaurant_id))

    menu_items = []
    
    #for index in range(len(restaurant_details['menu'])):
    for index in range(5):
        #for index2 in range(len(restaurant_details["menu"][index]["children"])):
        for index2 in range(1):
            menu_items.append(restaurant_details['menu'][index]['children'][index2]['name'])

    return menu_items

#returns the percent of suitable recipies according to allergy information
def get_percent_of_suitable_recipies(menu_item, allergy_array):
    #Searches all the recipies for a given menu item
    menu_item = menu_item.replace(" ","+")
    print "http://api.yummly.com/v1/api/recipes?_app_id=" + str(yummly_app_id) + "&_app_key=" + str(yummply_api_key) + "&q=" + str(menu_item)
    recipie_search = urllib2.urlopen("http://api.yummly.com/v1/api/recipes?_app_id=" + str(yummly_app_id) + "&_app_key=" + str(yummply_api_key) + "&q=" + str(menu_item) + "&maxResult=100")
    recipie_search = json.load(recipie_search)

    matching_indicator_array = []

    num_possible_recipes = len(recipie_search['matches'])
    for index in range(num_possible_recipes):
        matching_indicator_array.append(calculate_match(recipie_search['matches'][index]['ingredients'], allergy_array))

    if len(matching_indicator_array) == 0:
        return 0
    return float(sum(matching_indicator_array)) / float(len(matching_indicator_array))



def get_restaurant_suitability(restaurant_id, allergy_array, nutrition_array):
    menu_items = get_menu_items(restaurant_id)
    menu_item_match_allergy_percentages = []
    menu_item_match_nutrition_percentages =[]

    for menu_item in menu_items:
        menu_item_match_allergy_percentages.append(get_percent_of_suitable_recipies(menu_item, allergy_array))
        menu_item_match_nutrition_percentages.append(get_percent_of_nutrition_matches(menu_item, nutrition_array))

    returned_array = []
    returned_array.append(get_name(restaurant_id))
    returned_array.append(get_average_menu_item_price(restaurant_id))
    returned_array.append(float(sum(menu_item_match_allergy_percentages)) / float(len(menu_item_match_allergy_percentages)))
    returned_array.append(float(sum(menu_item_match_nutrition_percentages)) / float(len(menu_item_match_nutrition_percentages)))

    return returned_array
                                                                  
    #return [float(sum(menu_item_match_allergy_percentages)) / float(len(menu_item_match_allergy_percentages))
    #        , float(sum(menu_item_match_nutrition_percentages)) / float(len(menu_item_match_nutrition_percentages))]
        
    
def get_restaurants(street_address, city, zip_code, allergy_array, nutrition_array):
    nearby_restaurant_list = get_nearby_restaurants(street_address, city, zip_code)
    #print(len(nearby_restaurant_list))

    restaurant_match_list = [0 for index1 in range(5)]
    print(len(restaurant_match_list))
    for i in range(len(nearby_restaurant_list)):
        restaurant_id = nearby_restaurant_list[i]['id']
        restaurant_match_list[i] = get_restaurant_suitability(restaurant_id, allergy_array, nutrition_array)

    print restaurant_match_list
    return restaurant_match_list
       

#print get_restaurants("715 Techwood Drive", "Atlanta", "30332", ["Gluten-Free"], ["Low Sodium"])



