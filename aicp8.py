from datetime import datetime, timedelta

class BoatHireSystem:
    def __init__(self):
        self.boats = {i: {"is_hired": False, "return_time": None, "total_hours": 0, "money_taken": 0} for i in range(1, 11)}

    def task_1(self, boat_number, start_time, hours):
        if not 10 <= start_time <= 17:
            print("Boat can only be hired between 10:00 and 17:00.")
            return

        if not 0.5 <= hours <= 1:
            print("Invalid duration. You can only hire a boat for 0.5 or 1 hour.")
            return

        if self.boats[boat_number]["is_hired"]:
            print("Boat {} is already hired until {}.".format(boat_number, self.boats[boat_number]["return_time"]))
            return

        cost = 20 * hours if hours == 1 else 12
        self.boats[boat_number]["is_hired"] = True
        self.boats[boat_number]["return_time"] = (datetime.now() + timedelta(hours=hours)).strftime("%H:%M")
        self.boats[boat_number]["total_hours"] += hours
        self.boats[boat_number]["money_taken"] += cost

        print("Boat {} hired successfully for {} hour(s).".format(boat_number, hours))

    def task_2(self):
        current_time = datetime.now().hour
        available_boats = [boat for boat, data in self.boats.items() if not data["is_hired"]]
        if available_boats:
            print("Available boats: {}".format(available_boats))
        else:
            earliest_return_time = min(data["return_time"] for data in self.boats.values())
            print("No boats available. The earliest available boat will be at {}.".format(earliest_return_time))

    def task_3(self):
        total_money = sum(data["money_taken"] for data in self.boats.values())
        total_hours = sum(data["total_hours"] for data in self.boats.values())
        unused_boats = [boat for boat, data in self.boats.items() if not data["is_hired"]]
        most_used_boat = max(self.boats, key=lambda boat: self.boats[boat]["total_hours"])

        print("\nEnd of the day report:")
        print("Total money taken: ${}".format(total_money))
        print("Total hours boats were hired: {}".format(total_hours))
        print("Unused boats: {}".format(unused_boats))
        print("Most used boat: Boat {} with {} hours.".format(most_used_boat, self.boats[most_used_boat]["total_hours"]))


# Testing the program
boat_system = BoatHireSystem()

# Task 1 - Example usage
boat_system.task_1(2, 12, 1)
boat_system.task_1(5, 14, 0.5)

# Task 2 - Example usage
boat_system.task_2()

# Task 3 - Example usage
boat_system.task_3()
