__author__ = 'Paul YC Dong'
import media

toy_story = media.Movie("Toy Story",
                        "Toys are alive!",
                        "image url",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print toy_story.storyline
#toy_story.show_trailer()

print toy_story.__doc__
print media.Movie.__name__
print toy_story.__module__

