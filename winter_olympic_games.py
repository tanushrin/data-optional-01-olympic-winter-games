# pylint: disable=missing-docstring

import csv

COUNTRIES_FILEPATH = "data/dictionary.csv"
MEDALS_FILEPATH = "data/winter.csv"


def most_decorated_athlete_ever():
    """Returns who won the most winter olympic games medals
    (gold/silver/bronze) ever"""
    with open(MEDALS_FILEPATH, encoding='utf-8') as file1:
        records = csv.DictReader(file1)

        #'''Create a dict with {athlete_name: count_medals}'''
        athlete_best = {}
        for athlete in [record['Athlete'] for record in records]:
            if athlete in athlete_best:
                athlete_best[athlete] += 1
            else:
                athlete_best[athlete] = 1

        #Sort the dic values in descending
        athlete_best = dict(sorted(athlete_best.items(), key=lambda x:x[1], \
            reverse=True))
        #'''Fetch the 1st key'''
        for key in athlete_best.keys():
            return key


def country_with_most_gold_medals(min_year, max_year):
    """Returns which country won the most gold medals between `min_year` \
        and `max_year`"""
    with open(MEDALS_FILEPATH, encoding='utf-8') as file1:
        records = csv.DictReader(file1)

        country_best = {}
        for a_country in [record['Country'] for record in records \
            if (record['Medal']=="Gold" and \
                min_year<=int(record['Year'])<=max_year)]:
            if a_country in country_best:
                country_best[a_country] += 1
            else:
                country_best[a_country] = 1

        #'''Sort the dic values in descending'''
        country_best = dict(sorted(country_best.items(), key=lambda x:x[1], \
            reverse=True))
        #'''Fetch the 1st key'''
        for key in country_best.keys():
            with open(COUNTRIES_FILEPATH, encoding='utf-8') as file2:
                records2 = csv.DictReader(file2)
                country_lookup = "".join(record2['Country'] for record2 in \
                    records2 if record2['Code']==key)
                return country_lookup
            #break

def top_three_women_in_five_thousand_meters():
    """Returns the three women with the most 5000 meters
    medals(gold/silver/bronze)"""
    with open(MEDALS_FILEPATH, encoding='utf-8') as file1:
        records = csv.DictReader(file1)

        athlete_best = {}
        for athlete in [record['Athlete'] for record in records \
            if (record['Gender']=='Women' and record['Event']=='5000M' )]:
            if athlete in athlete_best:
                athlete_best[athlete] += 1
            else:
                athlete_best[athlete] = 1

        #'''Sort the dic values in descending'''
        athlete_best = dict(sorted(athlete_best.items(), key=lambda x:x[1], \
            reverse=True))
        #'''Fetch the 1st 3 keys'''
        return list(athlete_best)[0:3]
