"""Traverse a file system tree."""

from pathlib import Path
from typing import Dict, Tuple, Union

from rich.tree import Tree


def get_file_size(path: Path) -> Tuple[int, str]:
    """Compute the size of a file in bytes."""
    # TODO: implement this function so that it returns:
    # (1) the size of the file in bytes and 
    # (2) an error message if there was any problem
    # associated with computing the file size
    return (0, "")


def get_full_path(path: Path) -> str:
    """Get the fully qualified path name for a file."""
    # TODO: implement this function so that it returns the
    # fully qualified path name for a file; this means
    # that it must return all of the directories and
    # sub-directories that contain the file and then
    # also give the name of the file in a single string
    return ""


def build_directory_tree(
    path: Path, tree: Union[Tree, None], sizes: Dict[str, int] = {}
) -> Tuple[Tree, Dict]:
    """Recursively build a tree of the directory structure."""
    # TODO: implement this function so that it builds a tree
    # representation of the directory structure and also
    # computes the sizes of the files in the directory
    # TODO: ensure that this function is implemented recursively;
    # this means that the function should continue to call itself
    # until it has traversed the entire directory structure after
    # starting at the specified path in the variable called path
    # TODO: the output of this function should be a tuple
    # that contains the following two values:
    # (1) the tree representation of the directory structure
    # (2) a dictionary that maps the file names to their sizes
    # TODO: make sure that the tree representation of the 
    # directory structure is built recursively and uses the
    # rich.tree module to create the tree; note that this is
    # important because using rich.tree will make it easier
    # to visualize the tree in the output of this tool
    return (None, None)
