class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer  # Renamed from self.customer_ to self.customer
        self.restaurant = restaurant  # Renamed from self.restaurant_ to self.restaurant
        self.rating = rating  # Renamed from self.rating_ to self.rating
        Review.all_reviews.append(self)

    def get_rating(self):  # Renamed from rating to get_rating
        return self.rating

    def get_customer(self):  # Renamed from customer to get_customer
        return self.customer

    def get_restaurant(self):  # Renamed from restaurant to get_restaurant
        return self.restaurant

    @classmethod
    def all(cls):
        return cls.all_reviews

# Example
customer1 = "Evans"
restaurant1 = "Pepinos"
rating1 = 3

review1 = Review(customer1, restaurant1, rating1)

print(review1.get_customer())  # Changed from review1.customer() to review1.get_customer()
print(review1.get_restaurant())  # Changed from review1.restaurant() to review1.get_restaurant()
print(review1.get_rating())  # Changed from review1.rating() to review1.get_rating()

for review in Review.all():
    print(f"Customer: {review.get_customer()}, Restaurant: {review.get_restaurant()}, Rating: {review.get_rating()}")