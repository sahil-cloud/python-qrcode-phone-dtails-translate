import phonenumbers
from phonenumbers import geocoder , carrier , timezone

def details():
    ph_no = input("Enter the number")
    ch_no = phonenumbers.parse(ph_no,"CH")
    geo = geocoder.description_for_number(ch_no, "en")
    car = carrier.name_for_number(ch_no, "en")
    time = timezone.time_zones_for_number(ch_no)
    print(f'country : {geo}')
    print(f'carrier : {car}')
    print(f'timezone : {time}')

details()
