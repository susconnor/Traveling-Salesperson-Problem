# WGUPS Routing Program / Traveling Salesperson Problem

## Description

This Python program implements a routing algorithm for a package delivery service (WGUPS). It reads package information and delivery distances from CSV files, loads packages onto trucks based on specific criteria (deadlines, special notes, etc.), and then calculates optimal delivery routes using a nearest neighbor approach.  The program provides a command-line interface for users to query package information, view truck mileage, and check delivery status.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/susconnor/Traveling-Salesperson-Problem.git
    ```

2.  **Dependencies:**  This project uses standard Python libraries, so no additional installations are required beyond having Python 3.x installed.

## Usage

1.  **Data Files:** Ensure that the following CSV files are present in a `csvFiles` directory within the project folder.  These are required for the program to run:
    *   `Packages.csv`: Contains package information (ID, address, city, state, zip code, deadline, weight, notes).  The delimiter is a semicolon (`;`).
    *   `Distances.csv`: Contains the distances between addresses.
    *   `Address.csv`: Contains address indices and corresponding addresses.

2.  **Run the program:**
    ```bash
    python main.py
    ```

3.  **Command-Line Interface:**  The program will present a menu with the following options:

    ```
    select a number from one of the following options:
    1. display package details by ID
    2. display all package information
    3. display milage by truck
    4. display delivery status by time
    5. display packages by truck
    6. display delivery time vs deadline
    7. exit
    ```

    Follow the prompts to interact with the program and retrieve information about packages and delivery routes.

    The output of `2. display all package information` is below.


    ```
    WGUPS Router February 18, 2025

    select a number from one of the following options:
    1. display package details by ID
    2. display all package information
    3. display milage by truck
    4. display delivery status by time
    5. display packages by truck
    6. display delivery time vs deadline
    7. exit
    2
    ID |                 Address                 |       City       | State |  Zip  |  Weight  |  Deadline  | Delivery Time |  Special Notes
    # 1|            195 W Oakland Ave            |  Salt Lake City  |   UT  | 84115 | 21 kg(s) |  10:30 AM  |   08:52 AM    |
    # 2|               2530 S 500 E              |  Salt Lake City  |   UT  | 84106 | 44 kg(s) |    EOD     |   11:08 AM    |
    # 3|              233 Canyon Rd              |  Salt Lake City  |   UT  | 84103 |  2 kg(s) |    EOD     |   10:31 AM    | Can only be on truck 2
    # 4|               380 W 2880 S              |  Salt Lake City  |   UT  | 84115 |  4 kg(s) |    EOD     |   11:01 AM    |
    # 5|              410 S State St             |  Salt Lake City  |   UT  | 84111 |  5 kg(s) |    EOD     |   11:28 AM    |
    # 6|              3060 Lester St             | West Valley City |   UT  | 84119 | 88 kg(s) |  10:30 AM  |   09:57 AM    | Delayed on flight---will not arrive to depot until 9:05 am
    # 7|               1330 2100 S               |  Salt Lake City  |   UT  | 84106 |  8 kg(s) |    EOD     |   11:13 AM    |
    # 8|               300 State St              |  Salt Lake City  |   UT  | 84103 |  9 kg(s) |    EOD     |   11:32 AM    |
    # 9|              410 S State St             |  Salt Lake City  |   UT  | 84111 |  2 kg(s) |    EOD     |   11:28 AM    | Wrong address listed
    #10|             600 E 900 South             |  Salt Lake City  |   UT  | 84105 |  1 kg(s) |    EOD     |   11:22 AM    |
    #11|          2600 Taylorsville Blvd         |  Salt Lake City  |   UT  | 84118 |  1 kg(s) |    EOD     |   12:11 PM    |
    #12|  3575 W Valley Central Station bus Loop | West Valley City |   UT  | 84119 |  1 kg(s) |    EOD     |   10:33 AM    |
    #13|               2010 W 500 S              |  Salt Lake City  |   UT  | 84104 |  2 kg(s) |  10:30 AM  |   09:34 AM    |
    #14|              4300 S 1300 E              |     Millcreek    |   UT  | 84117 | 88 kg(s) |  10:30 AM  |   08:06 AM    | Must be delivered with 15, 19
    #15|              4580 S 2300 E              |     Holladay     |   UT  | 84117 |  4 kg(s) |  9:00 AM   |   08:13 AM    |
    #16|              4580 S 2300 E              |     Holladay     |   UT  | 84117 | 88 kg(s) |  10:30 AM  |   08:13 AM    | Must be delivered with 13, 19
    #17|              3148 S 1100 W              |  Salt Lake City  |   UT  | 84119 |  2 kg(s) |    EOD     |   10:53 AM    |
    #18|               1488 4800 S               |  Salt Lake City  |   UT  | 84123 |  6 kg(s) |    EOD     |   09:44 AM    | Can only be on truck 2
    #19|             177 W Price Ave             |  Salt Lake City  |   UT  | 84115 | 37 kg(s) |    EOD     |   10:28 AM    |
    #20|               3595 Main St              |  Salt Lake City  |   UT  | 84115 | 37 kg(s) |  10:30 AM  |   08:37 AM    | Must be delivered with 13, 15
    #21|               3595 Main St              |  Salt Lake City  |   UT  | 84115 |  3 kg(s) |    EOD     |   10:26 AM    |
    #22|           6351 South 900 East           |      Murray      |   UT  | 84121 |  2 kg(s) |    EOD     |   12:34 PM    |
    #23|           5100 South 2700 West          |  Salt Lake City  |   UT  | 84118 |  5 kg(s) |    EOD     |   12:10 PM    |
    #24|              5025 State St              |      Murray      |   UT  | 84107 |  7 kg(s) |    EOD     |   08:30 AM    |
    #25|         5383 South 900 East #104        |  Salt Lake City  |   UT  | 84117 |  7 kg(s) |  10:30 AM  |   09:23 AM    | Delayed on flight---will not arrive to depot until 9:05 am
    #26|         5383 South 900 East #104        |  Salt Lake City  |   UT  | 84117 | 25 kg(s) |    EOD     |   08:24 AM    |
    #27|            1060 Dalton Ave S            |  Salt Lake City  |   UT  | 84104 |  5 kg(s) |    EOD     |   09:39 AM    |
    #28|               2835 Main St              |  Salt Lake City  |   UT  | 84115 |  7 kg(s) |    EOD     |   11:04 AM    | Delayed on flight---will not arrive to depot until 9:05 am
    #29|               1330 2100 S               |  Salt Lake City  |   UT  | 84106 |  2 kg(s) |  10:30 AM  |   09:02 AM    |
    #30|               300 State St              |  Salt Lake City  |   UT  | 84103 |  1 kg(s) |  10:30 AM  |   09:20 AM    |
    #31|               3365 S 900 W              |  Salt Lake City  |   UT  | 84119 |  1 kg(s) |  10:30 AM  |   08:43 AM    |
    #32|               3365 S 900 W              |  Salt Lake City  |   UT  | 84119 |  1 kg(s) |    EOD     |   10:51 AM    | Delayed on flight---will not arrive to depot until 9:05 am
    #33|               2530 S 500 E              |  Salt Lake City  |   UT  | 84106 |  1 kg(s) |    EOD     |   08:57 AM    |
    #34|              4580 S 2300 E              |     Holladay     |   UT  | 84117 |  2 kg(s) |  10:30 AM  |   08:13 AM    |
    #35|            1060 Dalton Ave S            |  Salt Lake City  |   UT  | 84104 | 88 kg(s) |    EOD     |   10:12 AM    |
    #36|            2300 Parkway Blvd            | West Valley City |   UT  | 84119 | 88 kg(s) |    EOD     |   10:02 AM    | Can only be on truck 2
    #37|              410 S State St             |  Salt Lake City  |   UT  | 84111 |  2 kg(s) |  10:30 AM  |   09:17 AM    |
    #38|              410 S State St             |  Salt Lake City  |   UT  | 84111 |  9 kg(s) |    EOD     |   10:28 AM    | Can only be on truck 2
    #39|               2010 W 500 S              |  Salt Lake City  |   UT  | 84104 |  9 kg(s) |    EOD     |   10:17 AM    |
    #40|               380 W 2880 S              |  Salt Lake City  |   UT  | 84115 | 45 kg(s) |  10:30 AM  |   08:48 AM    |
    
    would you like to make another selection? (y/n)
    ```

##  Files

*   `main.py`: The main program file containing the core logic.
*   `Truck.py`: Defines the `Truck` class, representing delivery trucks with attributes like start time, mileage, and package list.
*   `HashTable.py`: Implements a hash table data structure for efficient package lookup.
*   `Package.py`: Defines the `Package` class, storing information about individual packages.
*   `csvFiles/Packages.csv`: CSV file containing package data.
*   `csvFiles/Distances.csv`: CSV file containing distance data.
*   `csvFiles/Address.csv`: CSV file containing address data.

## WGU Project Requirements - Data Structures & Algorithms 2

## Scenerio

```text
The Western Governors University Parcel Service (WGUPS) needs to determine the best route and delivery distribution for their Daily Local Deliveries (DLD) because packages
are not currently being consistently delivered by their promised deadline. The Salt Lake City DLD route has three trucks, two drivers, and an average of 40 packages to deliver
each day; each package has specific criteria and delivery requirements.

