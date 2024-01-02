import xml.etree.cElementTree as ET

myfile = '/tmp/vulnerable-countries.xml'
root = ET.Element("root")
ET.SubElement(root, "country", name="Iran")
ET.SubElement(root, "country", name="Antarctica")
ET.SubElement(root, "country", name="Panama")
tree = ET.ElementTree(root)
tree.write(myfile)