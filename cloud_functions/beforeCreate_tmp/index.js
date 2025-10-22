import gcipCloudFunctions from "gcip-cloud-functions";
import { v4 } from "uuid";

const authClient = new gcipCloudFunctions.Auth();

export async function _beforeCreateHandler(user, context) {
    const userUuid = v4();

    let updatedUserAttributes = {
        customClaims: {
            uuid: userUuid,
        },
    };

    return updatedUserAttributes;
}

export async function beforeCreateHandler(user, context) {
    try {
        return await _beforeCreateHandler(user, context);
    } catch (err) {
        console.error(`unexpected error, error = ${err}`);
        throw err;
    }
}

export const beforeCreate = authClient
    .functions()
    .beforeCreateHandler((user, context) => beforeCreateHandler(user, context));
