# Basic Conda Package Cookiecutter
A cookiecutter to generate a very basic conda package including framework for cli, a conda recipe, and auto-release using rever. 

## Quickstart
Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher):

```
pip install -U cookiecutter
```

Generate a Python package project:

```
cookiecutter https://github.com/kcpevey/cookiecutter-basic-conda.git
```

## Features
* Testing setup
* Release automation with [rever](https://regro.github.io/rever-docs/)
* Conda recipe structure setup
* Command line interface using Click (optional)

## Directory structure
This cookiecutter package generates the following directory structure:  

```
├── .gitignore          <- file types for git to ignore
├── CHANGELOG.rst       <- changelog for release, auto-filled by rever
├── LICENSE             <- license file
├── README.md           <- top-level README for developers using this project.
├── rever.xsh           <- rever config
├── setup.cfg           <- setup config
├── setup.py            <- makes this project pip installable with `pip install -e`
│
├── conda.recipe
│   └── meta.yaml       <- environment requirements for the conda recipe
│
├── news
│   └── TEMPLATE.rst    <- template for the changelog to be autofilled by rever
│
├── package_name
│   ├── __init__.py     <- makes package_name a Python module
│   ├── __main__.py     <- framework for cli
│   └── cli.py          <- framework for cli
│
└── tests
    ├── __init__.py     <- makes tests a Python module
    └── test_cli.py     <- basic cli test
```
