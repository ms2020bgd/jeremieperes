from bs4 import BeautifulSoup
import wikipedia

# Function distance_to_philo returns how many times you have to click on the first link of a Wikipedia article
# to find your way to Wikipedia Philosophy page

def distance_to_philo(page_wiki, count=1):
    page_html = wikipedia.page(page_wiki).html()
    soup = BeautifulSoup(page_html, features="html.parser")
    links = []
    # We are looking for all the web links inside paragraphs
    for a in soup.findAll('p'):
        elem = a.findAll('a', href=True)
        links.append(elem)
    # We need to get rid of edit page links to avoid getting into an infinite loop
    links_cleaned = [x for x in links if 'edit' not in str(x) and x != []]
    next_page = links_cleaned[0][0].get('title')

    if next_page == 'Philosophy':
        return count
    else:
        count += 1
        return distance_to_philo(next_page, count)

#Test
print('Distance from Reality to Philosophy is :',distance_to_philo('Reality'))
print('Distance from Reality to Curling is :',distance_to_philo('Curling'))
