import xml.etree.ElementTree as ET
import numpy as np
import math

class SVGPoints:
    
    def __init__(self) -> None:
        
        self.ns = "http://www.w3.org/2000/svg"
        self.path =  "../data/marker.svg"

        self.alpha_deg   = -15
        self.num_markers = 24
        self.base_points = self._get_base_points()
        self.points = [None] * self.num_markers
    
    def _get_base_points (self):
        tree = ET.parse(self.path)
        root = tree.getroot()
        
        nodes = [node for node in root[1] if node.tag == "{%s}g" % self.ns]
        nodes.sort(key=lambda node: int(node.get("id").split("g")[1]))

        base_polygon = nodes[0].find("ns:polygon", namespaces = { "ns": self.ns })
        return[ tuple([float(c) for c in (x + ",0").split(',')]) for x in base_polygon.get("points").strip().split(" ")]


    def get_reference_points (self, value):
        
        if value < 0 or value > self.num_markers - 1:
            raise Exception("Invalid marker value " + value)

        if self.points[value] is None:
            rad_alpha = math.radians(self.alpha_deg * (value))
            points    = []

            for point in self.base_points:
                x, y, _ = point
                x1      = round(x * math.cos(rad_alpha) - y * math.sin(rad_alpha), 2)
                y1      = round(x * math.sin(rad_alpha) + y * math.cos(rad_alpha), 2)
                points.append((x1, y1, 0.0))
            
            self.points[value] = np.array(points)

        return self.points[value]




