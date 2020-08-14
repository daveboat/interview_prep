from typing import List, Tuple


class HorizontalLine:
    """
    A class representing a horizontal line
    """
    def __init__(self, x1: float, x2: float, y: float):
        self.x1 = x1
        self.x2 = x2
        self.y = y


class VerticalLine:
    """
    A class representing a vertical line
    """
    def __init__(self, x: float, y1: float, y2: float):
        self.x = x
        self.y1 = y1
        self.y2 = y2


class Overlap:
    """
    A class representing the overlap between two horizontal or two vertical lines
    """
    def __init__(self, x1: float, x2: float, y1: float, y2: float):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


def find_horizontal_overlap(h1: HorizontalLine, h2: HorizontalLine) -> Tuple[bool, Overlap]:
    # finds the overlap, as an Overlap object, between two horizontal lines. Returns a bool with whether not an overlap
    # exists between the two lines, and the overlap. The overlap is only meaningful if the bool is True.
    if min(h1.x2, h2.x2) > max(h1.x1, h2.x1):
        return True, Overlap(max(h1.x1, h2.x1), min(h1.x2, h2.x2), min(h1.y, h2.y), max(h1.y, h2.y))
    else:
        return False, Overlap(0, 0, 0, 0)


def find_vertical_overlap(v1: VerticalLine, v2: VerticalLine) -> Tuple[bool, Overlap]:
    # finds the overlap, as an Overlap object, between two vertical lines. Returns a bool with whether not an overlap
    # exists between the two lines, and the overlap. The overlap is only meaningful if the bool is True.
    if min(v1.y2, v2.y2) > max(v1.y1, v2.y1):
        return True, Overlap(min(v1.x, v2.x), max(v1.x, v2.x), max(v1.y1, v2.y1), min(v1.y2, v2.y2))
    else:
        return False, Overlap(0, 0, 0, 0)


def box_exists(ho: Overlap, vo: Overlap) -> bool:
    # check the condition for a box to exist given a horizontal overlap object and a vertical overlap object
    return ho.x1 <= vo.x1 and ho.x2 >= vo.x2 and vo.y1 <= ho.y1 and vo.y2 >= ho.y2


def count_boxes(horizontal_lines: List[HorizontalLine], vertical_lines: List[VerticalLine]) -> int:
    # Counts the number of boxes from a list of horizontal and a list of vertical lines

    # get number of lines in each list, for convenience
    n_horizontal = len(horizontal_lines)
    n_vertical = len(vertical_lines)

    # check the necessary condition on the number of lines
    if n_horizontal < 2 or n_vertical < 2:
        return 0

    # find all horizontal overlaps and vertical overlaps
    horizontal_overlaps = []
    for i in range(n_horizontal):
        for j in range(i + 1, n_horizontal):
            overlap_found, ho = find_horizontal_overlap(horizontal_lines[i], horizontal_lines[j])
            if overlap_found:
                horizontal_overlaps.append(ho)

    vertical_overlaps = []
    for i in range(n_vertical):
        for j in range(i + 1, n_vertical):
            overlap_found, vo = find_vertical_overlap(vertical_lines[i], vertical_lines[j])
            if overlap_found:
                vertical_overlaps.append(vo)

    # iterate over all horizontal and vertical overlaps, and find the number of boxes which are possible
    num_boxes = 0
    for ho in horizontal_overlaps:
        for vo in vertical_overlaps:
            if box_exists(ho, vo):
                num_boxes += 1

    return num_boxes


if __name__ == '__main__':
    horizontal_lines = [HorizontalLine(0.5, 2.5, 1), HorizontalLine(-1, 1, 2), HorizontalLine(1, 3, 1.5)]
    vertical_lines = [VerticalLine(1, 1, 2.5), VerticalLine(2, -1, 1.5), VerticalLine(1.5, 0, 3)]

    print(count_boxes(horizontal_lines, vertical_lines))

