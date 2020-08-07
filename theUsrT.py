def executeBot():

	input_email_id = "benitocamelo4vcs@gmail.com"
	input_passw = "desig654?"


	driver.get('https://www.facebook.com/login.php?login_attempt=1&lwv=110')
	print("...Facebook is open...")



	#email = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/form/div/div[1]/input")
	email = driver.find_element_by_xpath('//*[@id="email"]')


	email.send_keys(input_email_id)
	print("Email OK")

	password = driver.find_element_by_name('pass')

	password.send_keys(input_passw)
	print("Password OK")

	#(//*[@id="loginbutton"])

	button =driver.find_element_by_xpath("//*[@id='loginbutton']")
	button.click()

	print("Cuenta de facebook abierta...")


#executeBot()
