from typing import NamedTuple, Optional

from mappymatch.constructs.coordinate import Coordinate
from mappymatch.constructs.road import Road


class Match(NamedTuple):
    """
    represents a match made by a map matching algorithm
    """

    road: Optional[Road]
    coordinate: Coordinate
    distance: float

    def set_coordinate(self, c: Coordinate):
        """
        set_coordinate 

        :param c: _description_
        :type c: Coordinate
        :return: _description_
        :rtype: _type_
        """
        return self._replace(coordinate=c)

    def to_json(self) -> dict:
        """
        to_json gets road ids of roads that are not None and return the data of this road in a dictionary. 

        :return: _description_
        :rtype: dict
        """
        out = {
            "road_id": self.road.road_id if self.road else None,
            "coordinate_id": self.coordinate.coordinate_id,
            "distance_to_road": self.distance,
        }
        return out
