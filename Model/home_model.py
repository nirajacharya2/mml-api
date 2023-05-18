from flask_mysqldb import MySQL
from app import app
from flask import jsonify

class home_model():
    def __init__(self):
        try:
            app.config['MYSQL_HOST'] = '127.0.0.1'
            app.config['MYSQL_DB'] = 'my_movie_list'
            app.config['MYSQL_PASSWORD'] ='root'
            app.config['MYSQL_USER'] = 'root'
            self.mysql = MySQL(app)
            print('db connection suscess')
        except:
            print('db connection error')









    # specific title data
    def getTitle(self,title_id):
        cur = self.mysql.connection.cursor()
        result = cur.execute(f"""SELECT avrageEpisodeDuration,awards,startdate,enddate,image,nepaliname,noOfEpisodes,rating,socialmedia,
                             sypnosis,titleType,title_id,titlename FROM titles where title_id={title_id}""")
        if result > 0:
            userDetails = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
            resultGenre=cur.execute(f"""select distinct genreName from `titles` inner join `titles_genres` on `titles`.`title_id`
                                    = `titles_genres`.`tg_title_id` inner join `genres` on `genres`.
                                    `genre_id` = `titles_genres`.`tg_genre_id` where `titles`.`title_id` = {title_id}""")
            if resultGenre > 0:
                genre=[dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
                userDetails[0]['genres']=genre
            # return jsonify(userDetails)

            resultStaff=cur.execute(f"""select characterName,firstname,miiddlename,lastname from `titles` inner join `staffs_titles` on `titles`.`title_id` = `staffs_titles`.`st_title_id` inner
                                    join `staff` on `staffs_titles`.`st_staff_id` = `staff`.`staff_id`
                                    left join `characters` on `staffs_titles`.`char_id` = `characters`.`char_id` where `titles`.`title_id` = {title_id} and `staffs_titles`.`staffType`='Actor'""")
            if resultStaff > 0:
                staff=[dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
                userDetails[0]['actorsAndTheirCharacter']=staff
                # return jsonify(staff)

            resultDirector=cur.execute(f"""select firstname,miiddlename,lastname from `titles` inner join `staffs_titles` on `titles`.`title_id` = `staffs_titles`.
                                       `st_title_id` inner join `staff` on `staffs_titles`.`st_staff_id` =
                                       `staff`.`staff_id` left join `characters` on `staffs_titles`.`char_id` = `characters`.`char_id` where `titles`.`title_id` = {title_id} and
                                       `staffs_titles`.`staffType`='Director'""")
            if resultDirector > 0:
                director=[dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
                userDetails[0]['Director']=director
                # return jsonify(staff)
            return jsonify(userDetails)

        # return jsonify(cur.fetchall())
        return jsonify({"result": "no data"})







    # data of a specific user
    def getUser(self,userid):
        cur = self.mysql.connection.cursor()
        result=cur.execute(f"""select created_at as accountCreated,user_aboutme,user_dob,user_id,user_image,user_sex,user_socialmedia,username from users where user_id={userid}""")
        if result > 0:
            userDetails = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
            reviews=cur.execute(f"select count(*) from reviews where ut_user_id={userid}")
            titles=cur.execute(f"select count(*) from users_titles where ut_user_id={userid}")
            cur.execute(f"select avg(ut_score) from users_titles where ut_user_id={userid}")
            avrage = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
            userDetails[0]['reviews']=reviews
            userDetails[0]['titles']=titles
            userDetails[0]['avrageRating']=avrage[0]['avg(ut_score)']

            return jsonify(userDetails)
        return jsonify({"result": "no data"})





    # data of a specific staff
    def getStaff(self,staffid):
        cur = self.mysql.connection.cursor()
        result=cur.execute(f"""select biography,firstname,lastname,miiddlename,height,staff_award as awards,staff_bloodtype as bloodtype,
                           staff_dob as dob,staff_hobby as hobby,staff_id,staff_image,staff_sex,staff_spouse,stagename from staff where staff_id={staffid}""")
        if result > 0:
            userDetails = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
            favorite=cur.execute(f"select * from favorite_staffs where f_staff_id={staffid}")
            favorite = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]

            userDetails[0]['favorite']=len(favorite)
            # userDetails[0]['favorite']=10
            return jsonify(userDetails)
        return jsonify({"result": "no data"})





        # data of a specific character
    def getCharacter(self,characterid):
        cur = self.mysql.connection.cursor()
        result=cur.execute(f"""select char_id,characterDescription,characterImage,characterName from characters where char_id={characterid}""")
        if result > 0:
            userDetails = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
            favorite=cur.execute(f"select * from favorite_characters where fc_staff_id={characterid}")
            favorite = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
            cur.execute(f"""select titlename from `characters` inner join `staffs_titles` on `characters`.`char_id` = `staffs_titles`.`char_id` inner join `titles` on
                        `staffs_titles`.`st_title_id` = `titles`.`title_id` where `characters`.`char_id` = {characterid}""")
            userDetails[0]['favorite']=len(favorite)
            userDetails[0]['titles']=cur.fetchall()
            cur.execute(f"""select firstname,miiddlename,lastname from `characters` inner join `staffs_characters` on `characters`.`char_id` = `staffs_characters`
                        .`sc_char_id` inner join `staff` on `staffs_characters`.`sc_staff_id` = `staff`.`staff_id` where `characters`.`char_id` = {characterid}""")
            actor = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
            userDetails[0]['actors']=actor
            # userDetails[0]['favorite']=10
            return jsonify(userDetails)
        return jsonify({"result": "no data"})






    # reviews of a title
    def getReviews(self,titleid,reviewAmount):
        cur = self.mysql.connection.cursor()
        result=cur.execute(f"select created_at as written,rw_content as review,rw_type as spoilers,updated_at as updated,ut_title_id as titleId,ut_user_id as userId from reviews where ut_title_id={titleid} limit {reviewAmount}")
        if result > 0:
            userDetails = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
            # userDetails[0]['favorite']=10
            return jsonify(userDetails)
        return jsonify({"result": "no data"})








    # character's comment
    def getComments(self,staffid,commentAmount):
        cur = self.mysql.connection.cursor()
        result=cur.execute(f"""select commentText,created_at as postedOn,sco_staff_id as staffId,sco_user_id as userId,st_comment_id as commentId from staff_comments where sco_staff_id={staffid} limit {commentAmount}""")
        if result > 0:
            userDetails = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
            # userDetails[0]['favorite']=10
            return jsonify(userDetails)
        return jsonify({"result": "no data"})






    # users's comment
    def getCommentsUser(self,getCommentsUser,commentAmount):
        cur = self.mysql.connection.cursor()
        result=cur.execute(f"""select commentText,created_at as posted,u1_user_id as commentedOn,u2_user_id as commentedBy,ur_comment_id as commentId from user_comments where u1_user_id={getCommentsUser} limit {commentAmount}""")
        if result > 0:
            userDetails = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
            # userDetails[0]['favorite']=10
            return jsonify(userDetails)
        return jsonify({"result": "no data"})








    # specific titlle data of a specific user
    def getUsers(self,userid,titleid):
        cur = self.mysql.connection.cursor()
        result=cur.execute(f"""select ut_startdate as startedWatching,updated_at as lastUpdated,ut_enddate as finishedWatching,ut_episodewatched as episodeWatched,ut_faviourite as isFaviourite,ut_score as scoreGiven,ut_title_id as titleId,ut_user_id as userId,ut_watchingstatus as watchingStatus  from users_titles where ut_user_id={userid} and ut_title_id={titleid}""")
        if result > 0:
            userDetails = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
            # userDetails[0]['favorite']=10
            return jsonify(userDetails)
        return jsonify({"result": "no data"})
