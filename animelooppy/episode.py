#!/usr/bin/python3
from animelooppy import series


class Episode:
    """Defines information about an Animeloop episode"""

    def __init__(self, json):
        """
        Initializes the Episode class with information for an episode
        :param json: String. Raw JSON
        """

        if "id" in json:
            self.id = json["id"]

        if "no" in json:
            self.no = json["no"]

        if "seriesid" in json:
            self.seriesid = json["seriesid"]

        if "series" in json:
            self.series = series.Series(json["series"])
