class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self

    def __repr__(self) -> str:
        return f"<Person: {self.name}>"


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()

    for person_data in people:
        Person(person_data["name"], person_data["age"])

    for person_data in people:
        person_obj = Person.people[person_data["name"]]

        if "wife" in person_data and person_data["wife"] is not None:
            wife_name = person_data["wife"]
            wife_obj = Person.people[wife_name]
            person_obj.wife = wife_obj

        if "husband" in person_data and person_data["husband"] is not None:
            husband_name = person_data["husband"]
            husband_obj = Person.people[husband_name]
            person_obj.husband = husband_obj

    return list(Person.people.values())
    '#final'
