import tweepy,time

auth = tweepy.OAuthHandler('UFUQqG0fjbZgZDz8BiguVe8ll', 'n0cdLRLRZOsk7MC8eqezSzpxBy5vb9oUVh9OJeGMUSmdOFkMid')
auth.set_access_token('1425435816-xe1jvvCa9uMGbq6SeRIGzRfHTiPUI7gn1wiDQAR','GR9a1DJktJZSTlrGuNbZntNRbRlYwv5yTinkEKhdWxrik')
print "Mhn baleis account me pollous followers an den exeis polu xrono (^.^)/"
api = tweepy.API(auth)
a1=raw_input()
a2=raw_input()
f1=[]
f2=[]
c=0
f1=[]
f2=[]
for page in tweepy.Cursor(api.followers_ids, screen_name=a1).pages():
    f1.extend(page)
    if (len(f1)%100==0):
        time.sleep(60)
for page in tweepy.Cursor(api.followers_ids, screen_name=a2).pages():
    f2.extend(page)
    if (len(f1)%100==0):
        time.sleep(60)
print "elegxos gia koinous filous:"
for i in range (0,len(f1)):
    for j in range (0,len(f2)):
        if (f1[i]==f2[j]):
            f1[i]=api.get_user(f1[i]).screen_name
            print f1[i]
            c+=1
if c==0:
        print "den exete koinous filous"
