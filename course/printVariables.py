def print_variables(scope):
    if scope == 'local':
        print("Local variables:")
        for name, value in locals().items():
            print(f"{name} = {value}")
    elif scope == 'global':
        print("Global variables:")
        for name, value in globals().items():
            print(f"{name} = {value}")
    else:
        print("Invalid scope. Use 'local' or 'global'.")

def example_function():
    a = 1
    b = 2
    print_variables('local')

