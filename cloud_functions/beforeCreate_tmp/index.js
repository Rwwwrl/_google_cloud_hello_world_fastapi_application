import gcipCloudFunctions from "gcip-cloud-functions";

const authClient = new gcipCloudFunctions.Auth();

export async function beforeCreateHandler(user, context) {
    console.log("beforeCreate was triggered");
}

export const beforeCreate = authClient
    .functions()
    .beforeCreateHandler((user, context) => beforeCreateHandler(user, context));
