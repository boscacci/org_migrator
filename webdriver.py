from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def page_check():
	try:
		driver.find_element_by_link_text("Next")
		return True
	except:
		return False

def load_repos(username):
	"""Returns list of repo_names"""
	
	driver = webdriver.Chrome()
	driver.get(f"https://github.com/{username}?utf8=%E2%9C%93&tab=repositories&q=&type=public&language=python")
	
	repo_names = []

	while True:

		repo_names.extend([repo_name.text for repo_name in driver.find_elements_by_tag_name("h3")][2:])

		if page_check():

			next_link = driver.find_element_by_link_text("Next")

			next_link.click()

			driver.implicitly_wait(1)

		else: 
			break

	driver.close()

	return repo_names

def filter_repos(repo_names, search_string):
	desired_repos = []
	for repo_name in repo_names:
		if search_string in repo_name:
			desired_repos.append(repo_name)
	return desired_repos