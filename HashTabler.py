# Create hash table
class HashTable:
    # default size is ten buckets
    def __init__(self, size=10):
        self.outside_list = []
        # add empty list to every bucket
        for i in range(size):
            self.outside_list.append([])

    # Insert package into hash table using the package ID as key and package object as value.
    def insert(self, key, value):
        # find bucket
        index = hash(key) % len(self.outside_list)
        # pull bucket
        inside_list = self.outside_list[index]
        # insert key and value as a list, into the bucket's list
        key_value = [key, value]
        # add to bucket
        inside_list.append(key_value)
        # update bucket
        self.outside_list[index] = inside_list

    # Look up package information in hash table using the package ID.
    def lookup(self, key):
        try:
            key = int(key)
            # find the bucket that the package should be in
            index = hash(key) % len(self.outside_list)
            inside_list = self.outside_list[index]
            # linear search bucket for the package
            for entry in inside_list:
                if key == entry[0]:
                    # return package
                    return entry[1]
            print("there is no package associated with that ID")
        except ValueError:
            print("package IDs are integers")

    # Remove package from hash table using the package ID
    def remove_item(self, key):
        index = hash(key) % len(self.outside_list)
        inside_list = self.outside_list[index]
        for entry in enumerate(inside_list):
            if key == entry[1][0]:
                inside_list.remove(entry[1])
                return
        print("key not found")

    # Return the size of hash table
    def size_of_hashtable(self):
        counter = 0
        # count the length of every list in every bucket
        for list in self.outside_list:
            counter += len(list)
        return counter
