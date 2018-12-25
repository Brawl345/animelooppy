#!/usr/bin/python3
from json import dumps
from urllib.parse import urlencode, unquote, urlparse, parse_qsl, ParseResult

import requests

from animelooppy import episode
from animelooppy import loop
from animelooppy import series
from animelooppy import tag

BASE_URL = "https://animeloop.org/api/v2/"


class ErrorMessages:
    UnknownError = "Error {0}"
    NoConnection = "Cannot fetch JSON data"
    NoResults = "No results found"


# General
def _api_request(search_url):
    r = requests.get(search_url)

    try:
        json = r.json()
    except:
        raise ConnectionError(ErrorMessages.NoConnection)

    if json["status"] != "success" or json["code"] != 200:
        if "message" in json:
            raise LookupError(str(json["message"]))
        raise LookupError(ErrorMessages.UnknownError.format(json["code"]))

    if len(json["data"]) == 0:
        raise LookupError(ErrorMessages.NoResults)

    return json


# Taken from https://stackoverflow.com/a/25580545/3146627
def _add_url_params(url, params):
    """ Add GET params to provided URL being aware of existing.

    :param url: string of target URL
    :param params: dict containing requested params to be added
    :return: string with updated URL

    >> url = 'http://stackoverflow.com/test?answers=true'
    >> new_params = {'answers': False, 'data': ['some','values']}
    >> add_url_params(url, new_params)
    'http://stackoverflow.com/test?data=some&data=values&answers=false'
    """
    # Unquoting URL first so we don't loose existing args
    url = unquote(url)
    # Extracting url info
    parsed_url = urlparse(url)
    # Extracting URL arguments from parsed URL
    get_args = parsed_url.query
    # Converting URL arguments to dict
    parsed_get_args = dict(parse_qsl(get_args))
    # Merging URL arguments dict with new params
    parsed_get_args.update(params)

    # Bool and Dict values should be converted to json-friendly values
    # you may throw this part away if you don't like it :)
    parsed_get_args.update(
        {k: dumps(v) for k, v in parsed_get_args.items()
         if isinstance(v, (bool, dict))}
    )

    # Converting URL argument to proper query string
    encoded_get_args = urlencode(parsed_get_args, doseq=True)
    # Creating new parsed result object based on provided with new
    # URL arguments. Same thing happens inside of urlparse.
    new_url = ParseResult(
        parsed_url.scheme, parsed_url.netloc, parsed_url.path,
        parsed_url.params, encoded_get_args, parsed_url.fragment
    ).geturl()

    return new_url


# Loops
def get_loop_by_id(loopid):
    """Returns one single loop by id"""
    search_url = BASE_URL + "/loop?id=" + loopid
    json = _api_request(search_url)
    return loop.Loop(json["data"])


def get_loops(seriesid=None, episodeid=None, collectionid=None, duration=None, source_from=None, full=True, page=1,
              limit=30):
    """
    Get a group of loops by querying.
    :param seriesid: String. ID of a series - filters after series. NOTE: Will be ignored if 'episodeid' is specified
    :param episodeid: String. ID of an episode - filters after episode
    :param collectionid: String. ID of a collection - filters after collection.
    :param duration: String. Length of the loops - specify a number range with NUMBER,NUMBER.
                     Example: 1,2 = searches loops that are 1 to 2 seconds long.
                     3.5,5.5 = searches loops that are 3.5 to 5.5 seconds long.
    :param source_from: String. Can be automator / upload
    :param full: Boolean. Returns full series and episode details. Default: True
    :param page: Integer. Search results page. Default: 1
    :param limit: Integer. Limit of search results. Default: 30
    :return: Array of loop.Loop
    """
    url = BASE_URL + "loop"
    params = dict()
    if seriesid:
        params["seriesid"] = seriesid
    if episodeid:
        params["episodeid"] = episodeid
    if collectionid:
        params["collectionid"] = collectionid
    if duration:
        params["duration"] = duration
    if source_from:
        params["source_from"] = source_from
    params["full"] = full
    params["page"] = page
    params["limit"] = limit
    search_url = _add_url_params(url, params)

    json = _api_request(search_url)
    results = []
    for result in json["data"]:
        results.append(loop.Loop(result))
    return results


def get_loop_count(seriesid=None, episodeid=None, collectionid=None, duration=None, source_from=None):
    """
    Get number of loops.
    :param seriesid: String. ID of a series - filters after series. NOTE: Will be ignored if 'episodeid' is specified
    :param episodeid: String. ID of an episode - filters after episode
    :param collectionid: String. ID of a collection - filters after collection.
    :param duration: String. Length of the loops - specify a number range with NUMBER,NUMBER.
                     Example: 1,2 = searches loops that are 1 to 2 seconds long.
                     3.5,5.5 = searches loops that are 3.5 to 5.5 seconds long.
    :param source_from: String. Can be automator / upload
    :return: Integer
    """
    url = BASE_URL + "loop/count"
    params = dict()
    if seriesid:
        params["seriesid"] = seriesid
    if episodeid:
        params["episodeid"] = episodeid
    if collectionid:
        params["collectionid"] = collectionid
    if duration:
        params["duration"] = duration
    if source_from:
        params["source_from"] = source_from
    search_url = _add_url_params(url, params)

    json = _api_request(search_url)
    return json["data"]["count"]


