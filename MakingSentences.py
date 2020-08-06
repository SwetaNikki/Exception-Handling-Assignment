"""
2. Implement a Python program to generate all sentences where subject is in
["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
["Baseball","cricket"].

"""

subject = ['Americans', 'Indians']
verb = ['Play', 'watch']
objects = ['Baseball','cricket']

for sub in subject :
    for v in verb:
        for ob in objects:
            print(sub+" "+v+" "+ob+".")

            
