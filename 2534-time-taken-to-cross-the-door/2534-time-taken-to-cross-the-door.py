class Solution(object):
    def timeTaken(self, arrival, state):
        """
        :type arrival: List[int]
        :type state: List[int]
        :rtype: List[int]
        """
        t, cur = 0, 0
        prev = None
        answer = [0] * len(arrival)
        entering, exiting = collections.deque(), collections.deque()
        arrival = collections.deque(arrival)
        state = collections.deque(state)
        length = len(arrival)
        while cur < length or (entering or exiting):
            while arrival and arrival[0] <= t:
                cur_arr, cur_state = arrival.popleft(), state.popleft()
                entering.append([cur, cur_arr, cur_state]) if cur_state == 0 else exiting.append([cur, cur_arr, cur_state])
                cur += 1
            if not (entering or exiting):
                prev = None
                t += 1
                continue
            if not prev:
                if exiting:
                    idx, arr, st = exiting.popleft()
                else:
                    idx, arr, st = entering.popleft()
                answer[idx] = t
                prev_t, prev_action = t, st
                prev = True
            elif prev_action == 0:
                if entering:
                    idx, arr, st = entering.popleft()
                else:
                    idx, arr, st = exiting.popleft()
                answer[idx] = t
                prev_t, prev_action = t, st
                prev = True
            elif prev_action == 1:
                if exiting:
                    idx, arr, st = exiting.popleft()
                else:
                    idx, arr, st = entering.popleft()
                answer[idx] = t
                prev_t, prev_action = t, st
                prev = True
            else:
                if entering and exiting:
                    if entering[0][1] < exiting[0][1]:
                        idx, arr, st = entering.popleft()
                    else:
                        idx, arr, st = exiting.popleft()
                elif entering:
                    idx, arr, st = entering.popleft()
                else:
                    idx, arr, st = exiting.popleft()
                answer[idx] = t
                prev_t, prev_action = t, st
                prev = True
            t += 1
        return answer