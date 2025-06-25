def hill_climbing():
    # Define the fitness function (the function we want to maximize)
    def fitness(x):
        return -1 * (x - 3)**2 + 9  # Peak is at x = 3

    current = 0       # Starting point
    step = 0.1        # How much we move in each step

    while True:
        next_val = current + step   # Try moving to the right

        # If the next value is better (higher fitness), move there
        if fitness(next_val) > fitness(current):
            current = next_val
        else:
            break  # No improvement, stop climbing

    print("Best solution found:", current)

hill_climbing()
