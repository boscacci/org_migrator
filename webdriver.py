from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def load_repos(username):
	
	driver = webdriver.Chrome()
	driver.get(f"https://github.com/{username}?tab=repositories")
	
	repo_names = []

	while driver.find_element_by_link_text("Next"):

		repo_names.extend([repo_name.text for repo_name in 
		driver.find_elements_by_tag_name("h3")][2:])

		next_link = driver.find_element_by_link_text("Next")

		next_link.click()

	import pdb; pdb.set_trace()

	elem.clear()
	elem.send_keys("pycon")
	elem.send_keys(Keys.RETURN)
	
	assert "No results found." not in driver.page_source

	driver.close()