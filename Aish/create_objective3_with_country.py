content = open('sustainable_energy/dashboard/templates/dashboard/objective2.html', 'r', encoding='utf-8').read()

# Replace all Objective 2 references with Objective 3
replacements = [
    ('Objective 2: Predict Carbon Emissions', 'Objective 3: Energy Access Classification'),
    ('CO₂ Emissions Forecasting', 'Energy Access Classification'),
    ('CO₂ emissions', 'Electricity Access'),
    ('co2-icon', 'bolt'),
    ('fa-smog', 'fa-bolt'),
    ('#e74c3c', '#667eea'),
    ('#c0392b', '#764ba2'),
    ('objective2', 'objective3'),
    ('Best Model: XGBoost (MSE = 0.0048)', 'Best Model: CatBoost (Accuracy = 0.9808)'),
    ('mseScores', 'accuracyScores'),
    ('mseValues', 'accuracyValues'),
    ('mseChart', 'accuracyChart'),
    ('id="mseChart"', 'id="accuracyChart"'),
    ('Sub-objective 2:', 'Sub-objective 3:'),
]

for old, new in replacements:
    content = content.replace(old, new)

# Replace the hardcoded scores
old_scores = '''const mseScores = {
            "Linear Regression": 0.0370,
            "Decision Tree": 0.0085,
            "KNN": 0.0089,
            "XGBoost": 0.0048,
            "LightGBM": 0.0349,
            "CatBoost": 0.0072,
            "Random Forest": 0.0074
        };'''

new_scores = '''const accuracyScores = {
            "Logistic Regression": 0.9425,
            "Decision Tree": 0.9562,
            "KNN": 0.9671,
            "XGBoost": 0.9781,
            "LightGBM": 0.9767,
            "CatBoost": 0.9808,
            "Random Forest": 0.9767
        };'''

content = content.replace(old_scores, new_scores)

# Change highlight from XGBoost to CatBoost
content = content.replace("if (model === 'XGBoost')", "if (model === 'CatBoost')")

# Add max: 1.0 for accuracy scale
content = content.replace('beginAtZero: true,\n                                        title:', 'beginAtZero: true,\n                                        max: 1.0,\n                                        title:')

# Change MSE to Accuracy in labels
content = content.replace("'MSE'", "'Accuracy'")
content = content.replace('MSE:', 'Accuracy:')
content = content.replace("text: 'MSE'", "text: 'Accuracy'")

with open('sustainable_energy/dashboard/templates/dashboard/objective3.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Objective 3 updated successfully with country selection!")
print("Features:")
print("  - Model comparison with hardcoded accuracy values")
print("  - CatBoost highlighted as best model (0.9808)")
print("  - Purple gradient country selection section")
print("  - Historical and prediction charts for selected country")
