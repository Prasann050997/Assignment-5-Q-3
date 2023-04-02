class student:

    def init(self,Name,Rollno):
        self._name=Name
        self._rollno=Rollno
    def set_name(self,x):
        self._name=x
        pass
    def get_name(self):
        return self._name
    pass
    def set_rollno(self,x):
        self._rollno=x
        pass
    def get_rollno(self):
        return self._rollno
    pass
name=input("enter name")
rollno=int(input("enter roll no"))
s=student()
s.set_name(name)
print(s.get_name())
#s.get_name()
s.set_rollno(rollno)
print(s.get_rollno())