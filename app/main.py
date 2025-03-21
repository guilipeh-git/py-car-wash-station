class Car:
    # write your code here
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str) -> None:

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    # write your code here
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: str, average_rating: float,
            count_of_ratings: int) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, list_cars: list) -> int:

        pass

    def calculate_washing_price(self) -> int:

        pass

    def wash_single_car(self) -> None:

        pass

    def rate_service(self) -> None:

        pass
