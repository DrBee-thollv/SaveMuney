# SaveMuney
## Python Installation
Below are the commands to run to install python:
<br/>`sudo apt update`
<br/>`sudo apt install software-properties-common`
<br/>`sudo add-apt-repository ppa:deadsnakes/ppa`
<br/>`sudo apt update`
<br/>`sudo apt install python3.8`
<br/><br/>

## GitHub Installation
`sudo apt install git`
### Creating SSH Key
Run command: `ssh-keygen`, continue to press enter until key generation has completed.
Install xclip using the following command `sudo apt-get install xclip`, the copy the key over using `xclip -sel clip < ~/.ssh/id_rsa.pub`</br>
The key is now copied ton your clipboard, go into the settings on your github and select add new SSH Key then copy it into the description and press add.
