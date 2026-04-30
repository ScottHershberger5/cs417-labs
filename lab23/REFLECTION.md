0. Three hardest things to change?
    - I think it will be hard to change the actual expense report that is printed out, as well as the csv parser and lastly sorting the transactions by category will be tough.

1. Before / after. What three things in the starter did you write down in Part 0 as "hard to change"? Were you right? What surprised you?
    - The csv parser I was definetely right, it took me half the lab for some reason. The expense report to was hard because it felt like I had to change it everytime I added a new implementation. It suprised me the sorting the transactions was actually easier I thought when it was an external file.

2. Name what you did. For each of Parts 1, 2, 3: which design idea from class shows up in your refactor? You learned several this semester — single responsibility, dependency injection, separation of I/O from logic, strategy / pluggable parts. Pick the one that fits each part. Point at the lines or function names in your code.
    - I definetely used single responsibility, in all three parts honestly build_report, categorize, and parse_json/csv. That was basically the whole point of the refactoring I did. I took apart main() from having all the responsibility and encapsulated the different responsibilities into four seperate functions. 

3. The change request that hurt the most. Which of the three was hardest, and why? What was your first attempt before you realized it wouldn't work?
    - The first request was the worst, parsing the csv. It was hard because I assumed it took a csv file as a parameter, but it took a string. I should have read the type hints. My first attempt I didnt have any 
    "with open("csv_file.csv", "w") as f: f.write(text)" which is what takes the str and turns it into a csv that I can work with more naturally.
    

4. One imagined future change. If next week the requirement is "now pull transactions from a remote API," walk through what you'd add or change in your refactored code. (You don't have to actually implement it. About a paragraph is enough.)
    - I'd write a new function parse_api that takes transactions from the API and returns the same list of dicts that parse_csv returns. Then in main() I'd just swap out parse_csv for parse_api. Then build_report and categorize can stay the same since they only care about the list of rows, not where it came from.