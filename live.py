from pywebcopy import save_website

# Prompt the user to input the URL
url = input("Enter the URL of the website you want to save: ")

save_website(
    url=url,
    project_folder=r"D:\Projects",
    project_name="my_site",
    bypass_robots=True,
    debug=True,
    open_in_browser=False,  # Set this to False if running in an environment without a browser
    delay=None,
    threaded=False,
)
