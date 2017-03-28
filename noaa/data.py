from datetime import datetime
from datetime import timedelta

import api_request


def get_daily_summary_for_station(
        token,
        start_date_string,
        end_date_string,
        station_id,
        time_gap=30
):
    start_date = datetime.strptime(start_date_string, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_string, '%Y-%m-%d')
    request_date_start = start_date
    request_date_end = request_date_start + timedelta(days=time_gap)

    data = []

    while request_date_end < end_date:
        result = api_request.paginated_get_request(
            url="https://www.ncdc.noaa.gov/cdo-web/api/v2/data",
            headers={"token": token},
            params={
                "datasetid": "GHCND",
                "startdate": request_date_start.strftime('%Y-%m-%d'),
                "enddate": request_date_end.strftime('%Y-%m-%d'),
                "stationid": station_id,
            }
        )

        data.extend(result)
        request_date_start = request_date_end + timedelta(days=1)
        request_date_end = request_date_end + timedelta(days=time_gap)

    return data


