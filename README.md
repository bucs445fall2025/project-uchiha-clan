# Cooky
## CS 445 Final Project
### Fall 2025

### Team: Uchiha Clan
Jackson Carey
Derek Li
Jack Sutera

## Getting Started
Cooky is a recipe-sharing site centered around a blog feature, where users can submit their favorite recipes, browse other  
users' recipes, and track dietary goals as an additional feature. Recipe posts can be liked, commented on, and added directly  
to your goals. Multiple goals can be created based on macro counts, and when you eat a posted recipe, you can add its macros  
directly to your goals from that recipe card. 

### Roadmap
  <<
A list of features, function or non-functional, you would like to add in the future if you had time, i.e. Phase 2 stuff
- [ ] Add Changelog
- [ ] Add a "recipe builder" to easily calculate caloric/macro amounts
- [ ] Add User Accounts
- [ ] Add a preliminary database of recipes
  >>
  
## SRS
[[Our SRS](https://docs.google.com/document/d/1vp6U_T2O5XnSDwcmeQRHlv02YtWfmNAtFRZirpYPtFM/edit?tab=t.0)](url to google doc)
  
### Prerequisites
* [Docker](https://www.docker.com/)
* <<any additional software. Be specific about versions.>>

### Installing
<<
 A step by step series of examples that tell you how to get a development env running
Say what the step will be  
`Give the example`  
And repeat  
`until finished`  
End with an example of getting some output from the system, such as a menu or prompt

1. Clone Repo to a new folder.
2. CD into /recipeblog/
3. Run "docker-compose up --build" in the command line (While CD'd into /recipeblog/)
4. Enter "localhost" into a browser of your choice.
5. Enjoy the features of the site!
6. After quitting app (ctrl+c in command line), run "docker-compose down"

## Built With
 << list all frameworks and modules used here >>
* [requests](https://docs.python-requests.org/en/latest/user/quickstart/#make-a-request) - request for humans

## License
MIT License

Copyright (c) 2025 Jack Sutera, Derek Li, Jackson Carey

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Acknowledgments
* Hat tip to anyone whose code was used
* Inspiration
* etc
