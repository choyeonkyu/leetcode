class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = [False] * len(rooms)
        visited[0] = True
        def dfs(room_num):
            for j in rooms[room_num]:
                if not visited[j]:
                    visited[j] = True
                    dfs(j)
                
        for i in rooms[0]:
            visited[i] = True
            dfs(i)
            
        return all(visited)
    
    
        