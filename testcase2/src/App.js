// App.js
import React, { useState, useEffect } from "react";
import "./App.css";
// The variable you need is ingredients, which is an empty array

const App = () => {
  const [data, setData] = useState([{}]);
  const [ingredients, setIngredients] = useState([]);
  const [newIngredient, setNewIngredient] = useState("");

  const addIngredient = () => {
    if (newIngredient.trim() !== "") {
      setIngredients([...ingredients, newIngredient]);
      setNewIngredient("");
    }
  };

  const removeIngredient = (index) => {
    const updatedIngredients = [...ingredients];
    updatedIngredients.splice(index, 1);
    setIngredients(updatedIngredients);
  };

  useEffect(() => {
    fetch("/")
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        console.log(data);
      });
  }, []);

  return (
    <div className="app-container">
      {typeof data.members === "undefined" ? (
        <p> Loading... </p>
      ) : (
        data.members.map((member, i) => <p key={i}>{member} </p>)
      )}
      <h1>Food Search</h1>
      <div className="content-container">
        <div className="half-screen">
          <h2>Ingredients</h2>
          <div>
            <input
              type="text"
              value={newIngredient}
              onChange={(e) => setNewIngredient(e.target.value)}
            />
            <button onClick={addIngredient}>Add</button>
          </div>
          <ul>
            {ingredients.map((ingredient, index) => (
              <li key={index}>
                {ingredient}
                <button onClick={() => removeIngredient(index)}>Remove</button>
              </li>
            ))}
          </ul>
        </div>
        <div className="half-screen">
          <h2>Recipes</h2>
          {/* Add your recipe content here */}
        </div>
      </div>
    </div>
  );
};

export default App;
