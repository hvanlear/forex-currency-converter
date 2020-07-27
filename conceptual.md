### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  1. Syntactic 
  2. Python is an Object Oriented Language, Javascript is more scripting
  3. NO Iimplict conversion between typs in python
  4. Python is more of a server side language where has JS runs more client side

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
   1. Using the .get() method

- What is a unit test?
  1. Testing the smallest possible parts of software/applicaitons

- What is an integration test?
  1. Testing larger, more grouped peices of an applicaition to ensure they run as a whole

- What is the role of web application framework, like Flask?
  1. Flask allows you to build a web application by providing tools, libraries, and technologies

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
    1. POST requests don't typically include a query string as they tend to include data that you want to keep within the request body, so you'll mostly be using them with GET requests.

- How do you collect data from a URL placeholder parameter using Flask?
  1. you create by adding <data> placeholders in the URL and accepting corresponding data arguments in the view function.

- How do you collect data from the query string using Flask?
  1. request.args.get('data')

- How do you collect data from the body of the request using Flask?
  1. pass it into the return render_template function as a variable

- What is a cookie and what kinds of things are they commonly used for?

- What is the session object in Flask?

- What does Flask's `jsonify()` do?
