def run_length_encode(data_block):
    """
    Performs Run-Length Encoding on a single block of quantized DCT coefficients.

    Args:
        data_block (list[int]): A list of 64 integers representing one block that has been
                                quantized and zig-zag scanned.

    Returns:
        list[tuple]: A list of RLE symbols. Each symbol is either ('EOB',)
                     or (num_zeros, value).
    """
    # Example: [52, -7, 0, 0, 3, 0, -2, 0, ..., 0]
    # -> [(0, 52), (0, -7), (2, 3), (1, -2), ('EOB',)]
    #
    # Hint: Iterate through the block. If you see a zero, increment a counter.
    # If you see a non-zero value, create a symbol with the current zero count
    # and the value, then reset the counter. Do not forget the EOB symbol.
    return []
