"""Analyze the results from performing a tree traversal of a filesystem."""

from typing import Dict, List, Tuple


def calculate_file_stats(
    file_sizes: Dict[str, int],
) -> Tuple[int, List[str], int, List[str], float]:
    """Calculate statistics about the sizes of files in a directory."""
    # TODO: calculate the minimum, maximum, and average file sizes;
    # use the values function to get a list of the file sizes
    min_size = 0
    max_size = 0
    avg_size = 0
    # TODO: bearing in mind that more than one file might have the minimum or maximum size
    # use list comprehension to create a list of files with the minimum and maximum sizes
    min_files = []
    max_files = []
    # TODO: return the calculated statistics about the files and their sizes,
    # including the names of the files along with minimum and maximum sizes
    return (min_size, min_files, max_size, max_files, avg_size)
