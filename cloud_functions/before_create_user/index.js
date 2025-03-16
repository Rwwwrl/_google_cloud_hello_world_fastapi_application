import gcipCloudFunctions from "gcip-cloud-functions";

const authClient = new gcipCloudFunctions.Auth();

export async function beforeCreateHandler(user, context) {
  // TODO: move it to env
  url = "https://fastapi-hello-world-test-eu.lm.r.appspot.com/users/create_user";

  data = {
    uid: user.uid,
    tenant_id: user.tenantId,
    email: user.email,
  };

  const res = await fetch(url, {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (res.status !== 201) {
    console.error("error during fetch fastapi-backend", res.status, JSON.stringify(res));
    throw new gcipCloudFunctions.https.HttpsError(
      "internal",
      "Failed to create user."
    );
  }
}

export const beforeCreate = authClient
  .functions()
  .beforeCreateHandler((user, context) => beforeCreateHandler(user, context));
