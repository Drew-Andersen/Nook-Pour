import { Link } from "react-router-dom";
import { Button } from "react-bootstrap";
import useApi from "../hooks/useApi";
import useBar from "../hooks/useBar";
import { api } from "../lib/api";
import DrinkCard from "../components/DrinkCard";
import { Loading, ErrorMessage, Empty } from "../components/Status";

export default function Drinks() {
  const { selectedIngredients, toggleIngredient } = useBar();
  const hasBar = selectedIngredients.length > 0;
  const { data, loading, error, retry } = useApi(
    () => (hasBar ? api.match(selectedIngredients) : Promise.resolve(null)),
    [selectedIngredients.join("|")]
  );

  if (!hasBar) {
    return (
      <Empty emoji="🧺" title="Your bar is empty">
        <p>Tell us what you have and we'll find drinks you can make.</p>
        <Button as={Link} to="/ingredients">Stock my bar</Button>
      </Empty>
    );
  }
  if (loading && !data) return <Loading label="Mixing up matches…" />;
  if (error) return <ErrorMessage error={error} onRetry={retry} />;

  const { can_make: canMake, almost, unlocks } = data;

  return (
    <div>
      <header className="page-head">
        <h1>What can I make?</h1>
        <p>
          Using {selectedIngredients.length} ingredient{selectedIngredients.length === 1 ? "" : "s"}{" "}
          from your bar · <Link to="/ingredients">Edit my bar</Link>
        </p>
      </header>

      <section className="mb-5">
        <div className="section-head">
          <h2>Ready to pour <span className="count">{canMake.length}</span></h2>
        </div>
        {canMake.length ? (
          <div className="row g-4">
            {canMake.map((d) => (
              <div className="col-sm-6 col-lg-4" key={d.id}>
                <DrinkCard drink={d} />
              </div>
            ))}
          </div>
        ) : (
          <p className="text-muted">
            Nothing complete yet — check the drinks below that are just a bottle or two away.
          </p>
        )}
      </section>

      {unlocks.length > 0 && (
        <section className="unlocks mb-5">
          <h2>Best next buy</h2>
          <p className="text-muted">Add one of these to unlock more drinks:</p>
          <div className="d-flex flex-wrap gap-2">
            {unlocks.map((u) => (
              <button
                key={u.ingredient}
                type="button"
                className="unlock-chip"
                onClick={() => toggleIngredient(u.ingredient)}
                title={`Unlocks ${u.drinks.join(", ")}`}
              >
                + {u.ingredient}
                <span>
                  unlocks {u.count} drink{u.count === 1 ? "" : "s"}
                </span>
              </button>
            ))}
          </div>
          <p className="small text-muted mt-2 mb-0">Tap one to add it to your bar.</p>
        </section>
      )}

      {almost.length > 0 && (
        <section>
          <div className="section-head">
            <h2>Almost there <span className="count">{almost.length}</span></h2>
          </div>
          <div className="row g-4">
            {almost.map((d) => (
              <div className="col-sm-6 col-lg-4" key={d.id}>
                <DrinkCard drink={d} missing={d.missing} />
              </div>
            ))}
          </div>
        </section>
      )}
    </div>
  );
}
