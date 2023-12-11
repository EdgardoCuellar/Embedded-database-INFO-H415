import matplotlib.pyplot as plt

def create_histogram(file_path):
    # Read data from file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Extract values and labels from each line
    data = [line.split() for line in lines]

    # Transpose data for easier handling
    data = list(map(list, zip(*data)))

    # Extract values and labels
    values_A = list(map(float, data[0]))
    values_B = list(map(float, data[1]))
    labels = data[2]

    # Set up the positions for the bars
    x = range(len(labels))
    width = 0.35  # Width of the bars

    # Create side-by-side histograms
    plt.bar(x, values_A, width, label='Value A')
    plt.bar([i + width for i in x], values_B, width, label='Value B')

    # Add labels and title
    plt.xlabel('Pairs')
    plt.ylabel('Values')
    plt.title('Comparison of Value A and Value B')
    plt.xticks([i + width / 2 for i in x], labels)

    # Add legend
    plt.legend()

    # Show the plot
    plt.savefig('histogram.png')
    plt.show()

# Example usage with a file named 'data.txt'
create_histogram('output_gps.txt')
