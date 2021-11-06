# Requirement specification

## Purpose of the application

With the application, user has the ability to log events in a diary. Multiple registered users can use the application, with their own logs in the journal.

## Users

Application is planned to have a _regular user_ role. Later in the development process an _admin user_ can be added. _Admin user_ mentioned in the [Further development ideas](#further-development-ideas).

## User Interface wireframe

The application consists of three views.

- Login screen
- Preview screen
- Editing screen

## Functionalities

### Before logging in / registering

- User can register new user to the system
    - Username must be unique, min. 3 characters
    - Password must be min. 3 characters long

- User can log in
    - Logging in is done by inputting username and correct password to form, and clicking "Login"
    - In the event of invalid username, or invalid username and password combination, login screen notifies the user

### After logging in

- User can view list of diary entries
- User can create a new entry
  - Entry is only visible to logged in user
- User can open an entry to edit mode
- User can log out

### Edit mode

- User can update the entry text
    - After update the user is kept on current entry edit screen
- User can delete the entry
    - After deletion user is returned to list of entries
- User can return to list of entries without deleting or updating entry

## Further development ideas

After basic functionalities, following list of backlog items can be added following agile development methods

- Adding separate heading input for entries
- Adding tags to entries
- Grouping selected entries to folders/groups
    - Based on tags
- Showing stats of the single entry/group of entries/all entries
    - In separate view
    - At the bottom of an entry
- Admin user
    - View to overall user stats
    - View to individual user stats
- Different types of entries, that would show stats based on values in the entries
    - Food diary
    - Fitness diary
    - Time tracking diary

