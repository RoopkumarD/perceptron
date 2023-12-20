from perceptron import Perceptron

perceptron = Perceptron(200, 200)

for _ in range(10):
    perceptron.training_on_random()


perceptron.get_final_weight_as_image()
