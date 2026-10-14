import { useMemo, useState } from "react";
import { Form, ButtonGroup, Button } from "react-bootstrap";
import useApi from "../hooks/useApi";
import { api } from "../lib/api";
import DrinkCard from "../components/DrinkCard";
import { Loading, ErrorMessage, Empty } from "../components/Status";

const KINDS = [
  ["", "All"],
  ["cocktail", "Cocktails"],
  ["shot", "Shots"],
];

export default function AllDrinks() {
  const { data: drinks, loading, error, retry } = useApi(() => api.drinks(), []);
  const [searchTerm, setSearchTerm] = useState("");
  const [kind, setKind] = useState("");

  const filtered = useMemo(() => {
    const term = searchTerm.trim().toLowerCase();
    return (drinks || []).filter(
      (d) =>
        (!kind || d.kind === kind) &&
        (!term ||
          d.name.toLowerCase().includes(term) ||
          d.ingredients.some((i) => i.name.toLowerCase().includes(term)))
    );
  }, [drinks, searchTerm, kind]);

  if (loading) return <Loading label="Lining up the glasses…" />;
  if (error) return <ErrorMessage error={error} onRetry={retry} />;

  return (
    <div>
      <header className="page-head">
        <h1>All drinks</h1>
        <p>Browse or search the full collection of {drinks.length} recipes.</p>
      </header>

      <div className="d-flex flex-column flex-md-row gap-3 mb-4">
        <Form.Control
          type="search"
          placeholder="Search by drink or ingredient…"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="search-input"
          aria-label="Search drinks"
        />
        <ButtonGroup aria-label="Filter by type">
          {KINDS.map(([value, label]) => (
            <Button
              key={value || "all"}
              variant={kind === value ? "primary" : "outline-primary"}
              onClick={() => setKind(value)}
            >
              {label}
            </Button>
          ))}
        </ButtonGroup>
      </div>

      {filtered.length ? (
        <div className="row g-4">
          {filtered.map((d) => (
            <div className="col-sm-6 col-lg-4" key={d.id}>
              <DrinkCard drink={d} />
            </div>
          ))}
        </div>
      ) : (
        <Empty emoji="🔍" title="No drinks found">
          Nothing matches “{searchTerm}”. Try a spirit like “gin” or “rum”.
        </Empty>
      )}
    </div>
  );
}
