import React from 'react';
import TraitSelector from './TraitSelector';

function TraitCard({ traitKey, traitOptions, parent1Value, parent2Value, onTraitChange }) {
  return (
    <div className="trait-card-container">
      {/* The main title is the trait itself */}
      <h2 className="trait-title">{traitKey.replace(/_/g, ' ')}</h2>
      
      {/* A wrapper for the side-by-side selectors */}
      <div className="selectors-wrapper">
        <div className="parent-selector-group">
          <h3>Parent 1</h3>
          <TraitSelector
            // We pass an empty label as the h3 is our main label
            label=""
            options={traitOptions}
            value={parent1Value}
            onChange={(value) => onTraitChange(1, traitKey, value)}
          />
        </div>

        <div className="parent-selector-group">
          <h3>Parent 2</h3>
          <TraitSelector
            label=""
            options={traitOptions}
            value={parent2Value}
            onChange={(value) => onTraitChange(2, traitKey, value)}
          />
        </div>
      </div>
    </div>
  );
}

export default TraitCard;