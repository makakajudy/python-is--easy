import time


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

            return f"{self.make} No repaired required"
        else:
            print(f"\u001b[31m vehicle is being reset....\u001b[0m")
            time.sleep(2)
            print()
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
            return f"{self.make} aged {self.year} weighing {self.weight} made {self.trips} trips," \
                   f"{100 - self.trips} more to go "
        else:
            self.stop()
            self.needs_service = True
            return f"{self.make} aged {self.year} weighing {self.weight} " \
                   f"\u001b[31m has over 100 trips and needs servicing!\u001b[0m "

    @staticmethod
    def Me_driving(car_list):
        results = 0
        for i, car in enumerate(car_list):
            print(i, car.make)

        selection = input("Please select a car to drive ").capitalize()
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

    def __str__(self):
        return self.switching_car()
        # if self.trips < 100:
        #
        # return f"\u001b[36m {self.make} :{self.model} aged {self.year},of {self.weight} tonne has now {self.trips}"
        # \ f" and service state is {self.needs_service}.This car does not need servicing!  \u001b[0m" else: return
        # f" {self.make}:{self.model} aged {self.year},of {self.weight} tonnes has {self.trips} " \ f"trips and
        # service state is {self.needs_service}!\u001b[31m This car requires servicing!!\u001b[0m "


class Planes(Vehicle):
    def __init__(self, make, model, year, weight, need_maintenance,
                 trips_since_maintenance, is_flying):
        Vehicle.__init__(self, make, model, year, weight,
                         need_maintenance, trips_since_maintenance)
        self.fly = is_flying

    def flying(self):
        self.fly = True

    def landing(self):
        self.fly = False

        return self.fly

    def __str__(self):
        if self.trips < 100:
            self.flying()
            self.needs_service = False
            return f"service status: {self.needs_service}," \
                   f" plane is okay to fly"
        else:
            self.needs_service = True
            self.landing()
            return f"service status:{self.needs_service}, " \
                   f"the plane can't fly until it's repaired!!"


# make model age service trip driving
vehicle1 = Cars("Range", "evoque", 8, 5000, False, 10, False)
vehicle2 = Cars("Toyota", "prius", 6, 2000, False, 88, True)
vehicle3 = Cars("Nissan", "X-trail", 7, 7000, True, 101, False)

plane1 = Planes("BA 1", "Boeing-000", 7, 7000, True, 101, False)
plane2 = Planes("KA 1", "Boeing-111", 6, 2000, False, 88, True)

# a list holding my 3 cars
my_cars = [vehicle1, vehicle2, vehicle3]
my_planes = [plane1, plane2]
print()
print()

while True:
    # class Cars to implement the static method
    print(Cars.Me_driving(my_cars))
    print()
    another = input("would you like to drive another car? y/n? ")
    print()

    if another == "y":
        continue
    else:
        for cars in my_cars:
            print(cars)
            print()
        print("  Repairing/Resetting stage!!  ")
        print()
        record = 0
        while record != len(my_cars):
            y = my_cars[record].Repair()
            print(y)
            record += 1

        print()
        print()
        print("\u001b[33m Finally Output \u001b[0m ")
        for cars in my_cars:
            print(cars)
            print()
        print("\u001b[33m Lets check our planes\u001b[0m ")
        print()

        for p in my_planes:
            print(f"{p.make} has {p.trips} and {p}")

        # print(f"can flights {plane1.make} fly ? ")
        # print(f"current trips {plane1.trips}")
        # print(plane1)
        break
