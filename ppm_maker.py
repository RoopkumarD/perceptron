import array
import math
from typing import List

from utils import bezier_gradient

DIM_PPM_SCALER = 2


def create_ppm_image(input: List[List[float]]):
    lowest_num = 1000000000000
    biggest_num = -100000000000

    for line in input:
        for i in line:
            if i < lowest_num:
                lowest_num = i

            if i > biggest_num:
                biggest_num = i

    height = len(input) * DIM_PPM_SCALER
    width = len(input[0]) * DIM_PPM_SCALER

    # using P6 than P3 as saving info in bytes and not ascii
    image_header = f"P6 {width} {height} 255\n"

    # not 2x2 but continuous linear array
    image = array.array("B", [0, 0, 0] * width * height)

    for i in range(height):
        for j in range(width):
            # this is because we want the 2x2 in 1d as our image array is 1d
            # (1,0) -> 3 in 1d so if we have 2d matrix with 3 * 3
            # 1 * 3 + 0 = 3
            # later multiplied by 3 as in above, the rgb channels are not separate list
            # but in same array, so [0,0,255] * 2 * 2 => [0,0,255,0,0,255,0,0,255,0,0,255]
            index = 3 * (i * width + j)

            # since we have scaled the image, now we want the find the color associated with it
            # and those cells will have same color as that of which expanded
            # thus dividing by the expansion to get the input
            # if input -> 2 * 2 and we expand by 2. Then image is 2 * 2 width and 2 * 2 height
            # now (0,0) (0,1) (1,0) (1,1) all are based of (0,0) in original input
            color = bezier_gradient(
                input[math.floor(i / DIM_PPM_SCALER)][math.floor(j / DIM_PPM_SCALER)],
                lowest_num,
                biggest_num,
            )
            for k in range(3):
                image[index + k] = color[k]

    with open("./image.ppm", "wb") as f:
        f.write(bytearray(image_header, "ascii"))
        image.tofile(f)

    print("Created image at ./image.ppm")

    return
