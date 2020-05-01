#coding:utf-8
groupmates = [
 {
     "name": u"Василий",
     "group": "912-2",
     "age": 19,
     "marks": [4, 3, 5, 5, 4]
 },
 {
     "name": u"Анна",
     "group": "912-1",
     "age": 18,
     "marks": [3, 2, 3, 4, 3]
 },
 {
     "name": u"Георгий",
     "group": "912-2",
     "age": 19,
     "marks": [3, 5, 4, 3, 5]
 },
 {
     "name": u"Валентина",
     "group": "912-1",
     "age": 18,
     "marks": [5, 5, 5, 4, 5]
 }
]


def print_students(students):
    print u"Имя студента".ljust(15), \
          u"Группа".ljust(8), \
          u"Возраст".ljust(8), \
          u"Оценки".ljust(20)
    for student in students:
        print \
              student["name"].ljust(15), \
              student["group"].ljust(8), \
              str(student["age"]).ljust(8), \
              str(student["marks"]).ljust(20)
    print "\n"

def average_marks(students):
    newgroupmates=[];
    ave = float(raw_input("VVEDITE ZNACHENYE "))
    for student in groupmates:
        ave_std = float(sum(student["marks"]))/float(len(student["marks"]))
        if (ave_std>ave):
            newgroupmates.append(student)
    print_students(newgroupmates)

print_students(groupmates)
average_marks(groupmates)
