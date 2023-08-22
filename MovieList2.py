#!/usr/bin/env python3

import os

def display_menu() :
    print("COMMAND MENU")
    print("list - List all movies")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("exit - Exit program and Save list")
    print()
    
def load():
    from pathlib import Path
    try:
        f= open("savedMovies.txt")
        f.close() 
    except:
        print("Previous data does not exist Creating new file.\n")
        f = open("savedMovies.txt", "x")
        f.close()
        main()
        return
       
    path = Path("savedMovies.txt")
    contents = path.read_text()
    lines = contents.split(', ')
    i = 0
    movies = ()
    movieList = []
    for line in lines:
        newLine = line.strip("()'")
        lines[i] = newLine
        i += 1
    j = len(lines)
    if j >= 2:
        try:
        
            while j != 0:
                year = lines.pop()
                movie = lines.pop()
                movies = (movie, year)
                movieList.append(movies)
                j -= 2
        except Exception as err:
            print("List data is corrupted. Please try again.")
            path.unlink("savedMovies.txt")
            quit()
        
        
    return movieList
    
def list(movies) :
    if len(movies) == 0 :
        print("No movies to list!\n")
    else :
        i = 1
        for movie in movies :
            print(f"{i} {movie[0]} ({movie[1]})")
            i += 1
        print()


def add(movies) :
    movie = input("Name: ")
    year = input("Year Released: ")
    if len(movies) == 0:
        movies.append( ( movie, int(year) ) )
        print(movie, "was added.\n")
    else:
        for i in movies:
            if i[0].lower() == movie.lower():
                print("Movie already exists in list.\n")
                break
          
            else:
                movies.append( ( movie, int(year) ) )
                print(movie, "was added.\n")
                break


def delete(movies) :
    if len(movies) == 0 :
        print("No movies to delete!\n")
    else :
        number = int(input("Number: "))
        if number < 1 or number > len(movies) :
            print("Invalid movie number!\n")
        else :
            movie = movies.pop(number - 1)
            print(movie[0], "was deleted.\n")

def exit(movies):
    from pathlib import Path
    path = Path("savedMovies.txt")
    saveString = str(movies).strip('[]')
    path.write_text(saveString)
    print("Movie List Saved.  Goodbye!\n")
    quit()


def main() :
    movie_list = load()
    
    display_menu()
    
    while True :
        command = input("Command: ")
        
        if command.lower() == "list" :
            list(movie_list)
        elif command.lower() == "del" :
            delete(movie_list)
        elif command.lower() == "add" :
            add(movie_list)
        elif command.lower() == "exit" :
            exit(movie_list)
        else :
            print("Not a valid command -- please try again.\n")
    print("Bye!")

if __name__ == "__main__" :
    main()
