
def earliest_ancestor(ancestors, starting_node):
    relationships = {}

    # set up relationships dictionary
    for tup in ancestors:
        parent = tup[0]
        child = tup[1]

        if child not in relationships:
            # child: parent
            relationships[child] = [parent]
        # else if child already has a parent, add another parent
        elif child in relationships:
            relationships[child].append(parent)
    
    if starting_node not in relationships.keys():
        return -1

    while starting_node in relationships.keys():
        # starting-node exists as a child... Means parent also exists.

        for starting_node_parent in relationships.get(starting_node):
            starting_node = starting_node_parent
            continue

    return starting_node
    