def get_random_loops(seriesid=None, episodeid=None, duration=None, source_from=None, full=True, limit=30):
    """
    Get a group of loops by querying, randomly sorted.
    :param seriesid: String. ID of a series - filters after series. NOTE: Will be ignored if 'episodeid' is specified
    :param episodeid: String. ID of an episode - filters after episode
    :param duration: String. Length of the loops - specify a number range with NUMBER,NUMBER.
                     Example: 1,2 = searches loops that are 1 to 2 seconds long.
                     3.5,5.5 = searches loops that are 3.5 to 5.5 seconds long.
    :param source_from: String. Can be automator / upload
    :param full: Boolean. Returns full series and episode details. Default: True
    :param limit: Integer. Limit of search results. Default: 30
    :return: Array of loop.Loop
    """
    url = BASE_URL + "rand/loop"
    params = dict()
    if seriesid:
        params["seriesid"] = seriesid
    if episodeid:
        params["episodeid"] = episodeid
    if duration:
        params["duration"] = duration
    if source_from:
        params["source_from"] = source_from
    params["full"] = full
    params["limit"] = limit
    search_url = _add_url_params(url, params)

    json = _api_request(search_url)
    results = []
    for result in json["data"]:
        results.append(loop.Loop(result))
    return results


# Episodes
def get_episode_by_id(episodeid):
    """Returns one single episode by id"""
    search_url = BASE_URL + "/episode?id=" + episodeid
    json = _api_request(search_url)
    return episode.Episode(json["data"])


def get_episodes(seriesid=None, no=None, full=True, page=1, limit=30):
    """
    Get episodes of a series.
    :param seriesid: String. ID of a series - filters after series.
    :param no: String. Episode number ("01") or "Movie" / "OVA"
    :param full: Boolean. Returns full series and episode details. Default: True
    :param page: Integer. Search results page. Default: 1
    :param limit: Integer. Limit of search results. Default: 30
    :return: Array of episode.Episode
    """
    url = BASE_URL + "episode"
    params = dict()
    if seriesid:
        params["seriesid"] = seriesid
    if no:
        params["no"] = no
    params["full"] = full
    params["page"] = page
    params["limit"] = limit
    search_url = _add_url_params(url, params)

    json = _api_request(search_url)
    results = []
    for result in json["data"]:
        results.append(episode.Episode(result))
    return results


def get_episode_count(seriesid=None, no=None):
    """
    Get episode count.
    :param seriesid: String. ID of a series - filters after series.
    :param no: String. Episode number ("01") or "Movie" / "OVA"
    :return: Integer
    """
    url = BASE_URL + "episode/count"
    params = dict()
    if seriesid:
        params["seriesid"] = seriesid
    if no:
        params["no"] = no
    search_url = _add_url_params(url, params)

    json = _api_request(search_url)
    return json["data"]["count"]


# Series / Bangumi
def get_series_by_id(seriesid):
    """Returns one single series by id"""
    search_url = BASE_URL + "/series?id=" + seriesid
    json = _api_request(search_url)
    return series.Series(json["data"])


def get_series(type=None, season=None, page=1, limit=30):
    """
    Get a group of series by querying.
    :param type: String. "OVA", "TV" or "Movie"
    :param season: String. Example: 2016-10
    :param page: Integer. Search results page. Default: 1
    :param limit: Integer. Limit of search results. Default: 30
    :return: Array of series.Series
    """
    url = BASE_URL + "series"
    params = dict()
    if type:
        params["type"] = type
    if season:
        params["season"] = season
    params["page"] = page
    params["limit"] = limit
    search_url = _add_url_params(url, params)

    json = _api_request(search_url)
    results = []
    for result in json["data"]:
        results.append(series.Series(result))
    return results


def get_series_count(type=None, season=None):
    """
    Get series count.
    :param type: String. "OVA", "TV" or "Movie"
    :param season: String. Example: 2016-10
    :return: Integer
    """
    url = BASE_URL + "series/count"
    params = dict()
    if type:
        params["type"] = type
    if season:
        params["season"] = season
    search_url = _add_url_params(url, params)

    json = _api_request(search_url)
    return json["data"]["count"]


def search_series(value):
    """Search series by name. Returns array of series.Series."""
    search_url = BASE_URL + "search/series?value={0}".format(value)
    json = _api_request(search_url)
    results = []
    for result in json["data"]:
        results.append(series.Series(result))
    return results


# Tags
def get_tags(loopid=None, type=None, source=None, confidence=None, page=1, limit=30):
    """
    Get a group of loops by querying.
    :param loopid: String. ID of a loop - filters after loop.
    :param type: String. Type of tags, can be "general", "character", "safe"
    :param source: String. Source of tags, e.g. "illustration2vec".
    :param confidence: String. Range of confidence - specify a number range with NUMBER,NUMBER, e.g. "0.85,0.9"
    :param page: Integer. Search results page. Default: 1
    :param limit: Integer. Limit of search results. Default: 30
    :return: Array of tag.Tag
    """
    url = BASE_URL + "tag"
    params = dict()
    if loopid:
        params["loopid"] = loopid
    if type:
        params["type"] = type
    if source:
        params["source"] = source
    if confidence:
        params["confidence"] = confidence
    params["page"] = page
    params["limit"] = limit
    search_url = _add_url_params(url, params)

    json = _api_request(search_url)
    results = []
    for result in json["data"]:
        results.append(tag.Tag(result))
    return results
