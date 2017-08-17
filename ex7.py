states = {
	'Organe':'OR',
	'Filorida':'FL',
	'California':'CA',
	'New York':'NY',
	'Michigan':'MT'
}

cities = {
	'CA':'San Francisco',
	'MI':'Detroit',
	'FL':'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-' * 10
print "NY State has", cities['NY']
print "OR State has", cities['OR']

print '-' * 10
print "Michigan's abbreviation is:", states['Michigan']

print '-' * 10
for stae, abbrev in states.items():
	print "%s is abbreviation %s" %(stae, abbrev)


print '*' * 10
for state, abbrev in states.items():
	print "state = %s, abbrev = %s, city = %s" %(state, abbrev, cities[abbrev])

























