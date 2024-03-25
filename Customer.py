# Assuming Restaurant and Review classes are correctly implemented elsewhere

class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)

class Restaurant:
    def _init_(self, name):
        self.name = name

class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []  # Added to store reviews for each customer
        Customer.all_customers.append(self)

    def get_given_name(self):
        return self.given_name

    def get_family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"
    
    @classmethod
    def all(cls):
        return cls.all_customers

    def restaurants(self):
        reviewed_restaurants = [review.restaurant for review in self.reviews]
        return list(set(reviewed_restaurants))

    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.reviews.append(review)  # Add the review to the customer's list of reviews

    def num_reviews(self):
        return len(self.reviews)

    @classmethod
    def find_by_name(cls, name):
        return next((customer for customer in cls.all_customers if customer.full_name() == name), None)

    @classmethod
    def find_all_by_given_name(cls, given_name):
        return [customer for customer in cls.all_customers if customer.given_name == given_name]

# Example:
customer1 = Customer("Dean", "Socrates")
customer2 = Customer("Johnnie", "Walker")

restaurant1 = Restaurant("Kwa Mathee")
restaurant2 = Restaurant("Fogo Gaucho")

print("Customer1:", customer1.full_name())
print("Customer2:", customer2.full_name())

customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 5)
customer2.add_review(restaurant1, 3)

print("Customer1's reviewed restaurants:", [r.name for r in customer1.restaurants()])