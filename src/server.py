from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

base_youtube_url = "https://www.youtube.com/embed/"
base_youtube_thumbnail = "https://img.youtube.com/vi/"
base_youtube_thumbnail_ending = "/default.jpg"
url = "mjnAE5go9dI"
urlStorage = "000"
url2 = "V5s-KLGVcTI"
url3 = "LGddm-hw-Xc"
url4 = "9UBWgeSJlWw"
url5 = "8KtiFY63jZM"

@app.route('/')
def home():
    return render_template("YouTube.html", video1=base_youtube_url+url, image1=base_youtube_thumbnail+url2+base_youtube_thumbnail_ending, image2=base_youtube_thumbnail+url3+base_youtube_thumbnail_ending, image3=base_youtube_thumbnail+url4+base_youtube_thumbnail_ending, image4=base_youtube_thumbnail+url5+base_youtube_thumbnail_ending )

@app.route("/forward/<videoNumber>", methods=['POST'])
def change_video(videoNumber, url=url, url2 = url2, url3 = url3, url4= url4, url5=url5, urlStorage=urlStorage):
    getVideoNumber(videoNumber)
    if (videoNumber=="1"):
        urlStorage = url
        url = url2
        url2 = urlStorage
    if (videoNumber == "2"):
        urlStorage = url
        url = url3
        url3 = urlStorage
    if (videoNumber == "3"):
        urlStorage = url
        url = url4
        url4 = urlStorage
    if (videoNumber == "4"):
        urlStorage = url
        url = url5
        url5 = urlStorage
    return render_template("YouTube.html", video1=base_youtube_url+url, image1=base_youtube_thumbnail+url2+base_youtube_thumbnail_ending, image2=base_youtube_thumbnail+url3+base_youtube_thumbnail_ending, image3=base_youtube_thumbnail+url4+base_youtube_thumbnail_ending, image4=base_youtube_thumbnail+url5+base_youtube_thumbnail_ending )

def getVideoNumber(videoNumber):
    print(videoNumber)
    return videoNumber

def setUrls(videoNumber):
    if (videoNumber == 1):
        return url

if __name__ == "__main__":
    app.run()