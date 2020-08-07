# twitoff2
Twitter Project

## To add users in terminal
```sh
from twitoff.db_model import db, User, Tweet
u1 = User(username='name', follower_count=int)
```

## To add to db and commit changes
```sh
db.session.add(u1)
db.session.commit()
```