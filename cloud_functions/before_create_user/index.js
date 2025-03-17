import gcipCloudFunctions from "gcip-cloud-functions";

const authClient = new gcipCloudFunctions.Auth();

export async function beforeCreateHandler(user, context) {
  // TODO: move it to env
  const url = "https://fastapi-hello-world-test-eu.lm.r.appspot.com/api/users";

  let data = {
    uid: user.uid,
    tenant_id: user.tenantId ?? null,
    email: user.email,
  };

  let res = await fetch(url, {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (res.status !== 201) {
    response_json = await res.json();
    console.error(
      `error during fetch fastapi-backend, res.status = ${res.status}, res.response = ${response_json}`
    );
    throw new gcipCloudFunctions.https.HttpsError(
      "internal",
      "Failed to create user."
    );
  }
}

export const beforeCreate = authClient
  .functions()
  .beforeCreateHandler((user, context) => beforeCreateHandler(user, context));
