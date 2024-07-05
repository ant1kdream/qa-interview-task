In this repository, you have a set of files required to test two json documents. 

One json document serves as a reference (folder "expected") the other one was retrieved from a real system (folder "actual").

The requirements.txt already has basic dependencies to run the test. Feel free to add more dependencies if you desire to use some specific libraries.

Your work should be placed in the test_topic.py file. You are supposed to produce a readable and understandable difference between two files in order to help developers of the system to quickly identify bugs. 

Please try to make the report as useful as possible, to highlight separately what is missing, what was added and what is new.

##### IMPORTANT: please do not use any existing libraries that will do dictionary comparison in a single line of code. They work nice only in simple cases and the output is time consuming to interpret. We are looking for a custom solution that will show case your ability to operate effectively on moderately complex data structures, like lists and dicts.