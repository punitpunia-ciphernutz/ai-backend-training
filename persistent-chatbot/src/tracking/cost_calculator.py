INPUT_COST = 0.000000075
OUTPUT_COST = 0.00000030

def calculate_cost(input_tokens, output_tokens):

    input_cost = (input_tokens * INPUT_COST)
    output_cost = (output_tokens * OUTPUT_COST)

    return (input_cost + output_cost)