from Review import Review

class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name  # Changed from self.name_ to self.name
        Restaurant.all_restaurants.append(self)

    def get_name(self):
        return self.name

    def reviews(self):
        return [review for review in Review.all_reviews if review.restaurant == self]  # Changed review.restaurant() to review.restaurant

    def customers(self):
        reviewers = [review.customer for review in self.reviews()]  # Changed review.customer() to review.customer
        return list(set(reviewers))

    def average_star_rating(self):
        ratings = [review.rating for review in self.reviews()]  # Changed review.rating() to review.rating
        if not ratings:
            return 0
        return sum(ratings) / len(ratings)


# Example
# Create an instance of the Restaurant class
restaurant = Restaurant("Pepinos")

# Print information about the restaurant and its reviews
print(f"Restaurant Name: {restaurant.get_name()}")
print(f"Customers: {restaurant.customers()}")
print(f"Average Star Rating: {restaurant.average_star_rating()}")