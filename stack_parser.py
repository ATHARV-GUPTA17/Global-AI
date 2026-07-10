def parse_stack(stack_text):

    stack = {}

    for line in stack_text.splitlines():

        if ":" in line:

            key, value = line.split(":", 1)

            stack[key.strip()] = value.strip()

    return stack