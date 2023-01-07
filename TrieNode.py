class TrieNode:
    def __init__(self):
        self.is_file = False
        self.children = {}
        self.content = ""
        self.is_binary = False
        self.is_buffer = False
        self.queue = []