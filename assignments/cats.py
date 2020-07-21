"""CaTZ lol"""

"""
Key concepts:
    Lists/Strings and Indexing
    Control (if, ==, booleans)
    Abstraction
    Loops/Recursion

Phase 2:

Q5 autocorrect
    Possible Concepts: Abstraction, Lists, Loops

    input:
        user_word:      String
        valid_words:    List
        diff_function:  Function
            takes in user_word, a word from valid word, then a limit
            returns the difference between user_word and the other word you passed in
        limit:          Number

    output:
        String:
            user_word:
                if the lowest difference between user_word and a word in valid_words is greater than limit
            word from valid_words:
                if that word has the lowest difference
    Note: the difference is based off the diff_function



Q6: shifty_shifts
    USE RECURSION!!! Base case(s), recursive case(s), leap of faith
    Possible Concepts: Control, String Indexing

    input:
        start:          String
        goal:           String
        limit:          Number

    output:
        Number:
          Number of character changes you'll have to do to convert start to end
          If that number is greater than limit at any point, just return that number immediately without doing additional computation



Q7: meowstake_matches
    Possible Concepts: Recursion, List indexing/slicing, Control

    input:
        start:          String
        goal:           String
        limit:          Number

    intermediates:
        edit operations: Each of the following adds 1 to the difference between start and goal
            add a letter to start
            remove a letter from start
            swap a letter in start

    output:
        Number:
            Number of edit operations needed to turn start into goal
            If the number of edits is greater than limit, return that number of edits without doing additional computation


Phase 3:
Q8: report_progress
    input:
        typed:              String
        prompt:             String
        id:                 Anything
        send:               Function
            takes in a dictionary of {"id": some_id, "progress": player_progress (described below)}
            then sends it to the server

    output:
        Number:
            The player's progress (number of correct words / total number of words in prompt)

Q9: time_per_word
    input:
        times_per_player:   List of Lists
            [player0, player1,...]
            where playerN is a list of direct timestamps for each player;
                eg: [1, 2, 3]
                # could be 1pm, 2pm, 3pm, but we don't really care about units
            we want this to be converted into how long each word took to type
                eg: the above would be [1, 1, 1]
        words:              List

    output:
        Game Object
            uses the given input to create a game object
            see def game(words, times): which is below the problem 10 code

Q10: fastest_words
    input:
        game:               Game object

    intermediates:
        word_at:             Function
            takes in game and word_index (Number)
            returns the word (String) corresponding to that index

        all_times:           Function
            Try reading for yourself what these do, practice with abstraction/reading descriptions
            These functions will be useful in turning your above input into the output below

        all_words:           Function

        time:                Function


    output:
        List of Lists:
            [player0, player1,...]
            playerN is a list of all the words player N typed the fastest
                eg: ["doofus", "big", "cheeseburger"] # playerN typed these the fastest
"""
