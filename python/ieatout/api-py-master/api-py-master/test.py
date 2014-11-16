#! python
import datetime
import uuid
import functools
from pprint import pprint
import random
import os

import ordrin

#
# Helper Decorators
#
def print_docstring_header(f):
  @functools.wraps(f)
  def g(*args, **kwargs):
    print ''
    print f.__doc__
    raw_input('Press enter to execute and see the response')
    return f(*args, **kwargs)
  return g

def print_api_errors(f):
  @functools.wraps(f)
  def g(*args, **kwargs):
    try:
      return f(*args, **kwargs)
    except BaseException as e:
      print "The API returned the following error:"
      print e
  return g

#
# Global Variables
#
api_key = raw_input("Please input your API key: ")

if not api_key:
  api_key = "2HGAzwbK5IWNJPRN_c-kvbqtfGhS-k2a6p-1Zg2iNN4"

api = ordrin.APIs(api_key, ordrin.TEST) # Create an API object

addr = "900 Broadway"
city = "New York"
addr_zip = "10003"

address = {'addr' : addr,
           'city' : city,
           'state' : 'NY',
           'zip' : addr_zip,
           'phone' : '555-555-5555'}
address_nick = 'addr1'

first_name = 'Test'
last_name = 'User'
credit_card = {'card_name' : first_name+' '+last_name,
               'card_expiry' : '01/' + str(datetime.date.today().year+2),
               'card_number' : '4111111111111111',
               'card_cvc' : '123',
               'card_bill_addr' : address["addr"],
               'card_bill_city' : address["city"],
               'card_bill_state' : address["state"],
               'card_bill_zip' : address["zip"],
               'card_bill_phone' : address["phone"]}
credit_card_save = {'card_expiry' : '01/' + str(datetime.date.today().year+2),
                    'card_number' : '4111111111111111',
                    'card_cvc' : '123',
                    'bill_addr' : addr,
                    'bill_city' : city,
                    'bill_state' : address["state"],
                    'bill_zip' : addr_zip,
                    'bill_phone' : address["phone"]}
credit_card_nick = 'cc1'

unique_id = uuid.uuid1().hex
email = 'py+{}@ordr.in'.format(unique_id)
password = 'password'
login = {'email' : email,
         'current_password' : password}
alt_first_name = 'Example'
alt_email = 'py+{}alt@ordr.in'.format(unique_id)
alt_login = {'email' : alt_email,
             'current_password' : password}
new_password = 'password1'

#
# Restaurant demo functions
#
@print_docstring_header
def delivery_list_immediate_demo():
  """Get a list of restaurants that will deliver if you order now"""
  delivery_list_immediate = api.delivery_list('ASAP', addr, city, addr_zip)
  pprint(delivery_list_immediate, indent=4, depth=2)
  return delivery_list_immediate

@print_docstring_header
def delivery_list_future_demo():
  """Get a list of restaurants that will deliver if you order for 12 hours from now"""
  future_datetime = datetime.datetime.now() + datetime.timedelta(hours=12) #A timestamp twelve hours in the future
  delivery_list_later = api.delivery_list(future_datetime.strftime('%m-%d+%H:%M'), addr, city, addr_zip)
  pprint(delivery_list_later, indent=4, depth=2)

@print_docstring_header
def delivery_check_demo(restaurant_id):
  """Get whether a particular restaurant will deliver if you order now"""
  delivery_check = api.delivery_check('ASAP', restaurant_id, addr, city, addr_zip)
  pprint(delivery_check, indent=4, depth=2)

@print_docstring_header
def fee_demo(restaurant_id):
  """Get fee and other info for ordering a given amount with a given tip"""
  subtotal = "$30.00"
  tip = "$5.00"
  fee_info = api.fee('ASAP', restaurant_id, subtotal, tip, addr, city, addr_zip)
  pprint(fee_info, indent=4, depth=2)

@print_docstring_header
def detail_demo(restaurant_id):
  """Get detailed information about a single restaurant"""
  restaurant_detail = api.restaurant_details(restaurant_id)
  pprint(restaurant_detail, indent=4, depth=3)
  return restaurant_detail

def find_deliverable_time(restaurant_id):
  """Find a time when this restaurant will deliver"""
  delivery_check = api.delivery_check('ASAP', restaurant_id, addr, city, addr_zip)
  delivery = delivery_check['delivery']
  if delivery:
    return 'ASAP'
  dt = datetime.datetime.now() + datetime.timedelta(hours=1)
  while not delivery:
    delivery_check = api.delivery_check(dt.strftime('%m-%d+%H:%M'), restaurant_id, addr, city, addr_zip)
    delivery = delivery_check['delivery']
    dt += datetime.timedelta(hours=1)
  return dt.strftime('%m-%d+%H:%M')
    
#
# User demo functions
#
@print_docstring_header
def get_user_demo():
  """Get information about a user"""
  user_info = api.get_account_info(**login)
  pprint(user_info)

@print_docstring_header
def create_user_demo():
  """Create a user"""
  response = api.create_account(email, password, first_name, last_name)
  pprint(response)

