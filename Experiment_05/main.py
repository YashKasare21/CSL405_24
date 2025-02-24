class StackDepth:
    def maximumDepth(self, stringInput: str) -> int:
        max_depth = 0
        current_depth = 0

        for char in stringInput:
            if char == "(":
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ")":
                current_depth -= 1

        return max_depth


stringInput = input("Enter a valid parentheses string: ")
stack_depth_solver = StackDepth()
print(f"Output: {stack_depth_solver.maximumDepth(stringInput)}")
