import gcipCloudFunctions from "gcip-cloud-functions";

const authClient = new gcipCloudFunctions.Auth();

const CREATE_USERS_API_ENDPOINT = process.env.CREATE_USERS_API_ENDPOINT;

export async function beforeCreateHandler(user, context) {
  let body = {
    uid: user.uid,
    email: user.email,
  };

  let res = await fetch(CREATE_USERS_API_ENDPOINT, {
    method: "POST",
    body: JSON.stringify(body),
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (res.status !== 201) {
    console.error(`error during fetch fastapi-backend, res.status = ${res.status}`);
    throw new gcipCloudFunctions.https.HttpsError(
      "internal",
      "Failed to create user."
    );
  }
}

export const beforeCreate = authClient
  .functions()
  .beforeCreateHandler((user, context) => beforeCreateHandler(user, context));
