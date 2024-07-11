class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {i : [] for i in range(numCourses)}
        
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)
            
        visited = set()
        def dfs(course) -> bool:
            print(course, prereqs[course])
            if prereqs[course] == []:
                return True
            if course in visited:
                return False
            
            visited.add(course)
            
            for prereq in prereqs[course]:
                if not dfs(prereq):
                    return False
                
            visited.remove(course)
            prereqs[course] = [] # optimization so we don't have to keep checking things we already know are valid
            
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True