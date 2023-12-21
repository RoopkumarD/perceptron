# Simple Perceptron

This project involves creating a perceptron designed to distinguish between rectangles and circles. 

It draws inspiration from the [First Ancient Neural Network in C | Tsoding
Daily](https://youtu.be/WEk_grxrCcg?si=5UUN7EHnWKAbuujR) and [Future Computers Will Be Radically Different (Analog Computing)
| Veritasium](https://youtu.be/GVsUOuSjvcg?si=ZZX_0x8V-YlOdLNz).

Keep in mind that this perceptron is not intended for serious applications; rather, it reflects my efforts to implement
concepts learned in a CS50AI class.

A bias is arbitrarily chosen, and after several iterations, the perceptron becomes capable of distinguishing between circles
and rectangles within its training dataset.

## Getting Started

```python
from perceptron import Perceptron

perceptron = Perceptron(200, 200) # width and height of frame

perceptron.training_on_random() # it trains the data on shapes
perceptron.get_final_weight_as_image() # creates ppm image of final weight
perceptron.dump_trained_data("trained_data.bin") # dumps the weights in a file
```

The `perceptron.py` file encompasses the perceptron class and includes the training segment. The perceptron is trained on
shapes generated randomly by selecting an arbitrary seed and creating rectangles and circles accordingly. The
`create_shapes.py` file contains the implementation for creating rectangles and circles.

The `ppm_maker.py` file includes the code for generating a ppm image from perceptron weights to visualize the weights. The
`utils.py` file contains the implementation of the bezier gradient function, which assigns colors to each pixel in the ppm
image based on the value of the corresponding weight.

The `main.py` file is used to test the perceptron.

## Future Plans

I plan to read the original perceptron paper and implement its concepts in future iterations of this project.
