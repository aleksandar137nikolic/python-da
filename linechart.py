import matplotlib.pyplot as plt
import numpy as np
import time

# Initialize an empty list to store the data points
data = []

# Create the initial figure and axis
fig, ax = plt.subplots()

# Set the initial axis limits
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

# Create the line object
line, = ax.plot([], [])

# Function to update the line chart
def update_line():
    # Generate a new data point
    if data:
        # Calculate the next data point based on the previous value
        new_value = data[-1] + np.random.normal(0, 2)
        data.append(new_value)
    else:
        # If no previous data points, start from a random value
        data.append(np.random.randint(0, 100))
    
    # Update the line data
    line.set_data(range(len(data)), data)
    
    # Adjust the axis limits if necessary
    ax.set_xlim(0, len(data))
    ax.set_ylim(min(data) - 5, max(data) + 5)
    
    # Redraw the plot
    fig.canvas.draw()

# Update the line chart every 2 seconds
while True:
    update_line()
    plt.pause(2)  # Pause for 2 seconds
