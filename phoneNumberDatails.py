# import python librarie's
import phonenumbers
from phonenumbers import timezone,geocoder,carrier
# take user number eg(+255 786404720)
number = input("enter your phone number start with +..: ")
# about number
phone = phonenumbers.parse(number)
#continent
time = timezone.time_zones_for_number(phone)
#company name
car = carrier.name_for_number(phone,'en')# en stand for language ==english==..choose your own
#country 
reg = geocoder.description_for_number(phone,'en')
print("="*54)
# let's get it
print('number: ',phone)
print('continent: ',time)
print('company: ', car)
print('counter: ',reg)
