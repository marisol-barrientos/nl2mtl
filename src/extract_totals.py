import json


def count_details(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    total_assumptions = 0
    total_ambiguities = 0
    total_mtl_expressions = len(data["MTL_expressions"])
    total_propositions = 0

    # Iterate over each MTL expression
    for expression in data["MTL_expressions"]:
        # Count propositions in this expression
        total_propositions += len(expression["propositions"])
        # Iterate over each proposition in the expression
        for prop in expression["propositions"]:
            # Add the number of assumptions and ambiguities from each proposition
            total_assumptions += len(prop["assumptions"])
            total_ambiguities += len(prop["ambiguities"])

    return total_assumptions, total_ambiguities, total_mtl_expressions, total_propositions


def overall_stats(files):
    assumptions = []
    ambiguities = []
    mtl_expressions = []
    propositions = []

    for file in files:
        file_assumptions, file_ambiguities, file_mtl_expressions, file_propositions = count_details(file)
        assumptions.append(file_assumptions)
        ambiguities.append(file_ambiguities)
        mtl_expressions.append(file_mtl_expressions)
        propositions.append(file_propositions)

    # Calculate statistics for each metric
    def calculate_stats(values):
        return {
            'average': sum(values) / len(values),
            'maximum': max(values),
            'minimum': min(values)
        }

    stats = {
        'assumptions': calculate_stats(assumptions),
        'ambiguities': calculate_stats(ambiguities),
        'mtl_expressions': calculate_stats(mtl_expressions),
        'propositions': calculate_stats(propositions)
    }

    return stats


# List of JSON files to process
# List of JSON files to process
json_files = ['/home/marisolbarrientosmoreno/Desktop/1st_semester_phd/new_submission/nl2mtl/data/test_1/output/cara_pump_requirements.json',
              '/home/marisolbarrientosmoreno/Desktop/1st_semester_phd/new_submission/nl2mtl/data/test_2/output/cara_pump_requirements.json',
              '/home/marisolbarrientosmoreno/Desktop/1st_semester_phd/new_submission/nl2mtl/data/test_3/output/cara_pump_requirements.json',
              '/home/marisolbarrientosmoreno/Desktop/1st_semester_phd/new_submission/nl2mtl/data/test_4/output/cara_pump_requirements.json']

stats = overall_stats(json_files)

print("Statistics for each category:")
for category, values in stats.items():
    print(f"{category.capitalize()}:")
    print(f" Average: {values['average']}")
    print(f" Maximum: {values['maximum']}")
    print(f" Minimum: {values['minimum']}")

