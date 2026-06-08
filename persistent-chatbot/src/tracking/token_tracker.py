def extract_usage(response):

    usage = response.usage_metadata

    return {
        "input_tokens":
            usage.get(
                "input_tokens",
                usage.get("prompt_token_count", 0)
            ),

        "output_tokens":
            usage.get(
                "output_tokens",
                usage.get("candidates_token_count", 0)
            ),

        "total_tokens":
            usage.get(
                "total_tokens",
                usage.get("total_token_count", 0)
            )
    }