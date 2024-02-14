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
