## Behave Framework
Walkthrough to install, set up and run the tests.\
Scenarios for the APIs [ReqRes](https://reqres.in/) and [JSON Place Holder](https://jsonplaceholder.typicode.com/posts/)

##
### Requirements - Windows (10 or +)

Install latest [**Python**](https://www.python.org/downloads/windows/) 
>**_Note_**: Check ``Add Python 3.8 to PATH`` option during the installation 

Install latest [**GIT**](https://git-scm.com/download/win) to clone the repository

Download the latest report framework [**Allure**](https://github.com/allure-framework/allure2/releases) and unzip in any folder (e.g. /Downloads)
 - Open the _Powershell_ terminal: ``Start Menu > type it 'Powershell'``
 - Set _Allure Framework_ ``PATH`` with the command: 
````bash
$env:PATH += ';\Allure_Folder_Path\allure-x.xx.x\bin'
````

Install latest [**Java JDK**](https://www.java.com/pt_BR/download/) and open the options: ``Start Menu > type it 'Environment' > 
'Edit Environment Variables' > Environment Variables``

- Create a new user variable ``JAVA_HOME`` and set has value the path where Java was installed
- Create a new system variable in _Path_, adding the expression ``%JAVA_HOME%\bin``
- Restart PC.

##
### Requirements - Linux (Ubuntu)
Install latest **Python** (executable): ``sudo apt-get install python3``

Install **Python pip**: ``sudo apt install python3-pip``

Install **GIT**: ``sudo apt install git``

Download the latest report framework [**Allure**](https://github.com/allure-framework/allure2/releases) and unzip in any folder.\
Open bash terminal and set the _Allure Framework_ folder path ``bin`` in ``PATH`` environment: 
````bash 
export PATH=$PATH:~/Allure_Path/bin
source ~/.bashrc
````

Install latest [**Java JDK**](https://www.java.com/pt_BR/download/) and create environment variable ``JAVA_HOME`` and set has value the path where Java was installed.\
Set the folder ``\bin`` in Path environment.
> _**Note**_: Guide to install Java in Linux [guia da Oracle](https://www.java.com/pt_BR/download/help/path.xml)  


After that it should be possible to check the _Allure_ version (``allure --version``) to confirm if ``PATH`` was set correctly.

##
### Git Clone and Libs Install

Create a folder that will receive the repository files.\
Clone the repo [Behave Framework](https://github.com/WillCoutinho/behave-framework.git) and access the cloned folder.

Install the package ``pipenv``: ``pip install pipenv``\
Run the VirtualEnv using command: ``pipenv shell``\
Install the dependencies from ``Pipfile`` (root directory): ``pipenv install``\
Wait for the all dependencies be installed.

To run all tests use the commands below. 
The parameters are:\
``-f allure_behave.formatter:AllureFormatter``: output format (_Allure Framework_)\
``-o allure_result_folder``: folder where the output will be saved\
``./features``: features that will be executed
       
````bash
behave features\employees\employee_management.feature -f allure_behave.formatter:AllureFormatter -o allure_result_folder
````
 
After test conclusion, use the command below to generate the Allure report.
This command will create a local server that will read the files from ``allure_result_folder`` and will launch the results on browser:
````bash
allure serve allure_result_folder
````

API tests reports are available on browser.
##
#### Git Repository

GitHub: [*Behave Framework*](https://github.com/WillCoutinho/behave-framework) 

##
#### Libs

* [Behave](https://pypi.org/project/behave/#description) - BDD with Python
* [Allure-Behave](https://pypi.org/project/allure-behave/#description) - Framework for reports
* [Faker](https://pypi.org/project/Faker/#description) - Faker data generator
* [Pipenv](https://pypi.org/project/pipenv/#description) - Package/VirtualEnv manager 
* [Requests](https://pypi.org/project/requests/#description) - HTTP library
* [PyHamcrest](https://pypi.org/project/PyHamcrest/#description) - Framework for matcher objects
