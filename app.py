from flask import Flask,render_template,request
import json
# from flask_cors import CORS,cross_origin

app = Flask(__name__)
# CORS(app)

a=[["""Get Movies or TV Series information.""",
    """title/1""",
    """
    {
        "Director":[{
            "firstname":"Tulsi Ghimire",
            "lastname":null,
            "miiddlename":null
            }],
        "actorsAndTheirCharacter":
            [{
                "characterName":"Arjun",
                "firstname":"Bhuwan ",
                "lastname":"K.C.",
                "miiddlename":null
            },
            {"
                characterName":"Suniti",
                "firstname":"Tripti ",
                "lastname":"Nadakar",
                "miiddlename":null},
            {
                "characterName":"Amar",
                "firstname":"Udit",
                "lastname":"Jha",
                "miiddlename":"Narayan"
            },
            {
                "characterName":"Suniti's dad",
                "firstname":"Neer",
                "lastname":"Shah",
                "miiddlename":"Bikram"
            }],
        "avrageEpisodeDuration":125,
        "awards":"",
        "enddate":null,
        "genres":[{"genreName":"Drama"},{"genreName":"Romance"},{"genreName":"Musical"}],
        "image":"https://m.media-amazon.com/images/M/MV5BZTE3YjRkNWUtN2MyNy00NTZmLWEwNGItM2ZkN2EwNGJlNGQ4XkEyXkFqcGdeQXVyNTk1NTkwNTI@._V1_Ratio0.7687_AL_.jpg",
        "nepaliname":"\u0915\u0941\u0938\u0941\u092e\u0947 \u0930\u0941\u092e\u093e\u0932",
        "noOfEpisodes":1,
        "contentRating":"Everyone",
        "socialmedia":null,
        "startdate":null,
        "sypnosis":"A girl falls in love with her classmate.
        While everything seems right
        , a worker starts dreaming of marrying her and anothe
        r classmate tries the same
        by force.",
        "titleType":"Movie",
        "title_id":1,
        "titlename":"Kusume Rumal"
}""","""You can get title information by following link where first parameter is title which is static and case sensitive followed by title id. You can get information of any title by their title id"""],
   ["""Get User's information.""","""users/22""","""
    {
        "accountCreated":"Sat, 24 Sep 2022 18:02:23 GMT",
        "avrageRating":"8.0000","reviews":1,"titles":1,
        "user_aboutme":null,
        "user_dob":"Mon, 05 Sep 2022 00:00:00 GMT",
        "user_id":22,
        "user_image":"https://i0.wp.com/wikifamouspeople.com/wp-content/uploads/2020/12/NymN-.jpg?
        resize=1024%2C761&ssl=1",
        "user_sex":1,"user_socialmedia":"",
        "username":"user11"
    }""","""You can get user information by following link where first parameter is users which is static and case sensitive followed by user id. You can get information of any user by their user id"""],
   ["""Get Staff's information.""","""staff/1""","""
    {
        "awards":null,
        "biography":"Bhuwan K.C. (Nepali: \u092d\u0941\u0935\u0928 \u0915\u0947\u0938\u0940;born: 17 September 1956) is a Nepali actor, director, producer, singer, and politician known for his work in Nepali cinema. He has started career through Radio Nepal as a childhood artist. He was among the most commercially successful Nepali actors of the 1980s, 1990s and 2000s. He is also a current chairman of Film Development Board, he was appointed for this position on 26 July 2022. \r\n",
        "bloodtype":null,
        "dob":"Mon, 17 Sep 1956 00:00:00 GMT",
        "favorite":2,
        "firstname":"Bhuwan",
        "height":null,
        "hobby":null,
        "lastname":"K.C.",
        "miiddlename":null,
        "staff_id":1,
        "staff_image":"https://upload.wikimedia.org/wikipedia/commons/b/bf/Bhuwan_KC.png",
        "staff_sex":1,
        "staff_spouse":"Vijaya Malla KC (separated) \r\nSushmita Bomjan (separated)\r\nJiya K.C. (2017-present)",
        "stagename":null
    }""","""You can get staff information by following link where first parameter is staff which is static and case sensitive followed by staff id. You can get information of any staff by their staff id"""],
   ["""Get Characters's information.""","""character/1""","""
    {
        "actors":[{
                "firstname":"Bhuwan ",
                "lastname":"K.C.",
                "miiddlename":null
            }],
        "char_id":1,
        "characterDescription":null,
        "characterImage":"https://i.ytimg.com/vi/xy3UTOdbrHk/hqdefault.jpg",
        "characterName":"Arjun",
        "favorite":2,
        "titles":[["Kusume Rumal"]]
    }""","""You can get character information by the following link where the first parameter is character id which is static and case sensitive followed by character id. You can get information of any character by their character id"""],
   ["""Get Titles's Reviews.""","""reviews/1/1""","""
    {
        "review":"asdasda",
        "spoilers":1,
        "titleId":1,
        "updated":"Sat, 24 Sep 2022 18:53:55 GMT",
        "userId":22,
        "written":"Sat, 24 Sep 2022 18:53:55 GMT"
    }""","""You can get titles reviews by the following link where the first parameter is review which is static and case sensitive followed by title id and at last the amount of reviews. You can only get 50 reviews at a time which are sorted by new."""],
   ["""Get Staff's Comments.""","""commentStaff/1/1""","""
    {
        "commentId":5,
        "commentText":"sdfsdfsdf",
        "postedOn":null,
        "staffId":1,
        "userId":22
    }""","""You can get staff comments by the following link where the first parameter is commentStaff which is static and case sensitive followed by staff id and at last the amount of comments. You can only get max 50 reviews at a time which are sorted by new."""],
   ["""Get User's Comments.""","""commentUser/22/1""","""
    {
        "commentId":21,
        "commentText":"qwewqeqw",
        "commentedBy":24,
        "commentedOn":22,
        "posted":null
    }
    ""","""You can get users comments by the following link where the first parameter is commentUser which is static and case sensitive followed by user id and at last the amount of reviews. You can only get max 50 reviews at a time which are sorted by new."""],
   ["""Get User's Title Information.""","""user/22/1""","""
    {
        "episodeWatched":1,
        "finishedWatching":null,
        "isFaviourite":1
        ,"lastUpdated":"Sat, 24 Sep 2022 18:03:46 GMT",
        "scoreGiven":8,
        "startedWatching":null,
        "titleId":1,
        "userId":22,
        "watchingStatus":"Completed"
    }
    ""","""You can get a users title information by the following link where first parameter is user which is static followed by user id and title id at last."""],
]



# @app.route('/')
# def index():
#     return 'Hello from Flask!'
@app.route('/')
def welcome():
    return render_template('index.html',a=a)
    # print("a",request.base_url)
    # return "a";

import Controller.home_controller as home_controller

app.run(host='0.0.0.0', port=81)
