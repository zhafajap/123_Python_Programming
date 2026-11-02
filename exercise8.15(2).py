import printing_functions

unprinted_designs = [
    "Phone Case",
    "Robot Pendant",
    "Dodecahedron"
]

completed_models = []

printing_functions.print_models(
    unprinted_designs,
    completed_models
)

printing_functions.show_completed_models(completed_models)