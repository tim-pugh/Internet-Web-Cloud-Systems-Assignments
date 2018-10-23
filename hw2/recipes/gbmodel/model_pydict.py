"""
Python dict model
"""

from .Model import Model

class model(Model):
    def __init__(self):
        self.recipes = {{'recipe':lasagna, 'ingredients':olives+noodles+sauce+tomatoes, 'reviews':its okay, 'time_to_cook':10_minutes},{'recipe':peanut butter w/ jelly, 'ingredients':bread+peanut butter+jelly, 'reviews':its a classic, 'time_to_cook':10_minutes}}

    def select(self):
        """
        Returns recipe list of dictionaries
        Each dictionary in recipes contains: recipe, ingredients, reviews, time_to_cook
        :return: List of dictionaries
        """
        return self.recipes

    def insert(self, recipe, ingredients, reviews, time_to_cook):
        """
        Appends a new list of values representing new message into guestentries
        :param recipe: String
        :param ingredients: String
        :param reviews: String
	:param time_to_cook: String
        :return: True
        """
        params = {'recipe':recipe, 'ingredients':ratings, 'reviews':reviews, 'time_to_cook':time_to_cook}
        self.recipes.append(params)
        return True
