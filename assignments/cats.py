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
    typed:              String
    prompt:             String
    id:                 ?
    send:               Function

Q9: time_per_word
    input:
        times_per_player:   List of Lists
        words:              List

Q10: fastest_words
    input:



"""
