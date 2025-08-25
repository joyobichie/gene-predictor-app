import React from 'react';

// Add the 'value' prop to make this a controlled component
function TraitSelector({ label, options, onChange, value }) {
  return (
    <div className="trait-selector">
      <label>{label}:</label>
      <select 
        onChange={(e) => onChange(e.target.value)} 
        value={value || ""} // Use the value prop here. `|| ""` prevents a React warning.
      >
        <option value="" disabled>Select phenotype</option>
        {options.map(option => (
          <option key={option} value={option}>{option}</option>
        ))}
      </select>
    </div>
  );
}

export default TraitSelector;