// Small fetch wrapper: throws a readable Error when the API is down or returns an error.
async function request(path, options = {}) {
  let res;
  try {
    res = await fetch(`/api${path}`, {
      headers: { "Content-Type": "application/json" },
      ...options,
    });
  } catch {
    throw new Error("Can't reach the Nook & Pour server. Is it running?");
  }
  const data = await res.json().catch(() => null);
  if (!res.ok) {
    throw new Error(data?.error || `Request failed (${res.status})`);
  }
  return data;
}

export const api = {
  ingredients: () => request("/ingredients"),
  drinks: (params = {}) => {
    const qs = new URLSearchParams(
      Object.entries(params).filter(([, v]) => v)
    ).toString();
    return request(`/drinks${qs ? `?${qs}` : ""}`);
  },
  drink: (slug) => request(`/drinks/${encodeURIComponent(slug)}`),
  match: (ingredients) =>
    request("/match", { method: "POST", body: JSON.stringify({ ingredients }) }),
};
