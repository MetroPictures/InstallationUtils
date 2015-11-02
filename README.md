## First, do this

1.	Make sure the public key is added to each sculpture (add metropictures.pub to `~/.ssh/authorized_keys`).
1.	Set the variable `PATH_TO_INSTALLATION_UTILS` to the full path of this repo on your machine.
1.	append the `.mp_bash_aliases` script to you bash profile by adding the line `source .mp_bash_aliases` to it.
1.	Run `source ~/.bash_profile` or whatever to start using.

## Then, the things you can do

1.	Startup _all_ sculptures: `metropictures.startup`
1.	Startup _one_ sculpture: `metropictures.startup sculptue`
1.	Shutdown _all_ sculptures: `metropictures.shutdown`
1.	Shutdown _one_ scuplture: `metropictures.shutdown sculpture`
1.	Restart _all_ sculptures: `metropictures.restart`
1.	Restart _one_ scuplture `metropictures.restart sculpture`
1.	SSH into a sculpture (port-forwarding automatically enabled): `metropictures.sculpture`