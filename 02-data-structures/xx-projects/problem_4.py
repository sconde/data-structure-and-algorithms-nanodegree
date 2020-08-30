"""
Problem 4: Active Directory
"""


class Group(object):

    def __init__(self, name):
        self.name = name
        self.groups = set()
        self.users = set()

    def add_group(self, group):
        self.groups.add(group)

    def add_user(self, user):
        self.users.add(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):

    if not isinstance(group, Group):
        raise AttributeError("Invalid group")

    if user in group.get_users():
        return True

    for grp in group.get_groups():
        return is_user_in_group(user, grp)

    return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
child_user = "child_user"
child.add_user(child_user)

child.add_group(sub_child)
parent.add_group(child)

# Test Case
answer = is_user_in_group("sub_child_user", parent)
print(answer)
# True

answer = is_user_in_group("sub_child_user", child)
print(answer)
# True

answer = is_user_in_group("a_child", parent)
print(answer)
# False

answer = is_user_in_group("child_user", parent)
print(answer)
# True

