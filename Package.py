class Package:
    # Create new Package object
    def __init__(self, p_id, address, city, state, zip_code, deadline, weight, notes):
        self.p_id = p_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.truck = None
        self.status = "At hub"
        self.time_delivered = None

    # This method is called using the cli.
    # The user will enter the time they want to search delivery status.
    # Method will print out every package ID and where the package is at that time.
    # If the package has been delivered, it will also print out the time of delivery.
    def print_status(self, submitted_time):
        delivered = self.time_delivered
        time_format = "%I:%M:%S %p"
        delivery_str = delivered.strftime(time_format)

        truck = self.truck
        if truck == None:
            print(self.p_id, self.status)
        elif submitted_time > delivered:
            self.status = "Delivered @ " + delivery_str
            print(self.p_id, self.status)
            self.status = "At hub"
        elif truck.start_time < submitted_time < delivered:
            self.status = "In route"
            print(self.p_id, self.status)
            self.status = "At hub"
        else:
            print(self.p_id, self.status)

    # String to print when a package object is called to print.
    def __str__(self):
        return f"#{self.p_id:2}| {self.address:^40}| {self.city:^17}| {self.state:^6}| {self.zip_code:^5} | {self.weight:^3}kg(s) | {self.deadline:^10} | {self.time_delivered.strftime('%I:%M %p'):^13} | {self.notes}"
