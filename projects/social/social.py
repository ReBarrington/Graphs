import random
from util import Stack

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def get_friends(self):
        return self.friendships

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
        Creates that number of users and a randomly distributed friendships
        between those users.
        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i}")


        # Create friendships
        # generate all possible friendship combinations
        possible_friendships = []

        # avoid dups by ensuring first num < second num
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # shuffle friendships
        random.shuffle(possible_friendships)

        # create friendships from the first N pairs of the list
        # N -> num_users * avg_friendships // 2
        N = num_users * avg_friendships // 2
        for i in range(N):
            friendship = possible_friendships[i]
            # user_id, friend_id = friendship
            user_id = friendship[0]
            friend_id = friendship[1]
            self.add_friendship(user_id, friend_id)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

        # create an empty stack and push PATH To the Starting Vertex
        s = Stack()
        s.push([user_id])

        # create a set to store visited vertices
        visited = set()
        degrees_of_separation = {}

        # while the stack is not empty
        while s.size() > 0:
            # pop the first PATH
            pth = s.pop()
            print(pth, ' is pth')
            # grab the last vertex from the Path
            current_user = pth[-1]
            # print(current_user, ' is the last vertex from the path.')

            # check if the vertex has not been visited
            if current_user not in visited:
                # is this vertex the target?
                if current_user == user_id:
                    degrees_of_separation[current_user] = pth
                    user_id = pth[-1]
                # mark it as visited
                visited.add(current_user)

                # then add a path to its friends to the back of the stack
                for friend in self.friendships.get(current_user):
                    print(friend, ' should be friend of ', current_user )
                    user_id = friend
                    # make a copy of the path
                    new_pth = list(pth)
                    # append the neighbor to the back of the path
                    new_pth.append(friend)
                    # push out new path
                    s.push(new_pth)

        return degrees_of_separation


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships, ' friendships')
    connections = sg.get_all_social_paths(1)
    print(connections, ' get_all_social_paths')
