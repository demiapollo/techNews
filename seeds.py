from app.models import User, Post, Comment, Vote
from app.db import Session, Base, engine


# drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()

# insert users
db.add_all([
  User(username='apo', email='apo@gmail.com', password='password123'),
  User(username='joe', email='rmebes1@sogou.com', password='password123'),
  User(username='jenny', email='cstoneman2@last.fm', password='password123'),
  User(username='lauren3', email='ihellier3@goo.ne.jp', password='password123'),
  User(username='david67', email='gmidgley4@weather.com', password='password123')
])

db.commit()

# insert posts
db.add_all([
  Post(title='Intro to to Computer Science', post_url='https://pll.harvard.edu/course/cs50-introduction-computer-science', user_id=1),
  Post(title='Intro to databases', post_url='https://cs50.harvard.edu/sql/2023/', user_id=1),
  Post(title='Intro to Programming with Python', post_url='https://pll.harvard.edu/course/cs50s-introduction-programming-python', user_id=2),
  Post(title='Computer Science for Business', post_url='https://pll.harvard.edu/course/cs50s-computer-science-business-professionals-0', user_id=3),
  Post(title='Computational Thinking', post_url='https://online.york.ac.uk/what-is-computational-thinking/', user_id=4)
])

db.commit()

# insert comments
db.add_all([
  Comment(comment_text='This is a great resource.', user_id=1, post_id=2),
  Comment(comment_text='Thanks for sharing this.', user_id=1, post_id=3),
  Comment(comment_text='Very useful.', user_id=2, post_id=1),
  Comment(comment_text='An excellent change to learn effectively.', user_id=2, post_id=3),
  Comment(comment_text='🙏🏼', user_id=3, post_id=3)
])

db.commit()

# insert votes
db.add_all([
  Vote(user_id=1, post_id=2),
  Vote(user_id=1, post_id=4),
  Vote(user_id=2, post_id=4),
  Vote(user_id=3, post_id=4),
  Vote(user_id=4, post_id=2)
])

db.commit()


db.close()

