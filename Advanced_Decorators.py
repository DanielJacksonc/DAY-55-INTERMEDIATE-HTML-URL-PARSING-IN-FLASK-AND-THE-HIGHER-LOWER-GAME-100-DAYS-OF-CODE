# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False
#
# def is_authenticated_decorator(function):
#     def wrapper( *args, **kwargs):
#         if args[0].is_logged_in == True:
#             function(args[0])
#     return wrapper
#
#
# @is_authenticated_decorator
# def create_a_blog_post(user):
#     print(f"This is {user.name}'s new blog post")
#
#
#
# new_user = User("Daniel")
# new_user.is_logged_in = True
# create_a_blog_post(new_user)











class User():
    def __init__(self, name):
        self.name = name
        self.is_logged_in = True

def is_authenticated_on(function):
    def wrapper(*args):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper
@is_authenticated_on
def create_blog_post(user):
    print(f"{user.name}'s created a blog post")

user = User("Daniel")
user.is_logged_in = True
create_blog_post(user)
























