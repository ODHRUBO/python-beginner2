student={
    "name":"seiam",
    "subject":{
        "c":70,
        "c++":80,
        "java":90,
        "python":95
    }
}
print(student.keys())
print(list(student.keys()))
print(student.values())
print(student.items())

print(student.get("subject"))
print(student.get("subject2"))#print none,bcos it does not exist
student.update({"city":"Mymensingh"})
print(student)

