class Solution:
    def twoEditWords(queries, dictionary):
        
        res = []
        for query in queries:
            for word in dictionary:
                diff = 0
                for c1, c2 in zip(query, word):
                    if c1 != c2:
                        diff += 1

                        if diff > 2:
                            break
                if diff <= 2:
                    res.append(query)
                    break
        return res



        