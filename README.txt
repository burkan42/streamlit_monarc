Documentation for OpenML mythbusting:

Description of web app:
This app uses a algorithms from OpenML to do the following:
    - Running flows on tasks
    - Checks for all task(of a benchmark_suite) if they are already ran on a flow, else runs them
    - Creates multiple plots comparing the flows on the given study

Documentation:
To launch our web app we use streamlit. Streamlit is an easy way to publish a python app online. Documentation of streamlit can be found here: https://streamlit.io/

When your streamlit app is pushed to a github repo e.g. https://github.com/<user>/<name of repo>
You can connect to your website with this link:
https://share.streamlit.io/<user>/<name of repo>/main/myapp.py

you can also chose to run this app locally in your (Ubuntu)console with: “streamlit run myapp.py”

In our case this is the repository:
https://github.com/burkan42/streamlit_monarc
and this our link to the web app:
https://share.streamlit.io/burkan42/streamlit_monarc/main/myapp.py

In the latter link all our code can be found.

The figurative “main” of this project is “myapp.py”. Here the webpage is loaded, the input is gathered from the input fields and this script collects all the data of the runs, if the data is unknown of the run, this script can gather these unknowns with 
“openml_gatheringruns.py.”
In this script we gather all the tasks that haven’t been run on the given flow yet, and return these to be run in the “myapp.py”. (Now we have known unknowns.) The script then tries to run the unknowns, but what we will often see is that it is impossible to run thesse flows on these tasks. 

“OpenML_connection.py”
creates the graphs (which are shown by myapp.py) with the data we collected.
It makes 3 graphs showing the results of the flow comparisons. We save these graphs as .png’s. 

In all scripts further local documentation can be found!


