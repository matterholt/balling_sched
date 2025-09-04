# Balling Soccer Schedule

Application that will show schedule games for all teams in the league.



<strong>League</strong> app is exploring, figuring out some tech out

<strong>game_schedule</strong> is primary focused with getting the game schedules on teh web


## Fix My Issue

- As a volunteer coach and parent of player, I wanted to make it easier for me to add my kiddos games to the calender.

- Make it easy to share information to other parent of players, Information is transferred by spreadsheet and SMS.


### Features

### Models

#### Season Schedule

Extracted from a spreadsheet

| SeasonSchedule |                         |
| -------------- | ----------------------- |
| date           | DateField               |
| time           | TimeField               |
| field          | CharField               |
| home           | CharField               |
| vistor         | CharField               |
| location       | foreignKey (short_name) |
| division       | foreignKey (name)       |


#### Locations

column in spreadsheet, which has just the short name.

| Venues               |           |
| -------------------- | --------- |
| short_name (indexed) | CharField |
| name                 | CharField |
| address              | CharField |
| city                 | CharField |
| state                | CharField |
| zip_code             | CharField |

#### Division

Tab in spreadsheet.

| Venues      |           |
| ----------- | --------- |
| name        | CharField |
| description | CharField |
| class       | CharField |
| name_SAY    | CharField |
| age_range   | CharField |





## Write up
### Build Decisions

The application current doesn't need to have a lot of js sending to client. Data is king, and just need to be able to show the user the information once or twice. The user shouldn't spend time tweaking data. Would just need to check the schedule, download a iCalender file, table /spreadsheet or the ability to print schedules.

I've been using python for a bit and wanted to get a project out in the wild that uses it. That would leave Flask, Django; maybe others like Quart and Starlette. the latter are interesting me but I wanted to use something robust and with a larger community. Flask I like, because of it un-opinionated nature and the ability to wire everything up. But this would require some overhead to get the project off the ground. Which leaves Django.


## RESOURCES

[classy class Django views](https://ccbv.co.uk/projects/Django/5.2/django.views.generic.edit/CreateView/)
