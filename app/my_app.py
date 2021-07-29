import psycopg2
import json
import requests

# the db creds
db_name = 'db'
db_user = 'username'
db_pass = 'secret'
db_host = 'db'
db_port = '5432'

# add the data to the database
def bulkInsert(records):
    # connect to the postgresql database
    connection = psycopg2.connect(user=db_user,
                                      password=db_pass,
                                      host=db_host,
                                      port=db_port,
                                      database=db_name)
    # add the data to the table characters
    try:
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO characters (name, height, homeworld, films, url) 
                           VALUES (%s, %s, %s, %s, %s) """

        # executemany() to insert multiple rows
        result = cursor.executemany(sql_insert_query, records)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into characters table")

    except (Exception, psycopg2.Error) as error:
        print("Failed inserting record into character table {}".format(error))

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    
# crawl the data from the swapi from a specific link
def crawl(link):
    # get the data from the swapi 
    response = requests.get(link)
    api_results = json.loads(response.content)
    # get the characters
    for character in api_results['results']:
        # filter for the first three movies
        if 'https://swapi.dev/api/films/1/' in character['films'] and 'https://swapi.dev/api/films/2/' in character['films'] and 'https://swapi.dev/api/films/3/' in character['films']: 
            # change the homeworld as described 
            homeworld_response = requests.get(character['homeworld'])
            homeworld = json.loads(homeworld_response.content)['name']            
            if homeworld and character['name'] and character['height'] and character['films'] and character['url'] is not None:
                output = [character['name'], character['height'], homeworld, character['films'], character['url']]
                yield output  
    # recursion to get the results from all the pages  
    if 'next' in api_results and api_results['next'] is not None:
        next_page = crawl(api_results['next'])
        for page in next_page:
            yield page

# get all the characters based on the descriptions
filtered_characters = crawl('https://swapi.dev/api/people')

# insert data to the db in table characters
bulkInsert(filtered_characters)