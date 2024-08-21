from flask import Flask, redirect, url_for, render_template, request
import requests
import uuid

app = Flask(__name__)
app.secret_key = uuid.uuid4().hex

#print(type(uuid.uuid4().hex))
#print(uuid.uuid4().hex)

Fb_APP_ID = "1548681436025259"
Fb_APP_SECRET = "3b84670594ccbc8bb7bdd340cf5404da"
FB_REDIRECT_URI = "http://firstly-magnetic-sparrow.ngrok-free.app/facebook/callback"

@app.route('/brand_image')
def home():
    return render_template('index.html')

@app.route('/brand_image/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/brand_image/terms_of_service')
def terms():
    return render_template('terms.html')

@app.route('/brand_image/data_del')
def data_del():
    return render_template('data_deletion.html')

@app.route('/facebook/login')
def facebook_login():
    return redirect(f"https://www.facebook.com/v20.0/dialog/oauth?client_id={Fb_APP_ID}&redirect_uri={FB_REDIRECT_URI}")

@app.route('/facebook/callback')
def facebook_callback():
    code = request.args.get('code')
    if code:
        response = requests.get(f"https://graph.facebook.com/v20.0/oauth/access_token?code={code}&client_id={Fb_APP_ID}&redirect_uri={FB_REDIRECT_URI}&client_secret={Fb_APP_SECRET}")
        data = response.json()
        
        if 'error' in data:
            return render_template('fail.html')
        else:
            user_response = requests.get(
                f"https://graph.facebook.com/v20.0/me?fields=id,name&access_token={data['access_token']}"
            )

            print(user_response.json())

            return render_template('success.html')


if __name__ == "__main__":
    app.run(debug = True)