from dataclasses import dataclass


@dataclass
class Car:
    position: int
    speed: int


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arrivals = []
        road = [Car(car[0], car[1]) for car in zip(position, speed)]
        road.sort(key=lambda x: x.position, reverse=True)

        for car in road:
            arrives = (target - car.position) / car.speed

            if len(arrivals) == 0 or arrivals[-1] < arrives:
                arrivals.append(arrives)

        return len(arrivals)
