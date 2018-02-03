from School import *

print("\n<---CREATING A NEW ROOM---->")
science_classroom = Class_room("Ariel Catli Room", 0, 20, "Prof. Horacio Delevine")
science_classroom.assistant = Assistant("Maria Leonora Teresa",science_classroom)
science_classroom.assign_subject(Subject("Science",40))
print(science_classroom)

print("\n<----ASSIGNING A NEW ASSISTANT---->")
science_classroom.assistant = Assistant("Lady Ada Byron",science_classroom)
print(science_classroom)

print("\n<---CREATING A NEW ROOM---->")
faculty_room = Room("The Faculty Room", 25, 30)
faculty_room.assistant = Assistant("Julia Childs", faculty_room)
print(faculty_room)

print("\n<---ADDING ROOMS TO BUILDING A---->")
building_a = Building()
building_a.add_room(science_classroom)
building_a.add_room(faculty_room)

print("\n<----ROOMS IN BUILDING A--->")
for room in building_a:
    print(room)