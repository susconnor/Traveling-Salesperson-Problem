from datetime import time, datetime, timedelta, date
from Truck import Truck
from HashTabler import HashTable
from Package import Package
import csv


# Read Packages.csv file one line at a time.
# Creates an instance of Package class and loads it into the hash table.
# .
def load_packages():
    with open('csvFiles/Packages.csv', 'r') as pfile:
        # delimiter cannot be comma because special notes can contain commas.
        csv_reader = csv.reader(pfile, delimiter=";")
        for row in csv_reader:
            pid = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip_code = row[4]
            deadline = row[5]
            weight = row[6]
            notes = row[7]
            new_package = Package(pid, address, city, state, zip_code, deadline, weight, notes)
            package_hash_table.insert(pid, new_package)


# Prioritization Algorithm
# This method takes in a list of three trucks and will strategically place package IDs
# into each truck's unsorted_packages list depending on the package's special needs.
# Space and time complexity are both O(n).
def truck_loader(trucks):
    # This list will hold package IDs that do not have any requirements.
    load_later = []
    truck1 = trucks[0]
    truck2 = trucks[1]
    truck3 = trucks[2]
    size = package_hash_table.size_of_hashtable()
    # This loops through each package in the package hash table and will place
    # its ID into one of the truck's unsorted_packages list.
    for i in range(1, size + 1):
        current_package = package_hash_table.lookup(i)
        # Packages that must be delivered together will go into the first truck.
        if "Must be delivered" in current_package.notes:
            truck1.package_list.append(current_package)
        # Certain packages are required to be in truck 2
        elif "truck 2" in current_package.notes:
            truck2.package_list.append(current_package)
        # Packages that are delayed will miss the early truck.
        # Delayed packages with deadlines may be placed in the middle truck if their deadline is less th
        elif "Delayed" in current_package.notes:
            if current_package.deadline == "EOD":
                truck3.package_list.append(current_package)
            else:
                truck2.package_list.append(current_package)
        # Packages with the wrong address are loaded into the last truck.
        elif "Wrong address" in current_package.notes:
            truck3.package_list.append(current_package)
        # Any package with a deadline is loaded into the earliest truck, unless already loaded.
        elif current_package.deadline != "EOD":
            truck1.package_list.append(current_package)
        # Packages that don't require any accommodates are placed into a new list that is dealt with later
        else:
            load_later.append(current_package)
    # Trucks are topped off to their max capacity with packages that didn't have any special needs.
    # The truck with the latest start time is topped off first because there aren't any deadlines on the truck.
    # The middle truck will have the lightest load because
    # there are multiple packages that are delayed and have early deadlines.
    for package in load_later:
        if len(truck3.package_list) < truck3.max_packages:
            truck3.package_list.append(package)
        elif len(truck1.package_list) < truck1.max_packages:
            truck1.package_list.append(package)
        elif len(truck2.package_list) < truck2.max_packages:
            truck2.package_list.append(package)
        else:
            print("Trucks are overfilled")


# This method sort and delivers a truck's packages using a nearest neighbor sorting algorithm.
# Space complexity is O(1) while the time complexity is O(n^2).
def sort_and_deliver_packages(truck):
    # Delivery time must be a datetime.datetime to work with timedelta
    delivery_time = datetime.combine(todays_date, truck.start_time)
    packages_per_truck = list(truck.package_list)
    addresses = address_dict()
    # starting_loc represents the address of the hub.
    starting_loc = 0
    # While loop will iterate through every package assigned to the truck until each
    # package has a place in the truck's route.
    while packages_per_truck:
        min_distance = float("inf")
        select_p = None
        # Starting from the hub, each package in the list is tested to see which is closest to the current location.
        for package in packages_per_truck:
            address = package.address
            distance = distance_between(starting_loc, addresses[address])
            # Each time a new closest package is found, the package and distance are captured.
            # Once every package has been checked, the package being held by selected_p will be delivered next.
            if distance < min_distance:
                min_distance = distance
                select_p = package

        # This is required so the user can look up package status's based on time.
        select_p.truck = truck
        # Update the odometer
        truck.miles_traveled += min_distance
        # Log the package's delivery time
        delivery_time += time_elapsed(min_distance, truck.avg_speed)
        select_p.time_delivered = delivery_time.time()
        # The new starting location is updated to the last delivered package.
        starting_loc = addresses[select_p.address]
        # Package is removed from the truck's package list.
        packages_per_truck.remove(select_p)

    # Return truck to the hub once every package has been delivered.
    distance = distance_between(starting_loc, 0)
    truck.miles_traveled += distance
    delivery_time += time_elapsed(distance, truck.avg_speed)
    truck.end_time = delivery_time.time()
    # Total milage for truck is rounded to remove any potential errors.
    truck.miles_traveled = round(truck.miles_traveled, 1)


