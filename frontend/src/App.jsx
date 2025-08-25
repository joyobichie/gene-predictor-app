import React, { useState } from 'react';
import TraitCard from './components/TraitCard.jsx';
import ResultsDisplay from './components/ResultsDisplay.jsx';
import './App.css';

const TRAIT_OPTIONS = {
  // ... (Your trait options are perfect, no changes needed)
  dimples: ['Dimples', 'No Dimples'],
  earlobes: ['Free Earlobes', 'Attached Earlobes'],
  nose_shape: ['Roman Nose', 'Straight Nose'],
  height: ['Tall', 'Short'],
  face_shape: ['Oval Face', 'Square Face'],
  pigmentation: ['Normal Pigmentation', 'Albinism'],
  hairline: ["Widow's Peak", 'Straight Hairline'],
  tooth_gap: ['Gap in Teeth', 'No Gap in Teeth'],
  head_shape: ['Round Head', 'Long Head'],
  freckles: ['Has Freckles', 'No Freckles'],
  cleft_chin: ['Cleft Chin', 'Smooth Chin'],
  eyebrow_shape: ['Connected Eyebrows', 'Separated Eyebrows'],
  eyelash_length: ['Long Eyelashes', 'Short Eyelashes'],
  hair_texture: ['Curly Hair', 'Straight Hair'],
  hair_color: ['Dark Hair', 'Light Hair'],
  finger_mid_digital_hair: ['Has Mid-Digital Hair', 'No Mid-Digital Hair'],
  hitchhikers_thumb: ['Straight Thumb', "Hitchhiker's Thumb"],
  tongue_rolling: ['Can Roll Tongue', 'Cannot Roll Tongue'],
  handedness: ['Right-Handed', 'Left-Handed'],
  earwax_type: ['Wet Earwax', 'Dry Earwax'],
};

const ALL_TRAIT_KEYS = Object.keys(TRAIT_OPTIONS);
const TOTAL_TRAITS = ALL_TRAIT_KEYS.length;

function App() {
  const [currentTraitIndex, setCurrentTraitIndex] = useState(0);
  const [parent1Traits, setParent1Traits] = useState({});
  const [parent2Traits, setParent2Traits] = useState({});
  const [results, setResults] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleTraitChange = (parent, trait, value) => {
    const setter = parent === 1 ? setParent1Traits : setParent2Traits;
    setter(prev => ({ ...prev, [trait]: value }));
  };

  const handleNextTrait = () => {
    if (currentTraitIndex < TOTAL_TRAITS - 1) {
      setCurrentTraitIndex(prev => prev + 1);
    }
  };

  const handlePreviousTrait = () => {
    if (currentTraitIndex > 0) {
      setCurrentTraitIndex(prev => prev - 1);
    }
  };
  
  const handleReset = () => {
    setCurrentTraitIndex(0);
    setParent1Traits({});
    setParent2Traits({});
    setResults(null);
    setError(null);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    
    // Check if any traits were selected
    if (Object.keys(parent1Traits).length === 0 && Object.keys(parent2Traits).length === 0) {
      setError("Please select at least one trait for one parent before predicting.");
      return; 
    }

    setIsLoading(true);
    setError(null);
    setResults(null);
    try {
      // *** THIS IS THE CORRECTED LINE ***
      // We use a relative path so the Vite proxy can forward the request.
      const response = await fetch('/api/predict_traits/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ parent1_traits: parent1Traits, parent2_traits: parent2Traits }),
      });
      if (!response.ok) throw new Error(`API request failed: ${response.statusText}`);
      const data = await response.json();
      setResults(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };
  
  const currentTraitKey = ALL_TRAIT_KEYS[currentTraitIndex];
  const progressPercentage = ((currentTraitIndex + 1) / TOTAL_TRAITS) * 100;

  if (isLoading || results || error) {
    return (
      <div className="App">
        <main>
          <ResultsDisplay isLoading={isLoading} error={error} results={results} />
          {!isLoading && <button onClick={handleReset} className="reset-btn">Start Over</button>}
        </main>
      </div>
    );
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>🧬 Gene Predictor 🧬</h1>
        <p>For each trait, select the phenotype for both parents. You can skip any.</p>
      </header>
      <main>
        <div className="progress-container">
          <div className="progress-bar" style={{ width: `${progressPercentage}%` }}></div>
          <div className="progress-label">
            Trait {currentTraitIndex + 1} of {TOTAL_TRAITS}
          </div>
        </div>

        <form onSubmit={handleSubmit}>
          <TraitCard
            traitKey={currentTraitKey}
            traitOptions={TRAIT_OPTIONS[currentTraitKey]}
            parent1Value={parent1Traits[currentTraitKey]}
            parent2Value={parent2Traits[currentTraitKey]}
            onTraitChange={handleTraitChange}
          />
          
          <div className="wizard-navigation">
            <button type="button" onClick={handlePreviousTrait} disabled={currentTraitIndex === 0}>
              Previous Trait
            </button>
            {currentTraitIndex < TOTAL_TRAITS - 1 ? (
              <button type="button" onClick={handleNextTrait}>
                Next / Skip
              </button>
            ) : (
              <button type="submit">
                Predict Traits
              </button>
            )}
          </div>
        </form>
      </main>
    </div>
  );
}

export default App;