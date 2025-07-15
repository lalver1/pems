# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/lalver1/pems/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                          |    Stmts |     Miss |   Branch |   BrPart |   Cover |   Missing |
|---------------------------------------------- | -------: | -------: | -------: | -------: | ------: | --------: |
| pems/\_\_init\_\_.py                          |        5 |        2 |        0 |        0 |     60% |       5-7 |
| pems/core/\_\_init\_\_.py                     |        0 |        0 |        0 |        0 |    100% |           |
| pems/core/context\_processors.py              |        6 |        1 |        0 |        0 |     83% |        12 |
| pems/core/management/\_\_init\_\_.py          |        0 |        0 |        0 |        0 |    100% |           |
| pems/core/management/commands/\_\_init\_\_.py |        0 |        0 |        0 |        0 |    100% |           |
| pems/core/management/commands/ensure\_db.py   |      181 |        4 |       42 |        4 |     96% |73, 87-89, 99, 103->exit, 230->232, 300->304 |
| pems/core/middleware.py                       |        9 |        1 |        2 |        1 |     82% |        19 |
| pems/core/urls.py                             |        4 |        4 |        0 |        0 |      0% |       1-7 |
| pems/districts/\_\_init\_\_.py                |        0 |        0 |        0 |        0 |    100% |           |
| pems/districts/admin.py                       |        3 |        0 |        0 |        0 |    100% |           |
| pems/districts/apps.py                        |        3 |        0 |        0 |        0 |    100% |           |
| pems/districts/migrations/0001\_initial.py    |        5 |        0 |        0 |        0 |    100% |           |
| pems/districts/migrations/\_\_init\_\_.py     |        0 |        0 |        0 |        0 |    100% |           |
| pems/districts/models.py                      |        7 |        0 |        0 |        0 |    100% |           |
| pems/districts/urls.py                        |        4 |        4 |        0 |        0 |      0% |      5-10 |
| pems/districts/views.py                       |       17 |        0 |        0 |        0 |    100% |           |
| pems/settings.py                              |       53 |        2 |        6 |        1 |     95% |   126-127 |
| pems/urls.py                                  |        3 |        3 |        0 |        0 |      0% |       1-4 |
| pems/wsgi.py                                  |        4 |        4 |        0 |        0 |      0% |     10-16 |
| streamlit\_app/\_\_init\_\_.py                |        0 |        0 |        0 |        0 |    100% |           |
| streamlit\_app/main.py                        |       16 |        0 |        2 |        0 |    100% |           |
| streamlit\_app/utils.py                       |       35 |        0 |        4 |        0 |    100% |           |
|                                     **TOTAL** |  **355** |   **25** |   **56** |    **6** | **92%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/lalver1/pems/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/lalver1/pems/blob/python-coverage-comment-action-data/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/lalver1/pems/python-coverage-comment-action-data/endpoint.json)](https://htmlpreview.github.io/?https://github.com/lalver1/pems/blob/python-coverage-comment-action-data/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2Flalver1%2Fpems%2Fpython-coverage-comment-action-data%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/lalver1/pems/blob/python-coverage-comment-action-data/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.