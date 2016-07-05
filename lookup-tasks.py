# task lookup
# usage:
#  $ python lookup-tasks.py <db.csv> <task-list.csv>
#
# windows command for generating task list:
#  > tasklist /FO csv | sort > "%userprofile%\desktop\tasks.csv"

# TODO: make these input params
db_path = 'task-db.csv'
task_list_path = 'tasks-scrosby.csv'

db = dict()

print "Reading in task DB"
first_line = True
db_file = open(db_path, 'r')
for entry in db_file:
    if first_line:
        first_line = False
    elif len(entry.strip()) == 0:
        pass
    else:
        parts = entry.strip().split(',')
        name = parts[0]
        req = parts[1]
        desc = parts[2]
        if name in db.keys():
            print "ERROR: task " + name + " is a duplicate"
        else:
            db[name] = "req: " + str(req) + " desc: " + desc
            print "db[" + name + "] - " + str(db[name])
db_file.close()

print "--------------------"
print "Reading in task list"
first_line = True
task_list_file = open(task_list_path, 'r')
for entry in task_list_file:
    if first_line:
        first_line = False
    elif len(entry.strip()) == 0:
        pass
    else:
        parts = entry.split(',')
        name = parts[0][1:-1]
        if name in db.keys():
            print str(name) + " - " + str(db[name])
        else:
            print str(name) + " - UNKNOWN"
task_list_file.close()
