#!/usr/bin/env python3
from factory.absfactory import ExamCenter

factory = ExamCenter()

check_1 = factory.person_age("student")
print(check_1)

check_2 = factory.person_age("non_student")
print(check_2)
