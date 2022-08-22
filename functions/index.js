/* eslint-disable max-len */
/* eslint-disable no-tabs */
/* eslint-disable no-mixed-spaces-and-tabs */
const functions = require("firebase-functions");
const request = require("request-promise");

const LINE_MESSAGING_API = "https://api.line.me/v2/bot/message";
const LINE_HEADER = {
  "Content-Type": "application/json",
  // eslint-disable-next-line max-len
  "Authorization": "Bearer ${reGGOrpOZ5RafgV+VqQHiULKInLdOq4gTKa3npfHWNzorpMn/V85a7axufVRJzmHvhxlGAuJ9wAqI6NMGIHjdL1yMqoFkR3JwoAHrTbNnqiI91pFvfp/AWgnOQCMk2vWEBvbGLgT4POpr+nZOye9ewdB04t89/1O/w1cDnyilFU=}",
};

exports.LineBot = functions.https.onRequest((req, _res) => {
  if (req.body.events[0].message.type !== "text") {
    return;
  }
  reply(req.body);
});

const reply = (bodyResponse) => {
  return request({
    method: "POST",
    uri: `${LINE_MESSAGING_API}/reply`,
    headers: LINE_HEADER,
    body: JSON.stringify({
      replyToken: bodyResponse.events[0].replyToken,
      messages: [
        {
          "type": "text",
          "text": "สวัสดีค้าบ เรา KinRaiDee(กินไรดี) จะมาช่วยเลือกร้านอาหารให้คุณ ",
        },
        {
          "type": "bubble",
          "hero": {
            "type": "image",
            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover",
            "action": {
              "type": "uri",
              "label": "Line",
              "uri": "https://linecorp.com/",
            },
          },
          "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "Brown Cafe",
                "weight": "bold",
                "size": "xl",
                "contents": [],
              },
              {
                "type": "box",
                "layout": "baseline",
                "margin": "md",
                "contents": [
                  {
                    "type": "icon",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                    "size": "sm",
                  },
                  {
                    "type": "icon",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                    "size": "sm",
                  },
                  {
                    "type": "icon",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                    "size": "sm",
                  },
                  {
                    "type": "icon",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                    "size": "sm",
                  },
                  {
                    "type": "icon",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png",
                    "size": "sm",
                  },
                  {
                    "type": "text",
                    "text": "4.0",
                    "size": "sm",
                    "color": "#999999",
                    "flex": 0,
                    "margin": "md",
                    "contents": [],
                  },
                ],
              },
              {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "margin": "lg",
                "contents": [
                  {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Place",
                        "size": "sm",
                        "color": "#AAAAAA",
                        "flex": 1,
                        "contents": [],
                      },
                      {
                        "type": "text",
                        "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
                        "size": "sm",
                        "color": "#666666",
                        "flex": 5,
                        "wrap": true,
                        "contents": [],
                      },
                    ],
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Time",
                        "size": "sm",
                        "color": "#AAAAAA",
                        "flex": 1,
                        "contents": [],
                      },
                      {
                        "type": "text",
                        "text": "10:00 - 23:00",
                        "size": "sm",
                        "color": "#666666",
                        "flex": 5,
                        "wrap": true,
                        "contents": [],
                      },
                    ],
                  },
                ],
              },
            ],
          },
          "footer": {
            "type": "box",
            "layout": "vertical",
            "flex": 0,
            "spacing": "sm",
            "contents": [
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "CALL",
                  "uri": "https://linecorp.com",
                },
                "height": "sm",
                "style": "link",
              },
              {
                "type": "button",
                "action": {
                  "type": "uri",
                  "label": "WEBSITE",
                  "uri": "https://linecorp.com",
                },
                "height": "sm",
                "style": "link",
              },
              {
                "type": "spacer",
                "size": "sm",
              },
            ],
          },
        },
	  ],
    }),
  });
};
