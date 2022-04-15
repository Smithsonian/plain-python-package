# `plain_python_package`
A boilerplate for Python packages. It demonstrates a minimum of files needed to build a Python package that can be installed in a Python environment. It also includes some highly recommended practices, such as a test suite, `.gitignore`, and a `setup.cfg` file. The latter is now recommended over a `setup.py` file, which is more dynamic. (cf. [the docs](https://packaging.python.org/en/latest/tutorials/packaging-projects/#configuring-metadata))

# Installation
```commandline
# Optional: Activate/create a virtual environment.
pip install .
```

See [this page](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments) for creating a virtual environment with plain Python. [Anaconda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands) works, too.

# Testing

```commandline
pytest
```

# Github Actions
Commits and pull requests to `main` will trigger Github Actions that tests the package in a container-like environment. See `.github/workflows/pytest.yml`.
