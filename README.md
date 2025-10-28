# Board Game Picker

A Flask-based web application to manage, filter, and explore board games. Users can add new games, view all games in a card layout, filter games by player count and categories, or pick a random game. The app features a modern, responsive design that works on both desktop and mobile.

## Features

- **Add New Games**  
  Add board games with:
  - Name  
  - Minimum and maximum number of players  
  - Categories (Simple, Complicated, Quick, Long, Cooperative, Party, Frenetic, Table, Couch)  
  Access to add games is protected by a secret word.

- **List All Games**  
  View all games in a responsive card layout with hover effects.

- **Filter Games**  
  Filter games by:
  - Number of players  
  - Game categories  
  Supports mutually exclusive categories:
  - Simple vs Complicated  
  - Quick vs Long  
  - Table vs Couch  
  Standalone categories (Party, Cooperative, Frenetic) can be combined freely.

- **Random Game Picker**  
  Pick a random game based on selected number of players and categories.

- **Responsive Design**  
  All pages use a card layout for games and a modern form design, working well on mobile and desktop.


