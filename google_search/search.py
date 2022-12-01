# This google search implementation was located at the link below:
# https://www.geeksforgeeks.org/performing-google-search-using-python-code/
# This returns the top 10 google search results for the keywords provided 
# by the user.

try:
    from googlesearch import search
    from sys import argv
except ImportError:
    print("Unable to locate module.")

# to search
query = argv[1]
print(query)

for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(j)
