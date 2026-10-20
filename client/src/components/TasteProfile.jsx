// Flavor, strength and vibe tags for a drink (see FLAVORS / STRENGTHS / VIBES in seed_data.py).
const STRENGTH_LABELS = { light: "Light & easy", balanced: "Balanced", strong: "Spirit forward" };
const VIBE_LABELS = { refreshing: "Refreshing", rich: "Rich & smooth", adventurous: "Adventurous" };
const cap = (s) => s.charAt(0).toUpperCase() + s.slice(1);

export default function TasteProfile({ drink }) {
  const flavors = drink.flavors || [];
  const vibes = drink.vibes || [];
  if (!flavors.length && !drink.strength && !vibes.length) return null;

  return (
    <div className="taste-profile" aria-label="Taste profile">
      {flavors.map((f) => (
        <span key={f} className={`taste-chip flavor-${f}`}>{cap(f)}</span>
      ))}
      {drink.strength && (
        <span className="taste-chip taste-strength">
          <span className={`strength-meter strength-${drink.strength}`} aria-hidden="true">
            <i /><i /><i />
          </span>
          {STRENGTH_LABELS[drink.strength] || cap(drink.strength)}
        </span>
      )}
      {vibes.map((v) => (
        <span key={v} className="taste-chip taste-vibe">{VIBE_LABELS[v] || cap(v)}</span>
      ))}
    </div>
  );
}
