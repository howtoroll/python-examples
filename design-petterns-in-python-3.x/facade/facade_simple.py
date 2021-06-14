# client
class FacadeClient:
    def __init__(self):
        pass

    def ask_even_organizer(self):
        facade = Facade()
        facade.arrange()


# facade
class Facade:
    def __init__(self):
        pass

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.book_hotel()

        self.florist = Florist()
        self.florist.set_flower_requirements()


# subsystems
class Hotelier:
    def __init__(self):
        print("--- Hotel Arrangement ---")

    def __is_available(self):
        print("Is the hotel available to oraganize launch event on the date?")
        return True

    def book_hotel(self):
        if self.__is_available():
            print("Registered the Booking.")


class Florist:
    def __init__(self):
        print("--- Flower Decoration ---")

    def set_flower_requirements(self):
        print("Tulips, ferns, lilies, Roses would be perfect fot the decorations.")
