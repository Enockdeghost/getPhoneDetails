
import phonenumbers
from phonenumbers import timezone, geocoder, carrier
from phonenumbers.phonenumberutil import number_type, region_code_for_number

# Input phone number
number = input("Enter your phone number (start with +..): ")

try:
    # Parse phone number
    phone = phonenumbers.parse(number)
    
    # Basic validity checks
    is_valid = phonenumbers.is_valid_number(phone)
    is_possible = phonenumbers.is_possible_number(phone)
    
    # Get details
    time = timezone.time_zones_for_number(phone)
    car = carrier.name_for_number(phone, 'en')
    reg = geocoder.description_for_number(phone, 'en')
    region = region_code_for_number(phone)
    
    # Determine number type
    num_type = number_type(phone)
    num_type_str = {
        0: "Fixed Line",
        1: "Mobile",
        2: "Fixed Line or Mobile",
        3: "Toll Free",
        4: "Premium Rate",
        5: "Shared Cost",
        6: "VoIP",
        7: "Personal Number",
        8: "Pager",
        9: "Universal Access Number",
        10: "Voicemail",
        27: "Unknown",
    }.get(num_type, "Unknown")
    
    # Output
    print("=" * 60)
    print(f"Entered Number : {phone}")
    print(f"Country        : {reg} ({region})")
    print(f"Continent      : {time}")
    print(f"Carrier        : {car}")
    print(f"Type           : {num_type_str}")
    print(f"Is Valid?      : {'Yes' if is_valid else 'No'}")
    print(f"Is Possible?   : {'Yes' if is_possible else 'No'}")
    print("=" * 60)

except Exception as e:
    print("Error: Invalid phone number format or unsupported number.")
    print("Details:", str(e))
