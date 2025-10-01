# **Project Overview**

## **Application Vision/Goal:**
[Describe the overall purpose and vision of the application. What problem does it solve? Who is the target audience?]
- Basic Idea: Recipe Blog Posting Site
- Implement a web page where users can individually post, search for, and use shared recipes
- Recipies will contain ingredients and instructions, along with calorie count and other food macros
- Solves an issue of finding popular home-cooked, healthy meals that meet macro goals
- Target audience: Home Chefs, Gymgoers, and generally people looking to cook their own meals

## **Scope:**
[List the major features and functionalities that define the scope of the project. Keep this high-level to avoid feature creep.]
- Blog
  - Posting
    - Users able to enter recipe posts with necessary and optional info
  - Searching
    - Users able to search for specific recipies by name
    - Users able to filter search results by cuisine, calorie count, etc.
    - Users able to search by popularity (see public interaction)
  - Public interaction
    - Users able to interact with recipie posts to reflect that they made the recipie
    - Increases a blog post's popularity, based on how many people have made it
Ideas:
- Report System?
    - Might be feature creep (let's assume for now users have good intentions)
    - Devs able to review peoples recipes to verify not spam/botting
- Calorie/Macro Tracker
    - Users able to track their daily macros, by inserting what they have eaten into the web application
    - May have to manual insert macros of meal (depending on our database of foods)

## **Deliverables:**
[List what will be delivered by the end of the project, such as a working MVP (Minimum Viable Product), specific features, documentation, etc.]
- Working Product:
  - Site where a user can complete the Blog, Search, and Public Interaction portions listed in the scope
  - Clean, aesthetic, neat site with smooth UI interactions
  - User can easily/efficiently track Calories/macros throughout their day

## **Success Criteria:**
[Define what will make this project successful. Examples include meeting deadlines, delivering core functionality, or achieving performance benchmarks.]
- Dedication to work outside of class-time
  - Nothing "over-the-top", but efforts outside of class needed to deliver on a quality product
- Users find product easy to use, happy with what the site does
- Measure gain of users/wk (if it goes live)
- Loading and searching data is relatively quick compared to todays standards

## **Assumptions:**
[List any assumptions about the technology, users, or resources that could impact development.]
- Users will access the application primarily via web browser (desktop + mobile responsive).
- Users want to create accounts to track macros, upload recipes, and interact with other users.
- We’ll initially support text uploads for recipes (no video/image yet).
- Traffic will be relatively low during MVP → scaling concerns can come later.
- MongoDB will handle recipes, user data, and goals (flexible schema needed).

Team is familiar with Python → Flask (or FastAPI) is the chosen backend framework.

## **Risks:**
[Identify potential risks and challenges, such as technical limitations, resource constraints, or dependency issues.]
- An obvious time limit of the semester's end
- Limited knowledge of tools we would like to use
  - Need to make an effort to learn about tools necessary to make the product succeed
- Learning curve for Flask/MongoDB integration.
- Handling file uploads (storage, size limits, compression).
- Authentication/authorization (security vulnerabilities if poorly implemented).
- MongoDB schema design could get messy without careful planning.

## **Design / Architectural Review:**
[Outline the initial thoughts on application architecture. Will it be monolithic or microservices? Will it use a database? What major components will be included?]
- Monolithic: One service working with one database that services many people.
- Database: MongoDB 

## **Test Environment:**
[Define how the application will be tested. Will you use automated tests? What environment will the tests run in?]
- Will consist of having the test go live, making posts, and seeing what gets represented in our database


---

# **Team Setup**

## **Team Members:**
[List all team members involved in the project.]
- Derek Li
- Jackson Carey
- Jack Sutera

## **Team Roles:**
[Define roles for each team member, such as developer, designer, project manager, QA tester, etc.]
- Derek:
- Jackson: developer/QA tester
- Jack: Developer, UI/UX Lead

## **Team Norms:**
[Establish how the team will communicate, how often meetings will happen, and any other ground rules for collaboration.]
- Communication will take place over iMessage, meetings ideally 2x/wk. Ask teammates for help on something you're unsure about.

## **Application Stack:**
[List all the technologies being used in the project, including programming languages, frameworks, and tools.]
- Backend: Python/Flask
- Frontend: HTML/CSS, JS
- DB: NoSQL - MongoDB
- Server: Nginx

### **Libraries/Frameworks:**
[List any specific libraries or frameworks your application will use, such as React, Flask, Django, etc.]
- Flask
- ? Anything else ?





