class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        transpose = [[] for _ in range(len(grid))]
        hash_table = {}
        for i, elem_i in enumerate(grid):
            str_elem_i = ''.join(str(elem_i))
            hash_table[str_elem_i] = hash_table.get(str_elem_i, 0) + 1
            for j, elem_j in enumerate(elem_i):
                transpose[j].append(elem_j)
        hash_table_tr = {}
        for i in transpose:
            str_elem = ''.join(str(i))
            hash_table_tr[str_elem] = hash_table_tr.get(str_elem, 0) + 1
        answer = 0
        for i in hash_table:
            if i in hash_table_tr:
                answer += hash_table[i] * hash_table_tr[i]
        return answer