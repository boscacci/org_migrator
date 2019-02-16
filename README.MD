# Org Migrator

Spins up a Selenium chrome driver to transfer repos from one github org to another in batch. Saves you the trouble of some potentially tedious clicking around.

## Usage

Prereq: Install selenium, put their weird file where it's supposed to go in /usr/local/bin. Read their docs for ref.

Run: 
$ python3 -i webdriver.py

1. all_repos = load_repos('your_username')

(A webdriver should appear and get a list of your repos)

2. filtered_repos = filter_repos(all_repos, "some_search_string")

3. logged_in_driver = log_in()

(Don't close the browser!)

4. [transfer_an_org(logged_in_driver, repo, 'new_org_name') for repo in filtered_repos]
