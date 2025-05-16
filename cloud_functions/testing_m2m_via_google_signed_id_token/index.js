const functions = require("@google-cloud/functions-framework");
const { GoogleAuth } = require("google-auth-library");

const AUDIENCE = process.env.AUDIENCE;
const BACKEND_API_HOST = process.env.BACKEND_API_HOST;

const auth = new GoogleAuth({
    keyFile: "key.json",
});

functions.http("testingM2MViaGoogleSignedIdToken", async (req, res) => {
    const client = await auth.getClient();

    const googleSignedIdToken = await client.fetchIdToken(AUDIENCE);

    const url =
        BACKEND_API_HOST +
        "/api/hello-world/test_protected_with_google_JWT_token_endpoint/";

    try {
        await fetch(url, {
            method: "POST",
            headers: {
                Authorization: `Bearer ${googleSignedIdToken}`,
            },
        });
        res.sendStatus(200);
    } catch (error) {
        console.error("Request failed:", error);
        res.sendStatus(500);
    }
});
