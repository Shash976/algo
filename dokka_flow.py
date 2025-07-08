import os
from bs4 import BeautifulSoup
import plantuml

def parse_dokka_html(html_file):
    """Parses Dokka HTML and extracts class, method, and inheritance information.

    Args:
        html_file (str): Path to the Dokka HTML file.

    Returns:
        list: A list of dictionaries representing classes with their methods and inheritance.
    """

    with open(html_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    classes = []
    for class_element in soup.find_all("a", href=lambda href: href and href.startswith("app/")):
        print(class_element)
        # Check if the link points to a class page
        if "/index.html" in class_element["href"]:  # Exclude index.html files
            class_name = class_element.text.strip()
            print(class_name)
            # Find the class details section
            class_details_element = class_element.parent.find_next_sibling(class_="class-details")
            print(class_element.parent.find_next_sibling())
            print(class_details_element)
            if class_details_element:
                # Extract methods
                methods = []
                for method_element in class_details_element.find_all("div", class_="method-content"):
                    method_name = method_element.find("h3").text.strip()
                    methods.append(method_name)

                # Extract inheritance
                inheritance_element = class_details_element.find("div", class_="inheritance-list")
                if inheritance_element:
                    parent_class = inheritance_element.find("a").text.strip()
                else:
                    parent_class = None

                # Check for interfaces and enums
                is_interface = "interface" in class_details_element["class"]
                is_enum = "enum" in class_details_element["class"]

                classes.append({"name": class_name, "methods": methods, "parent": parent_class, "is_interface": is_interface, "is_enum": is_enum})
        """visited_files =[]
        for link_element in class_details_element.find_all("a"):
            href = link_element["href"]
            if href.startswith("app/") and href not in visited_files:
                # Recursively parse linked file
                linked_file_path = os.path.join(os.path.dirname(html_file), href)
                linked_classes = parse_dokka_html(linked_file_path, visited_files)
                # Aggregate class information from linked files
                classes.extend(linked_classes)
                visited_files.add(linked_file_path)
        print(visited_files)"""
    return classes

def generate_plantuml(classes, output_file):
    """Generates PlantUML code based on the parsed class information.

    Args:
        classes (list): A list of dictionaries representing classes.
        output_file (str): Path to the output PlantUML file.
    """

    with open(output_file, "w") as f:
        f.write("@startuml\n")
        for class_info in classes:
            if class_info["is_interface"]:
                f.write(f"interface {class_info['name']} {{\n")
            elif class_info["is_enum"]:
                f.write(f"enum {class_info['name']} {{\n")
            else:
                f.write(f"class {class_info['name']} {{\n")

            for method in class_info['methods']:
                f.write(f"    +{method}()\n")
            f.write("}\n")

            if class_info['parent']:
                f.write(f"{class_info['name']} <|-- {class_info['parent']}\n")
        f.write("@enduml\n")

if __name__ == "__main__":
    html_file = r"C:\Users\shash\Downloads\dokka\index.html"  # Replace with your Dokka HTML file
    output_file = "class_diagram.plantuml"
    classes = parse_dokka_html(html_file)
    generate_plantuml(classes, output_file)
    #os.system(f"plantuml -tsvg {output_file}")  # Generate SVG image