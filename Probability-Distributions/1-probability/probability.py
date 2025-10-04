# Example code to calculate probabilities for given events
# Import required libraries
import numpy as np
# Function to compute probability
def compute_probability(favorable_outcomes, total_outcomes):
if total_outcomes == 0:
raise ValueError("Total outcomes must be greater than 0.")
return favorable_outcomes / total_outcomes
# Example: Probability of deaths due to heart failure or diabetes
heart_failure_deaths = 150
diabetes_deaths = 100
total_population = 1000
prob_heart_failure = compute_probability(heart_failure_deaths, total_population)
prob_diabetes = compute_probability(diabetes_deaths, total_population)
# Assuming independence for joint probability calculation
prob_joint = prob_heart_failure * prob_diabetes
print("Probability of deaths due to heart failure:", prob_heart_failure)
print("Probability of deaths due to diabetes:", prob_diabetes)
print("Probability of deaths due to both heart failure and diabetes:", prob_joint)
