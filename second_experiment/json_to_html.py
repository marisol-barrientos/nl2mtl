import json

def json_to_html(json_data):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>{title}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
                color: #333;
            }}
            .container {{
                width: 80%;
                margin: 20px auto;
                background: white;
                padding: 20px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
            h1, h2, h3 {{
                color: #007BFF;
            }}
            h1 {{
                border-bottom: 2px solid #007BFF;
            }}
            h2 {{
                border-bottom: 1px solid #007BFF;
            }}
            .expression, .non-formalized, .dependencies, .conflicts {{
                background-color: #E9ECEF;
                padding: 15px;
                margin-bottom: 20px;
                border-radius: 5px;
            }}
            .proposition {{
                background-color: #F8F9FA;
                margin: 10px 0;
                padding: 10px;
                border-left: 5px solid #007BFF;
                border-radius: 5px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{scenario_title}</h1>
            <p>{context}</p>
    """.format(title=json_data["scenario_title"], scenario_title=json_data["scenario_title"], context=json_data["context"])

    # MTL Expressions
    html += "<h2>MTL Expressions</h2>"
    for expression in json_data["MTL_expressions"]:
        mtl_expression = expression["MTL_expression"]
        mtl_expression = mtl_expression.replace('∞', '&infin;') \
            .replace('≤', '&le;') \
            .replace('≥', '&ge;') \
            .replace('⇒', '&rArr;') \
            .replace('¬', '&not;')

        html += """
                <div class="expression">
                    <h3>Expression {id}: {description}</h3>
                    <p><strong>MTL Expression:</strong> {MTL_expression}</p>
            """.format(id=expression["id"], description=expression["description"], MTL_expression=mtl_expression)
        for proposition in expression["propositions"]:
            html += """
                <div class="proposition">
                    <h4>Proposition {id}: {description}</h4>
                    <p><strong>Assumptions:</strong> {assumptions}</p>
                    <p><strong>Ambiguities:</strong> {ambiguities}</p>
                    <p><strong>Priority:</strong> {priority}</p>
                    <p><strong>Granularity:</strong> {granularity}</p>
                </div>
            """.format(id=proposition["id"], description=proposition["description"], assumptions=proposition["assumptions"],
                       ambiguities=proposition["ambiguities"], priority=proposition["priority"], granularity=proposition["granularity"])
        html += "</div>"

    # Non Formalized Parts
    if "non_formalized_parts" in json_data:
        html += "<h2>Non-Formalized Parts</h2>"
        for part in json_data["non_formalized_parts"]:
            html += """
                <div class="non-formalized">
                    <h3>ID: {id}</h3>
                    <p><strong>Description:</strong> {description}</p>
                    <p><strong>Reason for Non-Formalization:</strong> {reason}</p>
                </div>
            """.format(id=part["id"], description=part["description"], reason=part["reason_for_non_formalization"])

    # Sequence Dependencies
    if "sequence_dependencies" in json_data:
        html += "<h2>Sequence Dependencies</h2>"
        for dependency in json_data["sequence_dependencies"]:
            html += """
                <div class="dependencies">
                    <p><strong>Dependency:</strong> {dependency_description}</p>
                </div>
            """.format(dependency_description=dependency["dependency_description"])

    # Conflicts
    if "conflicts" in json_data:
        html += "<h2>Conflicts</h2>"
        for conflict in json_data["conflicts"]:
            html += """
                <div class="conflicts">
                    <p><strong>Conflict:</strong> {description}</p>
                </div>
            """.format(description=conflict["description"])

    # Closing tags
    html += """
        </div>
    </body>
    </html>
    """
    return html


# Read JSON data from file
with open('/home/marisolbarrientosmoreno/Desktop/1st_semester_phd/nl2mtl/second_experiment/output/quinces_output.json', 'r') as file:
    json_data = json.load(file)

# Convert JSON data to HTML
html_output = json_to_html(json_data)

# Write HTML output to a new file
with open('output/quinces_output.html', 'w') as file:
    file.write(html_output)