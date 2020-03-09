# '''
# Linked List hash table key/value pair
# '''

class LinkedPairIterator:
    def __init__(self, head):
        self.head = head
        self.node = head

    def __next__(self):
        if self.node == None:
            raise StopIteration
        else:
            to_return = self.node
            self.node = self.node.next
            return to_return



class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __iter__(self):
        return LinkedPairIterator(self)


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Part 1: Hash collisions should be handled with an error warning.

        Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        idx = self._hash_mod(key)
        node = self.storage[idx]
        # Collision detected
        if  node is None:
            # add a new list to store elements
            self.storage[idx] = LinkedPair(key, value)
            return

        last = node
        for pair in node:
            last = pair
            if pair.key == key:
                pair.value = value
                return  # overwrit an existing element
        # element wasn't already present, add it
        last.next = LinkedPair(key, value)



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        idx = self._hash_mod(key)
        l = self.storage[idx]
        if l is None:
            return  # no such element
        prev = None

        for node in l:
            if node.key == key:
                # link previous element and next element to delete this element
                if prev is not None:
                    prev.next = node.next
                # else this is the head element, set the head to the next element
                else:
                    self.storage[idx] = node.next
            prev = node


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        idx = self._hash_mod(key)
        l = self.storage[idx]

        if l is None:
            return # no such element

        for node in l:
            if node.key == key:
                return node.value



    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        old_storage = self.storage
        self.storage = [None] * self.capacity
        for l in old_storage:
            if l is None:
                continue # no such linked list as this spot
            for node in l:
                self.insert(node.key, node.value)


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

#    print(ht.storage)

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
