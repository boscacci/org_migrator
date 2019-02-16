from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def mac_chromedriver_install():
	"""
	Needs building;
	Downloads and deposits mac chromedriver in /usr/bin
	"""

def next_check(driver):
	"""
	Checks for presence of 'next' button on repo list page.
	"""
	try:
		driver.find_element_by_link_text("Next")
		return True
	except:
		return False

def load_repos(username):
	"""
	Instantiates a webdriver;
	Returns list of given user's repo_names.
	"""
	driver = webdriver.Chrome()
	driver.get(f"https://github.com/{username}?tab=repositories")
	repo_names = []
	while True:
		repo_names.extend([repo_name.text for repo_name in driver.find_elements_by_tag_name("h3")][2:])
		if next_check(driver):
			next_link = driver.find_element_by_link_text("Next")
			next_link.click()
			driver.implicitly_wait(1)
		else: 
			break
	driver.close()
	return repo_names

def filter_repos(repo_names, search_string):
	"""
	Returns filtered list of repo names that include given search string.
	"""
	desired_repos = []
	for repo_name in repo_names:
		if search_string in repo_name:
			desired_repos.append(repo_name)
	return desired_repos

def log_in():
	"""
	Logs your webdriver into your github.
	Returns logged-in web-driver.
	"""
	global username
	username = input("\nWhat's your username?\n")
	password = input("\nWhat's your password?\n")
	print('\n')
	driver = webdriver.Chrome()
	driver.get("https://github.com/login")
	login_field = driver.find_element_by_id("login_field")
	pword_field = driver.find_element_by_id("password")
	login_field.send_keys(username)
	pword_field.send_keys(password)
	pword_field.send_keys(Keys.RETURN)
	return driver

def transfer_an_org(driver, repo_name, new_org_name):
	"""
	Does all the clicking and typing to transfer a repo to an org.

	Feed it a logged-in driver, the repo to transfer, the org name.
	"""
	driver.get(f"https://github.com/{username}/{repo_name}")
	settings_button = driver.find_element_by_xpath(\
		"//*[@id='js-repo-pjax-container']/div[1]/nav/a[3]")
	
	settings_button.click()
	driver.implicitly_wait(1)
	transfer_button = driver.find_element_by_xpath(\
		"//*[@id='options_bucket']/div[8]/ul/li[2]/details/summary")
	
	transfer_button.click()
	driver.implicitly_wait(1)
	repo_field = driver.find_element_by_id(\
		"confirm_repository_name")
	
	confirm_new_field = driver.find_element_by_id(\
		"confirm_new_owner")
	
	repo_field.send_keys(repo_name)
	confirm_new_field.send_keys(new_org_name)
	
	transfer_final_button = driver.find_element_by_xpath(\
		"//*[@id='options_bucket']/div[8]/ul/li[2]/details/"
		"details-dialog/div[3]/div/form/button")

	transfer_final_button.click()
	
	pass

