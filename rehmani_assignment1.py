# Setup required packages
from pulp import LpProblem, LpMinimize, LpVariable, LpStatus, value

# Define problem:
prob = LpProblem("My_Plan_Basic", LpMinimize)

# # Define variables:
# a = LpVariable("Greek_Omelet", 0, None)
# b = LpVariable("Veg_Biryani", 0, None)
# c = LpVariable("Tandoori_Fish", 0, None)
# d = LpVariable("Salmon_Steak", 0, None)
# e = LpVariable("Swiss_Muesli", 0, None)

# Decision variables: at least 1 serving required (part 4)
a = LpVariable("Greek_Omelet", 1, None)
b = LpVariable("Veg_Biryani", 1, None)
c = LpVariable("Tandoori_Fish", 1, None)
d = LpVariable("Salmon_Steak", 1, None)
e = LpVariable("Swiss_Muesli", 1, None)

# Objective Function:
prob += 4.45 * a + 9.53 * b + 14.79 * c + 6.74 * d + 1.37 * e, "Total Cost"

# Constraints:
prob += 1338   * a + 2962.98 * b + 2426.25 * c + 718.74 * d + 97.3  * e <= 35000, "Sodium"
prob += 456    * a + 855.17  * b + 395.33  * c + 345.01 * d + 261   * e >= 14000, "Energy"
prob += 30     * a + 45.93   * b + 22.8    * c + 35.32  * d + 11    * e >= 350, "Protein"
prob += 3.1    * a + 0.36    * b + 12.5    * c + 18.5   * d + 1.5   * e >= 140, "Vitamin D"
prob += 463    * a + 1457.54 * b + 209.47  * c + 32.04  * d + 166.4 * e >= 9100, "Calcium"
prob += 9.2    * a + 10.47   * b + 2       * c + 1.09   * d + 1.62  * e >= 126, "Iron"
prob += 1648.2 * a + 1142.24 * b + 1031.92 * c + 665.84 * d + 350.8 * e >= 32900, "Potassium"

# Solve
prob.solve()

# Print the status of the solution:
print("Status:", LpStatus[prob.status])

# Print the values of the variables at the optimum:
for v in prob.variables():
    print(v.name, "=", v.varValue)

# Print the optimized total cost:
print("Total cost of the plan per week: $", round(value(prob.objective), 2))



