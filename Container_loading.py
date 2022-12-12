def bubble_sort(container):
    sort_check = False
    while not sort_check:
        sort_check = True
        for i in range(0, len(container) - 1):
            if container[i] > container[i + 1]:
                sort_check = False
                container[i], container[i + 1] = container[i + 1], container[i]
    return container


def container_loading(capacity, container):
    bubble_sort(container)
    n = len(container)
    container_loaded = 0
    i = 0
    while i < n and container[i] <= capacity:
        container_loaded += 1
        capacity -= container[i]
        i += 1

    return container_loaded
    print(container)


print(container_loading(400, [80, 60, 50, 60, 100, 150, 90, 300]))
