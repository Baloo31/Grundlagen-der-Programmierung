class Hotel:
    def __init__(self, guest_list, room_list, res_list):
        self.__guests = guest_list
        self.__rooms = room_list
        self.__resrvs = res_list

    def __str__(self):
        return f'{self.guests} ||| {self.rooms} ||| {self.resrvs}'

    @property
    def guests(self): return self.__guests

    @guests.setter
    def guests(self, val): self.__guests = val

    @property
    def rooms(self): return self.__rooms

    @rooms.setter
    def rooms(self, val): self.__rooms = val

    @property
    def resrvs(self): return self.__resrvs

    @resrvs.setter
    def resrvs(self, val): self.__resrvs = val
