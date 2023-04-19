[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/uwidcit/flaskmvc)
<a href="https://render.com/deploy?repo=https://github.com/uwidcit/flaskmvc">
  <img src="https://render.com/images/deploy-to-render-button.svg" alt="Deploy to Render">
</a>

![Tests](https://github.com/uwidcit/flaskmvc/actions/workflows/dev.yml/badge.svg)

# Food Refined TT
Food Refined TT is a project undertaken by three final year UWI Computer Science Students to reduce food wastage and hunger in Trinidad and Tobago. Restaurants/Supermarkets are allowed to browse a list of shelters and choose which one they would like to donate to. From here, the donation items can either be delivered to the destination or picked up by the shelters. 



# Dependencies
* Python3/pip3
* Packages listed in requirements.txt

# Installing Dependencies
```bash
$ pip install -r requirements.txt
```

# Flask Commands

wsgi.py is a utility script for performing various tasks related to the project. You can use it to import and test any code in the project. 
You just need create a manager command function, for example:

```python
# inside wsgi.py

user_cli = AppGroup('user', help='User object commands')

@user_cli.cli.command("create-user")
@click.argument("username")
@click.argument("password")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

app.cli.add_command(user_cli) # add the group to the cli

```

Then execute the command invoking with flask cli with command name and the relevant parameters

```bash
$ flask user create bob bobpass
```


# Running the Project

The project can be ran in the terminal by executing the "flask run" command
```
$ flask run
```


# Deploying
This application has been deployed on Render 
<a href="https://food-refined.onrender.com/"></a>


