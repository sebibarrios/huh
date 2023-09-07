class Person:
    def __init__(self, name, ssn, dob):
        """
        Initializes a new Person instance.
        
        Args:
        name (str): The name of the person.
        ssn (str): The social security number of the person, formatted as XXX-XX-XXXX.
        dob (str): The date of birth of the person, formatted as MM-DD-YYYY.
        """
        self.name = name
        self.ssn = ssn
        self.dob = dob

    def person_details(self):
        """
        Returns the details of the person in the specified format as a string.
        """
        return f"Name: {self.name}\nSSN: {self.ssn}\nDate of Birth: {self.dob}\n"


class Task:
    def __init__(self, title, description, due_date, completed, required_taskers):
        """
        Initializes a new Task instance.
        
        Args:
        title (str): The title of the task.
        description (str): The description of the task.
        due_date (str): The due date of the task.
        completed (bool): Indicates whether the task is completed.
        required_taskers (int): The number of taskers required for the task.
        """
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed
        self.required_taskers = required_taskers
        self.taskers = []

    def add_taskers(self, person):
        """
        Adds a person to the tasker's list.
        
        Args:
        person (Person): An instance of the Person class to be added to the tasker's list.
        """
        if isinstance(person, Person):
            self.taskers.append(person)
        else:
            print("Invalid input. Please provide an instance of the Person class.")

    def remove_taskers(self, person):
        """
        Removes a person from the tasker's list.
        
        Args:
        person (Person): An instance of the Person class to be removed from the tasker's list.
        
        Returns:
        bool: Indicates whether the removal was successful.
        """
        if person in self.taskers:
            self.taskers.remove(person)
            return True
        else:
            return False

    def total_taskers(self):
        """
        Returns the total number of assigned taskers.
        
        Returns:
        int: The total number of assigned taskers.
        """
        return len(self.taskers)

    def task_details(self):
        """
        Prints the details of the task and taskers in the specified format.
        """
        tasker_details = "\n".join([tasker.person_details() for tasker in self.taskers])
        print(f"Task Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nCompleted: {self.completed}\nRequired Taskers: {self.required_taskers}\nTasker Details:\n{tasker_details}")
