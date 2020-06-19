# SaveMuney

## <b>Detail Overview</b>
The overall goal of this is to create an application which will automate the budgeting process. Users will be able to create their own budgeting categories, link their bank account, and automatically sort through statements without the hassle. The program will then remember your decisions, and be able to automate any transactions in the future. None of the apps I've ever came across really fit my taste, so why not make your own. Hope to add onto this with more complex features, which will probably be documented within this doc, as for now KISS (keep it simple stupid).

## <b>Installation</b>
### Python Installation
Below are the commands to run to install python:
<br/>`sudo apt update`
<br/>`sudo apt install software-properties-common`
<br/>`sudo add-apt-repository ppa:deadsnakes/ppa`
<br/>`sudo apt update`
<br/>`sudo apt install python3.8`
<br/><br/>

### GitHub Installation
`sudo apt install git`
#### Creating SSH Key
Run command: `ssh-keygen`, continue to press enter until key generation has completed.
Install xclip using the following command `sudo apt-get install xclip`, the copy the key over using `xclip -sel clip < ~/.ssh/id_rsa.pub`</br>
The key is now copied ton your clipboard, go into the settings on your github and select add new SSH Key then copy it into the description and press add.</br>

## <b>Code Structure</b>
Below is a basic skeleton on how the class system works within the program. Each class is a seperate dropdown with its member variables listed beneath it. The type of variable is listed next to it (not like it matters cause we are in python).
<details>
<summary>User</summary>
    <ul>
        <li>Username - String</li>
        <li><details>
        <summary>Bank Account</summary>
            <ul>
            <li>Log in Info - String</li>
            <li>URL to Bank - String</li>
            <li>Bank Statements - List of seperate class</li>
            </ul>
        </details></li>
        <li><details>
        <summary>Categories</summary>
            <ul>
            <li>Name - String</li>
            <li>Time period</li>
            <li>Target Budget - Double</li>
            <li>Current Balance - Double</li>
            <li>Labels - List of strings most likely</li>
            </ul>
        </details></li>
    </ul>
</details>

## <b>Features</b>

<details>
<summary><input type="checkbox" disabled>Basic Functionality<br></summary>
<ul>
    <input type="checkbox" disabled>Create user and category class<br>
    <input type="checkbox" disabled>Create addition and removal functions of categories<br>
    <input type="checkbox" disabled>Have setters and getters for category class<br>
</ul>
</details>

<details>
<summary><input type="checkbox" disabled>Create basic gui application<br></summary>
<ul>
    <input type="checkbox" disabled>Create Log in Page<br>
    <input type="checkbox" disabled>Display user categories neatly<br>
    <input type="checkbox" disabled>Have add and remove categorie options on gui<br>
    <input type="checkbox" disabled>Display addition and subtraction of categories<br>
</ul>
</details>

<input type="checkbox" disabled>Link bank account and automatically update their budget<br>