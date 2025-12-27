from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def build_tree(self, arr):
        if not arr: return None
        root = TreeNode(arr[0])
        queue = deque([root])
        i = 1
        while queue and i < len(arr):
            node = queue.popleft()
            if i < len(arr): 
                node.left = TreeNode(arr[i]) if arr[i] is not None else None
                if node.left: queue.append(node.left)
                i += 1
            if i < len(arr): 
                node.right = TreeNode(arr[i]) if arr[i] is not None else None
                if node.right: queue.append(node.right)
                i += 1
        return root

    def level_order(self, root):
        if not root: return []
        queue = deque([root])
        result = []
        while queue:
            node = queue.popleft()
            result.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return result

    def print_level_visual(self, root):
        """Print tree in a visually balanced form."""
        if not root:
            return

        from collections import deque
        
        # Step 1: BFS to get all levels
        levels = []
        queue = deque([(root, 0)])
        current_level = 0
        current_nodes = []

        while queue:
            node, level = queue.popleft()
            if level != current_level:
                levels.append(current_nodes)
                current_nodes = []
                current_level = level
            current_nodes.append(node.val if node else None)

            if node:
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))
        levels.append(current_nodes)

        # Step 2: print with spacing
        max_level = len(levels)
        max_width = 2 ** max_level

        for depth, level_nodes in enumerate(levels):
            spacing = max_width // (2 ** depth)
            line = (" " * (spacing // 2)).join(
                [' ' if v is None else str(v) for v in level_nodes]
            )
            print(" " * (spacing // 2) + line)

    def print_top_down(self, root):
        """Print the tree in a balanced top-down (triangle) format."""
        if not root:
            print("<empty tree>")
            return
        
        # Get tree height
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))
        
        h = height(root)
        max_width = 2 ** h  # widest number of slots

        # BFS levels (including None children to preserve structure)
        from collections import deque
        result = []
        queue = deque([root])
        for _ in range(h):
            level = []
            next_q = deque()
            while queue:
                node = queue.popleft()
                level.append("" if node is None else str(node.val))
                if node:
                    next_q.append(node.left)
                    next_q.append(node.right)
                else:
                    next_q.append(None)
                    next_q.append(None)
            result.append(level)
            queue = next_q

        # Print top-down with spacing
        for depth, level in enumerate(result):
            spacing = max_width // (2 ** depth)
            line = (" " * (spacing // 2)).join(
                val.center(2) for val in level
            )
            print(" " * (spacing // 2) + line)

# Main
class invertTree:
    def use_BFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return root

# Usage
if __name__ == "__main__":

    def parse_value(x):
        if x.lower() == "none":
            return None
        return int(x)

    raw = input("Input your array here: ")

    # clean input
    raw = raw.replace("[", "").replace("]", "").replace(",", " ")
    arr = [parse_value(x) for x in raw.split()]

    tree = TreeNode()
    root = tree.build_tree(arr)

    print("\nInput Tree:")
    tree.print_top_down(root)
    print("Input level order:", tree.level_order(root))

    sol = invertTree()
    inverted = sol.use_BFS(root)

    print("\nInverted Tree:")
    tree.print_top_down(inverted)
    print("Output level order:", tree.level_order(inverted))