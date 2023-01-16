class Solution:
    def prefixCount(self, N, Q, li, query):
        # code here
        trie = {}
        end = '*'

        # dfs search of the words
        def recur(curTrie):
            if not curTrie:
                return 0

            count = 0
            if end in curTrie:
                count += curTrie[end]

            for char in curTrie:
                if char == end:
                    continue
                count += recur(curTrie[char])

            return count

        # generate trie
        for word in li:
            cur = trie
            for char in word[0]:
                if char not in cur:
                    cur[char] = {}
                cur = cur[char]
            if end not in cur:
                cur[end] = 0
            cur[end] += 1

        result = []
        cache = {}
        # count prefix
        for word in query:
            if word[0] in cache:
                result.append(cache[word[0]])
                continue

            cur = trie
            for char in word[0]:
                if char not in cur:
                    cur = None
                    break
                cur = cur[char]

            if not cur:
                word[0] = 0
                result.append(0)
                continue

            cache[word[0]] = recur(cur)
            result.append(cache[word[0]])

        return result

