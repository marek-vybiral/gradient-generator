import io
import random
import math
from PIL import Image

COLOR_COMPONENT_SIMILARITY_THRESHOLD = 50
COLOR_BRIGHTNESS_THRESHOLD = 0.8
COLOR_DARKNESS_THRESHOLD = 0.2


def _get_distance(a_x, a_y, b_x, b_y):
    return math.sqrt(math.pow(a_x - b_x, 2) + math.pow(a_y - b_y, 2))


def _mix_colors(colors, weights):
    assert len(colors) == len(weights)

    components = [[], [], []]

    for c in colors:
        for i, v in enumerate(c):
            components[i].append(v)

    color = [0, 0, 0]

    weights_sum = sum(weights)

    for i, v in enumerate(components):
        mixed_c = 0
        for ci, c in enumerate(v):
            mixed_c += c * weights[ci]

        mixed_c = mixed_c / weights_sum

        color[i] = int(mixed_c)

    return tuple(color)


def _get_random_color():
    def get_components():
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    while True:
        color = get_components()

        if COLOR_DARKNESS_THRESHOLD < (color[0] + color[1] + color[2]) / (255 * 3) < COLOR_BRIGHTNESS_THRESHOLD:
            break

    return color


def _get_different_color(ref_color):
    is_similar = True

    while is_similar:
        new_color = _get_random_color()

        is_similar = False
        for i, v in enumerate(new_color):
            if abs(v - ref_color[i]) < COLOR_COMPONENT_SIMILARITY_THRESHOLD:
                is_similar = True

    return new_color


def _get_random_color_pt(w, h):
    axis = random.choice(['x', 'y'])

    if axis == 'x':
        return random.randint(0, w), 0, _get_random_color()

    return 0, random.randint(0, h), _get_random_color()


def generate_gradient(width: int, height: int):
    w = int(width / 10)
    h = int(height / 10)

    pt = _get_random_color_pt(w, h)
    color_pts = [pt, (w - pt[0], h - pt[1], _get_different_color(pt[2]))]

    data = []

    for x in range(h):
        for y in range(w):
            colors = [pt[2] for pt in color_pts]

            distances = [_get_distance(x, y, pt[0], pt[1]) for pt in color_pts]

            min_dist = min(distances)
            max_dist = max(distances)

            weights = [min_dist + max_dist - d for d in distances]

            color = _mix_colors(colors, weights)
            data.append((color[0], color[1], color[2], 255))

    im = Image.new('RGBA', (w, h))
    im.putdata(data)

    im = im.resize((width, height), Image.ANTIALIAS)

    output = io.BytesIO()
    im.save(output, 'png')

    output.seek(0)
    return output
