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
          "type": "flex",
          "altText": "this is a flex message",
          "contents": {
            "type": "bubble",
            "hero": {
              "type": "image",
              "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
              "size": "full",
              "aspectRatio": "20:13",
              "aspectMode": "cover",
              "action": {
                "type": "uri",
                "uri": "http://linecorp.com/",
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
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "margin": "lg",
                  "spacing": "sm",
                  "contents": [
                    {
                      "type": "box",
                      "layout": "baseline",
                      "spacing": "sm",
                      "contents": [
                        {
                          "type": "text",
                          "text": "Place",
                          "color": "#aaaaaa",
                          "size": "sm",
                          "flex": 1,
                        },
                        {
                          "type": "text",
                          "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
                          "wrap": true,
                          "color": "#666666",
                          "size": "sm",
                          "flex": 5,
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
                          "color": "#aaaaaa",
                          "size": "sm",
                          "flex": 1,
                        },
                        {
                          "type": "text",
                          "text": "10:00 - 23:00",
                          "wrap": true,
                          "color": "#666666",
                          "size": "sm",
                          "flex": 5,
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
              "spacing": "sm",
              "contents": [
                {
                  "type": "button",
                  "style": "link",
                  "height": "sm",
                  "action": {
                    "type": "uri",
                    "label": "CALL",
                    "uri": "https://linecorp.com",
                  },
                },
                {
                  "type": "button",
                  "style": "link",
                  "height": "sm",
                  "action": {
                    "type": "uri",
                    "label": "WEBSITE",
                    "uri": "https://linecorp.com",
                  },
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": [],
                  "margin": "sm",
                },
              ],
              "flex": 0,
            },
          },
        },
	  ],
    }),
  });
};
