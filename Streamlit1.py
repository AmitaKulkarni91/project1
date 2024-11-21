from operator import index

import mysql.connector
import streamlit
import os
import pandas as pd
import googleapiclient.discovery
import googleapiclient.errors
import sys

def main_c():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyDtga3adPmqin0Vl4FPHorpLKLwhof8Gk0"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    request1 = youtube.channels().list(
        part="snippet, content_details, statistics",
        id=channel_id1
        )
    response1 = request1.execute()
    request2 = youtube.channels().list(
        part="snippet, content_details, statistics",
        id=channel_id2
        )
    response2 = request2.execute()
    # request3 = youtube.channels().list(
    #     part="snippet, content_details, statistics",
    #     id=channel_id3
    # )
    # response3 = request3.execute()
    # request4 = youtube.channels().list(
    #     part="snippet, content_details, statistics",
    #     id=channel_id4
    #     )
    # response4 = request4.execute()
    # request5 = youtube.channels().list(
    #     part="snippet, content_details, statistics",
    #     id=channel_id5
    #     )
    # response5 = request5.execute()
    # request6 = youtube.channels().list(
    #     part="snippet, content_details, statistics",
    #     id=channel_id6
    #     )
    # response6 = request6.execute()
    # request7 = youtube.channels().list(
    #     part="snippet, content_details, statistics",
    #     id=channel_id7
    #     )
    # response7 = request7.execute()
    # request8 = youtube.channels().list(
    #     part="snippet, content_details, statistics",
    #     id=channel_id8
    #     )
    # response8 = request8.execute()
    # request9 = youtube.channels().list(
    #     part="snippet, content_details, statistics",
    #     id=channel_id9
    #     )
    # response9 = request9.execute()
    # request10 = youtube.channels().list(
    #     part="snippet, content_details, statistics",
    #     id=channel_id10
    #     )
    # response10 = request10.execute()

    requestv1 = youtube.videos().list(
        part="id, snippet, contentDetails, statistics",
        id=video_id1
        )
    responsev1 = requestv1.execute()

    requestv2 = youtube.videos().list(
        part="id, snippet, contentDetails, statistics",
        id=video_id2
        )
    responsev2 = requestv2.execute()

    data1 = {
        "channel_name":response1['items'][0]['snippet']['title'],
            "channel_subscription_count":response1['items'][0]['statistics']['subscriberCount'],
            "channel_views":response1['items'][0]['statistics']['viewCount'],
            "channel_description":response1['items'][0]['snippet']['description'],
            "channel_playlist_id":response1['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    }
    data2 = {"channel_name":response2['items'][0]['snippet']['title'],
            "channel_subscription_count":response2['items'][0]['statistics']['subscriberCount'],
            "channel_views":response2['items'][0]['statistics']['viewCount'],
            "channel_description":response2['items'][0]['snippet']['description'],
            "channel_playlist_id":response2['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    }

    channel_df1 = pd.DataFrame(data1, index=[0])
    channel_df2 = pd.DataFrame(data2, index=[0])

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jaihanuman1",
        database="youtubeDB"
    )
    mycursor = mydb.cursor()
    # mycursor.execute("DROP TABLE ytchannel")
    mycursor.execute("CREATE TABLE IF NOT EXISTS ytchannel(id INT AUTO_INCREMENT PRIMARY KEY,channel_name varchar(255),channel_subscription_count int,channel_views varchar(255),channel_description varchar(1000), channel_playlist_id varchar(255), channel_video_count varchar(255))")
    # channel_df1.to_sql('ytchannel', con=mydb, if_exists='append',index=False)
    # channel_df2.to_sql('ytchannel', con=mydb, if_exists='append', index=False)

    sql = "INSERT INTO ytchannel(channel_name, channel_subscription_count, channel_views, channel_description, channel_playlist_id, channel_video_count) VALUES(%s, %s, %s, %s, %s, %s)"
    val =  (response1['items'][0]['snippet']['title'],
            response1['items'][0]['statistics']['subscriberCount'],
            response1['items'][0]['statistics']['viewCount'],
            response1['items'][0]['snippet']['description'],
            response1['items'][0]['contentDetails']['relatedPlaylists']['uploads'],
            response1['items'][0]['statistics']['videoCount']
            )
    mycursor.execute(sql, val)
    sql = "INSERT INTO ytchannel(channel_name, channel_subscription_count, channel_views, channel_description, channel_playlist_id, channel_video_count) VALUES(%s, %s, %s, %s, %s, %s)"
    val =  (response2['items'][0]['snippet']['title'],
            response2['items'][0]['statistics']['subscriberCount'],
            response2['items'][0]['statistics']['viewCount'],
            response2['items'][0]['snippet']['description'],
            response2['items'][0]['contentDetails']['relatedPlaylists']['uploads'],
            response2['items'][0]['statistics']['videoCount']
            )
    # mycursor.execute(sql, val)
    # sql = "INSERT INTO ytchannel(channel_name, channel_subscription_count, channel_views, channel_description, channel_playlist_id, channel_video_count) VALUES(%s, %s, %s, %s, %s, %s)"
    # val =  (response3['items'][0]['snippet']['title'],
    #         response3['items'][0]['statistics']['subscriberCount'],
    #         response3['items'][0]['statistics']['viewCount'],
    #         response3['items'][0]['snippet']['description'],
    #         response3['items'][0]['contentDetails']['relatedPlaylists']['uploads'],
    #         response3['items'][0]['statistics']['videoCount']
    #         )
    # mycursor.execute(sql, val)
    # sql = "INSERT INTO ytchannel(channel_name, channel_subscription_count, channel_views, channel_description, channel_playlist_id, channel_video_count) VALUES(%s, %s, %s, %s, %s, %s)"
    # val =  (response4['items'][0]['snippet']['title'],
    #         response4['items'][0]['statistics']['subscriberCount'],
    #         response4['items'][0]['statistics']['viewCount'],
    #         response4['items'][0]['snippet']['description'],
    #         response4['items'][0]['contentDetails']['relatedPlaylists']['uploads'],
    #         response4['items'][0]['statistics']['videoCount']
    #         )
    # mycursor.execute(sql, val)
    # sql = "INSERT INTO ytchannel(channel_name, channel_subscription_count, channel_views, channel_description, channel_playlist_id, channel_video_count) VALUES(%s, %s, %s, %s, %s, %s)"
    # val =  (response5['items'][0]['snippet']['title'],
    #         response5['items'][0]['statistics']['subscriberCount'],
    #         response5['items'][0]['statistics']['viewCount'],
    #         response5['items'][0]['snippet']['description'],
    #         response5['items'][0]['contentDetails']['relatedPlaylists']['uploads'],
    #         response5['items'][0]['statistics']['videoCount']
    #         )
    # mycursor.execute(sql, val)
    # sql = "INSERT INTO ytchannel(channel_name, channel_subscription_count, channel_views, channel_description, channel_playlist_id, channel_video_count) VALUES(%s, %s, %s, %s, %s, %s)"
    # val =  (response6['items'][0]['snippet']['title'],
    #         response6['items'][0]['statistics']['subscriberCount'],
    #         response6['items'][0]['statistics']['viewCount'],
    #         response6['items'][0]['snippet']['description'],
    #         response6['items'][0]['contentDetails']['relatedPlaylists']['uploads'],
    #         response6['items'][0]['statistics']['videoCount']
    #         )
    # mycursor.execute(sql, val)
    # sql = "INSERT INTO ytchannel(channel_name, channel_subscription_count, channel_views, channel_description, channel_playlist_id, channel_video_count) VALUES(%s, %s, %s, %s, %s, %s)"
    # val =  (response7['items'][0]['snippet']['title'],
    #         response7['items'][0]['statistics']['subscriberCount'],
    #         response7['items'][0]['statistics']['viewCount'],
    #         response7['items'][0]['snippet']['description'],
    #         response7['items'][0]['contentDetails']['relatedPlaylists']['uploads'],
    #         response7['items'][0]['statistics']['videoCount']
    #         )
    # mycursor.execute(sql, val)
    # sql = "INSERT INTO ytchannel(channel_name, channel_subscription_count, channel_views, channel_description, channel_playlist_id, channel_video_count) VALUES(%s, %s, %s, %s, %s, %s)"
    # val =  (response8['items'][0]['snippet']['title'],
    #         response8['items'][0]['statistics']['subscriberCount'],
    #         response8['items'][0]['statistics']['viewCount'],
    #         response8['items'][0]['snippet']['description'],
    #         response8['items'][0]['contentDetails']['relatedPlaylists']['uploads'],
    #         response8['items'][0]['statistics']['videoCount']
    #         )
    # mycursor.execute(sql, val)
    # sql = "INSERT INTO ytchannel(channel_name, channel_subscription_count, channel_views, channel_description, channel_playlist_id, channel_video_count) VALUES(%s, %s, %s, %s, %s, %s)"
    # val =  (response9['items'][0]['snippet']['title'],
    #         response9['items'][0]['statistics']['subscriberCount'],
    #         response9['items'][0]['statistics']['viewCount'],
    #         response9['items'][0]['snippet']['description'],
    #         response9['items'][0]['contentDetails']['relatedPlaylists']['uploads'],
    #         response9['items'][0]['statistics']['videoCount']
    #         )
    # mycursor.execute(sql, val)
    # sql = "INSERT INTO ytchannel(channel_name, channel_subscription_count, channel_views, channel_description, channel_playlist_id, channel_video_count) VALUES(%s, %s, %s, %s, %s, %s)"
    # val =  (response10['items'][0]['snippet']['title'],
    #         response10['items'][0]['statistics']['subscriberCount'],
    #         response10['items'][0]['statistics']['viewCount'],
    #         response10['items'][0]['snippet']['description'],
    #         response10['items'][0]['contentDetails']['relatedPlaylists']['uploads'],
    #         response10['items'][0]['statistics']['videoCount']
    #         )
    # mycursor.execute("DROP TABLE ytvchannel")
    mycursor.execute(
        "CREATE TABLE IF NOT EXISTS ytvchannel(id INT AUTO_INCREMENT PRIMARY KEY,Video_ID varchar(255),Video_Name varchar(255),Video_Description text,View_Count int, Like_Count int, Favorite_Count int, Comment_Count int, Thumbnail varchar(255), Caption_Status varchar(255))")

    sql = "INSERT INTO ytvchannel(Video_ID,Video_Name,Video_Description,View_Count, Like_Count, Favorite_Count, Comment_Count, Thumbnail, Caption_Status) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val =  (responsev1['items'][0]['id'],
            responsev1['items'][0]['snippet']['title'],
            responsev1['items'][0]['snippet']['description'],
            # responsev1['items'][0]['snippet']['publishedAt'],
            responsev1['items'][0]['statistics']['viewCount'],
            responsev1['items'][0]['statistics']['likeCount'],
            responsev1['items'][0]['statistics']['favoriteCount'],
            responsev1['items'][0]['statistics']['commentCount'],
            # responsev1['items'][0]['contentDetails']['duration'],
            responsev1['items'][0]['snippet']['thumbnails']['default']['url'],
            responsev1['items'][0]['contentDetails']['caption']
            )
    mycursor.execute(sql, val)
    sql = "INSERT INTO ytvchannel(Video_ID,Video_Name,Video_Description,View_Count, Like_Count, Favorite_Count, Comment_Count, Thumbnail, Caption_Status) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val =  (responsev2['items'][0]['id'],
            responsev2['items'][0]['snippet']['title'],
            responsev2['items'][0]['snippet']['description'],
            # responsev2['items'][0]['snippet']['publishedAt'],
            responsev2['items'][0]['statistics']['viewCount'],
            responsev2['items'][0]['statistics']['likeCount'],
            responsev2['items'][0]['statistics']['favoriteCount'],
            responsev2['items'][0]['statistics']['commentCount'],
            # responsev2['items'][0]['contentDetails']['duration'],
            responsev2['items'][0]['snippet']['thumbnails']['default']['url'],
            responsev2['items'][0]['contentDetails']['caption']
            )
    mycursor.execute(sql, val)
    mydb.commit()
    #
    # mycursor.execute("SELECT * FROM ytchannel")
    # result = mycursor.fetchall()
    # for row in result:
    #     streamlit.write(row)

streamlit.title("YouTube Data Harvesting")
channel_id1 = streamlit.text_input("Enter channel ID1:")
channel_id2 = streamlit.text_input("Enter channel ID2:")
# channel_id3 = streamlit.text_input("Enter channel ID3:")
# channel_id4 = streamlit.text_input("Enter channel ID4:")
# channel_id5 = streamlit.text_input("Enter channel ID5:")
# channel_id6 = streamlit.text_input("Enter channel ID6:")
# channel_id7 = streamlit.text_input("Enter channel ID7:")
# channel_id8 = streamlit.text_input("Enter channel ID8:")
# channel_id9 = streamlit.text_input("Enter channel ID9:")
# channel_id10 = streamlit.text_input("Enter channel ID10:")
video_id1 = streamlit.text_input("Enter video ID1:")
video_id2 = streamlit.text_input("Enter video ID2:")

if channel_id1 !="":
    if channel_id2 !="":
        # if channel_id3 != "":
        #     if channel_id4 != "":
        #         if channel_id5 != "":
        #             if channel_id6 != "":
        #                 if channel_id7 != "":
        #                     if channel_id8 != "":
        #                         if channel_id9 != "":
        #                             if channel_id10 != "":
                                            if video_id1 != "":
                                                if video_id2 != "":



                                                    if __name__ == "__main__":
                                                        main_c()
                                                    mydb = mysql.connector.connect(
                                                        host="localhost",
                                                        user="root",
                                                        password="Jaihanuman1",
                                                        database="youtubeDB"
                                                    )
                                                    mycursor = mydb.cursor()

                                                    if streamlit.button("Channel Names and View Counts for all Channels:"):
                                                        mycursor.execute("SELECT channel_name, channel_views FROM ytchannel")
                                                        for row1 in mycursor:
                                                            streamlit.write(row1)
                                                        # streamlit.stop()

                                                    if streamlit.button("Channel with most number of videos:"):
                                                        mycursor.execute("SELECT max(channel_video_count) FROM ytchannel")
                                                        for row2 in mycursor:
                                                            streamlit.write(row2)
                                                        # streamlit.stop()

                                                    if streamlit.button("Video with most number of likes:"):
                                                        mycursor.execute("SELECT max(Like_Count) FROM ytvchannel")
                                                        for row3 in mycursor:
                                                            streamlit.write(row3)
                                                        # streamlit.stop()

                                                    if streamlit.button("Video with most number of comments:"):
                                                        mycursor.execute("SELECT max(Comment_Count) FROM ytvchannel")
                                                        for row4 in mycursor:
                                                            streamlit.write(row4)
                                                        # streamlit.stop()

