# twitoff2
Twitter Project

## To run the app in your web browser
```sh
FLASK_APP=twitoff flask run
```

## To add users in terminal
```sh
FLASK_APP=twitoff flask shell
from twitoff.db_model import db, User, Tweet
u1 = User(username='name', follower_count=int)
```

## To create a new sqlite db
```sh
FLASK_APP=twitoff flask shell
from twitoff.db_model import db, User, Tweet
db.create_all()
```


## To add to db and commit changes
```sh
db.session.add(u1)
db.session.commit()
```