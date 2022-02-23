#multi-level inheritance
class family():
    def fam_name(self):
        print("This is our family")
class fam_members(family):
    def members(self):
        print("in our family there are 5 members")

class list(fam_members):
    def first_name(self):
        print("The first name is:Raghava Rao")
    def second_name(self):
        print("The second name is:usha rani")
    def third_name(self):
        print("The third name is:varshini")
    def fourth_name(self):
        print("The fourth name is:pravallika")

fam_list=list()
fam_list.fam_name()
fam_list.members()
fam_list.first_name()
fam_list.second_name()
fam_list.third_name()
fam_list.fourth_name()