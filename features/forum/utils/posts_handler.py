
def header_payload():
    return {"Content-Type": "application/json"}


def post_payload():
    from faker import Faker
    
    fake = Faker()
    
    return {
        "title": fake.ascii_email(),
        "body": fake.text(),
        "userId": fake.random_int(0, 100)
    }


def random_comment(post_id=None, comment_id=None):
    from features.forum.utils.comments_list import all_comments
    
    comment_obj = None
    
    if comment_id is None:
        for comment in all_comments:
            if comment['postId'] == post_id:
                comment_obj = comment
                break
                
    else:
        for comment in all_comments:
            if comment['id'] == comment_id:
                comment_obj = comment
                break
        
    return comment_obj


def random_post():
    from random import choice
    from features.forum.utils.posts_list import all_posts
    
    return choice(all_posts)

    