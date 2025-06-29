#1-> Write a Python program to update a value in a dictionary. 


student = {
    "name": "jaypalsinh",
    "age": 20,
    "roll_no": 9,
    "course": "b.c.a",
}

print(student)

student["age"] = 22

print(student)

#2-> Write a Python program to merge two lists into one dictionary using a loop. 



keys = ["name", "age", "city" ]
values = ["jaypalsinh", 25, "somnath"]

merged_dict = {}

for i in range(len(keys)):
    merged_dict[keys[i]] = values[i]

print(merged_dict)
