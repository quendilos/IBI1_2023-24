class IBI_Students_Data (object): 
# set a class named IBI_Students_Data
    def __init__ (self, students_name, major, socre_for_code_portfolio, score_for_group_project, exam_score):
# define it with several attributes
        self.students_name = students_name
        self.major=major
        self.score_for_code_portfolio=socre_for_code_portfolio
        self.score_for_group_project=score_for_group_project
        self.exam_score=exam_score
    def print_all_details(self):
#log the data in the class and define how to print it
        student_details=(self.students_name,self.major,self.score_for_code_portfolio,self.score_for_group_project,self.exam_score)
        print(student_details)
student_example_name = IBI_Students_Data('example_name','BMI',95,95,95)
student_example_name.print_all_details()