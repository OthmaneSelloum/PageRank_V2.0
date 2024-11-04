import xml.etree.ElementTree as ET
import PageRankScore as PR


def page_rank_score(xml_file, epsilon=1e-6):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    mat_adj = []

    for row in root.findall('row'):
        current_row = [int(cell.text) for cell in row.findall('cell')]
        mat_adj.append(current_row)
    return PR.page_rank_score(mat_adj, epsilon)