Your task is to determine the best algorithm, write code, and present a solution where all 40 packages, listed in the attached “WGUPS Package File,” will be delivered on time
with the least number of miles added to the combined mileage total of all trucks. The specific delivery locations are shown on the attached “Salt Lake City Downtown Map” and
distances to each location are given in the attached “WGUPS Distance Table.”

While you work on this assessment, take into consideration the specific delivery time expected for each package and the possibility that the delivery requirements—including the
expected delivery time—can be changed by management at any time and at any point along the chosen route. In addition, you should keep in mind that the supervisor should be
able to see, at assigned points, the progress of each truck and its packages by any of the variables listed in the “WGUPS Package File,” including what
has been delivered and what time the delivery occurred.

The intent is to use this solution (program) for this specific location and to use the same program in many cities in each state where WGU has a presence. As such, you will need to
include detailed comments, following the industry-standard Python style guide, to make your code easy to read and to justify the decisions you made while writing your program.
```

## Assumptions
```text
- Each truck can carry a maximum of 16 packages.
- Trucks travel at an average speed of 18 miles per hour.
- Trucks have a “infinite amount of gas” with no need to stop.
- Each driver stays with the same truck as long as that truck is in service.
- Drivers leave the hub at 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed. The day ends when all 40 packages have been delivered.
- Delivery time is instantaneous, i.e., no time passes while at a delivery (that time is factored into the average speed of the trucks).
- There is up to one special note for each package.
- The wrong delivery address for package #9, Third District Juvenile Court, will be corrected at 10:20 a.m. The correct address is 410 S State St., Salt Lake City, UT 84111.
- The package ID is unique; there are no collisions.
- No further assumptions exist or are allowed.
```
## Requirements 

```text
Your submission must be your original work. No more than a combined total of 30% of the submission and no more than a 10% match to any one individual source can be directly
quoted or closely paraphrased from sources, even if cited correctly. An originality report is provided when you submit your task that can be used as a guide.

