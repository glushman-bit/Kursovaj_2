from src.APIAdapter import APIAdapter
from utils.object_list import get_object_in_list
from utils.country_name import get_country_name


print("""
Программа: Добро пожаловать в программу для работы с трекером самолетов
      """)

if __name__ == "__main__":

    print("Введите название страны для вывода данных о самолетах: ")
    user_input_country: str = str(input()).strip()

    if not user_input_country:
        raise ValueError("Вы ничего не ввели.")

    country_coordinates = APIAdapter().get_coordinates(user_input_country)

    if not country_coordinates:
        print("Страна не найдена. Проверьте правильность написания.")
        exit()

    print("Вывести ТОП самолетов по высоте? да/нет")
    user_input = input()
    if user_input == "да" or user_input == "yes":
        user_input_top = input("Введите количество самолетов для фильтрации по высоте: ")

        if not user_input_top:
            print("Вы ничего не ввели.")
            exit()

        adapter = APIAdapter()
        adapter.get_aeroplanes(country_coordinates)
        get_planes = get_object_in_list(adapter.aeroplanes)

        top_planes = sorted(get_planes, key=lambda plane: plane.geo_altitude, reverse=True)[:int(user_input_top)]
        print(f"Топ {user_input_top} самолетов по высоте.")

        for i, plane in enumerate(top_planes, start=1):
            print(
                f"{i}. {plane.callsign} | Страна: {plane.country} | Высота: {plane.geo_altitude} м | Скорость: {plane.velocity} м/с" )


    print(" ")
    print("Вывести ТОП самолетов по скорости? да/нет")
    user_input = input()
    if user_input == "да" or user_input == "yes":
        user_input_top = input("Введите количество самолетов для фильтрации по скорости: ")

        adapter = APIAdapter()
        adapter.get_aeroplanes(country_coordinates)
        get_planes = get_object_in_list(adapter.aeroplanes)

        top_planes = sorted(get_planes, key=lambda plane: plane.velocity, reverse=True)[:int(user_input_top)]
        print(f"Топ {user_input_top} самолетов по скорости.")

        for i, plane in enumerate(top_planes, start=1):
            print(
                f"{i}. {plane.callsign} | Страна: {plane.country} | Высота: {plane.geo_altitude} м | Скорость: {plane.velocity} м/с")


    print(" ")
    print("Получить самолеты по стране их регистрации? да/нет")
    user_input_reg_country: str = str(input()).strip()
    if user_input_reg_country == "да" or user_input_reg_country == "yes":
        user_input = input("Введите страну для фильтрации: ").strip().capitalize()

        adapter = APIAdapter()
        adapter.get_aeroplanes(country_coordinates)
        get_planes = get_object_in_list(adapter.aeroplanes)

        planes_country = [plane for plane in get_planes if plane.country == get_country_name(user_input)]
        print(f"Найдено {len(planes_country)} самолетов в {user_input}:")

        for i, plane in enumerate(planes_country, start=1):
            print(
                f"{i}. {plane.callsign} | Страна: {plane.country} | Высота: {plane.geo_altitude} м | Скорость: {plane.velocity} м/с")


    print("Программа закончила работу.")
    exit()
