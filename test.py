from noaa import location, station

token = "TLkwHkXdkuRXbHgauLQtPvurhhhipjjU"
min_date = "2012-01-01"
city_list = location.get_city_information(token, min_date, "New York")

if len(city_list) != 1:
    raise "Found too an unexpected number of cities"

city_id = city_list[0]['id']
station_list = station.get_list_of_stations(token, min_date, city_id)

print