import { Link } from "react-router-dom";
import { Button } from "react-bootstrap";
import useApi from "../hooks/useApi";
import useBar from "../hooks/useBar";
import { api } from "../lib/api";
import DrinkCard from "../components/DrinkCard";
import { Loading, ErrorMessage, Empty } from "../components/Status";

export default function Favorites() {
  const { favorites } = useBar();
  const { data: drinks, loading, error, retry } = useApi(() => api.drinks(), []);

  if (loading) return <Loading />;
  if (error) return <ErrorMessage error={error} onRetry={retry} />;

  const saved = drinks.filter((d) => favorites.includes(d.id));

  return (
    <div>
      <header className="page-head">
        <h1>Favorites</h1>
        <p>Drinks you've saved with the ♡ button.</p>
      </header>
      {saved.length ? (
        <div className="row g-4">
          {saved.map((d) => (
            <div className="col-sm-6 col-lg-4" key={d.id}>
              <DrinkCard drink={d} />
            </div>
          ))}
        </div>
      ) : (
        <Empty emoji="♡" title="No favorites yet">
          <p>Tap the heart on any drink to keep it here.</p>
          <Button as={Link} to="/alldrinks">Browse drinks</Button>
        </Empty>
      )}
    </div>
  );
}
