import os
from slack_bolt import App

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

@app.message("\[タスク依頼\]")
def message_hello(message, say):
    say("successfully sent")
    print(f"Hey there <@{message['text']}>!")

if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))