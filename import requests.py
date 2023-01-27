import click
import datetime
import time

from github import Github

ACCESS_TOKEN = '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'
g = Github(ACCESS_TOKEN)


if __name__ == '__main__':
    keywords = input('Enter keyword(s)[e.g python, flask, postgres]: ')
    keywords = [keyword.strip() for keyword in keywords.split(',')]


print(keywords)

def search_github(keywords):
    query = '+'.join(keywords) + '+in:readme+in:description'
    result = g.search_repositories(query, 'stars', 'desc')
 
    print(f'Found {result.totalCount} repo(s)')
 
    #for repo in result:
     #   print(repo.clone_url)
    return result
 
temp =[]

temp=search_github(keywords)
for i in range(0,1000,100):
    print(temp[i].clone_url)
