#!/usr/bin/env python
#connect proxychains sshfs root@netcat.us:/root/redcloud  /root/blackcat

from project import views
from project import models
from project import config

app = views.app

# Return an App
if __name__ == "__main__":
    views.app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
