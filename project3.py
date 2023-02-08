""""Story is simple. Latvian cadastral Land Surveyor is all the time stuck in
government bureaucracy. All the time new laws, new rules.
There is one institution, who check Surveyors work, before plan registration in system.
And there is so much to do before work is done. How about make 1 of 1000 works
faster and better. This program helps calculate if parcel area changes is in allowed values.
There is two types of lands, and one of them is not measure with precise technology. This mean,
after 20 year of last land surveying, we need to make precise measure process. Area is already
in system and it can change, but...there is rulles, how much it can change. And there we go!
We need to check, if we need make more paperwork (it is outsaide allowed) or we can do our job."""

import math


def main():
    '#mernieks norada klasi 1 vai 2/ Surveyor give the class 1 (city) or 2 (villages, country side)'
    '#mernieks norada platibu/ Surveyor give parcels area'
    '#ciemi sadalās trīs vērtību zonās, katrai zonai mainās koeficents/ villages splits in 3 zones, each zone has own coeficent'
    '#pilsētas sadalās septiņās zonās, katrai zonai mainās procenti/ city splits in 7 zones, each zone have own precent value'
    '#zonas atkarīgas no zemes vienības platības./in witch zone is parcel depends on parcels area'
    '#veic aprēķinu/ done calculation'
    '#rezultats = mernieks uzzina pieļaujamo min un pieļaujamo max platību/ result = surveyor get know parcels allowed max and min area'


    print('Hello, Land Surveyor!')
    print('Number 1 calculate area in cities, but Number 2 in villages and country side.')
    choise = (print(input('Input area class: ')))
    area = area_for_calculation()
    if choise == 1:
        calculate_city_area(area)
        print('Your parcels area is ' + (str(area)) + ' ha')
        print('Minimal allowed area is ' + str(round((min_area_s(area)), 4)) + ' ha')
        print('Maximal allowed area is ' + str(round((max_area_s(area)), 4)) + ' ha')
    else:
        calculate_area_country_side(area)
        print('Your parcels area is ' + (str(area)) + ' ha')
        print('Minimal allowed area is ' + str(round((min_area_c(area)), 4)) + ' ha')
        print('Maximal allowed area is ' + str(round((max_area_c(area)), 4)) + ' ha')
    print('Good Luck!')

def area_for_calculation():
    area = (float(input('Your parcels area in VZD system/plan(ha): ')))
    return area

def calculate_area_country_side(area):
    r = kof(area) * squerroot(area)
    return r

def max_area_c(area):
    max_count = area + calculate_area_country_side(area)
    return max_count

def min_area_c(area):
    min_count = area - calculate_area_country_side(area)
    return min_count

def calculate_city_area(area):
    p = area * precent(area)
    return p

def min_area_s(area):
    min_city = area - calculate_city_area(area)
    return min_city

def max_area_s(area):
    max_city = area + calculate_city_area(area)
    return max_city

def squerroot(area):
    return math.sqrt(area)

def kof(area):
    b = ((1.0, 0.1), (200, 0.25), (None, 0.3))
    for subb in b:
        if subb[0] is None or area < subb[0]:
         return subb[1]


def precent(area):
    s = ((0.5, 0.030), (1.00, 0.023), (5.00, 0.018), (10.00, 0.015), (50.00, 0.0125), (100.00, 0.0105), (None, 0.01))
    for subs in s:
        if subs[0] is None or area < subs[0]:
         return subs[1]


if __name__ == '__main__':
    main()