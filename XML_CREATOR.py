import xml.etree.ElementTree as ET

def create_xml(file_name):
    top = ET.Element('start')
    top.text = 'first text'

    tree = ET.ElementTree(top)
    tree.write(file_name, xml_declaration=True)

create_xml("final_file.xml")