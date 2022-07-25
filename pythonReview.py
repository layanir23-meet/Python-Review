def create_youtube_video (title , description):
	youtubevideo = {"title" : title , "description" : description ,"likes" : 0 , "dislikes" : 0 , "comments" : {}}
	return youtubevideo
def like (youtubevideo):
	if "likes" in youtubevideo:
		youtubevideo["likes"] +=1 
	return youtubevideo 

def dislike (youtubevideo):
	if "dislikes" in youtubevideo:
		youtubevideo["dislikes"] +=1 
	return youtubevideo 

def add_comment(youtubevideo,username,comment_text):
	comment = {username: comment_text}
	youtubevideo["comments"] = comment
	return youtubevideo 

dict = create_youtube_video("books" , "fav book ")
dict = like(dict)
dict = dislike(dict)
dict = add_comment(dict,"lianar" , "hey")

for i in range (495):
	dict = like(dict)


print (dict)









