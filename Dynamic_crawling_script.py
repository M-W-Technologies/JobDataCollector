from selenium import webdriver

def webdriver_creator(drivertype, DRIVERPATH):
    """
    this function returns a webdriver
    Parameters :
        drivertype : string
        DRIVERPATH : string
    """
    if drivertype == 'Chrome':
        driver = webdriver.Chrome(executable_path=DRIVERPATH)
    elif drivertype == 'Edge':
        driver = webdriver.Edge(executable_path=DRIVERPATH)
    elif drivertype == 'Firefox':
        driver = webdriver.Firefox(executable_path=DRIVERPATH)
    else:
        driver = None
        
    return driver
    
def create_link(numberofpage, jobtitle): # create a function to get a link 
    """
    this function allows us to get a link containing 
    the jobtitle you search and the number of page you want. 
    this function will return an URL
    """
    replaced_jobtitle = jobtitle.replace(' ','%20')
    link = f"https://www.welcometothejungle.com/fr/jobs?query={replaced_jobtitle}&page={numberofpage}" # create the link using f format
    return link # return the link 


# New version of the function with default value for nb of pages.
# parameters with default values must always be at the end
def create_link_v2(jobtitle, numberofpage=1): # create a function to get a link 
    """
    this function allows us to get a link containing 
    the jobtitle you search and the number of page you want.
    Default number of page is 1
    this function will return an URL
    """
    replaced_jobtitle = jobtitle.replace(' ','%20')
    link = f"https://www.welcometothejungle.com/fr/jobs?query={replaced_jobtitle}&page={numberofpage}" # create the link using f format
    return link # return the link 