import unirest
import logging


def paginated_get_request(
        url=None,
        headers=None,
        params=None,
        max_result_size=5000,
        default_fetch_size=1000,
):
    accumulated_results = []
    params["limit"] = default_fetch_size
    response = _call_unirest_get(headers, params, url)

    if "results" in response.body:
        accumulated_results.extend(response.body["results"])
    else:
        return []

    meta = response.body['metadata']["resultset"]
    count = meta["count"]
    offset = meta["offset"]

    while offset + default_fetch_size < count and len(accumulated_results) <= max_result_size:
        params["offset"] = offset + default_fetch_size
        response = _call_unirest_get(headers, params, url)
        accumulated_results.extend(response.body["results"])

        meta = response.body['metadata']["resultset"]
        offset = meta["offset"]

    return accumulated_results


def _call_unirest_get(headers, params, url):
    logging.info("Requesting data from " + url + " with params " + str(params))
    response = unirest.get(url, headers=headers, params=params)
    return response
