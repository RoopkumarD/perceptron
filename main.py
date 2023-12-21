from perceptron import Perceptron

perceptron = Perceptron(200, 200)

perceptron.training_on_random()
perceptron.get_final_weight_as_image()
perceptron.dump_trained_data("trained_data.bin")
