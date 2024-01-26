#!/usr/bin/env python3
""" Pagination / Hypermedia pagination module """
import csv
from typing import List, Tuple, Dict


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
        """
        Finds the correct indices to paginate the dataset correctly and
        returns the appropriate page of the dataset

        Args:
            page (int): The current page
            page_size (int): Total number of pages

        Returns:
            List: A list containing the correct list of rows
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_index, end_index = self.index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """
        Returns a tuple containing a start and end index based on the
        range of indices in the pagination parameters

        Args:
            page (int): the page number
            page_size (int): total number of pages
        """
        start_index = (page - 1) * page_size
        end_index = start_index + page_size

        return start_index, end_index

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns a dictionary with key-value pairs for pagination details

        Args:
            page (int): The page number
            page_size (int): Total number of pages
        """
        page_details = {}
        page_data = self.get_page(page, page_size)
        total_pages = len(self.dataset()) // page_size
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        page_details['page_size'] = len(page_data)
        page_details['page'] = page
        page_details['data'] = page_data
        page_details['next_page'] = next_page
        page_details['prev_page'] = prev_page
        page_details['total_pages'] = total_pages

        return page_details
