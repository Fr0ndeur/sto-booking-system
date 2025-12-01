import itertools

def main():
    # Example usage of itertools to create a Cartesian product
    colors = ['red', 'green', 'blue']
    sizes = ['S', 'M', 'L']
    
    product = itertools.product(colors, sizes)
    
    for item in product:
        print(item)