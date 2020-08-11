from util import Stack

def earliest_ancestor(ancestors, starting_node):
    relationships = {}
    s = Stack()
    visited = set()

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

    print(relationships, ' RELATIONSHIPS')
    
    if starting_node not in relationships.keys():
        # not a key, means no parents
        return -1

    else:

        # stack the starting node
        s.push(starting_node)

        while s.size() > 0:
            top_node = s.pop()

            if top_node not in visited:
                visited.add(top_node)

                print(top_node, ' has been visited.')

                # if top node has parents
                if top_node in relationships.keys():
                    for parent_of_top_node in relationships.get(top_node):
                        s.push(parent_of_top_node)

        return top_node
    

