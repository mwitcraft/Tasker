import sys
import pickle

# Define task object
class Task:
    def __init__(self, name, dueDate):
        self.name = name
        self.dueDate = dueDate

# Create array to store tasks
tasks = []
# If a task file alreay exists, open it
with open('outfile', 'rb') as fp:
    tasks = pickle.load(fp)

# If program is just run, list the tasks
if len(sys.argv) == 1:
    for task in tasks:
        print("\t" + task.name + " \t\t" + task.dueDate)
# If program is run with add as 2nd argument, add that task
elif sys.argv[1] == "add":
    curTask = Task(sys.argv[2], sys.argv[3])
    tasks.append(curTask)
else:
    print("Unsupported for now")

# Write array to file    
with open('outfile', 'wb') as fp:
    pickle.dump(tasks, fp)