# This method takes in two integers that represent addresses from the Address.csv file.
# The return is the distance between those two locations.
def distance_between(loc1, loc2):
    # Matrix holds a 2D array that was created using milage()
    # Matrix is initialized before the main() method
    distance = milage_matrix[loc1][loc2]
    # If the 2D array is empty at the index, the locations are flipped
    if distance == '':
        distance = milage_matrix[loc2][loc1]
    return float(distance)


# This method takes in the distance between two locations and the speed of the truck.
# The return is how long it will take the truck to travel that distance.
def time_elapsed(distance, speed):
    time_spent = distance / speed
    time_spent = (3600 * time_spent)
    ts_delta = timedelta(seconds=time_spent)
    return ts_delta


# Read Distances.csv file one line at a time and place contents into a list.
# Return list that will be used by distance_between() to find the distance between two addresses.
def milage():
    with open('csvFiles/Distances.csv', 'r') as dfile:
        csv_reader = csv.reader(dfile)
        milage_list = []
        for row in csv_reader:
            milage_list.append(row)
        return milage_list


# Read Address.csv file one line at a time.
# Each line has an address and index that is placed in a dictionary.
# The key is the index and the value is the address.
def address_dict():
    address_holder = {}
    with open('csvFiles/Address.csv', 'r') as afile:
        csv_reader = csv.reader(afile)
        for row in csv_reader:
            aid = int(row[0])
            address = row[1]
            address_holder[address] = aid
    return address_holder


