def queue_time(customers, n):
    if len(customers) == 0:
        return 0
    if len(customers) == 0 or n == 1:
        return sum(customers)
    if len(customers) < n:
        return max(customers)
    
    queues = [0] * n
    for i in range(len(customers)):
        smallest = min(queues)
        smallest_index = queues.index(smallest)
        queues[smallest_index] += customers[i]
    return max(queues)