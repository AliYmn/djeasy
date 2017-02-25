import subprocess
import json
from termcolor import cprint
import os
import sys
import platform
from validators import domain,ipv4
"""
Djeasy : Django simple quick setup
"""

# Main directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# As program only works on Python 3, avoiding to run on Python 2
if not sys.version_info >= (3, 0):
    sys.exit("This program runs only on Python 3.x\nExiting...")

# This program will work only on Debian and Ubuntu.
if sys.version_info < (3, 7):
    if not "debian" or not "ubuntu" in str(platform.linux_distribution()).lower():
        sys.exit("This program runs only on Debian and Ubuntu\nExiting...")
else:
    if not "debian" or not "ubuntu" in str(platform.platform()).lower():
        sys.exit("This program runs only on Debian and Ubuntu\nExiting...")


class EasyInstall:
    """ Package Install and Settings """

    def __init__(self, project_name, server_name_or_ip, static_url,
                 gunicorn_file, nginx_file, project_file, virtualenv_file):
        """
        :param project_name: Django project folder
        :param server_name_or_ip: Server ip or domain
        :param static_url: Django settings.py STATIC_URL address
        :param gunicorn_file : gunicorn file name
        :param nginx_file : nginx file name
        :param virtualenv_file : virtualenv file directory
        """

        self.project_name = project_name
        self.server_name_or_ip = server_name_or_ip
        self.static_url = static_url
        self.gunicorn_file = gunicorn_file
        self.nginx_file = nginx_file
        self.project_file = project_file
        self.virtualenv_file = virtualenv_file

        # package.json read.
        with open("{}/client/file/package.json".format(BASE_DIR)) as data_file:
            self.data = json.load(data_file)


    def __call__(self, *args, **kwargs):
        """Packages Loader"""

        for package in self.data['package']:
            cprint("{}".format(package['message']), 'white', 'on_red', attrs=['bold'])
            subprocess.call(package['name'], shell=True)

        # Restart.
        subprocess.call("sudo systemctl daemon reload", shell=True)
        subprocess.call("sudo systemctl restart nginx", shell=True)

        # Successfull package
        cprint("The packages have been successfully installed.", 'white', 'on_red', attrs=['bold'])

    def __add__(self):
        """It records Gunicorn vs nginx files."""

        # gunicorn file save and move
        with open("{}/client/file/gunicorn.service".format(BASE_DIR)) as gunicorn_files:
            gunicorn = gunicorn_files.read().format(self.project_name,self.project_file,self.virtualenv_file)
            file_gunicorn = open('{}/package/{}.service'.format(BASE_DIR, self.gunicorn_file), 'w')
            file_gunicorn.write(gunicorn)
            file_gunicorn.flush()
            file_gunicorn.close()

        cprint("{}.service file created.".format(self.gunicorn_file), 'white', 'on_red', attrs=['bold'])

        # File move operations
        subprocess.call("sudo cp {}/package/{}.service /etc/systemd/system/".
                        format(BASE_DIR,self.gunicorn_file), shell=True)

        # Gunicorn recording and restart
        subprocess.call("sudo systemctl start {0} & sudo systemctl enable {0}".format(self.gunicorn_file), shell=True)
        cprint("Gunicorn was registered and restarted.", 'white', 'on_red', attrs=['bold'])

        # nginx file save and move
        with open("{}/client/file/nginx".format(BASE_DIR)) as nginx_files:
            nginx = nginx_files.read().format(self.server_name_or_ip,
                                              self.static_url,self.project_file,self.project_name)

            nginx_file = nginx.replace('[', '{').replace(']', '}')

            file_nignx = open("{}/package/{}".format(BASE_DIR, self.nginx_file), 'w')
            file_nignx.write(nginx_file)
            file_nignx.flush()
            file_nignx.close()

        cprint("{} file created.".format(self.nginx_file), 'white', 'on_red', attrs=['bold'])

        # File move operations
        subprocess.call("sudo cp {}/package/{} /etc/nginx/sites-available/".
                        format(BASE_DIR, self.nginx_file), shell=True)

        # Nginx recording and restart
        subprocess.call("sudo ln -s /etc/nginx/sites-available/{} /etc/nginx/sites-enabled".
                        format(self.nginx_file), shell=True)

    def __copy__(self):
        """Gunicorn and nginx setting files"""

        # Gunicorn
        for gunicorn_package in self.data['gunicorn']:
            cprint(gunicorn_package['message'], 'white', 'on_red', attrs=['bold'])
            subprocess.call(gunicorn_package['name'], shell=True)

        cprint("Gunicorn successful!", 'white', 'on_red', attrs=['bold'])

        # Nginx
        for nginx_package in self.data['nginx']:
            cprint(nginx_package['message'], 'white', 'on_red', attrs=['bold'])
            subprocess.call(nginx_package['name'], shell=True)

        cprint("Nginx successful!", 'white', 'on_red', attrs=['bold'])

    def requirements(self):
        """requirements.txt install"""

        subprocess.call('{}/bin/pip3 install -r {}/requirements.txt'.format(self.virtualenv_file,
                                                                           self.project_file),shell=True)

        subprocess.call('{}/bin/pip3 install gunicorn'.format(self.virtualenv_file),shell=True)
        cprint("requirements.txt successfully loaded.!", 'white', 'on_red', attrs=['bold'])

    def save(self):
        """Records information."""

        with open('{}/client/file/server.info'.format(BASE_DIR)) as server_file:
            server_file = server_file.read().format(self.project_name,self.server_name_or_ip,self.static_url,
                                                    self.gunicorn_file,self.nginx_file,
                                                    self.project_file,self.virtualenv_file)

            file_fix = server_file.replace('[', '{').replace(']', '}')
            file = open('/home/{}.json'.format(self.project_name), 'w')
            file.write(file_fix)
            file.flush()
            file.close()

        cprint("/home/{}.json file created...".format(self.project_name), 'white', 'on_red', attrs=['bold'])
        cprint("All successful!", 'white', 'on_red', attrs=['bold'])

        subprocess.call('sudo chmod -R 777 /home/{}.json'.format(self.project_name), shell=True)

