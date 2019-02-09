import numpy as np

from bs4 import BeautifulSoup
import urllib.request

class Employee:
    num_emp = 1
    name = ""
    family = ""
    salary = 0
    dept = ""

    def __init__(self, name, family, salary, dept):
        self.name = name
        self.family = family
        self.salary += salary
        self.dept = dept

    def avg_salary(self):
        return self.salary/self.num_emp;

class FullTimeEmployee (Employee):
    hours = 40

Andrew = Employee("Andrew", "Knowles", 19, "CS")
Andrew.num_emp=3
print(Andrew.avg_salary())
Susan = FullTimeEmployee("Andrew", "Knowles", 19, "CS")

print(np.random.random((2,3)))



with urllib.request.urlopen('https://en.wikipedia.org/wiki/Deep_learning') as response:
    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all('a'):
        print(anchor.get('href', '/'))
    for anchor in soup.find_all('title'):
        print(anchor)

def most_common(vector):
    arr = {}
    for x in vector:
        if x not in arr:
            arr[x] = 1
        else:
            arr[x] +=1
    most_common = max(arr.keys())
    print( most_common, "appears", arr[most_common], "time/s")

vector = np.random.randint(0, 20, size=15)
most_common(vector)