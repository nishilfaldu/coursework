// Webhook fulfillment server for a Dialogflow chatbot.
//
// Dialogflow handles the natural-language understanding; when the "Details"
// intent is matched it calls this webhook, which echoes back the user's details
// (captured from the conversation parameters) along with the creator's details.
//
// Deployed to Google Cloud Functions for the Cloud Computing course; it also
// runs as a standalone Express server via `node server.js`.

const express = require("express");
const cors = require("cors");
const path = require("path");
const { WebhookClient } = require("dialogflow-fulfillment");

require("dotenv").config();

const app = express();
app.use(cors());
app.use(express.json());

const port = process.env.PORT || 80;

// Conversation details captured from the most recent Dialogflow request.
let email = "";
let last_name = "";
let given_name = "";

// Dialogflow fulfillment endpoint: invoked by the agent on a matched intent.
app.post("/dialogflow-fulfillment", (request, response) => {
  const params = request.body.queryResult.parameters;
  if (params.email) {
    email = params.email;
    last_name = params["last-name"];
    given_name = params["given-name"];
  }
  handleDetails(request, response);
});

// Serve the embedded Dialogflow chat widget.
app.get("/", function (req, res) {
  res.sendFile(path.join(__dirname, "/index.html"));
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

// Maps the "Details" intent to a response summarizing user + creator details.
const handleDetails = (request, response) => {
  const agent = new WebhookClient({ request, response });

  function giveDetails(agent) {
    agent.add(
      `User First Name: ${given_name}, \n User Last Name: ${last_name}, \n User Email: ${email}, \n  Creator First Name: Nishil, \n Creator Last Name: Faldu,  \n Creator Email: faldund@mail.uc.edu`
    );
  }

  const intentMap = new Map();
  intentMap.set("Details", giveDetails);
  agent.handleRequest(intentMap);
};
