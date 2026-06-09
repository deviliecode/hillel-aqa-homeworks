class Romb:

    def __setattr__(self, key, value):

        if key == "side_a" and value <= 0:
            raise AttributeError(f"Значення сторони {key} повинно бути більше 0.")

        if key == "angle_a" and value == 0:
            raise AttributeError(f"Кут не може бути 0")

        if key == "angle_b" and value + self.angle_a != 180:
            raise AttributeError("Сума кутів angle_a та angle_b НЕ дорівнює 180")

        super().__setattr__(key, value)

    def __str__(self):
        return f"Дані цього ромба —— Сторна А = {self.side_a}, Кут А = {self.angle_a}, Кут Б = {self.angle_b}"


romb_1 = Romb()

romb_1.side_a = 10
romb_1.angle_a = 90
romb_1.angle_b = romb_1.angle_a

print(romb_1)