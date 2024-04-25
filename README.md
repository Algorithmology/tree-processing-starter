# 🔬 Processing Filesystem Trees

[![build](../../actions/workflows/build.yml/badge.svg)](../../actions/)
![Platforms: Linux, MacOS, Windows](https://img.shields.io/badge/Platform-Linux%20%7C%20MacOS%20%7C%20Windows-blue.svg)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Commits: Conventional](https://img.shields.io/badge/Commits-Conventional-blue.svg)](https://www.conventionalcommits.org/en/v1.0.0/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## ✨ Table of Contents

<!---toc start-->

* [🔬 Processing Filesystem Trees](#-processing-filesystem-trees)
  * [✨ Table of Contents](#-table-of-contents)
  * [🏁 Introduction](#-introduction)
  * [🤝 Seeking Assistance](#-seeking-assistance)
  * [🛫 Project Overview](#-project-overview)
  * [🎉 Program Specification](#-program-specification)

<!---toc end-->

## 🏁 Introduction

If you are a student completing this project as part of a class at Allegheny
College, you can check the schedule on the course web site for the due date or
ask the course instructor for more information about the due date or check the
due date by clicking the appropriate box inside of this file. Please note that
the content provided in the `README.md` file for this GitHub repository is an
overview of the project and thus may not include the details for every step
needed to successfully complete every project deliverable. This means that you
may need to schedule a meeting during the course instructor's office hours to
discuss aspects of this project. Finally, it is important to point out that
your repository for this project was created from the GitHub repository
template called
[tree-processing-starter](https://github.com/Algorithmology/tree-processing-starter);
you can check this repository for any updates to this project's documentation
or source code!

## 🤝 Seeking Assistance

Even though the course instructor will have covered all of the concepts central
to this project before you start to work on it, please note that not every
detail needed to successfully complete the assignment will have been covered
during prior classroom sessions. This is by design as an important skill that
you must practice as an algorithm engineer is to search for and then understand
and ultimately apply the technical content found in additional resources.

## 🛫 Project Overview

This project invites you to implement and use a program called `treeprocessor`
that performs a recursive traversal of a file system and then produces the
following output:

- A visualization of the filesystem's files and directories, expressed in a
hierarchical tree through the use of the `rich` package.
- A listing of each of the files discovered through the filesystem traversal
that includes the number of bytes used to store the file on the filesystem.
- A summary of key statistics about the filesystem, including:
  - The minumum and maximum file sizes.
  - The fully qualified name(s) of the files with the minimum and maximum sizes.
  - The average file size of all of the files in the traversed filesystem.

After cloning this repository to your computer, please take the following steps
to get started on the project:

- To install the necessary software for running the `treeprocessor` program that
you will create as a part of this project, you should install the
[`devenv`](https://devenv.sh/getting-started/) tool, bearing in mind that it is
not necessary for you to install the `cachix` program referenced by these
installation instructions. Please note that students who are using Windows 11
should first install Windows subsystem for Linux (`wsl2`) before attempting to
install `devenv`. Once you have installed `devenv` and cloned this repository to
your computer, you can `cd` into the directory that contains the
`pyproject.toml` file and then type `devenv shell`. It is important to note that
the first time you run this command it may complete numerous steps and take a
considerable amount of time.
- Once this command completes correctly, you will have a Python development
environment that contains Python `3.11.6` and Poetry `1.7.1`! You can verify
that you have the correct version of these two programs by typing:
  - `python --version` (note that you should see `3.11.6`)
  - `poetry --version` (note that you should see `1.7.1`)
- If some aspect of the installation with `devenv` did not work correctly, then
please resolve what is wrong before proceeding further! Alternatively, you may
install the aforementioned versions of Python and Poetry on your laptop. With
that said, please make sure that you only use the specified versions of Python
and Poetry to complete this project. This means that, to ensure that the results
from running the micro-benchmarks are consistent and, as best as is possible,
comparable to the results from other computers, you should use exactly the
specified version of either Python or Poetry.
- Before moving to the next step, you may need to again type `poetry install` in
order to avoid the appearance of warnings when you next run the `treeprocessor`
program. Now you can type the command `poetry run treeprocessor --help` and
explore how to use the program.

## 🎉 Program Specification

Before implementing the program so that it adheres to the following
requirements and produces the expected output, please note that the program
will not work unless you add the required source code at the designated `TODO`
markers. With that said, after you complete a correct implementation of all the
`treeprocessor`'s features you can run it with the command `poetry run
treeprocessor --directory example-dir` and see that it produces output like the
following. Please note that while the following example illustrates the type of
output that the `treeprocessor` might produce it may differ from the output that you see when it runs in GitHub Actions or on your laptop because of the fact that your operating system and computer architecture may differ from the one used to generate this output.

```text
File system traversal tool

Chosen directory: example-dir

File system tree hierarchy

example-dir
├── nested-dir
│   ├── filethree
│   └── filetwo
├── filefour
└── fileone

File system tree sizes (in bytes)

/home/gkapfham/working/teaching/github-classroom/algorithmology/algorithm-engineering/solutions/tree-processing-solution/t
reeprocessor/example-dir/nested-dir/filethree: 11 bytes
/home/gkapfham/working/teaching/github-classroom/algorithmology/algorithm-engineering/solutions/tree-processing-solution/t
reeprocessor/example-dir/nested-dir/filetwo: 28 bytes
/home/gkapfham/working/teaching/github-classroom/algorithmology/algorithm-engineering/solutions/tree-processing-solution/t
reeprocessor/example-dir/filefour: 10 bytes
/home/gkapfham/working/teaching/github-classroom/algorithmology/algorithm-engineering/solutions/tree-processing-solution/t
reeprocessor/example-dir/fileone: 25 bytes

File system tree statistics

Minimum file size: 10 bytes
Files with minimum size:
  - /home/gkapfham/working/teaching/github-classroom/algorithmology/algorithm-engineering/solutions/tree-processing-soluti
on/treeprocessor/example-dir/filefour
Maximum file size: 28 bytes
Files with maximum size:
  - /home/gkapfham/working/teaching/github-classroom/algorithmology/algorithm-engineering/solutions/tree-processing-soluti
on/treeprocessor/example-dir/nested-dir/filetwo
Average file size: 18.50 bytes
```

Please note that your implementation of the `treeprocessor` program should work
for any type of filesystem structure, excepting the fact that it does not need
to handle symbolic links that may introduce cycles into the filesystem. If you
study the files in the `treeprocessor/` directory you will see that they have
many `TODO` markers that designate the functions you must implement so as to
ensure that `treeprocessor` runs the in the desired fashion and produces the
correct output. Once you complete a task associated with a `TODO` marker, make
sure that you delete it and revise the prompt associated with the marker into a
meaningful comment. As you complete this project, please make sure that you
design your own `treeprocessor` that can work for filesystems on Windows,
MacOS, and Linux, as confirmed by the successful run of the program in GitHub
Actions and on your laptop. It is also important to note that the
`treeprocessor` that you implement should work for much larger directory
structures than that which is represented by the `example-dir/` provided in
this repository. Finally, please make sure that you focus on these key issues
to ensure that you meet the baseline requirements:

- If you have already installed the
[GatorGrade](https://github.com/GatorEducator/gatorgrade) program that runs the
automated grading checks provided by
[GatorGrader](https://github.com/GatorEducator/gatorgrader) you can, from the
repository's base directory, run the automated grading checks by typing
`gatorgrade --config config/gatorgrade.yml`.
- You may also review the output from running GatorGrader in GitHub Actions.
- Don't forget to provide all of the required responses to the technical writing
prompts in the `writing/reflection.md` file.
- Please make sure that you completely delete the `TODO` markers and their
labels from all of the provided source code. This means that instead of only
deleting the `TODO` marker from the code you should delete the `TODO` marker and
the entire prompt and then add your own comments to demonstrate that you
understand all of the source code in this project.
- Please make sure that you also completely delete the `TODO` markers and their
labels from every line of the `writing/reflection.md` file. This means that you
should not simply delete the `TODO` marker but instead delete the entire prompt
so that your reflection is a document that contains polished technical writing
that is suitable for publication on your professional web site.