def nginx_restart():
    """Nginx Restart"""
    subprocess.call("sudo service nginx restart", shell=True)
    subprocess.call("sudo systemctl restart nginx", shell=True)
    cprint("Nginx has been successfully restarted.", 'white', 'on_red', attrs=['bold'])

def gunicorn_restart(project_name):
    """Gunicorn Restart"""

    with open("/home/{}.json".format(project_name)) as gunicorn_file:
        data = json.load(gunicorn_file)

        subprocess.call("sudo systemctl restart {}".format(data['project_name']), shell=True)

    cprint("Gunicorn has been successfully restarted.", 'white', 'on_red', attrs=['bold'])



def RunEasy():
    """It receives information from the user."""

    # server_ip_or_domain
    while True:
        cprint("Please type in the server ip or domain address.", 'white', 'on_red', attrs=['bold'])
        server_name_or_ip = str(input('server ip or domain = '))

        if server_name_or_ip == "":
            cprint("Please do not leave blank, try again...", 'white', 'on_red', attrs=['bold'])
            continue
        else:
            if(domain(server_name_or_ip) or ipv4(server_name_or_ip)):
                break
            else:
                cprint("Please enter a valid address...", 'white', 'on_red', attrs=['bold'])
                continue

    # Static Url
    while True:
        cprint("Write your STATIC_URL (Django Settings.py)", 'white', 'on_red', attrs=['bold'])
        static_url = str(input('STATIC_URL = '))

        if static_url == "":
            cprint("Please do not leave blank, try again...", 'white', 'on_red', attrs=['bold'])
            continue
        else:
            break

    # guniorn file name
    while True:
        cprint("Write your gunicorn file name", 'white', 'on_red', attrs=['bold'])
        gunicorn_file = str(input('Gunicorn File name = '))

        if gunicorn_file == "":
            cprint("Please do not leave blank, try again...", 'white', 'on_red', attrs=['bold'])
            continue
        else:
            break

    # nginx file
    while True:
        cprint("Write your nginx file name", 'white', 'on_red', attrs=['bold'])
        nginx_file = str(input('Nginx File name = '))
        if nginx_file == "":
            cprint("Please do not leave blank, try again...", 'white', 'on_red', attrs=['bold'])
            continue
        else:
            cprint("Write your virtualenv file path", 'white', 'on_red', attrs=['bold'])
            cprint("Example : /home/DjangoEnv", 'white', 'on_red', attrs=['bold'])
            break

    # virtualenv file
    while True:
        virtualenv_file = str(input('Virtualenv File path = '))
        if virtualenv_file == "":
            cprint("Please do not leave blank, try again...", 'white', 'on_red', attrs=['bold'])
            continue

        else:
            if(os.path.isdir(virtualenv_file)):
               break
            else:
                cprint("No such file or directory", 'white', 'on_red', attrs=['bold'])
                continue

    # project file
    while True:
        cprint("Write your Project file path", 'white', 'on_red', attrs=['bold'])
        cprint("Example : /home/Blog", 'white', 'on_red', attrs=['bold'])
        project_file = str(input('Project File path = '))

        if project_file == "":
            cprint("Please do not leave blank, try again...", 'white', 'on_red', attrs=['bold'])
            continue

        else:
            if(os.path.isdir(project_file)):
                break
            else:
                cprint("No such file or directory", 'white', 'on_red', attrs=['bold'])
                continue


    project_name = str(project_file).split('/')[len(str(project_file).split('/'))-1]

    easy = EasyInstall(project_name, server_name_or_ip, static_url, gunicorn_file,
                       nginx_file, project_file, virtualenv_file)
    easy.__call__()
    easy.__add__()
    easy.__copy__()
    easy.requirements()
    easy.save()

    # Restarting.
    subprocess.call("sudo service nginx restart", shell=True)
    subprocess.call("sudo systemctl restart nginx", shell=True)
    subprocess.call("sudo systemctl restart {}".format(gunicorn_file), shell=True)


def main():
    """Working area"""

message = """
Options:

    --create                            Create a new site.
    --nginx                             Nginx restart
    Project_name --gunicorn             Gunicorn restart

"""

if (len(sys.argv)) == 2:

    if str(sys.argv[1]) == "--create":
        RunEasy()

    elif str(sys.argv[1]) == "--nginx":
        nginx_restart()

    else :
        print("Command not found\n", message)

else:

    if(len(sys.argv)) > 2:

        if  str(sys.argv[2]) == "--gunicorn":
            gunicorn_restart(sys.argv[1])

        else:
            print("Command not found\n",message)

    else:
        print(message)


if __name__ == '__main__':
    main()