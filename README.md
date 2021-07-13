
# Instagram Bookmark Remover Bot

A bot which automatically removes all posts in a desired Instagram bookmarks collection.
### Requirements
 - Latest version of Python3 must be installed
 - Ensure `venv` is installed (Should be by default with recent versions of Python3)
 - Ensure latest version of PIP is installed by running: `python -m pip install --upgrade pip`
 - Download the [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) that matches the version of Chrome on your system (I recommend saving it within the same directory)


## Environment Setup
If running any `python` commands in your terminal raises an error in the line of, `python command not known` then use `python3` command instead.

 - Create a new virtual environment by running command: `python -m venv instagramBotEnv`
 - Install required modules by running command: `pip install -r requirements.txt` or 
`python -m pip install -r requirments.txt`

## Code Setup
Use any code editor to fill in the all the variables with your Instagram account credentials, which allow the bot to access your bookmarked posts.

 - Variable `INSTAGRAM_LOGIN_USERNAME` must have value `String` with your Instagram Username
 - Variable `INSTAGRAM_LOGIN_PASSWORD` must have value `String` with your Instagram Password
 - Variable `BOOKMARK_URL` must have value `String` with the URL to the Bookmark Collection you wish to clear, example `https://www.instagram.com/charlesrossouww/saved/all-posts/`
 - Variable `driver` must have [File Path](https://medium.com/@Linda_Ikechukwu/understanding-file-paths-165c07ec5cf0) to the downloaded [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) that matches the version of Chrome that's installed on your system

Now you can run the code with the command: `python main.py`
