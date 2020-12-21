from web_scraper.scraper import get_citations_needed_count,get_citations_needed_report

def test_count():
    assert get_citations_needed_count('https://en.wikipedia.org/wiki/Automation')==3

def test_report():
    assert get_citations_needed_report('https://en.wikipedia.org/wiki/Automation')[0]=="The costs of automation to the environment are different depending on the technology, product or engine automated. There are automated engines that consume more energy resources from the Earth in comparison with previous engines and vice versa"
    assert get_citations_needed_report('https://en.wikipedia.org/wiki/Automation')[1]=="Hazardous operations, such as oil refining, the manufacturing of industrial chemicals, and all forms of metal working, were always early contenders for automation [dubious  – discuss]"
    assert get_citations_needed_report('https://en.wikipedia.org/wiki/Automation')[2]=="Online shopping could be considered a form of automated retail as the payment and checkout are through an automated Online transaction processing system, with the share of online retail accounting jumping from 5.1% in 2011 to 8.3% in 2016"
