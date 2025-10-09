import { useState } from 'react'
import Button from 'react-bootstrap/Button'

const IngredientSelector = () => {
    const [selected, setSelected] = useState([])

    let alcohols = [
        'Vodka',
        'Gin', 
        'Tequila', 
        'Whiskey',
        'Triple sec'
    ]

    let mixers = [
        'Orange Juice',
        'Cranberry Juice', 
        'Pineapple Juice', 
        'Tonic Water',
        'Club Soda',
        'Coke',
        'Lemonade',
        'Sprite',
        'Ginger Ale'
    ]

    const toggle = (item) => {
        setSelected((prev) => 
            prev.includes(item) ? prev.filter(i => i !== item) : [...prev, item]
        )
    }

    return (
        <>
            <div className="alcohol-div">
                <h2>What Alcohols Do You Have?</h2>
                {alcohols.map((i) => (
                    <Button 
                        key={i}
                        onClick={() => toggle(i)}
                        style={{
                            margin: '2px',
                            padding: '0.5rem 1rem',
                            background: selected.includes(i) ? '#ff9807ff' : '#4b4747ff',
                            border: '1px solid black',
                            borderRadius: '5px',
                            cursor: 'pointer'
                        }}
                    >
                        {i}
                    </Button>
                ))}
            </div>

            <div className="mixers-div">
                <h2>What Mixers Do You Have?</h2>
                {mixers.map((i) => (
                    <Button 
                        key={i}
                        onClick={() => toggle(i)}
                        style={{
                            margin: '2px',
                            padding: '0.5rem 1rem',
                            background: selected.includes(i) ? '#ff9807ff' : '#4b4747ff',
                            border: '1px solid black',
                            borderRadius: '5px',
                            cursor: 'pointer'
                        }}
                    >
                        {i}
                    </Button>
                ))}
            </div>
        </>
    )
}

export default IngredientSelector