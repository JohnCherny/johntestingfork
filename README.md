# Testing-Basics

Hello! For this assignment, follow the instructions below.

## Steps 

1. Find an interesting coding challenge or use one of the options below. 
    * Choose a challenge that can be competed with a single function.
    * Choose a challange that will accept 5-10 possible inputs. 
    * I'm not worried as much about the difficulty of the challenge as I am about create a good set of tests.
1. Create 2 new files called `challenge.py` and `test_challenge.py`.
1. Write the text of the challenge in a comment at the top of the `challenge.py` file.
1. Follow the 3 laws of TDD to complete that challenge.
    * I have provided `example.py` and `test_example.py` so you can see what the end result should look like.
    * Use the unittest built-in library for to write tests for this assignment.
1. You should have anywhere from 5-10 tests for the single function that you write.


## 📚  Resources 

* [Unittest docs](https://docs.python.org/3/library/unittest.html)
* [3 Laws of TDD](https://blog.cleancoder.com/uncle-bob/2014/12/17/TheCyclesOfTDD.html)

### Running your tests

After creating your test file, you will want to run your tests here is the command I used to run my tests:
```
python3 -m unittest test_example.py 
```

### Coding Challenge Ideas


1. Palindrome Checker
Write a function that checks if a given string is a palindrome (a word, phrase, or number that reads the same backward as forward). Ignore spaces, punctuation, and capitalization.

1. Anagram Finder
Create a function that takes two strings and checks if they are anagrams (i.e., the two words use the same letters in a different order). Ignore spaces and capitalization.

1. Reverse a String
Write a function that takes a string as input and returns the string reversed. Bonus: Do it without using any built-in string reversal methods.

1. Count Vowels
Write a program that counts the number of vowels (a, e, i, o, u) in a given string.

1. Find the Second Largest Number in a List
Given a list of numbers, write a function to find the second-largest number in the list. Handle edge cases, such as when all numbers are the same.

1. Prime Number Checker
Write a function that checks if a given number is prime (a number greater than 1 that is divisible only by 1 and itself).

1. Caesar Cipher
Create a simple Caesar cipher that shifts the letters of a given string by a certain number of positions in the alphabet. For example, with a shift of 2, "abc" would become "cde."

1. Sum of Digits
Write a function that takes an integer and returns the sum of its digits. For example, for the input 123, the output would be 6.

1. Find the Missing Number in a Sequence
Given a list of consecutive numbers starting from 1, but with one number missing, write a function that finds the missing number.

1. Factorial Calculation
Write a function that calculates the factorial of a given number (n!), where n! = n * (n-1) * (n-2) * ... * 1. For example, 5! = 5 * 4 * 3 * 2 * 1 = 120.

1. Longest Word in a Sentence
Write a function that takes a sentence as input and returns the longest word in the sentence.

1. Array Sum (Two Numbers)
Given an array of numbers and a target sum, write a function to find two numbers in the array that add up to the target sum. Return their indices.

1. Merge Two Sorted Arrays
Write a function that merges two sorted arrays into one sorted array without using any built-in sorting methods.

1. Convert Decimal to Binary
Write a function that converts a decimal number into its binary representation.

1. Guess the Number (Game)
Create a simple guessing game where the computer randomly selects a number between 1 and 100, and the player has to guess the number. Provide feedback if the guess is too high or too low.

1. Count Occurrences of a Character
Write a function that takes a string and a character as input and counts the number of times the character appears in the string.

1. Remove Duplicates from a List
Write a function that takes a list as input and returns a new list with duplicate elements removed.

1. Find the Median of a List
Write a function that finds the median of a given list of numbers. If the list has an odd length, return the middle element. If it has an even length, return the average of the two middle elements.