import pandas as pd
import xml.etree.ElementTree as ET

def main():
    tree = ET.parse('egXML.xml')
    root = tree.getroot()
    print(root)





if __name__ == "__main__":

    main()