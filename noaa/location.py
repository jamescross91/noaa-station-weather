import api_request


def get_list_of_cities(token, min_date):
    return api_request.paginated_get_request(
        url="https://www.ncdc.noaa.gov/cdo-web/api/v2/locations",
        headers={"token": token},
        params={
            "startdate": min_date,
            "locationcategoryid": "CITY"
        }
    )


def get_city_information(token, min_date, city):
    return filter(lambda x: "New York" in x["name"], get_list_of_cities(token, min_date))
