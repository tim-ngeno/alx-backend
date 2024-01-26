# API Pagination
## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
    - [Understanding Simple Page and Page Size Parameters](#understanding-simple-page-and-page-size-parameters)
3. [Enhancing Pagination](#enhancing-pagination)
    - [Leveraging Hypermedia Metadata](#leveraging-hypermedia-metadata)
4. [Advanced Pagination Strategies](#advanced-pagination-strategies)
    - [Handling Pagination in a Deletion-Resilient Manner](#handling-pagination-in-a-deletion-resilient-manner)
        - [Timestamp-based Pagination](#timestamp-based-pagination)
        - [Cursor-based Pagination](#cursor-based-pagination)

## Introduction
Pagination is a crucial concept in API development, allowing efficient handling of large datasets.

## Basic Concepts:
- **Page Size**: The number of items returned in a single API response.

- **Page Number (Offset)**: The specific set or "page" of data you are requesting.

- **Total Items**: The total number of items available across all pages.

## Why Pagination?
- Efficiency: Reduces the load on both the server and client side by fetching only a subset of data.

- Performance: Large datasets can be split into smaller parts, improving response time.

## API Pagination Techniques:
### Offset-Based Pagination:

Uses an offset (page number) and a limit (page size) to fetch data.
Commonly uses parameters like page and page_size.

### Cursor-Based Pagination:
Uses a specific identifier (cursor) to determine the next set of data.
Removes the dependency on page numbers and allows for more flexibility.


## Getting Started

### Understanding Simple Page and Page Size Parameters

At the foundational level, pagination involves the use of `page` and `page_size` parameters. These simple yet powerful parameters allow you to control the presentation of data in manageable chunks.

Example API Request:

```http
GET /api/data?page=1&page_size=10
```

This request retrieves the first page with 10 items. Adjust the `page` parameter to navigate through pages and `page_size` to control the number of items per page.

## Enhancing Pagination

### Leveraging Hypermedia Metadata

Hypermedia-driven APIs provide additional metadata for navigating through paginated results. This metadata includes links to the next, previous, first, and last pages, facilitating a more dynamic and navigable experience.

Example API Response:

```json
{
  "data": [...],
  "meta": {
    "pagination": {
      "current_page": 1,
      "total_pages": 5,
      "links": {
        "next": "/api/data?page=2",
        "prev": null,
        "first": "/api/data?page=1",
        "last": "/api/data?page=5"
      }
    }
  }
}
```

Explore and utilize the links provided in the `meta.pagination.links` section for seamless navigation between different pages.

## Advanced Pagination Strategies

### Handling Pagination in a Deletion-Resilient Manner

Dealing with deletions during pagination requires robust strategies to maintain data consistency. Two advanced strategies include timestamp-based pagination and cursor-based pagination.

#### Timestamp-based Pagination

Sort data by timestamps and paginate using time ranges.

Example API Request:

```http
GET /api/data?start_timestamp=1630435200&end_timestamp=1630518000
```

#### Cursor-based Pagination

Use a cursor (unique identifier) to paginate efficiently.

Example API Request:

```http
GET /api/data?cursor=abc123&page_size=10
```

Adapt these strategies based on specific requirements and API capabilities to ensure resilience in the face of deletions and maintain a consistent user experience.

### Working with Pagination in Python:

Let's consider an example where you have an API that returns a list of items, and you want to retrieve them in pages.

```python
import requests

def get_paginated_data(api_url, page=1, page_size=10):
    params = {'page': page, 'page_size': page_size}
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None

# Example usage
api_url = 'https://example.com/api/items'
page_number = 1
page_size = 10

while True:
    data = get_paginated_data(api_url, page=page_number, page_size=page_size)

    if not data:
        break

    # Process the retrieved data
    print(f"Processing Page {page_number}")
    for item in data['items']:
        print(item)

    total_items = data['total_items']
    page_number += 1

    if page_number * page_size > total_items:
        break
```

Using Cursor-Based Pagination:
```python
import requests

def get_paginated_data(api_url, cursor=None, page_size=10):
    params = {'cursor': cursor, 'page_size': page_size}
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None
```

## Example usage

```python
api_url = 'https://example.com/api/items'
cursor = None
page_size = 10

while True:
    data = get_paginated_data(api_url, cursor=cursor, page_size=page_size)

    if not data:
        break

    # Process the retrieved data
    print(f"Processing Page {data['page_number']}")
    for item in data['items']:
        print(item)

    cursor = data['next_cursor']

    if not cursor:
        break
```
---
