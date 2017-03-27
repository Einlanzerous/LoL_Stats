LoL_Stats
League of Legends Stats/API

Created by Ashley Dodson (database/Python), Leng Ghuy (HTML/CSS/JS), Michael Scott (front end help)

This is a proof of concept using the Riot API for pulling statistics for players. This is also our first full MEAN Stack, and is designed to be able to be deployed regardless of location (with the node.js server and the associated page). Somewhere you do need to run grab_names.py to act as a bridge between the two databases. It ensures that a valid name is entered and does't allow users to interact with the core server. 

By default this just pulls a few basic stats from your last five games and builds some information from this. I will include a picture of a positive name search, and an invalid one for future use. This was a group project.

<b>Databases:</b><br>
Katarina- Primary data location<br>
Caitlyn- Name list, awaiting entry<br>

<b>Change Log</b>
<i>example format:</i><br>
03/07/2017 | 08:04P- Created GitHub for project. AND<br>
03/18/2017 | night- Created Python script for putting data into the server. AND<br>
03/21/2017 | morning- Re-wrote code with comments and cleaner format. AND<br>
03/21/2017 | 08:35P- Pushed grab_name.py to server for linking two databases. Also pushed node.js file for sending name to Caitlyn. AND<br>
03/21/2017 | 09:46P- grab_name.py now works- runs and makes name requests as they come in. Added test js for demonstrating name inserting with node.js. AND<br>
03/22/2017 | 01:29P- Fixed a typo in the database, added a print script to shwow what is in database.<br>
