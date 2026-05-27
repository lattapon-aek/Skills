export type LoginResult =
  | { ok: true; sessionToken: string }
  | { ok: false; reason: "INVALID_CREDENTIALS" | "LOCKED" };

type UserRecord = {
  id: string;
  password: string;
  failedAttempts: number;
  locked: boolean;
};

export function login(user: UserRecord, password: string): LoginResult {
  if (user.locked) {
    return { ok: false, reason: "LOCKED" };
  }

  if (user.password !== password) {
    return { ok: false, reason: "INVALID_CREDENTIALS" };
  }

  if (user.failedAttempts >= 5) {
    return { ok: false, reason: "INVALID_CREDENTIALS" };
  }

  return {
    ok: true,
    sessionToken: `session:${user.id}`,
  };
}
