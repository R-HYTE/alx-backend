# Caching Algorithms Project

## Overview
This project explores various caching algorithms to understand their implementation and performance implications. The algorithms covered include FIFO, LIFO, LRU, MRU, and LFU.

## Learning Objectives
By the end of this project, you will be able to explain:
- What a caching system is and its purpose
- The meanings of FIFO, LIFO, LRU, MRU, and LFU
- The limitations of caching systems

## Requirements
- Python 3.7 on Ubuntu 18.04 LTS
- Code must follow `pycodestyle` (version 2.5)
- All files must be executable and include proper documentation

## Base Class: BaseCaching
All caching classes inherit from `BaseCaching`, which provides basic structure and a dictionary for storing data.

## Caching Classes
1. **BasicCache**: No limit on the number of items.
2. **FIFOCache**: Discards the first item added when the limit is reached.
3. **LIFOCache**: Discards the last item added when the limit is reached.
4. **LRUCache**: Discards the least recently used item when the limit is reached.
5. **MRUCache**: Discards the most recently used item when the limit is reached.
6. **LFUCache**: Discards the least frequently used item; if there's a tie, uses LRU.
