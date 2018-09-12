## 2. Authenticating with the API ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
parameter = {"t" : "day"}
response =requests.get("https://oauth.reddit.com/r/python/top" ,headers = headers, params = parameter)
python_top = response.json()

## 3. Getting the Most Upvoted Post ##

python_top_articles = []
for i in python_top["data"]["children"]:
    python_top_articles.append(i)
print(python_top_articles)
max_ups = 0 
max_id = ""
for j in (python_top_articles):
    if j["data"]["ups"] > max_ups: 
        max_ups = j["data"]["ups"]
        max_id = j["data"]["id"]
most_upvoted = max_id


## 4. Getting Post Comments ##

response = requests.get("https://oauth.reddit.com/r/python/comments/4b7w9u",headers = headers)
comments= response.json()

## 5. Getting the Most Upvoted Comment ##

print(comments[1]["data"]["children"][0]["data"]["ups"])
comments_list = []
for i in comments:
    comments_list.append(comments[1]["data"]["children"])
max_ups = 0
max_id = ""
for j in comments_list:
    if j[2]["data"]["ups"] > max_ups:
        max_ups = j[2]["data"]["ups"]
        max_id = j[2]["data"]["id"]
        
most_upvoted_comment = max_id

## 6. Upvoting a Comment ##

parameter = {"dir": 1, "id" :"d16y4ry"}
response = requests.post("https://oauth.reddit.com/api/vote",headers=headers, json=parameter )
status = response.status_code