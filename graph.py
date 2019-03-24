"""
There is ListGraph
"""

import json


class ListGraph:
    """Using for saving map"""

    def __init__(self, n):
        self.size = n
        self.__matrix = [[] for i in range(n)]
        example = {"name": None, "image": None, "text": ""}
        self.information = [example for i in range(n)]

    def add_choice(self, u, v):
        """Add edge"""
        if u >= len(self.__matrix) or u < 0:
            raise IOError('\"from\" is out of range')
        if v >= len(self.__matrix) or u < 0:
            raise IOError('\"to\" is out of range')
        exam = {"to": v, "term": None, "text": None, "gifts": None}
        self.__matrix[u].append(exam)

    def add_information(self, u, name, name_image, text):
        """Fill up information about vertex"""
        self.information[u] = {"name": name, "image": name_image, "text": text}

    def get_information(self, u):
        """Return name, name of image and text of slide"""
        ans = self.information[u].copy()
        return ans

    def add_content(self, u, num, term, inside, gifts):
        """Fill up edge by condition and string"""
        if u >= len(self.__matrix) or u < 0:
            raise IOError('\"from\" is out of range')
        if num >= len(self.__matrix[u]) or num < 0:
            raise IOError('This edge is not existing')
        k = self.__matrix[u][num]["to"]
        example = {"to": k, "term": term, "text": inside, "gifts": gifts}
        self.__matrix[u][num] = example

    def get_next_vertices(self, u):
        """It is not used on idea"""
        ans = self.__matrix[u].copy()
        return ans
