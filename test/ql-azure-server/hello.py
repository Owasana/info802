import graphene
import json
from datetime import datetime


class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    last_login = graphene.DateTime(required=False)

users = [ User(username='Alice', last_login=datetime.now()),User(username='Bob', last_login=datetime.now()), User(username='R2D2', last_login=datetime.now())]

class Query(graphene.ObjectType):
    userscat = graphene.List(User, first=graphene.Int())
    users = graphene.List(User)

    def resolve_userscat(self, info, first):
        return  users[:first]

    def resolve_users(self, info):
        return users

class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String()

    user = graphene.Field(User)

    def mutate(self, info, username):
        user = User(username=username)
        users.append(user)
        return CreateUser(user = user)

#class DeleteUser(graphene.Mutation):
#    class Arguments:
#        id = graphene.Int()

#    def mutate(self, info, id):
#        for i,user in enumerate(users):
#            if user.id == id :
#                users.pop(i)
#                break

class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()
#    delete_user = DeleteUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutations)



##    result = schema.execute(
#        '''
#        mutation createUser($username: String) {
#            createUser(username: $username){
#                user {
#                    username
#                }
#            }
#        }
#        ''',
#        variable_values={'username': 'R2d2'},
#        context={'is_vip': True}
#        )
#    print(result)
