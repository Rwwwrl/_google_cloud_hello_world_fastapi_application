const functions = require("@google-cloud/functions-framework");

const ENV_VARIABLE1 = process.env.ENV_VARIABLE1;
const ENV_VARIABLE2 = process.env.ENV_VARIABLE2;

// Register an HTTP function with the Functions Framework that will be executed
// when you make an HTTP request to the deployed function's endpoint.
functions.http("hello_world_js", (req, res) => {
  console.log(
    `ENV_VARIABLE1 = ${ENV_VARIABLE1}, ENV_VARIABLE2 = ${ENV_VARIABLE2}`
  );
  res.send("Hello World!");
});
