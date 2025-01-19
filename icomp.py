import os

def compress_image(input_image_path, output_image_path=None):
    # Read the input image file
    with open(input_image_path, 'rb') as input_file:
        input_data = input_file.read()

    # Compress the image data
    compressed_data = compress_data(input_data)

    # Determine the output path
    if output_image_path is None:
        output_image_path = os.path.join(os.getcwd(), os.path.basename(input_image_path))

    # Save the compressed image to the output path
    with open(output_image_path, 'wb') as output_file:
        output_file.write(compressed_data)

def compress_data(data):
    # Implement a complex compression algorithm (e.g., Huffman coding)
    frequency = {}
    for byte in data:
        if byte in frequency:
            frequency[byte] += 1
        else:
            frequency[byte] = 1

    # Build the Huffman tree
    huffman_tree = build_huffman_tree(frequency)

    # Generate Huffman codes
    huffman_codes = generate_huffman_codes(huffman_tree)

    # Compress the data using Huffman codes
    compressed_data = bytearray()
    for byte in data:
        compressed_data.extend(huffman_codes[byte])

    return compressed_data

def build_huffman_tree(frequency):
    # Build the Huffman tree based on the frequency of bytes
    from heapq import heappush, heappop, heapify
    heap = [[weight, [symbol, ""]] for symbol, weight in frequency.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return heap[0]

def generate_huffman_codes(huffman_tree):
    # Generate Huffman codes from the Huffman tree
    huffman_codes = {}
    for pair in huffman_tree[1:]:
        huffman_codes[pair[0]] = bytearray(pair[1], 'utf-8')
    return huffman_codes
