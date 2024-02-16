# PyWebCopy: Save Website

PyWebCopy is a Python library that allows you to save complete websites locally. This README provides an overview of how to use the `save_website` function to save a website to your local machine.

## Installation

You can install PyWebCopy via pip:

```bash
pip install pywebcopy
```

## Usage

```python
from pywebcopy import save_website

save_website(
    url="https://nashvillerenovators.com/",
    project_folder=r"D:\Projects",
    project_name="my_site",
    bypass_robots=True,
    debug=True,
    open_in_browser=True,
    delay=None,
    threaded=False,
)
```

### Parameters

- `url` (str): The URL of the website you want to save.
- `project_folder` (str): The folder where you want to save the website.
- `project_name` (str): The name you want to give to the saved website folder.
- `bypass_robots` (bool): If `True`, ignores robots.txt restrictions.
- `debug` (bool): If `True`, enables debug mode for detailed logging.
- `open_in_browser` (bool): If `True`, opens the saved website in the default web browser after completion.
- `delay` (float): The delay in seconds between each request. Useful for avoiding being blocked by websites with aggressive anti-bot measures.
- `threaded` (bool): If `True`, enables multi-threading for faster downloading.

## Examples

### Basic Usage

```python
from pywebcopy import save_website

save_website(
    url="https://nashvillerenovators.com/",
    project_folder=r"D:\Projects",
    project_name="my_site",
)
```

This will save the website https://nashvillerenovators.com/ to the folder "D:\Projects\my_site".

### Advanced Usage

```python
from pywebcopy import save_website

save_website(
    url="https://nashvillerenovators.com/",
    project_folder=r"D:\Projects",
    project_name="my_site",
    bypass_robots=True,
    debug=True,
    open_in_browser=True,
    delay=2.0,
    threaded=True,
)
```

This will save the website with advanced options like bypassing robots.txt restrictions, enabling debug mode, opening the saved website in the browser after completion, adding a delay of 2 seconds between requests, and using multi-threading for faster downloading.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
