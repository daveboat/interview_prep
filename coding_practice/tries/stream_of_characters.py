"""
LC1039 - Stream of characters

Implement the StreamChecker class as follows:

    StreamChecker(words): Constructor, init the data structure with the given words.
    query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to
    newest, including this letter just queried) spell one of the words in the given list.

Example:

StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
streamChecker.query('a');          // return false
streamChecker.query('b');          // return false
streamChecker.query('c');          // return false
streamChecker.query('d');          // return true, because 'cd' is in the wordlist
streamChecker.query('e');          // return false
streamChecker.query('f');          // return true, because 'f' is in the wordlist
streamChecker.query('g');          // return false
streamChecker.query('h');          // return false
streamChecker.query('i');          // return false
streamChecker.query('j');          // return false
streamChecker.query('k');          // return false
streamChecker.query('l');          // return true, because 'kl' is in the wordlist

Note:

    1 <= words.length <= 2000
    1 <= words[i].length <= 2000
    Words will only consist of lowercase English letters.
    Queries will only consist of lowercase English letters.
    The number of queries is at most 40000.

------------------------------------------------------------------------------------------------------------------------

Note: my solution here works but runs out of time on leetcode
"""


class Node:
    def __init__(self, complete=False):
        self.d = dict()
        self.complete = complete


def insert(node, word):
    # if our word is empty
    if len(word) == 0:
        node.complete = True
        return

    if word[0] not in node.d:  # if the appropriate node doesn't exist, make it
        node.d[word[0]] = Node()
    insert(node.d[word[0]], word[1:])  # continue with inserting down the line


class StreamChecker(object):
    # so we do this with a trie. each time a new letter comes in, check it against either the root of the trie or
    # the current node, depending on various factors. The question is what happens for a case like
    # ['abc', 'bef'] and the stream is ['a', 'b', 'e']. I guess, for every letter entered, we have to at least
    # be checking and keeping track of two nodes...
    #
    # what about cases like ['abcdef', 'bcdefg', 'cdefgh'] with stream ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
    # wouldn't you have to track three different nodes? In general, I suppose you have to be keeping track of
    # an arbitrary number of nodes. So how about this:
    # - we have a list of nodes that are currently being tracked
    # - Each time a letter comes in, we add the child of the root node that contains the letter if it exists.
    # - Each time a letter comes in, for each node in the list, if the letter is in its children, we update
    # that node to its child node. If that letter isn't in any child node, we remove that node from the list
    # - Return true if any node in the list has a complete flag after adding/updating/removing
    def __init__(self, words):
        """
        :type words: List[str]
        """
        # make our trie
        self.root = Node()
        for word in words:
            insert(self.root, word)

        # list of currently active nodes
        self.node_list = []

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        complete_found = False

        # first, check through the node list to see if the letter is in any of their children nodes. if it is,
        # update that node to its child. otherwise, remove it from the list.
        for i in range(len(self.node_list) - 1, -1, -1):
            if letter in self.node_list[i].d:
                self.node_list[i] = self.node_list[i].d[letter]
                if self.node_list[i].complete:
                    complete_found = True
            else:
                self.node_list.pop(i)

        # second, if the trie root has the letter in its children, add that node to the list
        if letter in self.root.d:
            if self.root.d[letter].complete:
                complete_found = True
            self.node_list.append(self.root.d[letter])

        return complete_found


if __name__ == '__main__':
    """
    ["StreamChecker", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query",
     "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query",
     "query", "query", "query", "query", "query", "query", "query"]
    [[["ab", "ba", "aaab", "abab", "baa"]], ["a"], ["a"], ["a"], ["a"], ["a"], ["b"], ["a"], ["b"], ["a"], ["b"], ["b"],
     ["b"], ["a"], ["b"], ["a"], ["b"], ["b"], ["b"], ["b"], ["a"], ["b"], ["a"], ["b"], ["a"], ["a"], ["a"], ["b"],
     ["a"], ["a"], ["a"]]
     [null,false,false,false,false,false,true,true,true,true,true,false,false,true,true,true,true,false,false,false,true,true,true,true,true,true,false,true,true,true,false]
             a     a     a     a     a     b    a    b   a     b    b
    """

    words = ["ab", "ba", "aaab", "abab", "baa"]
    S = StreamChecker(words)
    queries = [["a"], ["a"], ["a"], ["a"], ["a"], ["b"], ["a"], ["b"], ["a"], ["b"], ["b"],
     ["b"], ["a"], ["b"], ["a"], ["b"], ["b"], ["b"], ["b"], ["a"], ["b"], ["a"], ["b"], ["a"], ["a"], ["a"], ["b"],
     ["a"], ["a"], ["a"]]

    for q in queries:
        # print(S.query(q[0]))
        S.query('a')
        S.query('b')
        S.query('a')
        S.query('b')
        S.query('x')
        S.query('x')
