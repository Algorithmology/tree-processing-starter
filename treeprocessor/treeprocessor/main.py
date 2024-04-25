"""Perform traversals of filesystem trees."""

from pathlib import Path

import typer
from rich.console import Console

from treeprocessor.analyze import calculate_file_stats
from treeprocessor.filesystem import build_directory_tree

# create a Typer object to support the command-line interface
cli = typer.Typer()

# create a console for display of rich text
console = Console()


@cli.command()
def main(directory: Path = typer.Option(...)):
    """Traverse a file system tree."""
    # display details about the configuration of the traversal tool
    console.print("\n[bold red]File system traversal tool[/bold red]\n")
    console.print(f"Chosen directory: {directory}")
    # traverse the filesystem tree
    (filesystem_tree, filesystem_tree_sizes) = build_directory_tree(
        directory, None, {}
    )
    # display the filesystem tree
    console.print("\n[bold red]File system tree hierarchy[/bold red]\n")
    console.print(filesystem_tree)
    # display the sizes of the files in the filesystem tree
    console.print("\n[bold red]File system tree sizes (in bytes)[/bold red]\n")
    for path, size in filesystem_tree_sizes.items():
        console.print(f"{path}: {size} bytes")
    # calculate statistics about the sizes of the files in the directory
    min_size, min_files, max_size, max_files, avg_size = calculate_file_stats(
        filesystem_tree_sizes
    )
    # display the statistics about the sizes of the files in the directory
    console.print("\n[bold red]File system tree statistics[/bold red]\n")
    console.print(f"Minimum file size: {min_size} bytes")
    console.print("Files with minimum size:")
    for file in min_files:
        console.print(f"  - {file}")
    console.print(f"Maximum file size: {max_size} bytes")
    console.print("Files with maximum size:")
    for file in max_files:
        console.print(f"  - {file}")
    console.print(f"Average file size: {avg_size:0.2f} bytes")
