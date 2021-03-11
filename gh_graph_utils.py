def augment_owns(graph, user, lang=False):
    graph.add_node(user.login, node_type='user')
    repos = user.get_repos()
    for repo in repos:
        graph.add_node(repo.name, node_type='repo')
        graph.add_edge(user.login, repo.name, edge_type='owns')
        if lang:
            graph.add_node(repo.language, node_type='lang')
            graph.add_edge(user.login, repo.language, edge_type='users')
            graph.add_edge(repo.name, repo.language, edge_type='speaks')
    return repos

def augment_stargazers(graph, repo):
    try:
        gazers = repo.get_stargazers()
        for stargazer in gazers:
            graph.add_node(stargazer.login, node_type='user')
            graph.add_edge(stargazer.login, repo.name, edge_type='gazes')
        return gazers
    except: #It's fun to play at the... D   M  C  A
        return []