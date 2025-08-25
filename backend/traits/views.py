from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .genetics_logic import TRAITS_DATA # Import the "rulebook" from your genetics_logic.py file

@csrf_exempt
def predict_traits_view(request):
    """
    An API view to handle genetic trait prediction.
    It expects a POST request with JSON data containing phenotypes for two parents.
    It calculates the probabilities of the offspring's phenotypes for each trait.
    """
    # 1. --- BOILERPLATE AND INPUT VALIDATION ---
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

    try:
        data = json.loads(request.body)
        parent1_traits = data.get('parent1_traits')
        parent2_traits = data.get('parent2_traits')

        if not parent1_traits or not parent2_traits:
            return JsonResponse({'error': 'parent1_traits and parent2_traits are required.'}, status=400)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data provided'}, status=400)
    except Exception as e:
        return JsonResponse({'error': 'An unexpected error occurred during input processing', 'details': str(e)}, status=500)


    # 2. --- CORE CALCULATION LOGIC ---
    offspring_probabilities = {}

    # Loop through each trait provided for Parent 1
    for trait_name, p1_phenotype in parent1_traits.items():
        p2_phenotype = parent2_traits.get(trait_name)

        # Skip if the trait is missing for Parent 2 or not in our rulebook
        if not p2_phenotype or trait_name not in TRAITS_DATA:
            continue

        trait_rules = TRAITS_DATA[trait_name]
        
        # Get all possible genotypes for each parent's phenotype
        # e.g., 'Dimples' -> ['DD', 'Dd']
        p1_genotypes = trait_rules['allele_map'].get(p1_phenotype, [])
        p2_genotypes = trait_rules['allele_map'].get(p2_phenotype, [])

        if not p1_genotypes or not p2_genotypes:
            offspring_probabilities[trait_name] = {'error': f'Invalid phenotype provided for {trait_name}'}
            continue

        # --- Perform the Punnett Square Cross ---
        all_possible_offspring_genotypes = []
        # Cross every possible genotype of parent 1 with every possible genotype of parent 2
        for g1 in p1_genotypes:
            for g2 in p2_genotypes:
                # Get the two alleles from each parent's genotype
                alleles1 = [g1[0], g1[1]]
                alleles2 = [g2[0], g2[1]]
                # Combine them to create 4 possible offspring genotypes
                for a1 in alleles1:
                    for a2 in alleles2:
                        # Sort the alleles to standardize (e.g., 'dD' becomes 'Dd')
                        offspring_genotype = "".join(sorted(a1 + a2))
                        all_possible_offspring_genotypes.append(offspring_genotype)

        # --- Tally the Results ---
        phenotype_counts = {}
        # For each possible offspring genotype, find its corresponding phenotype
        for genotype in all_possible_offspring_genotypes:
            phenotype = trait_rules['phenotypes'][genotype]
            phenotype_counts[phenotype] = phenotype_counts.get(phenotype, 0) + 1

        # --- Calculate Percentages ---
        total_outcomes = len(all_possible_offspring_genotypes)
        trait_probabilities = {
            pheno: round((count / total_outcomes) * 100, 2)
            for pheno, count in phenotype_counts.items()
        }
        offspring_probabilities[trait_name] = trait_probabilities

    # 3. --- RETURN THE FINAL RESULT ---
    return JsonResponse(offspring_probabilities, status=200)