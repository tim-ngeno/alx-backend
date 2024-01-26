#!/usr/bin/env python3
""" Simple indexing helper module """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing a start and end index based on the range
    of indices in the pagination parameters

    Args:
        page (int): the page number
        page_size (int): total number of pages
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
