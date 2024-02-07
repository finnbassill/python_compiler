class Node:
    def __init__(self, data):
        self.data = data
    
    def append_data(self, data):
        self.data.append(data)

    # Method to set data of the node
    def set_data(self, data):
        self.data = data

    # Method to get data of the node
    def get_data(self):
        return self.data

class Node_Exit(Node):
    def __init__(self, data):
        super().__init__(data)

class Node_Expr(Node):
    def __init__(self, data):
        super().__init__(data)