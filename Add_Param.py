import xml.etree.ElementTree as ET


def Add_P(file_path, param_name, param_value):
    tree = ET.parse(file_path)
    root = tree.getroot()
    next_p = ET.SubElement(root[len(root) - 1], param_name)
    next_p.text = param_value
    tree.write(file_path)


def Add_S(file_path, param_name):
    tree = ET.parse(file_path)
    root = tree.getroot()
    ET.SubElement(root, param_name)
    tree.write(file_path)
