from data import fetch_data
from HashTable import HashTable
from Btree import BTree

def main():
    # Fetch data
    data = fetch_data()
    print(data.head())
    # Initialize hash table and B-tree
    hash_table = HashTable()
    b_tree = BTree()

    # Example: Insert data into hash table and B-tree
    # Depending on your implementation, you might loop through the data
    # and insert it into these structures.
    for index, row in data.iterrows():
        hash_table.insert(row['some_key'], row)
        b_tree.insert(row['some_key'], row)

    # Additional code for testing, analysis, etc.

if __name__ == "__main__":
    main()
