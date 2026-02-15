from src.Planes import Planes
from src.APIAdapter import APIAdapter


def get_object_in_list(planes_information: dict):
    """
    Преобразование данных о самолетах в объекты самолётов класса Planes в воздушном пространстве страны.
    :param planes_information: Словарь, полученный в методе get_aeroplanes из класса APIAdapter.
    Содержит информацию о каждом самолете в воздушном пространстве страны.
    :return: Список самолетов, экземпляры класса Planes.
    """
    object_list = []
    for aeroplane in planes_information['states']:
        object_ = Planes(aeroplane[3], aeroplane[2], aeroplane[1], aeroplane[9], aeroplane[13], aeroplane[8])
        object_list.append(object_)

    return object_list
