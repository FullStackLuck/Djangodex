# Product Requirements Documentation

**Summary**
| Field | Detail |
|-------|--------|
| Project Name | DjangoDex|
| Description |Gotta Catch em All |
| Live Website | N/A|
| Repo |git@github.com:FullStackLuck/Djangodex.git,  |
| Planning | https://miro.com/app/board/uXjVOvArU-k=/ https://trello.com/b/yJDAuuP1/unit-4-project-djangodex|
| Technologies | Jinja, CSS, Python , AWS, Netlify, Heroku, Imgur, Miro,Trello Styled-Components, Github. |

## User Stories

- As a user, I want to sign up for account
- As a user, I want to login using authentication
- As a user, I want User will be able to add Pokemon to Pokedex
- As a user, I want to be able to see a able to give a pokemon an item to hold.
- As a user, I want to be able teach pokemon new moves
- As a user, I want to be able to able to forget moves
- As a user, I want to be able to see a to remove a pokemon Item
- As a user, I want to be able to be able to remove a pokemon from Pokedex


## Route Tables

| Endpoint | Method | Response | Other |
| -------- | ------ | -------- | ----- |
| / | GET | Display of all Pokedex | |
| /pokemon | POST | Create new Wine | body must include data for new item |
| /pokemon/:id | GET | Get a Pokemon Details | |
| /pokemon/:id | PUT | Update/Change Pokemon information | body must include updated data |
| /:pokemon/:id | DELETE | Delete a pokemon by id | |


## ERD
[Imgur](https://i.imgur.com/1LjDDqG.png)


## User Interface Mockups


## Live Site

https://django-dex.herokuapp.com

## Future Enhancements
1.Adding Pokemon more Pokemon Data
2.Using Third Party API to get a list of pokemon to choose from
3.Render Pokemon on pokedex page.
4.Trade pokemon between users.
5.More CSS
