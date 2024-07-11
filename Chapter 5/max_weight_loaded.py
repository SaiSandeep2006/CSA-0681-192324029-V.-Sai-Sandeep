def max_weight_loaded(weights, max_capacity):
    weights.sort(reverse=True)
    current_weight = 0
    
    for weight in weights:
        if current_weight + weight <= max_capacity:
            current_weight += weight
    
    return current_weight


weights1 = [10, 20, 30, 40, 50]
max_capacity1 = 60
print("9) ",max_weight_loaded(weights1, max_capacity1)) 