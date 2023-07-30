import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):

    #Create list of connected pages
    connected = {}

    #Return probability to all pages if page has no outgoing links
    if len(corpus[page]) == 0:
        probability = 1/len(corpus)
        for page in corpus:
            connected[page] = probability
        return connected
        
    #Add probability to all pages
    probability = (1-damping_factor)/len(corpus)
    for key in corpus:
        connected[key] = probability 

    #Add values(probability) to connected pages
    probability = damping_factor/len(corpus[page])
    for key in corpus[page]:
        connected[key] += probability

    return connected
    


def sample_pagerank(corpus, damping_factor, n):
    pageRankDict = {}
    for key in corpus:
        pageRankDict[key] = 0
    page = random.choice(list(corpus.keys()))
    pageRankDict[page] += 1
    for _ in range(n-1):
        nextPageDict = transition_model(corpus,page,damping_factor)
        page = random.choices(list(nextPageDict.keys()),list(nextPageDict.values()))[0]
        pageRankDict[page] += 1
    for key in pageRankDict:
        pageRankDict[key] /= n
    return pageRankDict

    
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """


def iterate_pagerank(corpus, damping_factor):
    
    pageRankDict = {}
    pageLinks = {}

    N = len(corpus)
    value = 1/N

    for key in corpus:
        pageRankDict[key] = value
        pageLinks[key] = set()
        if len(corpus[key]) == 0:
            corpus[key]= set(corpus.keys())
    for key in corpus:
        for page in corpus[key]:
            pageLinks[page].add(key)
            
    change = 1
    while change > 0.001:
        change = 0
        oldPageRankDict = pageRankDict.copy()
        for key in pageRankDict:
            sumLinks = 0
            for link in pageLinks[key]:
                sumLinks += oldPageRankDict[link]/(len(corpus[link]))
            pageRankDict[key] = (1-damping_factor)/N + damping_factor*sumLinks
            change = max(change,abs(pageRankDict[key] - oldPageRankDict[key]))
    print("Sum: " + str(sum(pageRankDict.values())))
    return pageRankDict



if __name__ == "__main__":
    main()
