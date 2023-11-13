import matplotlib.pyplot as plt

def read_data(file_path):
    data = {"gps": [], "gps_left": []}
    with open(file_path, 'r') as file:
        for line in file:
            who, speed, time_taken = map(str, line.split())
            who = int(who)
            time_taken = float(time_taken)
            data["gps" if who == 0 else "gps_left"].append((speed, time_taken))
    return data

def plot_chart(data1, data2, label1, label2, title):
    speeds1, times1 = zip(*data1)
    speeds2, times2 = zip(*data2)
    plt.plot(speeds1, times1, label=label1)
    plt.plot(speeds2, times2, label=label2)
    plt.title(title)
    plt.xlabel("Insertion Speed")
    plt.ylabel("Time Taken")
    plt.legend()
    plt.savefig(title + "_chart")
    plt.show()

def create_comparison_charts(file_path1, file_path2):
    data1 = read_data(file_path1)
    data2 = read_data(file_path2)

    plot_chart(data1["gps"], data2["gps"], label1="SQLite", label2="Berkeley DB", title="gps data 1467 rows")
    plot_chart(data1["gps_left"], data2["gps_left"], label1="SQLite", label2="Berkeley DB", title="gps_left 144036 rows")


if __name__ == "__main__":
    file1_path = 'output_sqlite_insert.txt'
    file2_path = 'output_berkleley_insert.txt'
    
    create_comparison_charts(file1_path, file2_path)
