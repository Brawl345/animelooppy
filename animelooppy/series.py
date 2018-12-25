#!/usr/bin/python3


class Series:
    """Defines information about an Animeloop series ("bangumi") """

    def __init__(self, json):
        """
        Initializes the Series class with information for a series
        :param json: String. Raw JSON
        """

        if "id" in json:
            self.id = json["id"]

        if "title" in json:
            self.title = json["title"]

        if "title_romaji" in json:
            self.title_romaji = json["title_romaji"]

        if "title_english" in json:
            self.title_english = json["title_english"]

        if "title_japanese" in json:
            self.title_japanese = json["title_japanese"]

        if "description" in json:
            self.description = json["description"]

        if "genres" in json:
            self.genres = []
            for genre in json["genres"]:
                if genre != "":
                    self.genres.append(genre)

        if "type" in json:
            self.type = json["type"]

        if "total_episodes" in json:
            self.total_episodes = json["total_episodes"]

        if "anilist_id" in json:
            self.anilist_id = json["anilist_id"]

        if "season" in json:
            self.season = json["season"]

        if "image_url_large" in json:
            self.image_url_large = json["image_url_large"]
