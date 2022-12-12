import math


def generate_data():
    f = open('sample_data_1.txt')
    #f = open('sample_data_2.txt')
    number_of_nodes = int(f.readline().strip())
    lines = f.readlines()
    f.close()

    data = [[0 for _ in range(number_of_nodes)] for _ in range(number_of_nodes)]

    for line in lines:
        value = line.split()
        if len(value) != 3:
            continue
        else:
            row = int(value[0])
            column = int(value[1])
            cost = int(value[2])
            data[row][column] = cost

    return data


def select_path(previous_node, destination):
    passed_node = [destination]
    node = destination
    while True:
        node = previous_node[node]
        if node == None:
            break
        else:
            passed_node.insert(0, node)

    passed_node = [str(x) for x in passed_node]
    return ' -> '.join(passed_node)


def shortest_path(cost_value, shortest_cost):
    minimum = math.inf
    minimum_node = math.inf
    for node in range(len(cost_value)):
        if shortest_cost[node] == False and cost_value[node] < minimum:
            minimum = cost_value[node]
            minimum_node = node

    return minimum_node


def dijkstra(data, start_node, destination):
    number_of_nodes = len(data)
    cost_value = [math.inf for _ in range(number_of_nodes)]
    cost_value[start_node] = 0

    previous_node = [None for _ in range(number_of_nodes)]

    shortest_cost = [False for _ in range(number_of_nodes)]

    for i in range(number_of_nodes):
        x = shortest_path(cost_value, shortest_cost)

        if x == math.inf:
            print(f"There is no path from {start_node} to {destination}")
            return

        shortest_cost[x] = True
        if x == destination:
            print(f"Path found from {start_node} to {destination}")
            path = select_path(previous_node, destination)
            answer = (f"From {start_node} to {destination}: ") + path + " = " + str(cost_value[destination])
            print(answer)
            return
        else:
            for y in range(number_of_nodes):
                if shortest_cost[y] == False and data[x][y] > 0 and cost_value[y] > cost_value[x] + data[x][y]:
                    cost_value[y] = cost_value[x] + data[x][y]
                    previous_node[y] = x


def main():
    data = generate_data()
    number_of_nodes = len(data)
    print("Number of nodes: ", number_of_nodes)
    start_node = int(input("Enter start node: "))
    destination = int(input("Enter destination: "))
    if start_node in range(number_of_nodes) and destination in range(number_of_nodes):
        dijkstra(data, start_node, destination)


if __name__ == '__main__':
    main()