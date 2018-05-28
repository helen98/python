"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""

#locations = {'North America': {'USA': ['Mountain View']}}
usa_list = ['Mountain View']
north_america_dict = {'USA': usa_list}
locations = {'North America': north_america_dict}
india_list = ['Bangalore']
asia_dict = {'India': india_list}
locations['Asia'] = asia_dict
usa_list.append('Atlanta')
egypt_list = ['Cairo']
africa_dict = {'Egypt': egypt_list}
locations['Africa'] = africa_dict
china_list = ['Shanghai']
asia_dict['China'] = china_list
usa_list.sort()
print 1
for x in usa_list:
    print x
    pass
print 2

asia_city_list = india_list + china_list
asia_city_list.sort()
for x in asia_city_list:
    for country, cities in asia_dict.iteritems():
        if x in cities:
            print x + ' - ' + country


"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""