You must use the rubric to direct the creation of your submission because it provides detailed criteria that will be used to evaluate your work. Each requirement below may be
evaluated by more than one rubric aspect. The rubric aspect titles may contain hyperlinks to relevant portions of the course.

Section 1: Programming/Coding


    A. Identify the algorithm that will be used to create a program to deliver the packages and meets all  requirements specified in the scenario.

    B.  Write a core algorithm overview, using the sample given, in which you do the following:

        1.  Comment using pseudocode to show the logic of the algorithm applied to this software solution.

        2.  Apply programming models to the scenario.

        3.  Evaluate space-time complexity using Big O notation throughout the coding and for the entire program.

        4.  Discuss the ability of your solution to adapt to a changing market and to scalability.

        5.  Discuss the efficiency and maintainability of the software.

        6.  Discuss the self-adjusting data structures chosen and their strengths and weaknesses based on the scenario.

    C.  Write an original code to solve and to meet the requirements of lowest mileage usage and having all  packages delivered on time.

        1.  Create a comment within the first line of your code that includes your first name, last name, and student ID.

        2.  Include comments at each  block of code to explain the process and flow of the coding.

    D.  Identify a data structure that can be used with your chosen algorithm to store the package data.

        1.  Explain how your data structure includes the relationship between the data points you are storing.

        Note: Do NOT use any existing data structures. You must design, write, implement, and debug all code that you turn in for this assessment. Code downloaded from the internet or acquired from another student or any other source may not be submitted and will result in automatic failure of this assessment.

    E.  Develop a hash table, without using any additional libraries or classes, with an insertion function that takes the following components as input and inserts the components into the hash table:

        •  package ID number

        •  delivery address

        •  delivery deadline

        •  delivery city

        •  delivery zip code

        •  package weight

        •  delivery status (e.g., delivered, in route)

    F.  Develop a look-up function that takes the following components as input and returns the corresponding data elements:

        •  package ID number

        •  delivery address

        •  delivery deadline

        •  delivery city

        •  delivery zip code

        •  package weight

        •  delivery status (e.g., delivered, in route)

    G.  Provide an interface for the insert and look-up functions to view the status of any package at any time. This function should return all information about each package, including delivery status.

        1.  Provide screenshots to show package status of all packages at a time between 8:35 a.m. and 9:25 a.m.

        2.  Provide screenshots to show package status of all packages at a time between 9:35 a.m. and 10:25 a.m.

        3.  Provide screenshots to show package status of all packages at a time between 12:03 p.m. and 1:12 p.m.

    H.  Run your code and provide screenshots to capture the complete execution of your code.
```
