import click
import datetime
import time

from github import Github

ACCESS_TOKEN = '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'
g = Github(ACCESS_TOKEN)



def search_github(keywords):
    query = '+'.join(keywords) + '+in:readme+in:description'
    result = g.search_repositories(query, 'stars', 'desc')
 
    print(f'Found {result.totalCount} repo(s)')
 
    #for repo in result:
     #   print(repo.clone_url)
    return result



keywords = input('Enter keyword(s)[e.g python, flask, postgres]: ')
keywords = [keyword.strip() for keyword in keywords.split(',')]
temp =[]

temp=search_github(keywords)
for i in range(0,30):
    
    if(temp[i].stargazers_count>20):
        print(temp[i].clone_url,'stars',temp[i].stargazers_count)
