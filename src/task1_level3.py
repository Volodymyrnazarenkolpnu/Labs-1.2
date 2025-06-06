"""Lab4 task1 level3 variant3"""

class Node():
    """Nodes for AVL tree"""
    def __init__(self, value, priority, left = None, right = None, height = 1):
        self.value = value
        self.priority = priority
        self.left = left
        self.right = right
        self.height = height

def get_balance(node):
    """Returns a balance of a node"""
    if node is None:
        return 0
    return (get_height(node.left) - get_height(node.right))

def get_height(node):
    """Returns a height of a node"""
    if node is None:
        return 0
    return node.height

def print_queue(root, lst = None):
    """inorder queue print"""
    if lst is None:
        lst = []
    if root is None:
        return lst
    lst = print_queue(root.left, lst)
    lst.append((root, root.value))
    lst = print_queue(root.right, lst)
    return lst

def dequeue(root):
    """dequeue an element from the tree"""
    lst = []
    curr = root
    while True:
        lst.append(curr)
        if curr.left is not None:
            curr = curr.left
        else:
            lst.pop()
            rem = curr
            if len(lst) == 0:
                root = curr.right
            else:
                curr = lst.pop()
                curr.left = rem.right
            break
    for el in lst[::-1]:
        el.height = max(get_height(root.left), get_height(root.right)) + 1
        if get_balance(root) > 1:
            if get_balance(el.left) >= 0:
                root = right_rotate(root)
        if get_balance(root) > 1:
            if get_balance(el.left) < 0:
                root.left = left_rotate(root)
                root = right_rotate(root)
        if get_balance(root) < -1:
            if get_balance(el.right) <= 0 and root.right.priority != root.priority:
                root = left_rotate(root)
        if get_balance(root) < -1:
            if get_balance(el.left) > 0:
                root.right = right_rotate(root.right)
                root = left_rotate(root)
    return (rem, root)

def enqueue(root, node):
    """Enqueues an element into a tree"""
    if root is None:
        return node
    if node.priority > root.priority:
        root.left = enqueue(root.left, node)
    if node.priority <= root.priority:
        root.right = enqueue(root.right, node)
    root.height = max(get_height(root.left), get_height(root.right)) + 1
    if get_balance(root) > 1:
        if node.priority > root.left.priority:
            return right_rotate(root)
    if get_balance(root) > 1:
        if node.priority < root.left.priority:
            root.left = left_rotate(root)
            return right_rotate(root)
    if get_balance(root) < -1:
        if node.priority < root.right.priority and root.right.priority != root.priority:
            return left_rotate(root)
    if get_balance(root) < -1:
        if node.priority > root.right.priority:
            root.right = right_rotate(root.right)
            return left_rotate(root)
    return root

def left_rotate(node):
    """rotate tree left"""
    y = node.right
    t = y.left
    y.left = node
    node.right = t
    node.height = max(get_height(node.left), get_height(node.right)) + 1
    y.balance = max(get_height(node.left), get_height(node.right)) + 1
    return y

def right_rotate(node):
    """rotate tree right"""
    x = node.left
    t = x.right
    x.right = node
    node.left = t
    node.balance = max(get_height(node.left), get_height(node.right)) + 1
    x.balance = max(get_height(node.left), get_height(node.right)) + 1
    return x

