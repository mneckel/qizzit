# qizzit
A very simple quiz generator.  

- Less than 100 lines of Python
- Public domain
- No external modules to download
- Should work on Windows, Linux and macOS

## Quiz File Format
- Plain text file
- See the example file "questionsp1.txt"
- "!" starts a quiz question
- "=" for the correct answer
- "*" starts each possible answer. There must be 4 of them.
- "$" by itself indicates the end of the QA.
- "#" indicates the end of the quiz file

## Execution
At CLI:
```./qizzit.py questionsp1.txt```
