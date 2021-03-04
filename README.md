# Gradient Generator
Generate random but beautiful gradients in a super simple way.

## Demo
[![gradient](https://gradient-demo.lab.9roads.red/gradient?w=640&h=480)](https://gradient-demo.lab.9roads.red)
You can check out more examples [here](https://gradient-demo.lab.9roads.red)

## Features
- Super simple usage

## Current limitations
- No way to choose colors
- PNG only

## Installation
``` console
$ pip install gradient-generator
```

## Usage
``` python
from gradient_generator import generate_gradient

image = generate_gradient(640, 480)

image
<_io.BytesIO object at 0x10ce70040>

with open('test.png', 'wb') as f:
	f.write(image.getbuffer())

```

## Support
If you need help or found a bug, consider opening an issue on the project.


## Licence
The source code for this project is licensed under the MIT license, which you can find in the MIT-LICENSE.txt file.
