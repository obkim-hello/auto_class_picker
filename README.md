# auto_class_picker
This is a auto classes picker for York University 
USE IT ON YOUR OWN RISK (you will get ban if you try too many time in a short time)

If you look carefully there are many sleep() in the code, this is for simulate human operation

1. Download Pycharm: https://www.jetbrains.com/pycharm/download/#section=mac

2. Download chromedriver: https://chromedriver.chromium.org/downloads (download the one match your chrome version)

3. import post.py

4. In terminal type : pip install selenium

5. In line 4: change the path to wherever you downloaded you chromedrive

6. In line 8 and 10: put your username and password in

7. In line 5: put the number of time that you want to try

8. In line 33: put the amoung of time that you want to wait in each try cycle 

9. If you wish to add mutiple classes simplely copy following to before code: driver.close()

    driver.find_element_by_name('5.1.27.7.7').send_keys("the class code you wish to add ")
    sleep(4)
    driver.find_element_by_name('5.1.27.7.9').click()
    sleep(4)
    driver.find_element_by_name('5.1.27.11.9').click()
    sleep(4)
    driver.find_element_by_name('5.1.27.27.9').click()
    sleep(4)
    driver.find_element_by_name('5.1.3.1.1').click()
    sleep(4)

Now you can run the script 
