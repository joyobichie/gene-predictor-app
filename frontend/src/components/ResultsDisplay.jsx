import React from 'react';

function ResultsDisplay({ isLoading, error, results }) {
  if (isLoading) {
    return <div className="results-container"><p>Calculating...</p></div>;
  }
  if (error) {
    return (
      <div className="results-container error">
        <p><strong>Error:</strong> {error}</p>
      </div>
    );
  }
  if (!results) {
    return null;
  }
  return (
    <div className="results-container">
      <h2>Prediction Results</h2>
      {Object.entries(results).map(([trait, probabilities]) => (
        <div key={trait} className="result-item">
          <h3>{trait.replace(/_/g, ' ')}</h3>
          <ul>
            {Object.entries(probabilities).map(([phenotype, percentage]) => (
              <li key={phenotype}>
                {phenotype}: <strong>{percentage}%</strong>
              </li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
}

export default ResultsDisplay;