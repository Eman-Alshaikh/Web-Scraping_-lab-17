from web_scraper.scraper import *


def test_count_citations():
    count=get_citations_needed_count('https://en.wikipedia.org/wiki/History_of_Mexico'
    )
    assert count==5


def test_report():
    p='The first people to settle in Mexico encountered a climate far milder than the current one. In particular, the Valley of Mexico contained several large paleo-lakes (known collectively as Lake Texcoco) surrounded by dense forest. Deer were found in this area, but most fauna were small land animals and fish and other lacustrine animals were found in the lake region.[citation needed][6] Such conditions encouraged the initial pursuit of a hunter-gatherer existence.\n'

    url='https://en.wikipedia.org/wiki/History_of_Mexico'

    report=get_citations_needed_report(url)
    assert(p in report)
