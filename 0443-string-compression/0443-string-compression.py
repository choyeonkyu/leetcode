class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        read = 0
        write = 0
        n = len(chars)
        while read < len(chars):
            char = chars[read]
            count = 0
            while read < n and chars[read] == char:
                read += 1
                count += 1
            chars[write] = char
            write += 1
            if count > 1:
                chars[write: write + len(list(str(count)))] = list(str(count))
                write += len(list(str(count)))
        chars = chars[:write+1]
        return write