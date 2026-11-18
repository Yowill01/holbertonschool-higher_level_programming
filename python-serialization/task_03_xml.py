#!/usr/bin/env python3
"""Module that serializes and deserializes a dictionary using XML."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to an XML file.

    Args:
        dictionary: dictionary to serialize.
        filename: path of the output XML file.

    Returns:
        True if successful, False otherwise.
    """
    try:
        root = ET.Element("data")
        for key, value in dictionary.items():
            child = ET.SubElement(root, str(key))
            child.text = str(value)
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
        return True
    except (OSError, TypeError, ValueError):
        return False


def deserialize_from_xml(filename):
    """Deserialize an XML file into a dictionary.

    Values are returned as strings, since XML does not keep data types.

    Args:
        filename: path of the input XML file.

    Returns:
        A dictionary with the data, or None if the file is missing
        or malformed.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        return {child.tag: child.text for child in root}
    except (OSError, ET.ParseError):
        return None
