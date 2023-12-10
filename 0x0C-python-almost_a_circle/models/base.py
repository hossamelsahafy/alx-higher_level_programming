#!/usr/bin/python3
"""Define Base class"""
import json
import csv
import turtle
import random


class Base:
    """Define  class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save list of objects to a file"""
        if list_objs is None or len(list_objs) == 0:
            list_objs = []
        else:
            file_name = f"{cls.__name__}.json"
            json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            with open(file_name, "w") as i:
                i.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if not isinstance(json_string, str):
            raise TypeError("json_string must be str")
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """hat returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        file_name = f"{cls.__name__}.json"
        instance = []
        try:
            with open(file_name, "r") as i:
                json_string = i.read()
                list_dic = cls.from_json_string(json_string)
                for dic in list_dic:
                    instance.append(cls.create(**dic))
        except FileNotFoundError:
            pass
        return instance

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save list of objects to a file in CSV format"""
        if list_objs is None or len(list_objs) == 0:
            list_objs = []
        else:
            file_name = f"{cls.__name__}.csv"
            with open(file_name, "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                for obj in list_objs:
                    writer.writerow([obj.id] + list(obj.to_dictionary().values()))

    @classmethod
    def load_from_file_csv(cls):
        """Load list of instances from a CSV file"""
        file_name = f"{cls.__name__}.csv"
        instance = []
        try:
            with open(file_name, "r") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    id, *attributes = map(int, row)
                    if cls.__name__ == "Rectangle":
                        dummy = cls(1, 1, 0, 0, id)
                    elif cls.__name__ == "Square":
                        dummy = cls(1, 0, 0, id)
                    dictionary = dict(zip(dummy.to_dictionary().keys(), attributes))
                    instance.append(cls.create(**dictionary))
        except FileNotFoundError:
            pass
        return instance

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw all the Rectangles and Squares"""
        window = turtle.Screen()
        window.bgcolor("black")  # Change the background color to black

        t = turtle.Turtle()
        t.speed(1)  # Set the speed of the turtle

        colors = [
            "red",
            "green",
            "blue",
            "yellow",
            "purple",
            "orange",
        ]  # List of colors to choose from

        # Define the starting position
        start_x = -200
        start_y = 200

        for rect in list_rectangles + list_squares:
            t.penup()
            t.goto(start_x, start_y)  # Move the turtle to the starting position
            t.pendown()

            t.color(
                random.choice(colors)
            )  # Choose a random color for each rectangle/square
            t.begin_fill()  # Start filling the shape with the chosen color

            for _ in range(2):
                t.forward(rect.width)
                t.right(90)
                t.forward(rect.height)
                t.right(90)

            t.end_fill()  # End filling the shape

            # Update the starting position for the next shape
            start_x += rect.width + 50
            if start_x > 200:
                start_x = -200
                start_y -= 200

        t.hideturtle()
        turtle.done()
