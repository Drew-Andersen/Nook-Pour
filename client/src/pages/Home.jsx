import { Link } from "react-router-dom";
import { Button } from "react-bootstrap";
import useApi from "../hooks/useApi";
import useBar from "../hooks/useBar";
import { api } from "../lib/api";
import DrinkCard from "../components/DrinkCard";

const FEATURED = ["old-fashioned", "espresso-martini", "pumpkin-spice-white-russian"];

export default function Home() {
  const { selectedIngredients } = useBar();
  const { data: drinks } = useApi(() => api.drinks(), []);
  const featured = (drinks || []).filter((d) => FEATURED.includes(d.id));

  return (
    <>
      <section className="hero">
        <div className="hero-text">
          <p className="eyebrow">Your home bar, sorted</p>
          <h1 className="hero-title">
            What's in the cabinet?
            <br />
            <span>Let's pour something.</span>
          </h1>
          <p className="hero-lead">
            Tick off the bottles and mixers you have, and Nook &amp; Pour shows the cocktails and
            shots you can make right now — plus the ones you're one bottle away from.
          </p>
          <div className="d-flex flex-wrap gap-2">
            <Button as={Link} to={selectedIngredients.length ? "/drinks" : "/ingredients"} size="lg">
              {selectedIngredients.length ? "See what I can make" : "Stock my bar"}
            </Button>
            <Button as={Link} to="/alldrinks" size="lg" variant="outline-primary">
              Browse all drinks
            </Button>
          </div>
        </div>
        <img className="hero-logo" src="/images/logo.png" alt="A bottle pouring into a glass" />
      </section>

      <section className="steps">
        {[
          ["1", "Stock your bar", "Pick the spirits, mixers and garnishes you have on hand."],
          ["2", "Find your drink", "See every recipe you can make, and what you're close to."],
          ["3", "Pour & enjoy", "Follow the recipe and save your favorites for next time."],
        ].map(([n, title, text]) => (
          <div key={n} className="step">
            <span className="step-num">{n}</span>
            <h3>{title}</h3>
            <p>{text}</p>
          </div>
        ))}
      </section>

      {featured.length > 0 && (
        <section>
          <div className="section-head">
            <h2>House favorites</h2>
            <Link to="/alldrinks">See all →</Link>
          </div>
          <div className="row g-4">
            {featured.map((d) => (
              <div className="col-sm-6 col-lg-4" key={d.id}>
                <DrinkCard drink={d} />
              </div>
            ))}
          </div>
        </section>
      )}
    </>
  );
}
