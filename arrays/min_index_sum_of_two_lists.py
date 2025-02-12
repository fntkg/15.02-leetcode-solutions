class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        # Initialize a list to store the common restaurants with the minimum index sum
        common_restaurants = []
        # Initialize the minimum index sum to the maximum possible value
        min_index_sum = len(list1) + len(list2)

        # Populate the index_map with restaurants from list2
        index_map = {restaurant: i for i, restaurant in enumerate(list2)}

        # Iterate over list1 to find common restaurants
        for i, restaurant in enumerate(list1):
            if restaurant in index_map:
                # Calculate the index sum of the common restaurant
                index_sum = index_map.get(restaurant) + i
                if index_sum == min_index_sum:
                    # If the index sum is equal to the current minimum, add the restaurant to the list
                    common_restaurants.append(restaurant)
                if index_sum < min_index_sum:
                    # If the index sum is less than the current minimum, update the list and minimum index sum
                    common_restaurants = [restaurant]
                    min_index_sum = index_sum

        # Return the list of common restaurants with the minimum index sum
        return common_restaurants