#!/usr/bin/python3


class Tag:
    """Defines information about an Animeloop tag"""

    def __init__(self, json):
        """
        Initializes the Tag class with information for a loop
        :param json: String. Raw JSON
        """

        if "confidence" in json:
            self.confidence = json["confidence"]

        if "value" in json:
            self.value = json["value"]

        if "source" in json:
            self.source = json["source"]

        if "loopid" in json:
            self.loopid = json["loopid"]

        if "type" in json:
            self.type = json["type"]

        if "id" in json:
            self.id = json["id"]
