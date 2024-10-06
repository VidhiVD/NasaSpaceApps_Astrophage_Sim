from gettext import install
import pip

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# Simulation parameters
planet_radius = 1.5  # Relative radius compared to Earth
ocean_depth = 1 # Relative ocean depth compared to planet radius
atmosphere_thickness = 0.15  # Relative atmosphere thickness compared to planet radius

# Atmospheric composition parameters
water_vapor_ratio = 0.5
sulfur_dioxide_ratio = 0.15
hydrogen_sulfide_ratio = 0.2
carbon_dioxide_ratio = 0.05
sulfuric_acid_ratio = 0.05
other_gases_ratio = 0.05

# Ocean chemical properties
ocean_sulfur_concentration = 0.3  # Concentration of sulfur compounds in the ocean
ocean_iron_concentration = 0.15   # Concentration of iron compounds
ocean_acidity = 0.2  # Relative acidity of the water
# Create figure
fig, ax = plt.subplots(figsize=(8, 8))

# Define color gradients for the atmosphere and water
# Atmosphere: yellow-green gradient for sulfur-rich gases
atmosphere_colors = np.linspace(0.4, 0.8, 100)  # Values from 0 (black) to 1 (bright color)
# Ocean: green to dark brown gradient
ocean_colors = np.linspace(0.3, 0.6, 100)

# Create circular planet shape
theta = np.linspace(0, 2 * np.pi, 100)
planet_x = planet_radius * np.cos(theta)
planet_y = planet_radius * np.sin(theta)

# Create ocean layer (internal circle)
ocean_x = (planet_radius - ocean_depth) * np.cos(theta)
ocean_y = (planet_radius - ocean_depth) * np.sin(theta)

# Create atmosphere layer (external circle)
atmosphere_x = (planet_radius + atmosphere_thickness) * np.cos(theta)
atmosphere_y = (planet_radius + atmosphere_thickness) * np.sin(theta)

# Draw atmosphere layers with gradient color
for i, color in enumerate(atmosphere_colors):
    layer_x = (planet_radius + atmosphere_thickness * i / len(atmosphere_colors)) * np.cos(theta)
    layer_y = (planet_radius + atmosphere_thickness * i / len(atmosphere_colors)) * np.sin(theta)
    ax.fill(layer_x, layer_y, color=(color, color, 0.0), alpha=0.3)  # Greenish-yellow for sulfur gases

# Draw ocean layer with gradient color
for i, color in enumerate(ocean_colors):
    layer_x = (planet_radius - ocean_depth * i / len(ocean_colors)) * np.cos(theta)
    layer_y = (planet_radius - ocean_depth * i / len(ocean_colors)) * np.sin(theta)
    ax.fill(layer_x, layer_y, color=(0.0, color, 0.0), alpha=0.5)  # Greenish-brown for mineral-rich water

# Draw planet surface
ax.fill(planet_x, planet_y, color='gray', alpha=0.6)  # Planet's surface color (rocky/volcanic)

# Labels and title
ax.set_title("Simulated Atmosphere and Ocean of Kepler d")
ax.set_xlim(-planet_radius - atmosphere_thickness, planet_radius + atmosphere_thickness)
ax.set_ylim(-planet_radius - atmosphere_thickness, planet_radius + atmosphere_thickness)
ax.set_aspect('equal')
ax.axis('off')  # Hide axis for better visualization

# Display the plot &
plt.show()
print ("water vapor ratio " + water_vapor_ratio)
print (" sulfur dioxide ratio " + sulfur_dioxide_ratio)
print ("hydrogen sulfide ratio " + hydrogen_sulfide_ratio)
print("carbon dioxide ratio " + carbon_dioxide_ratio)
print ("sulfuric acid ration " + sulfuric_acid_ratio)
print("other gases ation " + other_gases_ratio)
print ("ocean sulfur concentration " + ocean_sulfur_concentration)
print("ocean iron concentration " + ocean_iron_concentration)
print("ocean acidity " + ocean_acidity)
print("atmosphere thickness " + atmosphere_thickness)
print ("ocean depth " + ocean_depth)
print (" planet radius " + planet_radius)
print ("atmoshpere thickness "+ atmosphere_thickness)
