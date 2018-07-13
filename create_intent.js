var watson = require('watson-developer-cloud');

var assistant = new watson.AssistantV1({
  username: '{username}',
  password: '{password}',
  version: '2018-02-16'
});

var params = {
  workspace_id: '9978a49e-ea89-4493-b33d-82298d3db20d',
  intent: 'hello',
  examples: [
    {
      text: 'Good morning'
    },
    {
      text: 'Hi there'
    }
  ]
};

assistant.createIntent(params, function(err, response) {
  if (err) {
    console.error(err);
  } else {
    console.log(JSON.stringify(response, null, 2));
  }
});
