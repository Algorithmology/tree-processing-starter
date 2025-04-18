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

# TODO: Add comments to explain the steps in the main function


@cli.command()
def main(directory: Path = typer.Option(...)):
    """Traverse a filesystem tree."""
    console.print("\n[bold red]File system traversal tool[/bold red]\n")
    console.print(f"Chosen directory: {directory}")
    (filesystem_tree, filesystem_tree_sizes) = build_directory_tree(
        directory, None, {}
    )
    console.print("\n[bold red]Filesystem tree hierarchy[/bold red]\n")
    console.print(filesystem_tree)
    console.print("\n[bold red]Filesystem tree sizes (in bytes)[/bold red]\n")
    for path, size in filesystem_tree_sizes.items():
        console.print(f"{path}: {size} bytes")
    min_size, min_files, max_size, max_files, avg_size = calculate_file_stats(
        filesystem_tree_sizes
    )
    console.print("\n[bold red]Filesystem tree statistics[/bold red]\n")
    console.print(f"Minimum file size: {min_size} bytes")
    console.print("Files with minimum size:")
    for file in min_files:
        console.print(f"  - {file}")
    console.print(f"Maximum file size: {max_size} bytes")
    console.print("Files with maximum size:")
    for file in max_files:
        console.print(f"  - {file}")
    console.print(f"Average file size: {avg_size:0.2f} bytes")
