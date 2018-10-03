from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import sys



#############
driver = webdriver.Chrome()
driver.get("https://www1.ticketmaster.com/event/0800543FDBC46486")


##<button title="Opens Captcha dialog box" id="find_tickets_action" type="button" class="button-large button" aria-describedby="tmplus-expanded-hover">Find Tickets</button>

time.sleep(10)
offer = driver.find_element_by_xpath("//*[@id='gotoffercode']")
driver.execute_script("arguments[0].click();",offer)

time.sleep(10)
#offerCode = find_element_by_class_name("mgRt5")

offerCode= driver.find_element_by_xpath("//*[@class='mgRt5']")

offerCode.send_keys("ONESHOT")
##OK
applybtn = find_element_by_xpath("//*[@class='button button-disabled']").submit()
okbtn= find_element_by_xpath("//*[@class='pw-popup-ok']").submit()


time.sleep(10)
findTickets = driver.find_element_by_xpath("//*[@id='find_tickets_action']")
driver.execute_script("arguments[0].click();",findTickets)

time.sleep(10)
#buy = driver.find_element_by_xpath("//*[@id='find_tickets_action']")
#driver.execute_script("arguments[0].click();",buy)


"""
file = open("Data.txt","w+")
file.write("* * * * *  Python Version * * * * * " + "\n"+ 
           sys.version + "\n" + "\n" +
           "* * * * * Data * * * * *" + "\n")


  ## define labels
labelLeft1 = driver.find_element_by_xpath("//div[@id='ticketFrame']/div[1]/div[2]/div[1]/h3[1]")
labelLeft2 = driver.find_element_by_xpath("//div[@id='ticketFrame']/div[1]/div[2]/div[1]/h3[2]")
labelLeft3 = driver.find_element_by_xpath("//div[@id='ticketFrame']/div[1]/div[2]/div[1]/h3[3]")
labelLeft4 = driver.find_element_by_xpath("//div[@id='ticketFrame']/div[1]/div[5]/h3")

time = driver.find_element_by_xpath("//div[@id='countdown_clock']/div[2]") 
## Values for Labels
valueRight1 = driver.find_element_by_xpath("//div[@id='ticketFrame']/div[1]/div[2]/div[1]/div[1]")
valueRight2 = driver.find_element_by_xpath("//div[@id='ticketFrame']/div[1]/div[2]/div[1]/div[2]")
valueRight3 = driver.find_element_by_xpath("//div[@id='ticketFrame']/div[1]/div[2]/div[1]/div[3]")
valueRight4 = driver.find_element_by_xpath("//div[@id='ticketFrame']/div[1]/div[5]/div[1]")

if ((labelLeft1.text == "Section")  and (labelLeft2.text == "Row") and (labelLeft3.text == "Seats") and (labelLeft4.text == "SUBTOTAL*")):
  #print ("Section " + valueRight1.text + "\n" + "Row " + valueRight2.text + "\n" +"Seats " + valueRight3.text + "\n" +"SUBTOTAL " + valueRight4.text)
  file.write( "Section " + valueRight1.text + "\n" + 
    "Row " + valueRight2.text + "\n" + 
    "Seats " + valueRight3.text + "\n" + 
    "SUBTOTAL " + valueRight4.text+"\n\n")




#print (time.text+"\n\n\n")
file.write(time.text+"\n\n\n")
file.write("- - - - - - - - - - - - - - -" + "\n")
file.write(datetime.datetime.now().ctime())
file.close()

"""