class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    users_list = []
    for data in people_data:
        name = data["name"]
        age = data["age"]

        person = Person(name, age)
        users_list.append(person)

    for data in people_data:
        name = data["name"]
        person = Person.people[name]
        if "wife" in data and data["wife"] is not None:
            person.wife = Person.people.get(data["wife"])
        if "husband" in data and data["husband"] is not None:
            person.husband = Person.people.get(data["husband"])
    return users_list
