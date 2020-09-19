from facepy import GraphAPI

graphApiAccessToken = ''

graph = GraphAPI(graphApiAccessToken)

graph.post(path = 'groups/GROUPNAME', message='Hello world')