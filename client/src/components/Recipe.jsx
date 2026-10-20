import TasteProfile from "./TasteProfile";

// Ingredient list + steps, shared by the recipe modal and the full recipe page.
export default function Recipe({ drink, have = [] }) {
  const owned = new Set(have.map((h) => h.toLowerCase()));
  const hasBar = have.length > 0;

  return (
    <div className="recipe">
      <TasteProfile drink={drink} />
      {drink.glass && (
        <p className="recipe-meta">
          <span>Glass</span> {drink.glass}
        </p>
      )}

      <h4 className="recipe-heading">Ingredients</h4>
      <ul className="recipe-ings">
        {drink.ingredients.map((ing) => {
          const inBar = owned.has(ing.name.toLowerCase());
          return (
            <li key={ing.name} className={hasBar && !inBar && !ing.optional ? "is-missing" : ""}>
              <span className="recipe-amount">{ing.amount}</span>
              <span className="recipe-name">
                {ing.name}
                {ing.optional && <em className="recipe-optional"> optional</em>}
              </span>
              {hasBar && (
                <span className="recipe-check" aria-label={inBar ? "In your bar" : "Not in your bar"}>
                  {inBar ? "✓" : ing.optional ? "" : "need"}
                </span>
              )}
            </li>
          );
        })}
      </ul>

      <h4 className="recipe-heading">Method</h4>
      <ol className="recipe-steps">
        {drink.instructions.map((step, i) => (
          <li key={i}>{step}</li>
        ))}
      </ol>
    </div>
  );
}
