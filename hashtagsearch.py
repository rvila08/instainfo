from info import getCreds, makeApiCall
from flask import Flask, render_template, request, redirect
import sys
import os

def getHashtagInfo( params ) :
	endpointParams = dict()
	endpointParams['user_id'] = params['instagram_account_id']
	endpointParams['q'] = params['hashtag_name']
	endpointParams['fields'] = 'id,name'
	endpointParams['access_token'] = params['access_token']

	url = params['endpoint_base'] + 'ig_hashtag_search'

	return makeApiCall( url, endpointParams, params['debug'] )

def getHashtagMedia( params ) :
	endpointParams = dict()
	endpointParams['user_id'] = params['instagram_account_id']
	endpointParams['fields'] = 'id,children,caption,comment_count,like_count,media_type,media_url,permalink'
	endpointParams['access_token'] = params['access_token']

	url = params['endpoint_base'] + params['hashtag_id'] + '/' + params['type']

	return makeApiCall( url, endpointParams, params['debug'] )

# Flask implementation
app = Flask(__name__)

@app.route('/')
def instainfo():
    return render_template('instainfo.html')

# Returns Desired Link Based on HTML Input
@app.route('/foo', methods=['GET', 'POST'])
def foo():
    hashtag = request.form['text']

    params = getCreds()
    params['hashtag_name'] = hashtag
    hashtagInfoResponse = getHashtagInfo( params )
    params['hashtag_id'] = hashtagInfoResponse['json_data']['data'][0]['id'];

    params['type'] = 'top_media'
    hashtagTopMediaResponse = getHashtagMedia( params )
    for post in hashtagTopMediaResponse['json_data']['data'] :
        link = post['permalink']
        break;
    return redirect(link, code=302)

# Redirects to Link Returned by Foo()
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
