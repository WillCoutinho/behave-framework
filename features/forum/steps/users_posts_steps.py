from behave import given, when, then
from hamcrest import assert_that, is_, has_entries


@given('I have a new post to create')
def step_impl(context):
    from features.forum.utils.posts_handler import post_payload
    
    context.forum_post = post_payload()


@when('I send this post to "{endpoint}"')
def step_impl(context, endpoint):
    from features.forum.page.posts_requests import create_post
    
    context.post_response = create_post(endpoint, body=context.forum_post)
    assert_that(context.post_response.status_code, is_(201), "Status Code should be Success (201)")


@then('the post data should be returned as response')
def step_impl(context):
    assert_that(context.post_response.json(),
                has_entries({
                    "title": context.forum_post["title"],
                    "body": context.forum_post["body"],
                    "userId": context.forum_post["userId"]}),
                "Response should return the same post data sent previously")


@given('I have an id from a post already created')
def step_impl(context):
    from features.forum.utils.posts_handler import random_post

    # JSON PlaceHolder doesn't persist (even in cache) any payload.
    # So the alternative to that is use the demo data available in their website.

    context.post_obj = random_post()


@given('I want to check all comment data from this post')
def step_impl(context):
    from features.forum.utils.posts_handler import random_comment
    
    context.comment_obj = random_comment(post_id=context.post_obj['id'])


@when('I send the comment id to "{endpoint}"')
def step_impl(context, endpoint):
    from features.forum.page.posts_requests import get_post
    
    context.post_response = get_post(endpoint, _id=str(context.comment_obj['id']))
    assert_that(context.post_response.status_code, is_(200), "Status Code should be Success (200)")


@then('the comment data should be returned as response')
def step_impl(context):
    assert_that(context.post_response.json(),
                has_entries({
                    "postId": context.post_obj["id"],
                    "id": context.comment_obj['id'],
                    "name": context.comment_obj['name'],
                    "email": context.comment_obj['email'],
                    "body": context.comment_obj['body']}),
                "Response should return the same data from post/comment choose in the list")


@when('I send the post id to "{endpoint}"')
def step_impl(context, endpoint):
    from features.forum.page.posts_requests import get_post_by_path
    
    endpoint = f'{endpoint}={context.post_obj["id"]}'
    context.post_response = get_post_by_path(endpoint)
    assert_that(context.post_response.status_code, is_(200), "Status Code should be Success (200)")
    
    
@then('the comment list should be returned as response')
def step_impl(context):
    from features.forum.utils.posts_handler import random_comment
    
    for obj in context.post_response.json():
        comment_obj = random_comment(comment_id=obj['id'])
        
        assert_that(obj,
                    has_entries({
                        "name": comment_obj['name'],
                        "email": comment_obj['email'],
                        "body": comment_obj['body']}),
                    "Response should return the same data from post/comment choose in the list")