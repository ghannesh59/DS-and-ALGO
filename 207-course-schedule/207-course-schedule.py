class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_dic={}
        for i in range(numCourses):
            pre_dic[i]=[]
        for course,prereq in prerequisites:
            pre_dic[course].append(prereq)
        visited=set()
        def dfs(curr):
            if curr in visited:
                return False
            if len(pre_dic[curr])==0:
                return True
            visited.add(curr)
            for i in pre_dic[curr]:
                if not dfs(i): return False
            visited.remove(curr)
            pre_dic[curr]=[]
            return True
        for i in pre_dic:
            if not dfs(i): return False
        return True