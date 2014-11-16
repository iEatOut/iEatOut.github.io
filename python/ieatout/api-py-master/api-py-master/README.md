# Ordr.in Python Library

A python library for the ordr.in API.
See full API documentation at http://hackfood.ordr.in

## Table of Contents

 - [Installation](#installation)
 - [Usage](#usage)
   - [Initialization](#initialization)
   
   - [Order Endpoints](#order-endpoints-api-reference)
     - [Guest Order](#guest-order-api-reference) (`order_guest`)
     - [User Order](#user-order-api-reference) (`order_user`)
     
   - [Restaurant Endpoints](#restaurant-endpoints-api-reference)
     - [Delivery Check](#delivery-check-api-reference) (`delivery_check`)
     - [Delivery List](#delivery-list-api-reference) (`delivery_list`)
     - [Fee](#fee-api-reference) (`fee`)
     - [Restaurant Details](#restaurant-details-api-reference) (`restaurant_details`)
     
   - [User Endpoints](#user-endpoints-api-reference)
     - [Change Password](#change-password-api-reference) (`change_password`)
     - [Create Account](#create-account-api-reference) (`create_account`)
     - [Create Address](#create-address-api-reference) (`create_addr`)
     - [Create Credit Card](#create-credit-card-api-reference) (`create_cc`)
     - [Remove address](#remove-address-api-reference) (`delete_addr`)
     - [Remove Credit Card](#remove-credit-card-api-reference) (`delete_cc`)
     - [Get Account Information](#get-account-information-api-reference) (`get_account_info`)
     - [Get All Saved Addresses](#get-all-saved-addresses-api-reference) (`get_all_saved_addrs`)
     - [Get all saved credit cards](#get-all-saved-credit-cards-api-reference) (`get_all_saved_ccs`)
     - [Get an Order](#get-an-order-api-reference) (`get_order`)
     - [Get Order History](#get-order-history-api-reference) (`get_order_history`)
     - [Get a single saved address](#get-a-single-saved-address-api-reference) (`get_saved_addr`)
     - [Get a single saved credit card](#get-a-single-saved-credit-card-api-reference) (`get_saved_cc`)
     

## Installation

This library can be installed with pip:

    pip install ordrin

## Usage

### Initialization

```python
import ordrin
ordrin_api = ordrin.APIs(api_key, servers)
```

In the initializer, the second argument sets the servers that API requests will
be sent to, and must be set to either `ordrin.PRODUCTION` or `ordrin.TEST`
(defaults to `ordrin.TEST`).


### Order Endpoints ([API Reference](http://hackfood.ordr.in/docs/order))

#### Guest Order ([API Reference](http://hackfood.ordr.in/docs/order#order_guest))

    ordrin.order_guest(rid, em, tray, tip, first_name, last_name, phone, zip, addr, city, state, card_number, card_cvc, card_expiry, card_bill_addr, card_bill_city, card_bill_state, card_bill_zip, card_bill_phone, addr2=None, card_name=None, card_bill_addr2=None, delivery_date=None, delivery_time=None)

##### Arguments
- `rid` : Ordr.in's unique restaurant identifier for the restaurant. (A number)
- `em` : The customer's email address
- `tray` : Represents a tray of menu items in the format '[menu item id]/[qty],[option id],...,[option id]'
- `tip` : Tip amount in dollars and cents
- `first_name` : The customer's first name
- `last_name` : The customer's last name
- `phone` : The customer's phone number
- `zip` : The zip code part of the address (5 digits)
- `addr` : The street address
- `addr2` : The second part of the street address, if needed
- `city` : The city part of the address
- `state` : The state part of the address (Two letters)
- `card_name` : Full name as it appears on the credit card
- `card_number` : Credit card number (16 digits)
- `card_cvc` : 3 or 4 digit security code (3 or 4 digits)
- `card_expiry` : The credit card expiration date. (mm/yyyy)
- `card_bill_addr` : The credit card's billing street address
- `card_bill_addr2` : The second part of the credit card's biling street address.
- `card_bill_city` : The credit card's billing city
- `card_bill_state` : The credit card's billing state (2 letters)
- `card_bill_zip` : The credit card's billing zip code (5 digits)
- `card_bill_phone` : The credit card's billing phone number


###### Either
- `delivery_date` : Delivery date (mm-dd)
- `delivery_time` : Delivery time (HH:MM)

###### Or
- `delivery_date` : Delivery date (ASAP)



#### User Order ([API Reference](http://hackfood.ordr.in/docs/order#order_user))

    ordrin.order_user(rid, tray, tip, first_name, last_name, email, current_password, phone=None, zip=None, addr=None, addr2=None, city=None, state=None, nick=None, card_name=None, card_number=None, card_cvc=None, card_expiry=None, card_bill_addr=None, card_bill_addr2=None, card_bill_city=None, card_bill_state=None, card_bill_zip=None, card_bill_phone=None, card_nick=None, delivery_date=None, delivery_time=None)

##### Arguments
- `rid` : Ordr.in's unique restaurant identifier for the restaurant. (A number)
- `tray` : Represents a tray of menu items in the format '[menu item id]/[qty],[option id],...,[option id]'
- `tip` : Tip amount in dollars and cents
- `first_name` : The customer's first name
- `last_name` : The customer's last name
- `email` : The user's email address
- `current_password` : The user's current password

###### Either
- `addr` : The street address
- `addr2` : The second part of the street address, if needed
- `city` : The city part of the address
- `phone` : The customer's phone number
- `state` : The state part of the address (Two letters)
- `zip` : The zip code part of the address (5 digits)

###### Or
- `nick` : The delivery location nickname. (From the user's addresses)



###### Either
- `card_bill_addr` : The credit card's billing street address
- `card_bill_addr2` : The second part of the credit card's biling street address.
- `card_bill_city` : The credit card's billing city
- `card_bill_phone` : The credit card's billing phone number
- `card_bill_state` : The credit card's billing state (2 letters)
- `card_bill_zip` : The credit card's billing zip code (5 digits)
- `card_cvc` : 3 or 4 digit security code (3 or 4 digits)
- `card_expiry` : The credit card expiration date. (mm/yyyy)
- `card_name` : Full name as it appears on the credit card
- `card_number` : Credit card number (16 digits)

###### Or
- `card_nick` : The credit card nickname. (From the user's credit cards)



###### Either
- `delivery_date` : Delivery date (mm-dd)
- `delivery_time` : Delivery time (HH:MM)

###### Or
- `delivery_date` : Delivery date (ASAP)




### Restaurant Endpoints ([API Reference](http://hackfood.ordr.in/docs/restaurant))

#### Delivery Check ([API Reference](http://hackfood.ordr.in/docs/restaurant#delivery_check))

    ordrin.delivery_check(datetime, rid, addr, city, zip)

##### Arguments
- `datetime` : Delivery date and time (ASAP or mm-dd+HH:MM)
- `rid` : Ordr.in's unique restaurant identifier for the restaurant. (A number)
- `addr` : Delivery location street address
- `city` : Delivery location city
- `zip` : The zip code part of the address (5 digits)


#### Delivery List ([API Reference](http://hackfood.ordr.in/docs/restaurant#delivery_list))

    ordrin.delivery_list(datetime, addr, city, zip)

##### Arguments
- `datetime` : Delivery date and time (ASAP or mm-dd+HH:MM)
- `addr` : Delivery location street address
- `city` : Delivery location city
- `zip` : The zip code part of the address (5 digits)


#### Fee ([API Reference](http://hackfood.ordr.in/docs/restaurant#fee))

    ordrin.fee(datetime, rid, subtotal, tip, addr, city, zip)

##### Arguments
- `datetime` : Delivery date and time (ASAP or mm-dd+HH:MM)
- `rid` : Ordr.in's unique restaurant identifier for the restaurant. (A number)
- `subtotal` : The cost of all items in the tray in dollars and cents.
- `tip` : The tip in dollars and cents.
- `addr` : Delivery location street address
- `city` : Delivery location city
- `zip` : The zip code part of the address (5 digits)


#### Restaurant Details ([API Reference](http://hackfood.ordr.in/docs/restaurant#restaurant_details))

    ordrin.restaurant_details(rid)

##### Arguments
- `rid` : Ordr.in's unique restaurant identifier for the restaurant. (A number)



### User Endpoints ([API Reference](http://hackfood.ordr.in/docs/user))

#### Change Password ([API Reference](http://hackfood.ordr.in/docs/user#change_password))

    ordrin.change_password(email, password, current_password)

##### Arguments
- `email` : The user's email address
- `password` : The user's new password (SHA256 hex encoded)
- `current_password` : The user's current password

#### Create Account ([API Reference](http://hackfood.ordr.in/docs/user#create_account))

    ordrin.create_account(email, pw, first_name, last_name)

##### Arguments
- `email` : The user's email address
- `pw` : The user's password
- `first_name` : The user's first name
- `last_name` : The user's last name


#### Create Address ([API Reference](http://hackfood.ordr.in/docs/user#create_addr))

    ordrin.create_addr(email, nick, phone, zip, addr, city, state, current_password, addr2=None)

##### Arguments
- `email` : The user's email address
- `nick` : The nickname of this address
- `phone` : The customer's phone number
- `zip` : The zip code part of the address (5 digits)
- `addr` : The street address
- `addr2` : The second part of the street address, if needed
- `city` : The city part of the address
- `state` : The state part of the address (Two letters)
- `current_password` : The user's current password

#### Create Credit Card ([API Reference](http://hackfood.ordr.in/docs/user#create_cc))

    ordrin.create_cc(email, nick, card_number, card_cvc, card_expiry, bill_addr, bill_city, bill_state, bill_zip, bill_phone, current_password, bill_addr2=None)

##### Arguments
- `email` : The user's email address
- `nick` : The nickname of this address
- `card_number` : Credit card number (16 digits)
- `card_cvc` : 3 or 4 digit security code (3 or 4 digits)
- `card_expiry` : The credit card expiration date. (Two digits/Four digits)
- `bill_addr` : The credit card's billing street address
- `bill_addr2` : The second part of the credit card's biling street address.
- `bill_city` : The credit card's billing city
- `bill_state` : The credit card's billing state (2 letters)
- `bill_zip` : The credit card's billing zip code (5 digits)
- `bill_phone` : The credit card's billing phone number
- `current_password` : The user's current password

#### Remove address ([API Reference](http://hackfood.ordr.in/docs/user#delete_addr))

    ordrin.delete_addr(email, nick, current_password)

##### Arguments
- `email` : The user's email address
- `nick` : The nickname of this address
- `current_password` : The user's current password

#### Remove Credit Card ([API Reference](http://hackfood.ordr.in/docs/user#delete_cc))

    ordrin.delete_cc(email, nick, current_password)

##### Arguments
- `email` : The user's email address
- `nick` : The nickname of this address
- `current_password` : The user's current password

#### Get Account Information ([API Reference](http://hackfood.ordr.in/docs/user#get_account_info))

    ordrin.get_account_info(email, current_password)

##### Arguments
- `email` : The user's email address
- `current_password` : The user's current password

#### Get All Saved Addresses ([API Reference](http://hackfood.ordr.in/docs/user#get_all_saved_addrs))

    ordrin.get_all_saved_addrs(email, current_password)

##### Arguments
- `email` : The user's email address
- `current_password` : The user's current password

#### Get all saved credit cards ([API Reference](http://hackfood.ordr.in/docs/user#get_all_saved_ccs))

    ordrin.get_all_saved_ccs(email, current_password)

##### Arguments
- `email` : The user's email address
- `current_password` : The user's current password

#### Get an Order ([API Reference](http://hackfood.ordr.in/docs/user#get_order))

    ordrin.get_order(email, oid, current_password)

##### Arguments
- `email` : The user's email address
- `oid` : Ordr.in's unique order id number. (A number)
- `current_password` : The user's current password

#### Get Order History ([API Reference](http://hackfood.ordr.in/docs/user#get_order_history))

    ordrin.get_order_history(email, current_password)

##### Arguments
- `email` : The user's email address
- `current_password` : The user's current password

#### Get a single saved address ([API Reference](http://hackfood.ordr.in/docs/user#get_saved_addr))

    ordrin.get_saved_addr(email, nick, current_password)

##### Arguments
- `email` : The user's email address
- `nick` : The nickname of this address
- `current_password` : The user's current password

#### Get a single saved credit card ([API Reference](http://hackfood.ordr.in/docs/user#get_saved_cc))

    ordrin.get_saved_cc(email, nick, current_password)

##### Arguments
- `email` : The user's email address
- `nick` : The nickname of this address
- `current_password` : The user's current password


