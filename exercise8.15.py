def print_models(designs, completed_models):
    while designs:
        current_design = designs.pop()
        print(f"Mencetak model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nModel yang sudah dicetak:")

    for model in completed_models:
        print(model)
        
import printing_functions as pf

designs = ["robot", "pesawat", "mobil"]
completed_models = []

pf.print_models(designs[:], completed_models)
pf.show_completed_models(completed_models)