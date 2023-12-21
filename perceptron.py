import os
import pickle
import random
from typing import List, Tuple

from create_shapes import create_random_circle, create_random_rectangle
from ppm_maker import create_ppm_image


class Perceptron:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.sample_size_of_training_data = 100
        self.training_data_seed = 69  # nice
        self.weights = [[0.0] * width for _ in range(height)]
        # arbitarily choosed this bais
        self.bais = 1

    def check_with_weights(self, input_image: List[Tuple[int, int]]):
        # doing dot product of each cell with it's weight
        total = 0
        for point in input_image:
            total += self.weights[point[0]][point[1]] * 1.0

        # for i in range(self.height):
        #     for j in range(self.width):
        #         total += self.weights[i][j] * input_image[i][j]

        # not equal to as at start let's have total = 0 as not activated
        if total > self.bais:
            return True
        else:
            return False

    def adjust_weights(self, input_image: List[Tuple[int, int]], shape_name: str):
        if shape_name == "circle":
            for point in input_image:
                self.weights[point[0]][point[1]] -= 1
        elif shape_name == "rectangle":
            for point in input_image:
                self.weights[point[0]][point[1]] += 1
        else:
            raise Exception("Unexpected shape")

        # I did this because at the end, i am just adding 1 to where the points are
        # as in activation function and rest of the points are zero which won't change
        # weights

        # if shape_name == "circle":
        #     for i in range(self.height):
        #         for j in range(self.width):
        #             self.weights[i][j] = self.weights[i][j] + input_image[i][j]
        # elif shape_name == "rectangle":
        #     for i in range(self.height):
        #         for j in range(self.width):
        #             self.weights[i][j] = self.weights[i][j] - input_image[i][j]
        # else:
        #     raise Exception("Unexpected shape")

        return

    def training_on_random(self):
        repeat_training = 100

        for m in range(repeat_training):
            random.seed(self.training_data_seed)
            total_times_adjusted = 0

            for _ in range(self.sample_size_of_training_data):
                random_rect = create_random_rectangle(self.height, self.width)
                if self.check_with_weights(random_rect) == False:
                    total_times_adjusted += 1
                    self.adjust_weights(random_rect, "rectangle")
                random_circle = create_random_circle(self.height, self.width)
                if self.check_with_weights(random_circle) == True:
                    total_times_adjusted += 1
                    self.adjust_weights(random_circle, "circle")

            print(
                f"Iteration {m + 1}: Total times adjusted {total_times_adjusted} out of {repeat_training * 2}"
            )

            if total_times_adjusted == 0:
                break

        return

    def load_trained_data(self, filename: str):
        if os.path.isfile(f"./{filename}") == False:
            raise Exception(
                "FileNotFound: Make sure file is at same directory as of rest of the files, also be sure to give extension"
            )

        with open(f"./{filename}", "rb") as f:
            self.weights = pickle.load(f)

        return

    def dump_trained_data(self, filename: str):
        with open(f"./{filename}", "wb") as f:
            pickle.dump(self.weights, f)

        print(f"Save data at {filename}")
        return

    def get_final_weight_as_image(self):
        create_ppm_image(self.weights)
        return
