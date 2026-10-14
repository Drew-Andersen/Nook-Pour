import { Badge } from "react-bootstrap";
import DrinkImage from "./DrinkImage";
import FavoriteButton from "./FavoriteButton";
import useBar from "../hooks/useBar";

export default function DrinkCard({ drink, missing }) {
  const { handleShowModal, isFavorite, toggleFavorite } = useBar();
  const required = drink.ingredients.filter((i) => !i.optional).map((i) => i.name);

  return (
    <article
      className="drink-card h-100"
      role="button"
      tabIndex={0}
      onClick={() => handleShowModal(drink)}
      onKeyDown={(e) => (e.key === "Enter" || e.key === " ") && handleShowModal(drink)}
    >
      <FavoriteButton
        className="drink-card-fav"
        active={isFavorite(drink.id)}
        onClick={() => toggleFavorite(drink.id)}
      />
      <DrinkImage drink={drink} />
      <div className="drink-card-body">
        <div className="d-flex align-items-center gap-2 mb-1">
          <h3 className="drink-card-title">{drink.name}</h3>
          {drink.kind === "shot" && <Badge bg="dark">Shot</Badge>}
        </div>
        <p className="drink-card-desc">{drink.description}</p>
        <p className="drink-card-ings">{required.join(" · ")}</p>
        {missing?.length > 0 && (
          <div className="missing-row">
            <span>Need:</span>
            {missing.map((m) => (
              <span key={m} className="missing-badge">{m}</span>
            ))}
          </div>
        )}
      </div>
    </article>
  );
}