def print_tree(root):
    """show tree in a console graphically"""
    if root is not None:
        root_left = root.left
        root_right = root.right
        data_rt = str(root.value) + ","
        priority_rt = str(root.priority)
        len_rt = len(data_rt + priority_rt)
        if root_right is None:
            len_r = 4
            data_r = "None"
            priority_r = ""
        else:
            data_r = str(root_right.value) + ","
            priority_r = str(root_right.priority)
            len_r = len(data_r + priority_r)
        if root_left is None:
            len_l = 4
            data_l = "None"
            priority_l = ""
        else:
            data_l = str(root_left.value) + ","
            priority_l = str(root_left.priority)
            len_l = len(data_l + priority_l)
        len_gen = max((len_l * 2 + 1),(len_r * 2 + 1),(len_rt + 1))
        line1 = "" + " " * len_gen
        line2 = "" + " " * len_gen
        line3 = "" + " " * len_gen
        start = len(line1) // 2 - len(data_rt + priority_rt) // 2
        line1 = line1[:start] + data_rt + priority_rt + line1[start + len_rt:]
        line2 = line2[:len_gen // 4] + "/" + line2[len_gen // 4 + 1:len_gen // 2 + len_gen // 4] + "\\" + line2[len_gen // 2 + len_gen // 4 + 1:]
        line3 = line3[:len_gen // 4 - len_l // 2] + data_l + priority_l + " " + line3[len_gen // 4 - len_l // 2 + len_l + 1: 3 * len_gen // 4 - len_r // 2] + data_r + priority_r + line3[ 3 * len_gen // 4 - len_r // 2 + len_r:]
        print(line1)
        print(line2)
        print(line3)

def import_tree():
    """imports a tree from a file"""
    file = open("tree.txt", "r", encoding="utf8")
    root = file.readline()
    args = root.split(",")
    l_arg = args[-1].split("\n")
    args[-1] = l_arg[0]
    root_1 = Node(int(args[0]), int(args[1]))
    node_list = [root_1]
    while True:
        line = file.readline()
        if len(line) <= 1:
            break
        args = line.split(",")
        l_arg = args[-1].split("\n")
        args[-1] = l_arg[0]
        new_nodes = []
        while len(args) >= 2:
            if args[0] == "None":
                new_nodes.append(None)
                args.pop(0)
            else:
                new_nodes.append(Node(int(args[0]),int(args[1])))
                args.pop(0)
                args.pop(0)
            next_nodes = []
        for node in node_list:
            node.left = new_nodes[0]
            if new_nodes[0] is not None:
                next_nodes.append(new_nodes[0])
            new_nodes.pop(0)
            node.right = new_nodes[0]
            if new_nodes[0] is not None:
                next_nodes.append(new_nodes[0])
            new_nodes.pop(0)
        node_list = next_nodes[:]
    return root_1
def mainloop():
    """the main loop of the app"""
    root_1 = Node(1, 1)
    root_1 = enqueue(root_1, Node(1,1))
    root_1 = enqueue(root_1, Node(0,0))
    root_1 = enqueue(root_1, Node(3,3))
    root_1 = enqueue(root_1, Node(2,2))
    root_1 = enqueue(root_1, Node(4,4))
    rem, root_1 = dequeue(root_1)
    print(print_queue(root_1))
    traversal_list = [root_1]
    while True:
        command = input()
        if command == "enqueue":
            try:
                print("Enter Node data:")
                data = input()
                data = int(data)
                print("Enter Node priority:")
                priority = input()
                priority = int(priority)
                traversal_list[0] = enqueue(traversal_list[0], Node(data, priority))
            except ValueError:
                print("Priority and Data mush be a whole numbers")
        elif command == "dequeue":
            rem, traversal_list[0] = dequeue(traversal_list[-1])
            print((rem, rem.value))
        elif command == "print":
            if len(traversal_list) != 0:
                print_tree(traversal_list[-1])
            else:
                print("Tree is clear")
        elif command == "left":
            if traversal_list[-1].left is not None:
                traversal_list.append(traversal_list[-1].left)
                print_tree(traversal_list[-1])
            else:
                print("Cannot show children of nonexistent node")
        elif command == "right":
            if traversal_list[-1].right is not None:
                traversal_list.append(traversal_list[-1].right)
                print_tree(traversal_list[-1])
            else:
                print("Cannot show children of nonexistent node")
        elif command == "back":
            if len(traversal_list) >= 2:
                traversal_list.pop()
                print_tree(traversal_list[-1])
            else:
                print("Top reached")
        elif command == "import":
            root = import_tree()
            traversal_list = [root]
            print_tree(traversal_list[-1])
mainloop()
