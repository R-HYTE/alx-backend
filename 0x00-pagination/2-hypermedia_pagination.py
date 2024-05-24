#!/usr/bin/env python3
"""
This module provides a Server class for paginating a dataset of
popular baby names. It includes the implementation of pagination methods
to return specific pages and hypermedia pagination details.

The dataset is loaded from a CSV file and cached to improve performance.
The module includes helper functions to calculate index ranges and
methods to return paginated data along with hypermedia pagination details.

Key functionalities:
- index_range: Calculates the start and end indices for pagination.
- Server class:
  - dataset: Loads and caches the dataset.
  - get_page: Returns a specific page of the dataset.
  - get_hyper: Returns a dictionary with pagination details including next
  and previous pages.
"""

import csv
import math
from typing import List, Dict, Optional


def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(
        self, page: int = 1, page_size: int = 10
    ) -> Dict[str, Optional[object]]:
        """Return a dictionary containing pagination details.
        """
        data = self.get_page(page, page_size)
        total_data = len(self.dataset())
        total_pages = math.ceil(total_data / page_size)

        hypermedia = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }

        return hypermedia
