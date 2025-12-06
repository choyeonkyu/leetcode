class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        def check_diff(curr, cand):
            cnt = 0
            for i in range(8):
                if curr[i] == cand[i]:
                    continue
                else:
                    cnt += 1
            if cnt == 1:
                return True
            else:
                return False
        q = collections.deque()
        q.append((startGene, 0))
        visited = set()
        visited.add(startGene)
        while q:
            curr, level = q.popleft()
            if curr == endGene:
                return level
            for cand in bank:
                if cand not in visited and check_diff(curr, cand):
                    q.append((cand, level + 1))
                    visited.add(cand)
        return -1