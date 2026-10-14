import { useState } from "react";

// Shows the drink illustration, or a friendly emoji badge when there isn't one.
export default function DrinkImage({ drink, size = "md" }) {
  const [failed, setFailed] = useState(false);
  const showImage = drink.image && !failed;
  return (
    <div className={`drink-image drink-image-${size}`}>
      {showImage ? (
        <img src={drink.image} alt={drink.name} loading="lazy" onError={() => setFailed(true)} />
      ) : (
        <span className="drink-emoji" role="img" aria-label={drink.name}>
          {drink.icon || "🍸"}
        </span>
      )}
    </div>
  );
}
