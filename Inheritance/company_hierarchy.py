class Employee:
    def __init__(self, name, empid, salary):
        self.name = name 
        self.empid = empid
        self.salary = salary

    def cal_salary(self):
        return self.salary
    
    def display_info(self):
        print(f"Name : {self.name}, Employee id : {self.empid}, salary : {self.salary}")


class Manager(Employee):
    def __init__(self, name, empid, salary, department, teamsize):
        super().__init__(name, empid, salary)
        self.department = department
        self.teamsize = teamsize

    def assign_task(self, task):
        print(f"Task '{task}' assigned")

    def manage_team(self):
        print("managing team")

class TeamLead(Manager):
    def __init__(self, name, empid, salary, department, teamsize, projectassign):
        super().__init__(name, empid, salary, department, teamsize)
        self.projectassign = projectassign
    
    def monitorprogress(self):
        print("Monitor progress")

    def reviewteam(self):
        print("Reviewing team")

class TeamMember(TeamLead):
    def __init__(self, name, empid, salary, department, teamsize, projectassign, taskassign, progress_stat):
        super().__init__(name, empid, salary, department, teamsize, projectassign)
        self.taskassign = taskassign
        self.progress_stat = progress_stat

    def workontask(self, task):
        print(f"Working on task '{task}'")

    def updateprogress(self, task, status):
        print(f"Task '{task}', progress = '{status}")

employee = Employee("John Doe", 1001, 60000)
employee.display_info()

manager = Manager("Alice Smith", 2001, 80000, "HR", 5)
manager.assign_task("Recruitment")
manager.manage_team()

team_lead = TeamLead("Bob Johnson", 3001, 100000, "IT", 10, "Software Project")
team_lead.monitorprogress()
team_lead.reviewteam()

team_member = TeamMember("Eva Williams", 4001, 70000, "IT", 10, "Software Project", ["Code Refactoring"], "50%")
team_member.workontask("Code Refactoring")
team_member.updateprogress("Code Refactoring", "70%")
