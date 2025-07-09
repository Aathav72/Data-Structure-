# Initial Queue
queue = ["Compiler", "Firewall", "Algorithm", "Protocol", "Cache"]

# Question 1: Perform two dequeue operations
dequeued_1 = queue.pop(0)  # Removes 'Compiler'
dequeued_2 = queue.pop(0)  # Removes 'Firewall'
print("After two dequeue operations:")
print("Dequeued elements:", dequeued_1, dequeued_2)
print("Current Queue:", queue)

# Question 2: Enqueue 'Virtualization'
queue.append("Virtualization")
print("\nAfter enqueuing 'Virtualization':")
print("Current Queue:", queue)

# Question 3: Perform one dequeue operation
dequeued_3 = queue.pop(0)  # Removes 'Algorithm'
print("\nAfter one dequeue operation:")
print("Dequeued element:", dequeued_3)
print("Current Queue:", queue)

# Question 4: Enqueue 'Cloud'
queue.append("Cloud")
print("\nAfter enqueuing 'Cloud':")
print("Current Queue:", queue)

# Question 5: Check if 'Protocol' is still present
is_protocol_present = "Protocol" in queue
print("\nIs 'Protocol' present in the queue?", is_protocol_present)

# Question 6: Enqueue 'Machine Learning'
queue.append("Machine Learning")
print("\nAfter enqueuing 'Machine Learning':")
print("Current Queue:", queue)

# Question 7: Perform one final dequeue operation
dequeued_4 = queue.pop(0)  # Removes 'Protocol'
print("\nAfter final dequeue operation:")
print("Dequeued element:", dequeued_4)
print("Final Queue:", queue)
