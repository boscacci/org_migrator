# Org Migrator

Spins up a Selenium chrome driver to transfer repos from one github org to another in batch. Saves you the trouble of some potentially tedious clicking around.


## Prereq

Install selenium, put their weird file where it's supposed to go in /usr/local/bin. Read their docs for ref.

## Usage

Run: 
$ python3 -i webdriver.py

>> all_repos = load_repos('your_username')

(A webdriver should appear and get a list of your repos)

>> filtered_repos = filter_repos(all_repos, "some_search_string")

>> logged_in_driver = log_in()

(Don't close the browser!)

>> [transfer_an_org(logged_in_driver, repo, 'new_org_name') for repo in filtered_repos]
