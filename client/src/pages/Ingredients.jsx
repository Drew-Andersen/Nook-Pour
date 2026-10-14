import { useMemo, useState } from "react";
import { useNavigate } from "react-router-dom";
import { Button, Form } from "react-bootstrap";
import useApi from "../hooks/useApi";
import useBar from "../hooks/useBar";
import { api } from "../lib/api";
import { Loading, ErrorMessage } from "../components/Status";

const CATEGORY_ICONS = { spirit: "🥃", liqueur: "🍷", mixer: "🍋", garnish: "🌿" };

export default function Ingredients() {
  const { selectedIngredients, setSelectedIngredients, toggleIngredient } = useBar();
  const { data, loading, error, retry } = useApi(() => api.ingredients(), []);
  const [filter, setFilter] = useState("");
  const navigate = useNavigate();

  const groups = useMemo(() => {
    if (!data) return [];
    const term = filter.trim().toLowerCase();
    return data.categories
      .map((cat) => ({
        ...cat,
        items: data.ingredients.filter(
          (i) => i.category === cat.key && i.name.toLowerCase().includes(term)
        ),
      }))
      .filter((g) => g.items.length > 0);
  }, [data, filter]);

  if (loading) return <Loading label="Opening the cabinet…" />;
  if (error) return <ErrorMessage error={error} onRetry={retry} />;

  const count = selectedIngredients.length;

  return (
    <div className="pb-5">
      <header className="page-head">
        <h1>My Bar</h1>
        <p>Tap everything you have on hand. We'll remember it for next time.</p>
      </header>

      <Form.Control
        type="search"
        placeholder="Filter ingredients…"
        value={filter}
        onChange={(e) => setFilter(e.target.value)}
        className="search-input mb-4"
        aria-label="Filter ingredients"
      />

      {groups.length === 0 && <p className="text-muted">No ingredients match “{filter}”.</p>}

      {groups.map((group) => (
        <section key={group.key} className="ing-group">
          <h2 className="ing-group-title">
            <span aria-hidden="true">{CATEGORY_ICONS[group.key]}</span> {group.label}
          </h2>
          <div className="chip-grid">
            {group.items.map((ing) => {
              const active = selectedIngredients.includes(ing.name);
              return (
                <button
                  key={ing.id}
                  type="button"
                  className={`chip ${active ? "is-active" : ""}`}
                  aria-pressed={active}
                  onClick={() => toggleIngredient(ing.name)}
                >
                  {active && <span className="chip-check">✓</span>}
                  {ing.name}
                </button>
              );
            })}
          </div>
        </section>
      ))}

      <div className="action-bar">
        <div className="container d-flex align-items-center justify-content-between gap-3">
          <span>
            <strong>{count}</strong> ingredient{count === 1 ? "" : "s"} selected
          </span>
          <div className="d-flex gap-2">
            {count > 0 && (
              <Button variant="outline-secondary" onClick={() => setSelectedIngredients([])}>
                Clear
              </Button>
            )}
            <Button disabled={count === 0} onClick={() => navigate("/drinks")}>
              Find drinks →
            </Button>
          </div>
        </div>
      </div>
    </div>
  );
}
