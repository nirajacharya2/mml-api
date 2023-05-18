from app import app
from Model.home_model import home_model
from flask import request
obj=home_model()




# get specific title
@app.route('/title/<titleid>')
def getTitle(titleid):
    return obj.getTitle(titleid)



# get user's data
@app.route('/users/<userid>')
def getUser(userid):
    return obj.getUser(userid)



# get staffs's data
@app.route('/staff/<staffid>')
def getStaff(staffid):
    return obj.getStaff(staffid)




# get character's data
@app.route('/character/<characterid>')
def getCharacter(characterid):
    return obj.getCharacter(characterid)




# get title's reviews
@app.route('/reviews/<titleid>/<reviewAmount>')
def getReviews(titleid,reviewAmount):
    return obj.getReviews(titleid,reviewAmount)







# get staff's comment
@app.route('/commentUser/<userid>/<commentAmount>')
def getCommentsUser(userid,commentAmount):
    return obj.getCommentsUser(userid,commentAmount)





# get character's comment
@app.route('/commentStaff/<staffid>/<commentAmount>')
def getComments(staffid,commentAmount):
    return obj.getComments(staffid,commentAmount)









# get user's title data of a specific title
@app.route('/user/<userid>/<titleid>')
def getUsers(userid,titleid):
    return obj.getUsers(userid,titleid)