@print_docstring_header
@print_api_errors
def update_user_demo():
  """Update a user"""
  response = api.user.update(email, password, alt_first_name, last_name)
  pprint(response)

@print_docstring_header
def get_all_addresses_demo():
  """Get a list of all saved addresses"""
  address_list = api.get_all_saved_addrs(**login)
  pprint(address_list)

@print_docstring_header
def get_address_demo():
  """Get an address by nickname"""
  addr = api.get_saved_addr(email, address_nick, password)
  pprint(addr)

@print_docstring_header
@print_api_errors
def set_address_demo():
  """Save an address with a nickname"""
  response = api.create_addr(email, address_nick, current_password=password, **address)
  pprint(response)

@print_docstring_header
@print_api_errors
def remove_address_demo():
  """Remove a saved address by nickname"""
  response = api.delete_addr(email, address_nick, password)
  pprint(response)

@print_docstring_header
def get_all_credit_cards_demo():
  """Get a list of all saved credit cards"""
  credit_card_list = api.user.get_all_saved_ccs(**login)
  pprint(credit_card_list)

@print_docstring_header
def get_credit_card_demo():
  """Get a saved credit card by nickname"""
  credit_card = api.get_saved_cc(email, credit_card_nick, password)
  pprint(credit_card)

@print_docstring_header
@print_api_errors
def set_credit_card_demo():
  """Save a credit card with a nickname"""
  response = api.create_cc(email, credit_card_nick, current_password=password, **credit_card_save)
  pprint(response)

@print_docstring_header
@print_api_errors
def remove_credit_card_demo():
  """Remove a saved credit card by nickname"""
  response = api.delete_cc(email, credit_card_nick, current_password)
  pprint(response)

@print_docstring_header
def get_order_history_demo(login):
  """Get a list of all orders made by this user"""
  order_list = api.get_order_history(**login)
  pprint(order_list)

@print_docstring_header
def get_order_detail_demo(oid):
  """Get the details of a particular order made by this user"""
  order_detail = api.get_order(email, oid, current_password)
  pprint(order_detail)

@print_docstring_header
@print_api_errors
def set_password_demo():
  """Set a new password for a user"""
  response = api.change_password(email, new_password, password)
  pprint(response)
  
#
# Order demo functions
#
@print_docstring_header
@print_api_errors
def anonymous_order_demo(restaurant_id, tray, date_time):
  """Order food as someone without a user account"""
  tip = "%.2f" % (random.randint(0, 500)/100.0)
  if date_time == 'ASAP':
    response = api.order_guest(restaurant_id, email, tray, tip, first_name, last_name, delivery_date='ASAP', **dict(address, **credit_card))
  else:
    del_date, del_time = date_time.split('+')
    response = api.order_guest(restaurant_id, email, tray, tip, first_name, last_name, delivery_date=del_date, delivery_time=del_time, **dict(address, **credit_card))
  pprint(response)

@print_docstring_header
@print_api_errors
def order_with_nicks_demo(restaurant_id, tray, date_time):
  """Order food as a logged in user using previously stored address and credit card"""
  tip = "%.2f" % (random.randint(0, 500)/100.0)
  if date_time == 'ASAP':
    response = api.order_user(restaurant_id, tray, tip, first_name, last_name, email, password, nick=address_nick, card_nick=credit_card_nick, delivery_date='ASAP')
  else:
    del_date, del_time = date_time.split('+')
    response = api.order_user(restaurant_id, tray, tip, first_name, last_name, email, password, nick=address_nick, card_nick=credit_card_nick, delivery_date=del_date, delivery_time=del_time)
  pprint(response)
  return response

def find_item_to_order(item_list):
  for item in item_list:
    if item['is_orderable']:
      if float(item['price'])>=5.00:
        return item['id']
    else:
      if 'children' in item:
        item_id = find_item_to_order(item['children'])
        if item_id is not None:
          return item_id
  return None
    

#
# Main
#
def run_demo():
  """Run through the entire demo sequence"""
  # Restaurant functions
  delivery_list = delivery_list_immediate_demo()
  delivery_list_future_demo()
  restaurant_id = str(delivery_list[0]['id'])
  delivery_check_demo(restaurant_id)
  fee_demo(restaurant_id)
  detail = detail_demo(restaurant_id)

  # User functions
  create_user_demo()
  get_user_demo()
  #update_user_demo()
  #get_user_demo()
  set_address_demo()
  get_address_demo()
  set_credit_card_demo()
  get_credit_card_demo()

  # Order functions
  order_date_time = find_deliverable_time(restaurant_id)
  print "Ordering food at {}".format(order_date_time)
  item_id = find_item_to_order(detail['menu'])
  tray = '{}/{}'.format(item_id, 10)
  anonymous_order_demo(restaurant_id, tray, order_date_time)
  order = order_with_nicks_demo(restaurant_id, tray, order_date_time)
  if order:
    get_order_detail_demo(order['refnum'])
  get_order_history_demo(login)

  # Clean up/removing stuff
  remove_address_demo()
  get_all_addresses_demo()
  remove_credit_card_demo()
  get_all_credit_cards_demo()
  set_password_demo()

if __name__=='__main__':
  run_demo()
  
