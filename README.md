#NOAA Station Weather

A small set of utility functions for fetching weather station data from weather stations in a given city.  Leverages the [NOAA Climate Data Online API](https://www.ncdc.noaa.gov/cdo-web/webservices/v2#gettingStarted)

###Usage

Firstly you need to register for an API token from the [token request page](https://www.ncdc.noaa.gov/cdo-web/token).

The following sample will fetch all data for New York City between the 1st January 2012 and the 31st of January 2012.

```
import logging

from noaa import location, station
from noaa.data import get_daily_summary_for_station

logging.basicConfig(level=logging.DEBUG)

token = "YOUR TOKEN HERE"
min_date = "2012-01-01"
max_date = "2012-01-31"
city_list = location.get_city_information(token, min_date, "New York")

if len(city_list) != 1:
    raise "Found too an unexpected number of cities"

city_id = city_list[0]['id']
station_list = station.get_list_of_stations(token, min_date, city_id, "GHCND")

data = []
for station in station_list:
    res = get_daily_summary_for_station(token, min_date, max_date, station["id"], time_gap=30)
    data.extend(res)
```

