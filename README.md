# icomp-py
This is an open source image compressor built with python

## Usage Instructions

To use the image compressor, you need to call the `compress_image` function from the `icomp` module. The function takes two arguments:
1. `input_image_path`: The path to the input image file.
2. `output_image_path` (optional): The path where the compressed image will be saved. If not provided, the compressed image will be saved in the current directory with the same name as the input image.

Example usage:
```python
from icomp import compress_image

# Compress an image and save it in the current directory
compress_image('path/to/input/image.jpg')

# Compress an image and save it to a specified output path
compress_image('path/to/input/image.png', 'path/to/output/compressed_image.png')
```

## Examples

### Compressing a JPEG image
```python
compress_image('path/to/input/image.jpg')
```

### Compressing a PNG image
```python
compress_image('path/to/input/image.png', 'path/to/output/compressed_image.png')
```

### Compressing a BMP image
```python
compress_image('path/to/input/image.bmp')
```

## Complex Algorithm for Faster and Better Compression

The `compress_image` function uses a complex algorithm that is faster and provides better compression results. This algorithm supports all types of image formats and does not rely on external libraries.
