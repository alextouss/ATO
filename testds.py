movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]
# bars are by default width 0.8, so we'll add 0.1 to the left coordinates # so that each bar is centered
xs = [i + 0.1 for i,_ in enumerate(movies)]
print(xs)