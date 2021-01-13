from typing import List, Optional


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        d = {e.id: e for e in employees}

        def f(i):
            e = d[i]
            return e.importance + sum(map(f, e.subordinates))
        return f(id)

    # def getImportance(self, employees: List['Employee'], id: int) -> int:
    #     employee = self.__get_subordinates(employees, id)
    #     if not employee:
    #         return 0
    #     subordinates = employee.subordinates
    #     if len(subordinates) == 0:
    #         return employee.importance
    #     subordinates_importance = employee.importance
    #     for item in subordinates:
    #         subordinates_importance = subordinates_importance + self.getImportance(employees, item)
    #     return subordinates_importance
    #
    # def __get_subordinates(self, employees: List['Employee'], id: int) -> Optional[Employee]:
    #     for item in employees:
    #         if item.id == id:
    #             return item
    #     return None


employee1 = Employee(1, 5, [2, 3])
employee2 = Employee(2, 3, [])
employee3 = Employee(3, 3, [])
print(Solution().getImportance([employee1, employee2, employee3], 1))
