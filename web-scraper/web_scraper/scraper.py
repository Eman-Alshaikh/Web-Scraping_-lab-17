from email.errors import HeaderDefect
from turtle import title
import requests
from bs4 import BeautifulSoup


def get_citations_needed_count (url):
    """
    get_citations_needed takes in a url and returns an integer

    """
    # request data from URL 
    page=requests.get(url)

    # GET THE CONTENTS 
    s=BeautifulSoup(page.content,'html.parser')
    
    result=0

    for i in s.find_all('a',href= True):
        if i ['href']=='/wiki/Wikipedia:Citation_needed':
            result+=1
     
    return result


def get_citations_needed_report(url):
    """
    get_citations_needed_report takes in a url and returns a string
the string should be formatted with each citation needed on own line, 
in order found.
    """

     # request data from URL 
    page=requests.get(url)

    # GET THE CONTENTS  
    s=BeautifulSoup(page.content,'html.parser') 

    report=''
    prefix='Citation needed for: \n'

    for i in s.find_all('a', href=True) :
        if i['href']=='/wiki/Wikipedia:Citation_needed':
            parents=i.find_parents('p')
            for parent in parents:
                report+=prefix+parent.text+'\n'

          
    return (report)


if __name__=="__main__":

        url='https://en.wikipedia.org/wiki/History_of_Mexico'
        count=get_citations_needed_count(url)
        print (count)

        report=get_citations_needed_report(url)
        print(report)

