const functions = require("@google-cloud/functions-framework");
const { JWT } = require("google-auth-library");

const keys = require("./keys.json");
// m2m-cloud-function-to-backend service account keys

const AUDIENCE = process.env.AUDIENCE;

functions.http("testingM2MViaGoogleSignedIdToken", async (req, res) => {
    console.log(AUDIENCE);

    const client = new JWT({
        email: keys.client_email,
        key: keys.private_key,
    });

    const googleSignedIdToken = await client.fetchIdToken(AUDIENCE);

    console.log(googleSignedIdToken);

    res.sendStatus(200);
});
