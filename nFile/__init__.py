class People:
    def __init__(self, id, name, occupation):
        self.id = id
        self.name = name
        self.occupation = occupation

    def introduce(self):
        print("%s is %s and have id is %d\n" % (self.name, self.occupation, int (self.id)))

try :
    Employee_file = open("Employee.csv", "r")
except FileNotFoundError :
    print("Cannot Openfile")
arr = []
line = Employee_file.readlines()
for i  in range(len(line) - 1) :
    tmp = line [i +1].split(",")
    ppl = People(tmp[0],tmp[1],tmp[2])
    arr.append(ppl)
for i in range(len(arr)) :
    arr[i].introduce()
Employee_file.close()
