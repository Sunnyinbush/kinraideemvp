/* eslint-disable no-tabs */
/* eslint-disable no-mixed-spaces-and-tabs */
const functions = require("firebase-functions");
const request = require("request-promise");

const LINE_MESSAGING_API = "https://api.line.me/v2/bot/message";
const LINE_HEADER = {
  "Content-Type": "application/json",
  // eslint-disable-next-line max-len
  "Authorization": "Bearer reGGOrpOZ5RafgV+VqQHiULKInLdOq4gTKa3npfHWNzorpMn/V85a7axufVRJzmHvhxlGAuJ9wAqI6NMGIHjdL1yMqoFkR3JwoAHrTbNnqiI91pFvfp/AWgnOQCMk2vWEBvbGLgT4POpr+nZOye9ewdB04t89/1O/w1cDnyilFU=",
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
          type: "text",
          text: bodyResponse.events[0].message.text,
        },
	  ],
    }),
  });
};
