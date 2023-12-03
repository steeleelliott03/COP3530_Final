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
        parent.insert_item(item_to_move_up)

        self.items = self.items[mid_point + 1:]
        self.children = self.children[mid_point + 1:]

        return new_node

    def insert_item(self, item):
        self.items.append(item)
        self.items.sort(key=lambda x: x['key'])

    def search(self, condition, results):
        print(f"Searching in Node with items: {[item['key'] for item in self.items]}")
        for item in self.items:
            if condition(item['value']):
                results.append(item['value'])
        if not self.is_leaf:
            for child in self.children:
                child.search(condition, results)
class BTree:
    def __init__(self, order=4):
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

    def search(self, condition):
        results = []
        self.root.search(condition, results)
        return results

