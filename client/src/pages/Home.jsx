import IngredientSelector from "../components/IngredientSelector"

export default function Home () {
    return (
        <>
            <h1>Welcome to <span className="app-name">Nook & Pour</span></h1>
            <IngredientSelector></IngredientSelector>
        </>
    )
}