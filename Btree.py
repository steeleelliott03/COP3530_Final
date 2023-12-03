class BTreeNode:
    def __init__(self, items=None, children=None, is_leaf=True):
        self.items = items if items is not None else []
        self.children = children if children is not None else []
        self.is_leaf = is_leaf

    def split(self, parent, item):
        new_node = BTreeNode(self.items[:], self.children[:], self.is_leaf)
        mid_point = len(new_node.items) // 2
        item_to_move_up = new_node.items[mid_point]  # Define item_to_move_up
        if isinstance(item_to_move_up, str):
            item_to_move_up = {'key': item_to_move_up, 'value': None}
        elif isinstance(item_to_move_up, dict) and 'value' not in item_to_move_up:
            item_to_move_up['value'] = None
        parent.insert_item(item_to_move_up)

        self.items = self.items[mid_point + 1:]
        self.children = self.children[mid_point + 1:]

        return new_node

    def insert_item(self, item):
        # Find if the key already exists
        for existing_item in self.items:
            if existing_item['key'] == item['key']:
                existing_item['values'].append(item['value'])
                return
        # If key does not exist, insert new item with a list of values
        self.items.append({'key': item['key'], 'values': [item['value']]})
        self.items.sort(key=lambda x: x['key'])


    def search(self, key, results):
        # Find the first key greater than or equal to the given key
        i = 0
        while i < len(self.items) and key > self.items[i]['key']:
            i += 1

        # If the found key is equal, add its value to the results
        if i < len(self.items) and self.items[i]['key'] == key:
            results.extend(self.items[i]['values'])

        # If the node is not a leaf, continue searching in the child
        if not self.is_leaf:
            if i < len(self.children):
                self.children[i].search(key, results)

class BTree:
    def __init__(self, order=100):
        self.root = BTreeNode()
        self.order = order

    def insert(self, key, value):
        item = {'key': key, 'value': value}  # Create the item dictionary
        root = self.root
        if len(root.items) == self.order - 1:
            new_root = BTreeNode(children=[root])
            root.split(new_root, item)  # Pass the item directly, not as a keyword argument
            self.root = new_root
        self._insert_non_full(self.root, key, value)


    def _insert_non_full(self, node, key, value):
        if node.is_leaf:
            node.insert_item({'key': key, 'value': value})
        else:
            i = 0
            while i < len(node.items) and key > node.items[i]['key']:
                i += 1
            if i < len(node.children):
                if len(node.children[i].items) == self.order - 1:
                    self._split_child(node, i)
                    if key > node.items[i]['key']:
                        i += 1
                self._insert_non_full(node.children[i], key, value)

    def _split_child(self, node, i):
        new_node = node.children[i].split(node, node.children[i].items[self.order // 2])
        node.children.insert(i + 1, new_node)

    def search(self, key):
        results = []
        self.root.search(key, results)
        return results


