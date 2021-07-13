from selenium import webdriver
import time
from time import sleep

INSTAGRAM_LOGIN_USERNAME = "Enter Your Username"
INSTAGRAM_LOGIN_PASSWORD = "Enter Your Password"
BOOKMARK_URL = "Enter URL of Bookmarks Collection to be cleared"

# Driver setup and load
driver = webdriver.Chrome("Enter Path To Webdriver")
driver.get("https://www.instagram.com/")

print("Bot is Active for: ", INSTAGRAM_LOGIN_USERNAME)

# Login to Instagram
sleep(3)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(INSTAGRAM_LOGIN_USERNAME)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(INSTAGRAM_LOGIN_PASSWORD)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()

# Naviage to Bookmarks page
sleep(5)
driver.get(BOOKMARK_URL)


# Click on first element
sleep(5)
bookmarksConnection = driver.find_elements_by_class_name('Nnq7C')

# Start Timer
startTime = time.time()


# Enter inside the Collection Row
for row in bookmarksConnection:

	images = row.find_elements_by_class_name('v1Nh3')
	print("Number of Images in Row: ", len(images))

	# Enter single Images of a Collection Row
	for image in images:
		# Click on the Image
		sleep(1)
		image.click()

		sleep(2)
		# Remove from bookmarks
		image.find_element_by_xpath("(//button[@class='wpO6b  '])[5]").click()

		driver.find_element_by_xpath("/html/body/div[5]/div[3]/button").click()

		print("REMOVED AN IMAGE!")


endTime = time.time()
totalTime = endTime - startTime

print("Time Elapsed: ", totalTime, " seconds")
print("All Bookmarks removed from Collection")