from typing import Callable, TypeVar
from dataclasses import dataclass
def sum_numbers(numbers: list[int]) -> int:
    return sum([n for n in numbers if n % 2 == 0])

def sum_numbers_if(predicate_fn: Callable[[int], bool], numbers: list[int]) -> int:
    return sum([n for n in numbers if predicate_fn(n)])

@dataclass
class Person:
    name: str
    age: int

    def is_adult(self) -> bool:
        return self.age >= 18

class PeopleService:
    def __init__(self, people: list[Person] = None) -> None:
        if people is None:
            people = []
        self._people = people

    def add(self, person: Person) -> None:
        self._people.append(person)

    def filter(self, predicate_fn: Callable[[Person], bool]) -> list[Person]:
        return [person for person in self._people if predicate_fn(person)]


class ItemsService[T]:
    def __init__(self, items: list[T] = None) -> None:
        if items is None:
            items = []
        self._items = items

    def add(self, item: T) -> None:
        self._items.append(item)

    def filter(self, predicate_fn: Callable[[T], bool]) -> list[T]:
        return [item for item in self._items if predicate_fn(item)]

def main() -> None:
    # print(sum_numbers([10, 11, 20, 21]))
    # print(sum_numbers_if(lambda x: x % 2 == 0, [10, 11, 20, 21]))
    # print(sum_numbers_if(lambda x: x > 10, [10, 11, 20, 21]))

    # ps = PeopleService()
    # ps.add(Person(name="John", age=17))
    # ps.add(Person(name="Ann", age=29))
    # ps.add(Person(name="Tim", age=39))
    # print(ps.filter(lambda person: person.is_adult()))

    items_service = ItemsService[Person]()
    items_service.add(Person(name="John", age=17))
    items_service.add(Person(name="Ann", age=29))
    items_service.add(Person(name="Tim", age=39))
    print(items_service.filter(lambda person: person.is_adult()))

    items_service = ItemsService[int]([11, 23])
    items_service.add(21)
    items_service.add(28)
    items_service.add("ala")
    print(items_service.filter(lambda n: n % 2 == 0))


if __name__ == '__main__':
    main()