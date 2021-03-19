from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

_transport = RequestsHTTPTransport(
    url='https://info802-ep-ql.azurewebsites.net/graphql',
    use_json=True,
)


client = Client(
    transport=_transport,
    fetch_schema_from_transport=True,
)
query0 = gql("""
{
    users{
        username
    }
}
""")

query = gql("""
{
  userscat(first : 1) {
    username
  }
}
""")

query1 = gql("""
{
  userscat(first : 2) {
    username
  }
}
""")

query2 = gql("""
mutation createUser{
  createUser(username : "Roger"){
    user {
      username
    }
  }
}
""")

print(client.execute(query0))
print(client.execute(query))
print(client.execute(query1))
print(client.execute(query2))
print(client.execute(query0))
