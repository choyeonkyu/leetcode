class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        hash_1, hash_2 = {}, {}
        for i in word1:
            hash_1[i] = hash_1.get(i, 0) + 1
        for i in word2:
            hash_2[i] = hash_2.get(i, 0) + 1
        if set(hash_1.keys()) != set(hash_2.keys()) or set(hash_1.values()) != set(hash_2.values()) or hash_1.values().sort() != hash_2.values().sort():
            return False

        temp_1, temp_2 = [], []
        for key, val in hash_1.items():
            temp_1.append(key)
            temp_1.append(val)
        for key, val in hash_2.items():
            temp_2.append(key)
            temp_2.append(val)
        print(sorted(hash_1.values()))
        return sorted(hash_1.values()) == sorted(hash_2.values())