# This method allows the user to interact with the program using the command line interface.
def command_line_interface(trucks):
    size = package_hash_table.size_of_hashtable()
    # While loop allows the user to make more than one selection before the program closes.
    keep_searching = True
    while keep_searching:
        print("\nselect a number from one of the following options:")
        print("1. display package details by ID")
        print("2. display all package information")
        print("3. display milage by truck")
        print("4. display delivery status by time")
        print("5. display packages by truck")
        print("6. display delivery time vs deadline")
        print("7. exit")
        initial_input = input()
        # Entering 1 and then a valid package ID will print out the package's information.
        if initial_input == "1":
            id = input("enter the ID for the package\n")
            package = package_hash_table.lookup(id)
            if package is not None:
                print("ID |                 Address                 |       City       | State |  Zip  |  Weight  |  "
                      "Deadline  | Delivery Time |  Special Notes ")

                print(package)
            # This will return false if the uses says they want to exit the program.
            # If the user wants to continue, keep_searching will call command_line_interface() again.
            keep_searching = recall_cli(trucks)
        # Entering 2 will print out the package information for everything in the package_hash_table.
        elif initial_input == "2":
            print("ID |                 Address                 |       City       | State |  Zip  |  Weight  |  "
                  "Deadline  | Delivery Time |  Special Notes ")
            for i in range(1, size + 1):
                print(package_hash_table.lookup(i))
            keep_searching = recall_cli(trucks)
        # Entering 3 will display how far each truck traveled as well as the total distance traveled by all trucks.
        elif initial_input == "3":
            total = 0
            for truck in trucks:
                # Trucks are differentiated by their start times.
                print(truck.start_time.strftime("%I:%M %p"), "truck:", truck.miles_traveled, "mile(s)")
                total += truck.miles_traveled
            print("total distance:", total, "mile(s)")
            keep_searching = recall_cli(trucks)
        # Entering 4 will prompt the user to enter a time in a specific format.
        elif initial_input == "4":
            try:
                str_time_input = input("enter the time to search by in the following format: HH:MM AM/PM\n")
                time_input = datetime.strptime(str_time_input, "%I:%M %p").time()
                print("\nID     PACKAGE STATUS")
                for i in range(1, size + 1):
                    package_hash_table.lookup(i).print_status(time_input)
                keep_searching = recall_cli(trucks)
            except ValueError:
                print("improper time format entered")
        # Entering 5 will print each truck's package list.
        elif initial_input == "5":
            packs = []
            for truck in trucks:
                for package in truck.package_list:
                    packs.append(package.p_id)
                print(truck.start_time.strftime("%H:%M%p"),"Truck", packs)
                packs.clear()
            keep_searching = recall_cli(trucks)
        # Entering 6 will display all the package IDs that have deadlines, along with their delivery times.
        elif initial_input == "6":
            print("ID   DEADLINE    DELIVERED")
            for i in range(1, size + 1):
                p = package_hash_table.lookup(i)
                if p.deadline != "EOD":
                    print(p.p_id, "  ", p.deadline, "  ", p.time_delivered.strftime("%H:%M %p"))
            keep_searching = recall_cli(trucks)
        elif initial_input == "7":
            print("exiting")
            keep_searching = False

        else:
            print("invalid choice")


# This method is called throughout command_line_interface()
# The user is prompted to make a selection from a list of choices, after the user makes their decision,
# this method is called which will ask the user if they want to make another selection or close the program.
def recall_cli(trucks):
    # The program will exit after three wrong attempts to enter a valid selection.
    counter = 0
    while counter < 3:
        text = input("\nwould you like to make another selection? (y/n)").lower()
        if text == "y":
            command_line_interface(trucks)
            break
        elif text == "n":
            print("\nexiting")
            break
        else:
            print("\ninvalid entry")
            counter += 1
    if counter == 3:
        print("\nexiting")
    return False


package_hash_table = HashTable()
milage_matrix = milage()
todays_date = date.today()
today_formatted = todays_date.strftime("%B %d, %Y")


# Main method is where the other methods are called from.
def main():
    # Packages are loaded into hashtable.
    load_packages()
    # Three truck objects are created and placed into a list.
    early_truck = Truck(time(8, 00))
    middle_truck = Truck(time(9, 15))
    late_truck = Truck(time(12, 00))
    trucks = [early_truck, middle_truck, late_truck]
    # Packages are loaded into trucks based on their requirements.
    truck_loader(trucks)
    # First two trucks have their routes optimized and delivers their packages.
    sort_and_deliver_packages(early_truck)
    sort_and_deliver_packages(middle_truck)
    # Package 9 is updated with the correct address.
    package_hash_table.lookup(9).address = "410 S State St"
    package_hash_table.lookup(9).zip_code = 84111
    # The last truck leaves when a driver returns to the hub.
    # Last truck will not leave before package number 9's address is updated.
    dont_leave_before = time(10, 20)
    if early_truck.end_time > middle_truck.end_time:
        late_truck.start_time = max(middle_truck.end_time, dont_leave_before)
    if middle_truck.end_time > early_truck.end_time:
        late_truck.start_time = max(early_truck.end_time, dont_leave_before)
    # Late truck has its route optimized and delivers its packages.
    sort_and_deliver_packages(late_truck)
    # Print program name and user interface
    print("\nWGUPS Router", today_formatted)
    command_line_interface(trucks)


if __name__ == "__main__":
    main()
