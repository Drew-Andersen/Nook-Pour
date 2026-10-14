import { Link, useParams } from "react-router-dom";
import { Badge } from "react-bootstrap";
import useApi from "../hooks/useApi";
import useBar from "../hooks/useBar";
import { api } from "../lib/api";
import DrinkImage from "../components/DrinkImage";
import FavoriteButton from "../components/FavoriteButton";
import Recipe from "../components/Recipe";
import { Loading, ErrorMessage } from "../components/Status";
import NotFound from "./NotFound";

export default function DrinkDetail() {
  const { slug } = useParams();
  const { selectedIngredients, isFavorite, toggleFavorite } = useBar();
  const { data: drink, loading, error, retry } = useApi(() => api.drink(slug), [slug]);

  if (loading) return <Loading />;
  if (error?.message === "Drink not found") return <NotFound what="drink" />;
  if (error) return <ErrorMessage error={error} onRetry={retry} />;

  return (
    <article className="detail">
      <Link to="/alldrinks" className="back-link">← All drinks</Link>
      <div className="row g-4 g-lg-5 mt-1">
        <div className="col-md-5">
          <DrinkImage drink={drink} size="xl" />
        </div>
        <div className="col-md-7">
          <div className="d-flex align-items-center gap-2 flex-wrap">
            <h1 className="detail-title">{drink.name}</h1>
            <FavoriteButton active={isFavorite(drink.id)} onClick={() => toggleFavorite(drink.id)} />
            {drink.kind === "shot" && <Badge bg="dark">Shot</Badge>}
          </div>
          <p className="detail-desc">{drink.description}</p>
          <Recipe drink={drink} have={selectedIngredients} />
        </div>
      </div>
    </article>
  );
}
