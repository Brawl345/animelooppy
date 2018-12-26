#!/usr/bin/python3
from datetime import datetime

from animelooppy import episode
from animelooppy import series


class Loop:
    """Defines information about an Animeloop loop"""

    def __init__(self, json):
        """
        Initializes the Loop class with information for a loop
        :param json: String. Raw JSON
        """

        if "id" in json:
            self.id = json["id"]

        if "duration" in json:
            self.duration = json["duration"]

        if "period" in json:
            self.period = []
            try:
                self.period.append(datetime.strptime(json["period"]["begin"], "%H:%M:%S.%f"))
            except ValueError:
                self.period.append(datetime.strptime(json["period"]["begin"], "%H:%M:%S"))
            try:
                self.period.append(datetime.strptime(json["period"]["end"], "%H:%M:%S.%f"))
            except ValueError:
                self.period.append(datetime.strptime(json["period"]["end"], "%H:%M:%S"))
            self.duration = (self.period[1] - self.period[0]).total_seconds()

        if "frame" in json:
            self.frame = []
            self.frame.append(json["frame"]["begin"])
            self.frame.append(json["frame"]["end"])

        if "sourceFrom" in json:
            self.sourceFrom = json["sourceFrom"]

        if "uploadDate" in json:
            self.uploadDate = datetime.strptime(json["uploadDate"], "%Y-%m-%dT%H:%M:%S.%fZ")

        if "files" in json:
            if "jpg_360p" in json["files"]:
                self.jpg_360p = json["files"]["jpg_360p"]

            if "mp4_360p" in json["files"]:
                self.mp4_360p = json["files"]["mp4_360p"]

            if "gif_360p" in json["files"]:
                self.gif_360p = json["files"]["gif_360p"]

            if "jpg_720p" in json["files"]:
                self.jpg_720p = json["files"]["jpg_720p"]

            if "mp4_720p" in json["files"]:
                self.mp4_720p = json["files"]["mp4_720p"]

            if "mp4_1080p" in json["files"]:
                self.mp4_1080p = json["files"]["mp4_1080p"]

            if "jpg_1080p" in json["files"]:
                self.jpg_1080p = json["files"]["jpg_1080p"]

        if "episodeid" in json:
            self.episodeid = json["episodeid"]

        if "seriesid" in json:
            self.seriesid = json["seriesid"]

        if "episode" in json:
            self.episode = episode.Episode(json["episode"])

        if "series" in json:
            self.series = series.Series(json["series"])
