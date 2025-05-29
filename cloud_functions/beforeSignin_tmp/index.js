import gcipCloudFunctions from "gcip-cloud-functions";

const authClient = new gcipCloudFunctions.Auth();

export async function beforeSignInHandler(user, context) {
    console.log("beforeSignIn was triggered:");
}

// Export as Cloud Function
export const beforeSignIn = authClient
    .functions()
    .beforeSignInHandler((user, context) => beforeSignInHandler(user, context));
