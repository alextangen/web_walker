try:
    from googlesearch import search
    from sys import argv
except ImportError:
    print("Required Module is not found")

# to search
query = argv[1]
print(query)

for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(j)
