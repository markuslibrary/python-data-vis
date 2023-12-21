import matplotlib.pyplot as plt
import numpy as np

from matplotlib.font_manager import FontProperties

# Define fonts
font = FontProperties(family='Arial', size = 12)
font_leg = FontProperties(family='Arial', size = 12)

# Import data
month, rain, snow, t_avg, t_max, t_min = np.genfromtxt('weather_data.csv', unpack = True, delimiter = ',', skip_header = 1)

# Generate figure and axes
fig, ((ax1), (ax2)) = plt.subplots (ncols = 1, nrows = 2, sharex = True, figsize = (4.5, 4.5))

# Plot Data
ax1.errorbar(month, t_max, marker = 'o', linewidth = 1, markerfacecolor = 'mistyrose', markeredgecolor = 'coral', color = 'coral', label = 'Max.')
ax1.errorbar(month, t_avg, marker = 'o', linewidth = 1, markerfacecolor = 'white', markeredgecolor = 'grey', color = 'grey', label = 'Avg.')
ax1.errorbar(month, t_min, marker = 'o', linewidth = 1, markerfacecolor = 'lightsteelblue', markeredgecolor = 'royalblue', color = 'royalblue', label = 'Min.')

ax2.bar(month, rain, color = 'lightsteelblue', align = 'edge', width = 0.3, label = 'Rain', edgecolor = 'royalblue')
ax2.bar(month, snow, color = 'ghostwhite', align = 'edge', width = -0.3, label = 'Snow', edgecolor = 'lightsteelblue')

#Create filled regions
ax1.fill_between(month, t_min, t_avg, color = 'lightsteelblue', alpha = 0.3)
ax1.fill_between(month, t_avg, t_max, color = 'mistyrose', alpha = 0.5)

# Create legends
ax1.legend(prop = font_leg, loc = 'upper left')
ax2.legend(prop = font_leg, loc = 'upper right')

# Set ax1 y limits so legend fits nicely
ax1.set_ylim(20, 110)

# Set y axis labels and title
ax1.set_ylabel('Temperature (F)', fontproperties = font)
ax2.set_ylabel('Precipitation (in)', fontproperties = font)
ax1.set_title('NYC Weather 1981 - 2010', fontproperties = font)

# Set month ticks and labels
ax1.set_xticks(month)
ax2.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], fontproperties = font, rotation = 45)

# Make ticks on all sides, pointing inwards, make slightly shorter than default
ax1.tick_params(direction = 'in', axis = 'both', top = True, right = True, length = 3)
ax2.tick_params(direction = 'in', axis = 'both', top = True, right = True, length = 3)

# Set tick label fonts
for label in ax1.get_yticklabels():
    label.set_fontproperties(font)

for label in ax2.get_yticklabels():
    label.set_fontproperties(font)
    


# Set layout to tight to remove extra white space
plt.tight_layout()

# Export and save figure as PNG
plt.savefig('weather_plot.png', transparent = True)

