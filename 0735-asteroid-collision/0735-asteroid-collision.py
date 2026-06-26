class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        answer = []
        for i in asteroids:
            # sign = '+' if i > 0 else '-'
            if len(answer) == 0:
                answer.append(i)
                continue
            if i > 0:
                answer.append(i)
            elif i < 0 and answer[-1] * i < 0:
                if abs(i) < answer[-1]:
                    continue # need to check
                elif abs(i) > answer[-1]:
                    while answer and answer[-1] * i < 0 and abs(i) > answer[-1]:
                        answer.pop()
                    if answer and answer[-1] * i < 0 and abs(i) < answer[-1]:
                        continue
                    elif answer and answer[-1] * i < 0 and abs(i) == answer[-1]:
                        answer.pop()
                        continue
                    else:
                        answer.append(i)
                else:
                    answer.pop()
                    continue # need to check
            else:
                answer.append(i)
        return answer