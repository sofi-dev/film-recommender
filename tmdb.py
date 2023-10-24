import tmdbsimple as tmdb
import numpy as np
import pandas as pd

tmdb.API_KEY = '78b74aad78b8672c26d0fb8596c37841'

movie = tmdb.Movies(100)
response = movie.info()
print(movie.title)
