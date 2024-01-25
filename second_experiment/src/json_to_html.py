import json


def process_non_formalized_parts(data):
    """ Generate HTML content for Non Formalized Parts. """
    html_content = '<h2>Non Formalized Parts</h2>'
    for part in data['non_formalized_parts']:
        html_content += f'<div class="non-formalized">ID {part["id"]}: {part["description"]} (Reason: {part["reason_for_non_formalization"]})</div>'
    return html_content


def process_dependency_sequence(data):
    """ Generate HTML content for the Dependency Sequence. """
    html_content = '<h2>Dependency Sequence</h2>'
    for dep in data['dependency_sequence']:
        html_content += f'<div class="dependency">From ID {dep["preceding_id"]} to ID {dep["following_id"]}: {dep["dependency_description"]}</div>'
    return html_content


class JsonToHtmlConverter:
    def __init__(self, json_file, html_file):
        self.json_file = json_file
        self.html_file = html_file

    @staticmethod
    def replace_special_symbols(expression):
        """ Replace special symbols in MTL expressions with their HTML entities. """
        return (expression.replace('∞', '&infin;')
                          .replace('≤', '&le;')
                          .replace('≥', '&ge;')
                          .replace('⇒', '&rArr;')
                          .replace('→', '&rArr;')
                          .replace('¬', '&not;')
                          .replace('∧', '&and;'))

    def process_mtl_expressions(self, data):
        """ Generate HTML content for MTL Expressions. """
        html_content = '<h2>MTL Expressions</h2>'
        for expr in data['MTL_expressions']:
            formatted_mtl_expression = self.replace_special_symbols(expr["MTL_expression"])
            html_content += f'<div class="mtl-expression"><strong>ID {expr["id"]}</strong>: {expr["description"]}<ul>'
            for prop in expr["propositions"]:
                html_content += f'<li class="proposition"><strong>Proposition ID {prop["id"]}</strong>: {prop["description"]}<ul>'
                for assumption in prop["assumptions"]:
                    html_content += f'<li class="assumption"><strong>Assumption:</strong> {assumption}</li>'
                for ambiguity in prop["ambiguities"]:
                    html_content += f'<li class="ambiguity"><strong>Ambiguity:</strong> {ambiguity}</li>'
                html_content += f'<li class="granularity"><strong>Granularity:</strong> {prop["granularity"]}</li>'
                html_content += '</ul></li>'
            html_content += f'<li><strong>MTL Expression</strong>: {formatted_mtl_expression}</li>'
            html_content += '</ul></div>'
        return html_content

    def convert(self):
        """ Convert JSON data to a readable HTML format. """
        with open(self.json_file, 'r') as file:
            data = json.load(file)

        html_content = '''
        <html>
        <head>
            <title>Quince Harvesting Process</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f4f4f4;
                    color: #333;
                }
                .container {
                    width: 80%;
                    margin: auto;
                    overflow: hidden;
                }
                header {
                    background: #0077B6;  /* Deep Blue */
                    color: #fff;
                    padding-top: 30px;
                    min-height: 70px;
                    border-bottom: #023E8A 3px solid;  /* Darker Blue */
                }
                header a {
                    color: #ffffff;
                    text-decoration: none;
                    text-transform: uppercase;
                    font-size: 16px;
                }
                header ul {
                    padding: 0;
                    margin: 0;
                    list-style: none;
                    overflow: hidden;
                }
                header li {
                    float: left;
                    display: inline;
                    padding: 0 20px 0 20px;
                }
                header #branding {
                    float: left;
                }
                header #branding h1 {
                    margin: 0;
                }
                header nav {
                    float: right;
                    margin-top: 10px;
                }
                header .highlight, header .current a {
                    color: #023E8A; /* Darker Blue */
                    font-weight: bold;
                }
                header a:hover {
                    color: #48CAE4; /* Light Blue */
                    font-weight: bold;
                }
                .mtl-expression, .proposition, .dependency, .non-formalized {
                    background: #fff;
                    padding: 15px;
                    margin-bottom: 15px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
                h2 {
                    color: #0077B6; /* Deep Blue */
                }
                .proposition {
                    background-color: #CAF0F8; /* Very Light Blue */
                    margin-left: 20px;
                }
                .assumption, .ambiguity, .granularity {
                    font-style: italic;
                    color: #555;
                }
            </style>
        </head>
        <body>
            <header>
                <div class="container">
                    <div id="branding">
                        <h1>Quince Harvesting Process</h1>
                    </div>
                </div>
            </header>
            <div class="container">
        '''
        html_content += self.process_mtl_expressions(data)
        html_content += process_dependency_sequence(data)
        html_content += process_non_formalized_parts(data)

        html_content += '</div></body></html>'

        with open(self.html_file, 'w') as file:
            file.write(html_content)

