import justpy as jp

from webapp.about import About
from webapp.home import Home
from webapp.dictionary import Dictionary

#Route only expects function path, no arguments
jp.Route(About.path, About.serve)
jp.Route(Home.path, Home.serve)
jp.Route(Dictionary.path, Dictionary.serve)

jp.justpy(port=8001)

