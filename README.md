# Tackle Take Home Project (Full Stack Software Engineer)

# Instructions
You have been provided a simple full stack web application composed of a SQLite database, python (flask) server, and a react front end client.

Please create a git repository and make meaningful commits as you work on the following problem. After you have completed the project or have spent four hours working on the project (which ever comes first) please zip the contents of the repository and send it back to us.

Tackle.io is a software vendor that has listed two products on the AWS marketplace. One is an Amazon Machine Image (AMI) called "Tackle Amazon Machine Image" and the second is a Software as a Service (SaaS) listing called "Tackle for GovCloud". 

Since listing on the AWS marketplace six months ago they have received several orders. Tackle has requested that a webpage be built to view all of their listings and the orders associated with each listing. They would also like to see the total revenue generated through the AWS marketplace.

***BONUS***
As a stretch goal Tackle briefly mentioned that they would want to see a graph of revenue over the last year segmented by month.

# Grading
The most important thing about the take home project is that it serves as a code sample in a vacuum as well as problem solving ability within some time constraint.  We want to make sure you have some level of mastery over the primary programming languages we use (python & javascript).  There are many factors that we evaluate, but the most important are roughly:
 1) code quality, correctness, and approach/process
 2) completion - seeing work on both backend/frontend
 3) front end design / ux
 4) error handling
 5) write a few tests; illustrate intent, 100% coverage is not necessary

### Run the API (Python 3.7.6)
```
cd tackle-api
```
Optionally create a virutal environment to keep your python packages isolated.
```
python -V
>> Python 3.7.6
python -m virtualenv venv
source venv/bin/activate
```
Install dependencies in requirements.txt.
```
pip install -r requirements.txt
```
Start the server.
```
python server.py
```

In a separate terminal use the canary test to make sure your server is running:
```
curl localhost:5000/canary
```

The response should say:
```
Welcome to the Tackle Take Home Project API!
```

### Run the Client
```
cd tackle-app
yarn --version
>> 1.3.2
yarn install
yarn start
```

To test that the client is running open a browser and navigate to localhost:3000.

### Loading Seed Data into SQLite
To load the seed data into your database start a python shell and import util. Util has a function called build_or_refresh_db you can call to load all of the seed data into a SQLite db called `tkldb`.

```
cd tackle-api
source venv/bin/activate
python
>>> import util
>>> util.build_or_refresh_db()
data refreshed!
>>> 
```

