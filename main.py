def optimal_consumption(budget, prices, weights):
    """
    Computes the optimal consumption bundle given a budget, prices, and preference weights.
    
    :param budget: Total budget available (M)
    :param prices: Dictionary of {good: price}
    :param weights: Dictionary of {good: preference weight}
    :return: Dictionary of {good: optimal quantity}
    """
    total_weight = sum(weights.values())
    optimal_quantities = {}
    
    for good in prices:
        optimal_quantities[good] = (weights[good] / total_weight) * (budget / prices[good])
    
    return optimal_quantities

# Example usage:
budget = 1800
prices = {"apples": 2, "bananas": 4, "oranges": 3}
weights = {"apples": 0.5, "bananas": 0.5, "oranges": 0.5}

optimal_bundle = optimal_consumption(budget, prices, weights)
print(optimal_bundle)
