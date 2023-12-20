from typing import List

from create_shapes import create_random_circle, create_random_rectangle
from ppm_maker import create_ppm_image


class Perceptron:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.training_iterations = 100
        self.weights = [[0.0] * width for _ in range(height)]
        # arbitarily choosed this bais
        self.bais = 0

    def check(self, input_image: List[List[float]]):
        # doing dot product of each cell with it's weight
        total = 0

        for i in range(self.height):
            for j in range(self.width):
                total += self.weights[i][j] * input_image[i][j]

        # not equal to as at start let's have total = 0 as not activated
        if total > self.bais:
            return True
        else:
            return False

    def adjust_weights(self, input_image: List[List[float]], shape_name: str):
        for i in range(self.height):
            for j in range(self.width):
                if shape_name == "circle":
                    self.weights[i][j] = self.weights[i][j] + input_image[i][j]
                elif shape_name == "rectangle":
                    self.weights[i][j] = self.weights[i][j] - input_image[i][j]

        return

    def training_on_random(self):
        total_wrong = 0

        for _ in range(self.training_iterations):
            random_rect = create_random_rectangle(self.height, self.width)
            if self.check(random_rect) == True:
                total_wrong += 1
                self.adjust_weights(random_rect, "rectangle")

            random_circle = create_random_circle(self.height, self.width)
            if self.check(random_circle) == False:
                total_wrong += 1
                self.adjust_weights(random_circle, "circle")

        print(
            "Total percent it predictated wrong is",
            (total_wrong / (self.training_iterations * 2)) * 100,
        )
        return

    def get_final_weight_as_image(self):
        create_ppm_image(self.weights)
        return
