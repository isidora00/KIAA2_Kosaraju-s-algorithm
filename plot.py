import matplotlib.pyplot as plt

def plot_coordinates(file_path, save_path):
    # Lists to store x and y coordinates
    x_coordinates = []
    y_coordinates = []

    # Read data from the text file
    with open(file_path, 'r') as file:
        for line in file:
            # Split each line into x and y coordinates
            x, y = map(int, line.split())
            x_coordinates.append(x)
            y_coordinates.append(y)

    # Plot the coordinates
    plt.plot(x_coordinates, y_coordinates, linestyle='-')
    plt.title('Vreme izvrsavanja Kosaraju algoritma')
    plt.xlabel('V+E')
    plt.ylabel('t')
    plt.grid(True)
    plt.ylim(0,60)
    plt.savefig(save_path, format='png')
    plt.show()

# Replace 'your_file.txt' with the actual path to your text file
file_path = 'data2.txt'
save_path = 'vremena_izvrsavanja2.png'
plot_coordinates(file_path,save_path)