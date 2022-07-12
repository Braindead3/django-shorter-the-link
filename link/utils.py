import string

from .models import Url
import random


def generate_short_url():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_letters = random.sample(letters, 5)
        rand_letters = "".join(rand_letters)
        short_url = Url.objects.filter(short_url=rand_letters).first()
        if not short_url:
            return rand_letters
