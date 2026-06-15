# Dialogflow Chatbot

[![Node.js](https://img.shields.io/badge/Node.js-339933?logo=nodedotjs&logoColor=white)](https://nodejs.org/)
[![Express](https://img.shields.io/badge/Express-000000?logo=express&logoColor=white)](https://expressjs.com/)
![Dialogflow](https://img.shields.io/badge/Dialogflow-FF9800?logo=googleassistant&logoColor=white)
![Google Cloud Functions](https://img.shields.io/badge/Google%20Cloud%20Functions-4285F4?logo=googlecloud&logoColor=white)

A conversational chatbot built with **Google Dialogflow** and a Node.js webhook,
created for a Cloud Computing course. Dialogflow handles the natural-language
understanding; this server provides the fulfillment logic behind it.

## How it works

```
user ──► Dialogflow agent ──► (matched intent) ──► webhook fulfillment (this server)
                                                          │
                                                          ▼
                                          response built from conversation params
```

- **`index.html`** embeds Dialogflow's chat widget so you can talk to the agent
  in the browser.
- **`server.js`** is an Express webhook. When the agent matches the `Details`
  intent, it calls `POST /dialogflow-fulfillment`; the server reads the
  conversation parameters (name, email) and responds with the user's and
  creator's details.
- The webhook was deployed to **Google Cloud Functions** for the course, and
  also runs as a plain Express server locally.

## Running it locally

```bash
npm install
npm start
# server starts on PORT (default 80)
```

To exercise the webhook end to end you need a Dialogflow agent configured to call
this server's `/dialogflow-fulfillment` endpoint as its fulfillment webhook (for
example, via an ngrok tunnel or the Cloud Functions deployment).

## Notes

- The focus of this project was the cloud side — wiring a managed NLP service
  (Dialogflow) to a serverless webhook — rather than the chatbot's conversation
  design.
- Service-account credentials are intentionally not committed (see
  `.gitignore`).
