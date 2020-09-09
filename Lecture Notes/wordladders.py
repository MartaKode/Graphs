import string

words = set()

with open("words.txt") as f:
    for word in f:
        words.add(word.lower().strip())

# print("zzzzzz" in words)
# print("hello" in words)
# import sys; sys.exit(0)

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

cache = {}

def get_neighbors(word):
    if True or word not in cache:
        neighbors = []

        for w in words:
            if len(w) != len(word):
                continue

            diffs = 0

            for i in range(len(w)):
                if w[i] != word[i]:
                    diffs += 1

                if diffs > 1:
                    break

            if diffs == 1:
                neighbors.append(w)

            cache[word] = neighbors

    return cache[word]

# print(get_neighbors('sail'))
# import sys; sys.exit(0)

def get_neighbors_2(word): # word = 'sail'
    word_letters = list(word) # word_letters = ['s', 'a', 'i', 'l']

    neighbors = []

    for i in range(len(word)): # i from 0 to 3
        for l in string.ascii_lowercase: # l from a ... z
            candidate_letters = list(word_letters) # make a copy of word_letters = ['s', 'a', 'i', 'l']
            candidate_letters[i] = l # ['s','a','i','l'] -> ['a','a','i','l'] --> change 1 letter 
            candidate = "".join(candidate_letters) # turn it back into a string

            if candidate != word and candidate in words: # is "aail" in the dictionary?
                neighbors.append(candidate)
    
    return neighbors

# print(get_neighbors_2("sail"))
# print(get_neighbors_2("ball"))
# import sys; sys.exit(0)

def bfs(begin_word, end_word):
    visited = set()
    q = Queue()

    q.enqueue([begin_word])

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]

        if v not in visited:
            visited.add(v)

            if v == end_word:
                return path

            # for neighbor in get_neighbors(v):
            for neighbor in get_neighbors_2(v):
                q.enqueue(path + [neighbor]) # Makes a new list --> same as 3 lines below
                # path_copy = list(path)
                # path_copy.append(neighbor)
                # q.enqueue(path_copy)

print(bfs("sail", "boat"))