class Solution:

    def __init__(self):
        self.course_to_prereqs: dict[int, set[int]] = {}
        self.can_finish = set()

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        for prereq_list in prerequisites:
            cur_course, cur_prereq = prereq_list
            if cur_course not in self.course_to_prereqs:
                self.course_to_prereqs[cur_course] = set()
            self.course_to_prereqs[cur_course].add(cur_prereq)
            
        for course in range(numCourses):
            #print(f"checking {course=}")
            if not self.canFinishSingle(course, set(), ""):
                return False

        return True
    
    def canFinishSingle(self, course: int, already_examined:set[int], spacer: string) -> bool:
        
        # print(f"{spacer}-canFinishSingle {course=} {already_examined=}")
        
        if course in already_examined:
            return False
        """
        A requires B + C
        """

        current_prereqs = set()
        if course in self.course_to_prereqs:
            current_prereqs = self.course_to_prereqs[course]

        
        already_examined.add(course)
        for prereq in current_prereqs:
            if prereq in self.can_finish:
                continue
            if not self.canFinishSingle(prereq, already_examined, spacer + " "):
                return False

        self.can_finish.add(course)
        return True

