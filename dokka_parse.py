import os
from bs4 import BeautifulSoup

# Function to extract class, method, and inheritance data from Dokka HTML
def extract_classes_methods_inheritance(dokka_html_dir):
    class_data = {}  # Dictionary to store class names and methods
    inheritance_data = []  # List to store inheritance relationships

    # Loop through HTML files in the Dokka output directory
    for root, _, files in os.walk(dokka_html_dir):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as html_file:
                    soup = BeautifulSoup(html_file, 'html.parser')

                    # Find the class name (usually in <h1> or <h2> tags in Dokka HTML)
                    class_name_tag = soup.find('h1') or soup.find('h2')
                    if class_name_tag:
                        class_name = class_name_tag.get_text().strip()
                        class_data[class_name] = []

                        # Check for inheritance (usually in <span> or <p> tags in Dokka HTML)
                        inheritance_tag = soup.find('span', class_='supertypes') or soup.find('p', class_='supertypes')
                        if inheritance_tag:
                            # Extract inheritance relationship
                            for link in inheritance_tag.find_all('a'):
                                parent_class = link.get_text().strip()
                                inheritance_data.append((class_name, parent_class))

                        # Find methods (typically in <code> or <section> tags for method signatures)
                        method_tags = soup.find_all('code')  # May vary depending on Dokka's HTML structure
                        for method_tag in method_tags:
                            method_name = method_tag.get_text().strip()
                            if '(' in method_name and ')' in method_name:  # Ensure it’s a method signature
                                class_data[class_name].append(method_name)

    return class_data, inheritance_data

# Function to generate Mermaid class diagram with inheritance from extracted data
def generate_mermaid_class_diagram(class_data, inheritance_data):
    mermaid_output = "```mermaid\nclassDiagram\n"
    
    # Add classes and methods to the diagram
    for class_name, methods in class_data.items():
        mermaid_output += f"  class {class_name} {{\n"
        for method in methods:
            mermaid_output += f"    +{method}()\n"
        mermaid_output += "  }\n"
    
    # Add inheritance relationships to the diagram
    for child_class, parent_class in inheritance_data:
        mermaid_output += f"  {parent_class} <|-- {child_class}\n"
    
    mermaid_output += "```"
    
    return mermaid_output

# Main function to run the script
def main():
    dokka_html_dir = r"C:\Users\shash\Downloads\dokka" # Set this to your Dokka HTML directory
    class_data, inheritance_data = extract_classes_methods_inheritance(dokka_html_dir)
    
    print("Extracted class and method data:")
    print(class_data)
    print("\nExtracted inheritance data:")
    print(inheritance_data)

    if class_data:
        # Generate the Mermaid diagram from the extracted data
        mermaid_diagram = generate_mermaid_class_diagram(class_data, inheritance_data)
        
        # Save the Mermaid diagram to a Markdown file
        with open(r'C:\Users\shash\Desktop\Code\VSC\algo\mermaid_class_diagram.md', 'w', encoding='utf-8') as output_file:
            output_file.write(mermaid_diagram)
        
        print("Mermaid class diagram generated and saved as 'mermaid_class_diagram.md'")
    else:
        print("No class or method data found in the provided Dokka HTML directory.")

if __name__ == "__main__":
    main()