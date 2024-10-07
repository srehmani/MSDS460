import pulp

# List of food items and their nutritional values
foods = ['Chicken Breast', 'Oatmeal', 'Spinach', 'Milk', 'Eggs', 'Salmon', 'Broccoli', 'Banana', 'Almonds']

# Nutritional data and cost (per serving)
costs = {'Chicken Breast': 2.00, 'Oatmeal': 0.50, 'Spinach': 0.60, 'Milk': 0.70,
         'Eggs': 0.80, 'Salmon': 3.00, 'Broccoli': 0.50, 'Banana': 0.25, 'Almonds': 1.00}

sodium = {'Chicken Breast': 60, 'Oatmeal': 1, 'Spinach': 24, 'Milk': 98,
          'Eggs': 140, 'Salmon': 75, 'Broccoli': 30, 'Banana': 1, 'Almonds': 1}

energy = {'Chicken Breast': 165, 'Oatmeal': 150, 'Spinach': 23, 'Milk': 149,
          'Eggs': 148, 'Salmon': 208, 'Broccoli': 55, 'Banana': 105, 'Almonds': 164}

protein = {'Chicken Breast': 31, 'Oatmeal': 6, 'Spinach': 3, 'Milk': 8,
           'Eggs': 12, 'Salmon': 20, 'Broccoli': 4, 'Banana': 1, 'Almonds': 6}

vitaminD = {'Chicken Breast': 0, 'Oatmeal': 0, 'Spinach': 0, 'Milk': 2.9,
            'Eggs': 2.0, 'Salmon': 16, 'Broccoli': 0, 'Banana': 0, 'Almonds': 0}

calcium = {'Chicken Breast': 11, 'Oatmeal': 52, 'Spinach': 30, 'Milk': 276,
           'Eggs': 50, 'Salmon': 9, 'Broccoli': 43, 'Banana': 5, 'Almonds': 76}

iron = {'Chicken Breast': 0.9, 'Oatmeal': 1.7, 'Spinach': 0.8, 'Milk': 0.1,
        'Eggs': 1.2, 'Salmon': 0.7, 'Broccoli': 0.7, 'Banana': 0.3, 'Almonds': 1.0}

potassium = {'Chicken Breast': 256, 'Oatmeal': 164, 'Spinach': 167, 'Milk': 322,
             'Eggs': 126, 'Salmon': 366, 'Broccoli': 230, 'Banana': 422, 'Almonds': 208}

# Initialize the problem
prob = pulp.LpProblem("Minimize_Food_Cost", pulp.LpMinimize)

# Define decision variables
food_vars = pulp.LpVariable.dicts("Food", foods, lowBound=0)

# Objective function: Minimize total cost over 7 days
prob += 7 * pulp.lpSum([costs[i] * food_vars[i] for i in foods]), "Total Cost"

# Constraints for nutritional intake per day
prob += pulp.lpSum([sodium[i] * food_vars[i] for i in foods]) <= 5000, "Sodium"
prob += pulp.lpSum([energy[i] * food_vars[i] for i in foods]) >= 2000, "Energy"
prob += pulp.lpSum([protein[i] * food_vars[i] for i in foods]) >= 50, "Protein"
prob += pulp.lpSum([vitaminD[i] * food_vars[i] for i in foods]) >= 20, "Vitamin D"
prob += pulp.lpSum([calcium[i] * food_vars[i] for i in foods]) >= 1300, "Calcium"
prob += pulp.lpSum([iron[i] * food_vars[i] for i in foods]) >= 18, "Iron"
prob += pulp.lpSum([potassium[i] * food_vars[i] for i in foods]) >= 4700, "Potassium"

# Solve the problem
prob.solve()

# Output results
print("Status:", pulp.LpStatus[prob.status])
for var in food_vars:
    print(f"{var}: {food_vars[var].varValue}")

# Total cost
print("Total weekly cost: $", pulp.value(prob.objective))
