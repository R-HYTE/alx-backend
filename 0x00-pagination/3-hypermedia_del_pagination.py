#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination

This module provides a Server class for paginating a database of
popular baby names. It includes methods to retrieve paginated data and
hypermedia pagination details, ensuring resilience to deletions from the
dataset between queries.

The dataset is loaded from a CSV file and indexed by sorting position, allowing
efficient retrieval of specific pages and pagination details.

Key functionalities:
- indexed_dataset: Loads and indexes the dataset,
  ensuring efficient pagination.
- get_hyper_index: Retrieves paginated data and hypermedia pagination details,
  handling deletions from the dataset between queries.
"""

import csv
from typing import List, Dict, Optional


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return paginated data and hypermedia pagination details.

        Args:
        - index (int, optional): The current start index of the return page.
                                 Defaults to None.
        - page_size (int, optional): The size of the page. Defaults to 10.

        Returns:
        A dictionary containing pagination details including index, data,
        page_size, and next_index.

        Raises:
        AssertionError: If index is out of range or invalid.
        """
        assert index is not None and isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        indexed_dataset = self.indexed_dataset()
        total_items = len(indexed_dataset)
        assert index < total_items

        data = []
        current_index = index

        while len(data) < page_size and current_index < total_items:
            if current_index in indexed_dataset:
                data.append(indexed_dataset[current_index])
            current_index += 1

        next_index = current_index if current_index < total_items else None

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index
        }
