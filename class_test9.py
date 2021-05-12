class Vehicle:
    def __init__(self, make, model, yr, weight, need_maintenance=False,
                 trips_since_maintenance=0):
        self.make = make
        self.model = model
        self.year = yr
        self.weight = weight
        self.needs_service = need_maintenance
        self.trips = trips_since_maintenance

    # getter
    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getYear(self):
        return self.year

    def getWeight(self):
        return self.weight

    # setter
    def setMake(self, make):
        self.make = make

    def setModel(self, model):
        self.model = model

    def setYear(self, year):
        self.year = year

    def setWeight(self, weight):
        self.weight = weight

    def Repair(self):
        if self.trips < 100:

            return "no repaired needed"
        else:
            print(f"\u001b[31m vehicle is being reset....\u001b[0m")
            self.trips = 0
            self.needs_service = False
            return f"{self.make} is now repaired and reset"


class Cars(Vehicle):
    def __init__(self, make, model, year, weight, need_maintenance,
                 trips_since_maintenance, is_driving):
        Vehicle.__init__(self, make, model, year, weight,
                         need_maintenance, trips_since_maintenance)
        self.is_driving = is_driving

    def Drive(self):
        self.is_driving = True
        return self.is_driving

    def stop(self):
        self.is_driving = False
        return self.is_driving

    def switching_car(self):  # for switching drive to stop depending on the trip
        if self.trips <= 100:
            self.Drive()
            self.trips += 1
            self.needs_service = False
            return f"made {self.trips} trips,{100 - self.trips} more to go"
        else:
            self.stop()
            self.needs_service = True
            return f" has over 100 trips and needs servicing! "

    @staticmethod
    def Me_driving(car_list):
        results = 0
        for i, car in enumerate(car_list):
            print(i, car.make)
        selection = input("Please select a car to drive ")
        drives = int(input("how many times ?"))

        i = 0
        while i != len(car_list):
            if selection == car_list[i].make:
                print("current no of trips :", car_list[i].trips)
                car_list[i].trips += drives
                results = car_list[i].trips
                break
            i += 1
        return f"trip after my drive :{results}"

    # def drive(self, trip):
    #     self.trips = trip
    #     self.switching_car()
    #     counter = 0
    #     while counter < self.trips:
    #         return self.switching_car()
    #     counter += 1

    def __str__(self):
        if self.trips < 100:
            return f"\u001b[36m {self.make} :{self.model} aged {self.year},of {self.weight} tonne has now {self.trips}" \
                   f"and service state is {self.needs_service}.This car does not need servicing!  \u001b[0m"
        else:
            return f" {self.make}:{self.model} aged {self.year},of {self.weight}t onnes has {self.trips} " \
                   f"trips and service state is {self.needs_service}!This car requires servicing "


# make model age service trip driving
vehicle1 = Cars("x", "nissan", 8, 5000, False, 10, True)
vehicle2 = Cars("y", "toyota", 6, 2000, False, 88, True)
vehicle3 = Cars("navara", "toyota", 7, 7000, True, 101, False)

# print(vehicle1)
# print(vehicle1.Repair())
# print(vehicle1)


# a list holding my 3 cars

my_cars = [vehicle1, vehicle2, vehicle3]

print(Cars.Me_driving(my_cars))  # class Cars to implement the static method
for cars in my_cars:
    print(cars)
