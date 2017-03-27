import api_request


def get_list_of_stations(token, min_date, location_id):
    return api_request.paginated_get_request(
        url="https://www.ncdc.noaa.gov/cdo-web/api/v2/stations",
        headers={"token": token},
        params={
            "startdate": min_date,
            "locationid": location_id
        }
    )
