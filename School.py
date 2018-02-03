# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 11:05:44 2017

@author: Ariel Domingo Catli
"""
import random

#This is the module
class Building:
    def __init__(self):
        self.__rooms = []
        
    def __iter__(self):
        self.__index = -1
        return self
    
    def __next__(self):
        if self.__index >= len(self.__rooms)-1:
            raise StopIteration()
        self.__index += 1
        return self.__rooms[self.__index]
    
    def add_room(self, room):
        self.__rooms.append(room)

class Room:
    def __init__(self, name, number, key_length):
        self.name = name
        self.number = number
        self.door_key = self.__generate_door_key(key_length)
        self.assistant = Assistant("N/A", "N/A")
    
    
    
    def __str__(self):
        return (f"Room Number: {self.number}\n"+ 
              f"Room Name: {self.name}\n"+
              f"Assistant: {self.assistant.name}\n"+
              f"Door Key: {self.door_key}\n")
        
    def __generate_door_key(self, key_length):
        allowed_chars = ['1','2','4','d','#','%','@']
        key = ""
        for i in range(0,10):
            key += random.choice(allowed_chars)
        return key
    
    @property
    def door_key(self):
        return self.__door_key
    
    @door_key.setter
    def door_key(self, key):
        self.__door_key = key
    
    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, number):
        if(number<=1000):
            self.__number = number
        else:
            print("The room number should be equal to or below 1000.")
            self.__number = "N/A"
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
        
    @property
    def assistant(self):
        return self.__assistant
    @assistant.setter
    def assistant(self, assistant):
        self.__assistant = assistant
    
class Class_room(Room):
    def __init__(self, name, number, key_length, assigned_professor):
        Room.__init__(self, name, number, key_length)
        self.__assigned_professor = assigned_professor
    
    def assign_subject(self, subject):
        self.__subject = subject
        
    def __str__(self):
        return (Room.__str__(self))+ f"Subject: {self.__subject.name}\n" 
        + f"Enrolled Students: {self.__subject.enrolled}\n"
        + f"Professor: {self.__assigned_professor}\n"


class Assistant:
    def __init__(self, name, assigned_room):
        self.name = name
        self.assigned_room = assigned_room
    
    def assign_room(self, room):
        self.room = room
        
class Subject:
    def __init__(self, name, num_enrolled):
        self.name = name
        self.enrolled = num_enrolled