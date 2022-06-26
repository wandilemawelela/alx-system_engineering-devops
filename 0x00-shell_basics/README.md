Task 0
======
Write a script that prints the absolute path name of the current working directory.

Task 01
=======
Display the contents list of your current directory.

Task 02
=======
Write a script that changes the working directory to the user’s home directory.
	- You are not allowed to use any shell variables

Task 03
======
Display current directory contents in a long format

Task 04
=======
Display current directory contents, including hidden files (starting with .). Use the long format.

Task 05
======
Display current directory contents.
	- Long format
	- with user and group IDs displayed numerically
	- And hidden files (starting with .)

Task 06
=======
Create a script that creates a directory named my_first_directory in the /tmp/ directory.

Task 07
=======
Move the file betty from /tmp/ to /tmp/my_first_directory.

Task 08
=======
Delete the file betty.
	- The file betty is in /tmp/my_first_directory

Task 09
=======
Delete the directory my_first_directory that is in the /tmp directory.

Task 10
=======
Write a script that changes the working directory to the previous one.

Task 11
=======
Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.

Task 12
=======
Write a script that prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script.

Task 13
=======
Create a symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working directory.

Task 14
=======
Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.

You can consider that all HTML files have the extension .html

Task 15
=======
Create a script that moves all files beginning with an uppercase letter to the directory /tmp/u.

You can assume that the directory /tmp/u will exist when we will run your script

Task 16
=======
Create a script that deletes all files in the current working directory that end with the character ~.

Task 17
=======
Create a script that creates the directories welcome/, welcome/to/ and welcome/to/school in the current directory.

You are only allowed to use two spaces (and lines) in your script, not more.

Task 18
=======
Write a command that lists all the files and directories of the current directory, separated by commas (,).
	- Directory names should end with a slash (/)
	- Files and directories starting with a dot (.) should be listed
	- The listing should be alpha ordered, except for the directories . and .. which should be listed at the very beginning
	- Only digits and letters are used to sort; Digits should come first
	- You can assume that all the files we will test with will have at least one letter or one digit
	- The listing should end with a new line

Task 19
=======
Create a magic file school.mgc that can be used with the command file to detect School data files. School data files always contain the string SCHOOL at offset 0.
