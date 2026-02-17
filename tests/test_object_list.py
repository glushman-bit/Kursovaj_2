from src.Planes import Planes
from utils.object_list import get_object_in_list


def test_get_object_in_list_correct(mock_planes_info):
    """Проверка правильности работы функции get_object_in_list"""
    objects = get_object_in_list(mock_planes_info)
    assert len(objects) == 1

    plane = objects[0]

    assert isinstance(plane, Planes)
    assert plane.time_position == 1766166618
    assert plane.country == "Switzerland"
    assert plane.callsign == "SWR438A"
    assert plane.velocity == 189.7
    assert plane.geo_altitude == 4282.44
    assert plane.on_ground == False
