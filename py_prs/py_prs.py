import requests

def get_review_requests():
  query = """
  {
    search(query: "type:pr state:open review-requested:<USER_ID>", type: ISSUE, first: 100) {
      issueCount
      pageInfo {
        endCursor
        startCursor
      }
      edges {
        node {
          ... on PullRequest {
            repository {
              nameWithOwner
            }
            number
            url
          }
        }
      }
    }
  }
  """

  response = requests.post("https://api.github.com/graphql", json={"query": query}, headers={"Authorization": "bearer <GH_ACCESS_TOKEN>"})
  print(response.status_code)
  print(response.text)
