import praw

reddit = praw.Reddit(client_id = '',
                     client_secret = '',
                     username = '',
                     password = '',
                     user_agent = '')
subreddit = reddit.subreddit('all')

keyphrase1 = 'essential oils work '
keyphrase2 = 'they do work '
keyphrase3 = 'it does work '

for comment in subreddit.stream.comments():
    if (keyphrase1 in comment.body) or (keyphrase2 in comment.body) or (keyphrase3 in comment.body):
        try:
            comment_reply = 'No they don\'t honey please check out *https://www.huffpost.com/entry/essential-oils_l_5d93a00de4b0019647b010df*'
            comment.reply(comment_reply)
            print('Comment Posted')
            #exit()
        except:
            print('You might be doing this to often please take a break.')
                     

