Class Solution:
	'''
	Idea: First do a BFS on the word graph. The purpose of the BFS is two-fold. First, we calculates the distance from beginWord to all words in wordList. If endWord is not in the same connected component as beginWord, we return []. We store the result in a dictionary dist. In particular, we know that the distance d from beginWord to endWord (dist[endWord]) is exactly the length of the shortest transformation sequences from beginWord to endWord. Secondly, we can construct the adjacency list representation of the word graph with the BFS, which is a dictionary graph that maps each word to its set of neighbors in the word graph. This facilitates the construction of the shortest transformation sequences using DFS in the next step, because the value corresponding to a particular key will be the set of all the neighbors of the key.

Next, we do a DFS starting from beginWord. We can use the dictionary dist to prune most of the search spaces, because we already know that each of the shortest transformation sequences is of length dist[endWord] = d, so that the transformation sequence is of the form [beginWord, word1, word2, ..., endWord], where dist[beginWord] = 0, dist[word1] = 1, dist[word2] = 2, ..., dist[endWord] = d. Therefore, we only need to make recursive DFS calls on those neighbors of the current word which are of distance dist[currentWord]+1 to the beginWord. We initialize two lists, res which holds the result, and tmp which holds all the words in the current DFS subtree. Once the DFS call is on endWord, we create a shallow copy of tmp and append it to res, and return
	'''
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        def dfs(word):
            tmp.append(word)
            if word == endWord:
                res.append(list(tmp))
                tmp.pop()
                return 
            if word in graph:
                for nei in graph[word]:
                    if dist[nei] == dist[word]+1:
                        dfs(nei)
            tmp.pop()

        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        q = collections.deque([(beginWord, 0)])
        dist = {}
        graph = collections.defaultdict(set)
        seen = set([beginWord])
        while q:
            u, d = q.popleft()
            dist[u] = d
            for i in range(len(u)):
                for alph in alphabets:
                    if alph != u[i]:
                        new = u[:i]+alph+u[i+1:]
                        if new in wordSet:
                            graph[u].add(new)
                            graph[new].add(u)
                            if new not in seen:
                                q.append((new, d+1))
                                seen.add(new)
        if endWord not in dist:
            return []
        res = []
        tmp = []
        dfs(beginWord)
        return res 

		
