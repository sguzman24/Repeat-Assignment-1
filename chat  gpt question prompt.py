# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 18:44:52 2023

@author: sguzman24
"""

def calculate_max_height(initial_velocity):
    g = 32.2  # acceleration due to gravity in ft/s^2

    max_height = (initial_velocity ** 2) / (2 * g)
    return max_height

# Example usage
initial_velocity = 50  # ft/s
max_height = calculate_max_height(initial_velocity)
print(f"The maximum height of the ball is {max_height:.2f} feet.")
