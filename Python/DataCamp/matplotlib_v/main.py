import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

plt.plot(year, pop) # or plt.scatter(year, pop)
plt.show()
plt.clf() # Clear the plot

# Histogram
values = [0, 0.6, 1.4, 1.6, 2.2, 2.5, 2.9, 3.1, 3.2, 3.9, 4.2]
plt.hist(values,bins=3)
plt.show()

# Customization
plt.clf()
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projections')
plt.yticks([0, 2, 4, 6, 8, 10], ['0', '2B', '4B', '6B', '8B', '10B'])
plt.show()
